#!/usr/bin/env python3
"""UFO model merging - the engine behind Cell 6 of heft_merging/merge_exports.wl (driven by ufo_merge.wl).

WHAT THIS DOES
Builds one UFO model out of UFO exports already on disk, with no FeynRules: for sub-models
A_1..A_N and the SM-only baseline LO, every coupling entry becomes

    C(A_1 u ... u A_N)  =  C(LO) + Sum_i ( C(A_i) - C(LO) ),

the identity of lheft_merge.wl (Lagrangian) and fa_merge.wl (FeynArts), one export format later.
It is exact because the model keeps one Wilson-coefficient insertion per vertex.

HOW, FILE BY FILE (FeynRules 2.3.49 UFO output)
- vertices.py / couplings.py: merged per ENTRY, keyed by (particles, colour string, Lorentz
  structure by content, coupling orders). FeynRules writes one Vertex per coupling-order set (the
  SM part of hhhh and its WCOrder part are two Vertex objects) and numbers GC_n and the Lorentz
  names per export, so names mean nothing across exports and only content is compared. Entries
  are combined as text: the value is copied verbatim when at most one source differs from the
  baseline, otherwise written as  (C_a) + (C_b) + ... - (m-1)*(LO). A missing entry counts as 0, so
  the sum is right even when two exports decomposed a vertex into different Lorentz structures.
  A composed entry that is numerically zero at three random parameter points is dropped.
- lorentz.py: union by content, renamed per spin prefix (baseline first).
- parameters.py: external parameters united (name, nature, type must agree; a differing value is
  warned about and the baseline's kept); an internal parameter whose value differs between exports
  (MZ in "heft" with P1/P12/PT; G1, GW, vev, hlambda, MW in "gf"/"aem") is merged with the same
  identity, valid because it is linear in its operator's coefficient. Block HEFTBOSONIC is numbered
  positionally per export, so its codes are renumbered; any other (block, code) clash is refused.
  Internal parameters are written in dependency order. An internal parameter ABSENT from the baseline
  that two sources define differently (FeynRules' per-export flavour-sum abbreviations I<k>a<ij>) is
  renamed <name>_m<i> in each source, couplings included, before merging (2026-10-12).
- particles.py, coupling_orders.py, __init__.py, propagators.py, function_library.py,
  object_library.py, write_param_card.py (and form_factors.py / CT_vertices.py if present): must
  be identical in every export (the '# Date:' line aside) and are copied from the baseline.
- CT_couplings.py: must hold no coupling (tree level); copied.
- decays.py: OMITTED (user decision D2, 2026-10-06). FeynRules' widths are quadratic in the
  couplings, so they are not additive; MadGraph computes widths itself (compute_widths / Auto).

REFUSED (exit code 2, message on stderr): a static file that differs, a non-empty CT_couplings.py,
a baseline vertex (particles, orders) missing from a source, the same particle set written in two
orders (decision D3), conflicting parameter declarations or LHA codes, unexpected syntax.
The configuration checks (heft_export.json records, overlapping operators, ...) are done by
ufo_merge.wl before this script is called.

Usage:  python3 ufo_merge.py spec.json
spec = {"baseline": dir, "sources": [dir, ...], "out": dir, "overwrite": bool}
Prints progress lines and, last, '@@SUMMARY@@ <json>'.
"""
import ast
import cmath
import json
import os
import random
import re
import shutil
import sys
from collections import OrderedDict

STATIC = ['particles.py', 'coupling_orders.py', '__init__.py', 'propagators.py',
          'function_library.py', 'object_library.py', 'write_param_card.py']
STATIC_OPTIONAL = ['form_factors.py', 'CT_vertices.py']
MERGED = ['parameters.py', 'couplings.py', 'lorentz.py', 'vertices.py']
OMITTED = ['decays.py']
RENUMBERED_BLOCKS = {'HEFTBOSONIC'}
ZERO_TOL = 1e-9


class Refuse(Exception):
    pass


def say(msg):
    print('[HEFT UFO merge] ' + msg, flush=True)


# ---------------------------------------------------------------------------------------------
# Reading: ast only, nothing is imported (FeynRules' object_library.py is Python 2 code).
# ---------------------------------------------------------------------------------------------

def node_val(n, where):
    if isinstance(n, ast.Constant):
        return n.value
    if isinstance(n, ast.Attribute):
        return node_val(n.value, where) + '.' + n.attr
    if isinstance(n, ast.Name):
        return n.id
    if isinstance(n, ast.List):
        return [node_val(e, where) for e in n.elts]
    if isinstance(n, ast.Tuple):
        return tuple(node_val(e, where) for e in n.elts)
    if isinstance(n, ast.Dict):
        return OrderedDict((node_val(k, where), node_val(v, where)) for k, v in zip(n.keys, n.values))
    if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
        return -node_val(n.operand, where)
    raise Refuse('unexpected syntax in %s: %s' % (where, ast.dump(n)[:120]))


def read_objects(path, cls):
    """[(variable, {keyword: value})] for every 'var = cls(...)' at top level of path."""
    if not os.path.exists(path):
        return []
    tree = ast.parse(open(path).read(), filename=path)
    out = []
    for st in tree.body:
        if (isinstance(st, ast.Assign) and isinstance(st.value, ast.Call)
                and isinstance(st.value.func, ast.Name) and st.value.func.id == cls):
            kws = OrderedDict((kw.arg, node_val(kw.value, path)) for kw in st.value.keywords)
            out.append((st.targets[0].id, kws))
    return out


def header_of(path):
    """The text before the first object definition (comments and imports)."""
    lines = open(path).read().split('\n')
    for i, l in enumerate(lines):
        if re.match(r'^\w+\s*=\s*\w+\(', l):
            return '\n'.join(lines[:i]).rstrip('\n') + '\n'
    return '\n'.join(lines)


def static_text(path):
    return '\n'.join(l for l in open(path).read().split('\n') if not l.startswith('# Date:'))


def read_export(d):
    E = {'dir': d, 'name': os.path.basename(os.path.normpath(d))}
    for f in MERGED:
        if not os.path.exists(os.path.join(d, f)):
            raise Refuse('%s has no %s - not a UFO export' % (E['name'], f))
    E['params'] = OrderedDict(read_objects(os.path.join(d, 'parameters.py'), 'Parameter'))
    E['couplings'] = OrderedDict(read_objects(os.path.join(d, 'couplings.py'), 'Coupling'))
    E['lorentz'] = OrderedDict(read_objects(os.path.join(d, 'lorentz.py'), 'Lorentz'))
    E['vertices'] = read_objects(os.path.join(d, 'vertices.py'), 'Vertex')
    E['ct'] = read_objects(os.path.join(d, 'CT_couplings.py'), 'Coupling')
    return E


def entries(E):
    """Coupling entries of one export: key -> value string, plus the (particles, orders) groups
    in order of appearance and the original order dicts."""
    lor = {k: (tuple(v['spins']), v['structure']) for k, v in E['lorentz'].items()}
    prefix = {}
    for k, v in E['lorentz'].items():
        prefix.setdefault((tuple(v['spins']), v['structure']), re.sub(r'\d+$', '', k))
    out, groups, odicts, extra = OrderedDict(), OrderedDict(), {}, {}
    for var, v in E['vertices']:
        parts = tuple(v['particles'])
        cols, lors = v['color'], v['lorentz']
        for (ci, li), cref in v['couplings'].items():
            for r in (cref if isinstance(cref, list) else [cref]):
                c = E['couplings'][r.split('.', 1)[1]]
                ok = tuple(sorted(c['order'].items()))
                odicts.setdefault(ok, c['order'])
                lkey = lor[lors[li].split('.', 1)[1]]
                key = (parts, cols[ci], lkey, ok)
                val = c['value']
                out[key] = '(%s) + (%s)' % (out[key], val) if key in out else val
                groups.setdefault((parts, ok), True)
    for k, v in E['lorentz'].items():
        extra.setdefault((tuple(v['spins']), v['structure']),
                         OrderedDict((a, b) for a, b in v.items() if a not in ('name', 'spins', 'structure')))
    return {'out': out, 'groups': groups, 'odicts': odicts, 'prefix': prefix, 'lextra': extra}


# ---------------------------------------------------------------------------------------------
# Numerical zero test for composed entries
# ---------------------------------------------------------------------------------------------

def _f(g):
    return lambda z: g(complex(z))


FUNCS = {
    'cmath': cmath, 'complex': complex, 'abs': abs, 'float': float, 'int': int,
    'complexconjugate': lambda z: complex(z).conjugate(),
    're': lambda z: complex(z).real, 'im': lambda z: complex(z).imag,
    'sec': _f(lambda z: 1 / cmath.cos(z.real)), 'csc': _f(lambda z: 1 / cmath.sin(z.real)),
    'asec': _f(lambda z: cmath.acos(1 / z.real)), 'acsc': _f(lambda z: cmath.asin(1 / z.real)),
    'cot': _f(lambda z: 1 / cmath.tan(z)),
}


def names_in(expr):
    try:
        t = ast.parse(expr, mode='eval')
    except SyntaxError:
        return None
    return {n.id for n in ast.walk(t) if isinstance(n, ast.Name)} - set(FUNCS)


def evaluate(expr, point):
    ns = names_in(expr)
    if ns is None:
        return None
    env = dict(FUNCS)
    for n in ns:
        env[n] = random.Random('%s|%d' % (n, point)).uniform(0.5, 1.5)
    try:
        return complex(eval(compile(expr, '<coupling>', 'eval'), {'__builtins__': {}}, env))
    except Exception:
        return None


def is_zero(expr, terms):
    for pt in range(3):
        v = evaluate(expr, pt)
        if v is None:
            return False
        scale = max([abs(evaluate(t, pt) or 0) for t in terms] + [1e-300])
        if abs(v) > ZERO_TOL * scale:
            return False
    return True


def compose(L, Cs):
    """LO + Sum_i (C_i - LO) as text; None = absent = 0. Returns (value or None, composed?, terms)."""
    differ = [c for c in Cs if c != L]
    m = len(differ)
    if m == 0:
        return L, False, []
    if m == 1 and differ[0] is not None:
        return differ[0], False, []
    terms = [c for c in differ if c is not None]
    text = ' + '.join('(%s)' % t for t in terms)
    k = m - 1                                   # LO is subtracted m - 1 times
    if L is not None and k > 0:
        sub = ('%d*(%s)' % (k, L)) if k > 1 else '(%s)' % L
        text = (text + ' - ' + sub) if text else '-' + sub
        terms = terms + [L]
    if not text:
        return None, True, []
    return text, True, terms


# ---------------------------------------------------------------------------------------------
# The merge
# ---------------------------------------------------------------------------------------------

def check_static(base, subs, warnings):
    for f in STATIC:
        if not os.path.exists(os.path.join(base['dir'], f)):
            raise Refuse('the baseline %s has no %s' % (base['name'], f))
    for s in subs:
        for f in STATIC + STATIC_OPTIONAL:
            pb, ps = os.path.join(base['dir'], f), os.path.join(s['dir'], f)
            if os.path.exists(pb) != os.path.exists(ps):
                raise Refuse('%s exists in only one of %s, %s' % (f, base['name'], s['name']))
            if os.path.exists(pb) and static_text(pb) != static_text(ps):
                raise Refuse('%s differs between %s and %s - these exports are not of the same model '
                             '(particles, orders or FeynRules version)' % (f, base['name'], s['name']))
    for e in [base] + subs:
        if e['ct']:
            raise Refuse('%s has counterterm couplings in CT_couplings.py; only tree-level exports '
                         'can be merged' % e['name'])
        extra = sorted(set(os.listdir(e['dir'])) - set(STATIC + STATIC_OPTIONAL + MERGED + OMITTED +
                       ['CT_couplings.py', 'heft_export.json', '__pycache__']))
        extra = [x for x in extra if not x.endswith('.pyc')]
        if extra:
            warnings.append('%s: files not merged and not copied: %s' % (e['name'], ', '.join(extra)))


def check_particle_order(all_entries, names):
    seen = {}
    for en, nm in zip(all_entries, names):
        for (parts, ok) in en['groups']:
            seen.setdefault(tuple(sorted(parts)), {}).setdefault(parts, nm)
    bad = {k: v for k, v in seen.items() if len(v) > 1}
    if bad:
        k, v = next(iter(bad.items()))
        raise Refuse('the particle set %s is written in different orders (%s); merging such exports '
                     'would need the colour and Lorentz indices permuted, which is not implemented '
                     '(decision D3)' % (', '.join(k), '; '.join('%s in %s' % (', '.join(p), n) for p, n in v.items())))


IDENT = re.compile(r'(?<![\w.])[A-Za-z_]\w*')


def substitute(expr, ren):
    """Rename whole identifiers in an expression string (not attributes such as cmath.sqrt)."""
    return IDENT.sub(lambda m: ren.get(m.group(0), m.group(0)), expr) if ren else expr


def rename_source_internals(base, subs, stats):
    """Internal parameters absent from the baseline are named per export by FeynRules - its flavour-sum
    abbreviations I<k>a<ij> are numbered per export, so I1a11 is CKM*CNQ1 in one export and CKM*CNQ11 in
    another (TESTS/T42).  A name that two sources define differently is renamed in each of them,
    <name>_m<i> (i = the source's position, 1-based), in its parameters and couplings; a parameter whose
    definition then differs because it uses a renamed one is renamed too (repeated to a fixed point).
    Names defined identically in every source that has them are kept.  Names in the baseline are never
    renamed: there an internal parameter is the same quantity in every export (MZ, G1, vev, ...) and is
    merged with the LO + Sum(C_i - LO) identity.  (2026-10-12)"""
    B = set(base['params'])
    taken = set(B).union(*[set(s['params']) for s in subs])
    ren = [dict() for _ in subs]
    while True:
        occ = OrderedDict()
        for i, s in enumerate(subs):
            for var, kws in s['params'].items():
                if var in B or var in ren[i] or kws.get('nature') == 'external':
                    continue
                occ.setdefault(var, []).append((i, substitute(str(kws.get('value')), ren[i])))
        clash = [n for n, o in occ.items() if len({v for _, v in o}) > 1]
        if not clash:
            break
        for n in clash:
            for i, _ in occ[n]:
                new = '%s_m%d' % (n, i + 1)
                if new in taken:
                    raise Refuse('cannot rename internal parameter %s of %s: %s is already a parameter name'
                                 % (n, subs[i]['name'], new))
                ren[i][n] = new
                taken.add(new)
    for s, r in zip(subs, ren):
        if not r:
            continue
        params = OrderedDict()
        for var, kws in s['params'].items():
            kws = OrderedDict(kws)
            if kws.get('nature') != 'external' and isinstance(kws.get('value'), str):
                kws['value'] = substitute(kws['value'], r)
            if var in r:
                kws['name'] = r[var]
            params[r.get(var, var)] = kws
        s['params'] = params
        for c in s['couplings'].values():
            c['value'] = substitute(c['value'], r)
        stats['internal_renamed'][s['name']] = len(r)
    return ren


def merge_couplings(LO, S, base_name, sub_names, stats):
    for g in LO['groups']:
        for s, n in zip(S, sub_names):
            if g not in s['groups']:
                raise Refuse('the baseline vertex [%s] with orders %s is missing from %s; a sub-model '
                             'carries the whole SM, so this export lost a vertex' %
                             (', '.join(g[0]), dict(g[1]), n))
    keys = list(LO['out'])
    for s in S:
        keys += [k for k in s['out'] if k not in LO['out']]
    keys = list(OrderedDict.fromkeys(keys))
    merged = OrderedDict()
    for k in keys:
        val, composed, terms = compose(LO['out'].get(k), [s['out'].get(k) for s in S])
        if val is None:
            stats['entries_removed'] += 1
            continue
        if composed:
            stats['entries_composed'] += 1
            if is_zero(val, terms):
                stats['entries_cancelled'] += 1
                continue
        merged[k] = val
    return merged


def merge_parameters(exports, warnings):
    allp = OrderedDict()
    for i, E in enumerate(exports):
        for var, kws in E['params'].items():
            allp.setdefault(var, []).append((i, kws))
    out = OrderedDict()
    for var, occ in allp.items():
        first = occ[0][1]
        for i, kws in occ[1:]:
            for f in ('nature', 'type'):
                if kws.get(f) != first.get(f):
                    raise Refuse('parameter %s has %s %r in %s but %r in %s' %
                                 (var, f, first.get(f), exports[occ[0][0]]['name'], kws.get(f), exports[i]['name']))
        p = OrderedDict(first)
        if first.get('nature') == 'external':
            vals = {repr(k.get('value')) for _, k in occ}
            if len(vals) > 1:
                warnings.append('external parameter %s has different default values (%s); the %s one '
                                'is kept' % (var, ', '.join(sorted(vals)), exports[occ[0][0]]['name']))
            blk = {(k.get('lhablock'), tuple(k.get('lhacode', []))) for _, k in occ}
            if len(blk) > 1 and first.get('lhablock') not in RENUMBERED_BLOCKS:
                raise Refuse('external parameter %s has different LHA entries in different exports: %s'
                             % (var, sorted(blk)))
        else:
            in_base = occ[0][0] == 0
            if in_base:
                L = first['value']
                Cs = [dict((i, k['value']) for i, k in occ).get(j) for j in range(1, len(exports))]
                Cs = [c if c is not None else L for c in Cs]   # absent from a source = unchanged
                val, composed, _ = compose(L, Cs)
                p['value'] = val
            else:
                vals = {k['value'] for _, k in occ}
                if len(vals) > 1:
                    raise Refuse('internal parameter %s is absent from the baseline and defined '
                                 'differently in %s' % (var, ', '.join(exports[i]['name'] for i, _ in occ)))
        out[var] = p
    # Renumber the positional blocks, then refuse any (block, code) used twice.
    for b in RENUMBERED_BLOCKS:
        n = 0
        for var, p in out.items():
            if p.get('lhablock') == b:
                n += 1
                p['lhacode'] = [n]
    used = {}
    for var, p in out.items():
        if p.get('nature') == 'external':
            k = (p.get('lhablock'), tuple(p.get('lhacode', [])))
            if k in used:
                raise Refuse('LHA entry %s %s is used by both %s and %s' % (k[0], list(k[1]), used[k], var))
            used[k] = var
    return out


def order_parameters(params):
    ext = [v for v, p in params.items() if p.get('nature') == 'external']
    intl = [v for v, p in params.items() if p.get('nature') != 'external']
    zero = [v for v in intl if v == 'ZERO']
    intl = [v for v in intl if v != 'ZERO']
    deps = {v: (names_in(params[v]['value']) or set()) & set(intl) - {v} for v in intl}
    done, order = set(), []
    pending = list(intl)
    while pending:
        progressed = False
        for v in list(pending):
            if deps[v] <= done:
                order.append(v); done.add(v); pending.remove(v); progressed = True
        if not progressed:
            raise Refuse('circular dependency among internal parameters: %s' % ', '.join(pending))
    return zero + ext + order


# ---------------------------------------------------------------------------------------------
# Writing
# ---------------------------------------------------------------------------------------------

def py(v):
    return repr(v)


def write_parameters(path, header, params, order):
    out = [header]
    for var in order:
        p = params[var]
        fields = ['name = %s' % py(p.get('name', var))]
        for f in ('nature', 'type'):
            fields.append('%s = %s' % (f, py(p[f])))
        fields.append('value = %s' % py(p['value']))
        if 'texname' in p:
            fields.append('texname = %s' % py(p['texname']))
        if p.get('nature') == 'external':
            fields.append('lhablock = %s' % py(p['lhablock']))
            fields.append('lhacode = [ %s ]' % ', '.join(str(c) for c in p['lhacode']))
        for f, v in p.items():
            if f not in ('name', 'nature', 'type', 'value', 'texname', 'lhablock', 'lhacode'):
                fields.append('%s = %s' % (f, py(v)))
        out.append('%s = Parameter(%s)\n' % (var, (',\n' + ' ' * (len(var) + 13)).join(fields)))
    open(path, 'w').write('\n'.join(out))


def fmt_order(od):
    return '{' + ','.join('%s:%s' % (py(k), v) for k, v in od.items()) + '}'


def build_output(merged, LO, S, base_name, sub_names):
    odicts, prefix, lextra = dict(LO['odicts']), dict(LO['prefix']), dict(LO['lextra'])
    for s in S:
        for k, v in s['odicts'].items(): odicts.setdefault(k, v)
        for k, v in s['prefix'].items(): prefix.setdefault(k, v)
        for k, v in s['lextra'].items(): lextra.setdefault(k, v)
    # couplings: one name per distinct (value, orders)
    cname, couplings = OrderedDict(), []
    for (parts, col, lk, ok), val in merged.items():
        if (val, ok) not in cname:
            cname[(val, ok)] = 'GC_%d' % (len(cname) + 1)
            couplings.append((cname[(val, ok)], val, odicts[ok]))
    # Lorentz names, per spin prefix, in order of use
    lname, counter, lorentz = OrderedDict(), {}, []
    for (parts, col, lk, ok) in merged:
        if lk not in lname:
            pre = prefix.get(lk, ''.join('X' for _ in lk[0]))
            counter[pre] = counter.get(pre, 0) + 1
            lname[lk] = '%s%d' % (pre, counter[pre])
            lorentz.append((lname[lk], lk, lextra.get(lk, {})))
    # vertices: one per (particles, orders) group, baseline groups first
    groups = OrderedDict()
    for (parts, col, lk, ok), val in merged.items():
        groups.setdefault((parts, ok), []).append((col, lk, cname[(val, ok)]))
    vertices = []
    for (parts, ok), ents in groups.items():
        cols = list(OrderedDict.fromkeys(c for c, _, _ in ents))
        lors = list(OrderedDict.fromkeys(l for _, l, _ in ents))
        coup = OrderedDict(((cols.index(c), lors.index(l)), g) for c, l, g in ents)
        vertices.append((parts, cols, [lname[l] for l in lors], coup))
    return couplings, lorentz, vertices


def write_couplings(path, header, couplings):
    out = [header]
    for n, val, od in couplings:
        out.append("%s = Coupling(name = %s,\n%svalue = %s,\n%sorder = %s)\n" %
                   (n, py(n), ' ' * (len(n) + 12), py(val), ' ' * (len(n) + 12), fmt_order(od)))
    open(path, 'w').write('\n'.join(out))


def write_lorentz(path, header, lorentz):
    out = [header]
    for n, (spins, struct), extra in lorentz:
        if extra:
            raise Refuse('Lorentz structure %s carries %s (form factors), which the merge does not '
                         'support' % (n, ', '.join(extra)))
        ind = ' ' * (len(n) + 11)
        fields = ['name = %s' % py(n), 'spins = [ %s ]' % ', '.join(str(s) for s in spins),
                  'structure = %s' % py(struct)]
        out.append('%s = Lorentz(%s)\n' % (n, (',\n' + ind).join(fields)))
    open(path, 'w').write('\n'.join(out))


def write_vertices(path, header, vertices):
    out = [header]
    for i, (parts, cols, lors, coup) in enumerate(vertices, 1):
        n = 'V_%d' % i
        ind = ' ' * (len(n) + 10)
        fields = ['name = %s' % py(n),
                  'particles = [ %s ]' % ', '.join(parts),
                  'color = [ %s ]' % ', '.join(py(c) for c in cols),
                  'lorentz = [ %s ]' % ', '.join('L.' + l for l in lors),
                  'couplings = {%s}' % ','.join('(%d,%d):C.%s' % (ci, li, g) for (ci, li), g in coup.items())]
        out.append('%s = Vertex(%s)\n' % (n, (',\n' + ind).join(fields)))
    open(path, 'w').write('\n'.join(out))


def merge(spec):
    warnings, stats = [], {'entries_removed': 0, 'entries_composed': 0, 'entries_cancelled': 0,
                           'internal_renamed': OrderedDict()}
    base = read_export(spec['baseline'])
    subs = [read_export(d) for d in spec['sources']]
    names = [base['name']] + [s['name'] for s in subs]
    out_dir = os.path.normpath(spec['out'])
    if out_dir in [os.path.normpath(d) for d in [spec['baseline']] + spec['sources']]:
        raise Refuse('the output directory is one of the inputs')
    say('baseline %s; sources %s' % (base['name'], ', '.join(s['name'] for s in subs)))
    check_static(base, subs, warnings)
    rename_source_internals(base, subs, stats)
    LO, S = entries(base), [entries(s) for s in subs]
    check_particle_order([LO] + S, names)
    merged = merge_couplings(LO, S, base['name'], names[1:], stats)
    params = merge_parameters([base] + subs, warnings)
    order = order_parameters(params)
    couplings, lorentz, vertices = build_output(merged, LO, S, base['name'], names[1:])

    if os.path.exists(out_dir):
        if not spec.get('overwrite'):
            raise Refuse('%s exists (overwrite not allowed)' % out_dir)
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)
    note = '# Merged by HEFT ufo_merge.py: baseline %s, sources %s\n' % (base['name'], ', '.join(names[1:]))
    hdr = lambda f: note + header_of(os.path.join(base['dir'], f))
    write_parameters(os.path.join(out_dir, 'parameters.py'), hdr('parameters.py'), params, order)
    write_couplings(os.path.join(out_dir, 'couplings.py'), hdr('couplings.py'), couplings)
    write_lorentz(os.path.join(out_dir, 'lorentz.py'), hdr('lorentz.py'), lorentz)
    write_vertices(os.path.join(out_dir, 'vertices.py'), hdr('vertices.py'), vertices)
    for f in STATIC + STATIC_OPTIONAL + ['CT_couplings.py']:
        if os.path.exists(os.path.join(base['dir'], f)):
            shutil.copy2(os.path.join(base['dir'], f), os.path.join(out_dir, f))
    for f in ['parameters.py', 'couplings.py', 'lorentz.py', 'vertices.py']:
        ast.parse(open(os.path.join(out_dir, f)).read(), filename=f)   # never write a broken file

    stats.update({'vertices': len(vertices), 'couplings': len(couplings), 'lorentz': len(lorentz),
                  'parameters': len(params), 'entries': len(merged),
                  'renumbered': {b: sum(1 for p in params.values() if p.get('lhablock') == b)
                                 for b in RENUMBERED_BLOCKS},
                  'decays': 'omitted', 'warnings': warnings, 'out': out_dir})
    for w in warnings:
        say('WARNING: ' + w)
    if stats['internal_renamed']:
        say('internal parameters renamed per source (same name, different definition): %s' %
            ', '.join('%s %d' % kv for kv in stats['internal_renamed'].items()))
    say('%d vertices, %d couplings, %d Lorentz structures, %d parameters; %d entries composed, '
        '%d cancelled to zero and dropped, %d removed (absent from a source that differs). '
        'decays.py omitted.' % (len(vertices), len(couplings), len(lorentz), len(params),
                                stats['entries_composed'], stats['entries_cancelled'], stats['entries_removed']))
    return stats


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    spec = json.load(open(sys.argv[1]))
    try:
        stats = merge(spec)
    except Refuse as e:
        print('[HEFT UFO merge] REFUSED: %s' % e, file=sys.stderr, flush=True)
        print('@@REFUSED@@ ' + json.dumps({'reason': str(e)}), flush=True)
        sys.exit(2)
    print('@@SUMMARY@@ ' + json.dumps(stats), flush=True)


if __name__ == '__main__':
    main()
