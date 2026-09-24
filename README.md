# HEFT-FR

**A FeynRules implementation of the Higgs Effective Field Theory (HEFT).**

HEFT-FR builds the electroweak chiral Lagrangian with a singlet Higgs, in the mass basis,
from an operator set you choose — and exports it as a **UFO** or
**FeynArts** model files.

- **Version 1.0** · MIT licensed · see [Authors](#authors)
- **Entry point:** [`heft_fr_notebook.wl`](heft_fr_notebook.wl) — open it in Mathematica and
  evaluate cell by cell. Nothing else needs editing.

---

## Contents

- [What you get](#what-you-get)
- [References and operator set](#references-and-operator-set)
- [Power counting](#power-counting)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Configuration options](#configuration-options)
- [The Kappa and Delta frameworks](#the-kappa-and-delta-frameworks)
- [Input scheme (EW)](#input-scheme-ew)
- [Wilson coefficients — the WCxf workflow](#wilson-coefficients--the-wcxf-workflow)
- [Adding your own operators](#adding-your-own-operators)
- [Exports](#exports)
- [The LHEFT cache](#the-lheft-cache)
- [Merging cached models](#merging-cached-models)
- [Performance](#performance)
- [Repository layout](#repository-layout)
- [Rules of the road](#rules-of-the-road)
- [Known limitations](#known-limitations)
- [Authors](#authors)

---

## What you get

- **The NLO operator set of [Brivio et al. 1604.06801](https://arxiv.org/abs/1604.06801)** —
  bosonic, two-fermion (2F) and four-fermion (4F). That is 42 bosonic, 53 2F and 56 4F
  operator labels, each with its own flare-function tower of Wilson coefficients.
- **A pick-and-choose operator selection.** You name the operators you want; everything else
  stays out of the Lagrangian entirely.
- **Wilson coefficients in [WCxf](https://arxiv.org/abs/1712.05298) JSON** — written out for
  your selection.
- **Three electroweak input schemes** — heft, gf, aem.
- **A build cache** - the expensive step happens once per physics configuration, and a
  **merge facility** that can assemble a large model out of small cached ones.
- **UFO and FeynArts exports**, plus optional plain-text and LaTeX listings of the Feynman
  rules. The UFO carries `ChiralOrder` and `WCOrder` as coupling orders, so the
  [power counting](#power-counting) can be applied at the amplitude level in MadGraph.
- **Example user-defined operators**, in the two `_User.fr` files, as a worked template
  for [adding your own](#adding-your-own-operators) operators.

## References and operator set

There is **one operator set (1604.06801)** and **one gauge (unitary)**.

| | Reference |
|---|---|
| **Operator set** | I. Brivio, J. Gonzalez-Fraile, M.C. Gonzalez-Garcia, L. Merlo, *The complete HEFT Lagrangian after the LHC Run I*, [arXiv:1604.06801](https://arxiv.org/abs/1604.06801) — **the operators this model implements** |
| **Power counting** | I. Brivio, R. Gröber, K. Schmid, *The Art of Counting: a reappraisal of the HEFT expansion*, [arXiv:2511.23410](https://arxiv.org/abs/2511.23410) — the counting this model follows |
| Framework | A. Alloul, N. Christensen, C. Degrande, C. Duhr, B. Fuks, *FeynRules 2.0*, [arXiv:1310.1921](https://arxiv.org/abs/1310.1921) |
| Coefficient exchange format | J. Aebischer et al., *WCxf: an exchange format for Wilson coefficients*, [arXiv:1712.05298](https://arxiv.org/abs/1712.05298) |


## Power counting

Three parameters organise the EFT part of the Lagrangian.

| Bookkeeper | Counts | Expansion |
|---|---|---|
| **`ChiralOrder^n`** | the chiral order of the operator | none — operator label only |
| **`WCOrder`** | one power per Wilson-coefficient vertex insertion | fixed at `WCOrder^1` — one insertion per vertex, always |
| `LamF` | the power of `h/v` inside every flare function | `HiggsMaxOrder`|

`ChiralOrder` and `WCOrder` reach the exported UFO **as coupling orders**.

HEFT Lagrangian is organised by **chiral dimension**. This model follows the prescription described
in detail in [2511.23410](https://arxiv.org/abs/2511.23410).

At the operator level, leading order (LO) means just `ChiralOrder^0` and nothing else. 

| `ChiralOrder` | Bosonic (42) | Fermionic (109) |
|---|---|---|
| **0** | `PT`, `PG`, `PB`, `PW`, `P1`, `P12`, `S1`, `S2D`, `S8`, `SG`, `SB`, `SW` — 12 | 2F `NQ1`–`NQ8`, `NQ29`–`NQ36`, `NL1`, `NL2`, `NL12`–`NL17` — 24 · 4F **all 56**: `RQ1`–`RQ26`, `RQL1`–`RQL23`, `RL1`–`RL7` |
| **1** | `PGGG`, `PWWW`, `SGGG`, `SWWW`, `P2`–`P5`, `P13`, `P14`, `P17`, `S2`, `S3`, `S4`, `S7`, `S9` — 16 | 2F `NQ9`–`NQ28`, `NL3`–`NL11` — 29 |
| **2** | `PDH`, `P6`, `P8`, `P11`, `P18`, `P20`–`P24`, `P26`, `S5`, `S6`, `S15` — 14 | — |

`P` and `S` are the CP-even and CP-odd bosonic operators, `NQ`/`NL` the two-fermion and
`RQ`/`RQL`/`RL` the four-fermion ones. The three user examples `PGHD1`, `PGHD2`, `SGHD` are
chiral order 2. The SM Lagrangian is always present and carries **no** `ChiralOrder` factor at
all. Cell 1 prints this same catalogue, grouped the same way.

### One Wilson-coefficient insertion per vertex

**Every exported vertex is at most linear in the HEFT Wilson coefficients.** The Lagrangian is
already linear term by term: each EFT operator carries exactly one `WCOrder`, as does each
Delta-framework deviation (`DeltaFCn1/2`, `DeltaLam3/4`, `dyuH`/`dydH`/`dylH`) and each flagged
`h/v` tower (`FFC`, `FVHiggs`, `FQU`/`FQD`/`FLE`). Kappa rescalings multiply interactions the SM
already has, and are deliberately **not** flagged.

Only two substitutions could put a *second* coefficient into a vertex, and both are expanded to
first order in `WCOrder` and cut there:

1. **The A–Z rotation** — [`gauge_normalization.fr`](model_files/gauge_normalization.fr). `P1` (W³–B kinetic mixing) and `P12` (W³ rescaling) change the gauge kinetic matrix
   at `h⁰`, so `AZnorm` depends on `CP1n0` and `CP12n0` and enters every vertex with a W³ or B
   leg. All such contributions are linearised, so in the end every vertex contains at most one
   insertion of Wilson coefficient.

2. **The input relations** — [`input_scheme.fr`](model_files/input_scheme.fr).
Five HEFT operators change the tree-level relation: `P1`, `P12`, `PT` and
   `RL2`/`RL5`. Again, such contributions are linearised, so in the end every vertex contains at most one insertion of Wilson coefficient.

### Two derivatives on two flares: one combined coefficient

Eight operators put a derivative on each of **two** flare functions, `∂_μF₁(h)·∂_νF₂(h)`, which
would leave two Wilson coefficients in one vertex. They are written with a **single combined
family** instead — an exact rewrite, since the vertex only ever depends on that one combination:

| Operators | Coefficient | `nh` |
|---|---|---|
| `P8`, `P20`, `P21`, `P22` | `C<op>n<nh>prime` | `2 … 2·HiggsMaxOrder` |
| `PDH` (that bilinear squared) | `CPDHn<nh>prime` | `4 … 4·HiggsMaxOrder` |
| `NQ9`, `NQ10`, `NL3` | `C<op>n<nh>prime[f1,f2]`, a 3×3 tensor per `nh` | `2 … 2·HiggsMaxOrder` |

`nh` counts the Higgs fields the term puts into the vertex, the differentiated ones included —
so `CP8n4prime` multiplies the four-Higgs term. (`prime` is spelled out because `'` is not a
legal UFO/FeynArts/WCxf identifier character.) A related rule: **a flare under a derivative
starts at `n = 1`**, since `∂_μF(h)` kills the constant term. Both are checked when the model
loads (`HEFTFlareSpecCheck[]`), which aborts naming the operator at fault — user-defined
operators included.


## Requirements

- **Mathematica 14.0** — this is the version HEFT-FR is developed and tested on.
- **FeynRules** (2.3.x) — install it yourself and point `$FeynRulesPath` at the directory
  containing `FeynRules.m`. This is the first line of the Configuration cell.

No installation step: clone the repository and open the notebook.

## Quick start

Open [`heft_fr_notebook.wl`](heft_fr_notebook.wl) in Mathematica and work down it. Every path
is resolved relative to the file itself, so the repository can live anywhere.

> **Quit the kernel before every run.** *Evaluation ▸ Quit Kernel*. See
> [Rules of the road](#rules-of-the-road) — this one matters.

| Cell | What it does |
|------|--------------|
| **1 — Reference** | Prints what this model is, the full configuration-option table, and the operator catalogue grouped by chiral order. No FeynRules, no model loading; safe to re-run any time you need to look up a label. |
| **2 — Configuration** | The single place every run option is set. Re-evaluate it after every change. |
| **3 — Banner and coefficient files** | Loads FeynRules, checks the configuration (unknown operator labels and removed options abort here), echoes it, and writes `wcxf/wcxf_init.json` and `wcxf/wcxf_output.json` for exactly your operator selection. Closes with the cache verdict, so you know before Cell 5 whether it will load or build. |
| **4 — Edit coefficients** *(optional)* | Skip it for defaults. Otherwise edit `wcxf/wcxf_output.json` in a text editor; this cell just prints the paths and re-runs the cache lookup. |
| **5 — Build** | `LoadModel`, restrictions, then `LHEFT` — the mass-basis Lagrangian. Loads from cache when this exact configuration has been built before; otherwise builds from scratch (minutes to hours). |
| **6 — Feynman rules** *(optional)* | `RulesHEFT = FeynmanRules[LHEFT]`, saved as `.mx`, plain text and a standalone LaTeX document. Cells 7 and 8 do **not** need this. |
| **7 — UFO export** | Writes `output/UFO/<OutputName>/`. |
| **8 — FeynArts export** | Writes `output/FeynArts/<OutputName>/` (`.mod`, `.gen`, `.pars`). |

Cells 7 and 8 are independent — run either, or both. Both need only `LHEFT` from Cell 5.

## Configuration options

Everything below lives in **Cell 2**. Cell 1 prints the same table with the allowed values;
[`model_files/heft_defaults.wl`](model_files/heft_defaults.wl) holds the fallback used for
anything you leave unset. There are no power-counting options — see
[Power counting](#power-counting).

### Physics and expansion

| Option | Default | Meaning |
|---|---|---|
| `HiggsMaxOrder` | `3` | Highest power of `h/v` kept in every flare function. The single strongest driver of build and export cost. |
| `EFTOperators` | `{}` | The active operator labels. `{}` means the SM-like LO Lagrangian only. Must come from the catalogue Cell 1 prints; an unknown label aborts Cell 3. A selected operator is always kept — there is no order cut. |
| `KappaFramework` | `True` | `True` → Kappa (multiplicative) parameterisation of SM-coupling deviations; `False` → Delta (additive). See [below](#the-kappa-and-delta-frameworks). |
| `LOYukawaExpansion` | `True` | Keep the multi-Higgs tower `FQU`/`FQD`/`FLE` (`n ≥ 2`) on top of the LO Yukawa. `False` drops it *and* does not declare `CQUn`/`CQDn`/`CLEn` at all. The fermion mass and the single-Higgs coupling are unaffected. |

### Inputs and restrictions

| Option | Default | Meaning |
|---|---|---|
| `EWInputScheme` | `"heft"` | `"heft"`, `"gf"` or `"aem"` — see [Input scheme (EW)](#input-scheme-ew). |
| `Massless` | `False` | If True → load `restrictions/Massless.rst`: light fermion masses set to zero, only τ, b and t stay massive. |
| `DiagonalCKM` | `False` | If True → load `restrictions/DiagonalCKM.rst`: CKM → identity. |

### Coefficients, output and cache

| Option | Default | Meaning |
|---|---|---|
| `InitialiseWCs` | `1` | Value written for the **effective** coefficients (`1` or `0`). SM couplings always keep their SM value regardless. See [below](#initialisewcs). |
| `OutputName` | — | Subdirectory name under `output/`, and the readable half of the cache folder name. |
| `MaxVertexLegs` | `Automatic` | Export-time cut on vertex multiplicity — see [below](#maxvertexlegs). |
| `ForceRebuildLHEFT` | `False` | Skip the cache lookup and rebuild. | 

### `InitialiseWCs`

Sets the value Cell 3 writes for every **effective** coefficient. The 13 SM
couplings (`KappaV`, `Kappa2V`, `Kappa3H`, `Kappa4H`, `KappaQU`…`KappaLT`, or their `Delta*`
counterparts) keep their SM value.

Note that the SM point depends on the framework: `κ = 1` with `KappaFramework = True`, `Δ = 0`
with `False`. `InitialiseWCs = 0` is the natural starting point for switching one coefficient
on at a time. It changes numbers in the JSON files and nothing in the Lagrangian, so it is
**not** part of the cache key.

### `MaxVertexLegs`

Caps the number of legs a vertex may have in the output. `Automatic` exports everything; an
integer `n ≥ 3` keeps only vertices with at most `n` legs. Honoured by Cells 6, 7 **and** 8 —
it becomes FeynRules' own `MaxParticles`, which the UFO and FeynArts writers forward to the
`FeynmanRules` call they make internally, so it really does shrink the exported model.

Measured on `{PG, PW, P12}`, `HiggsMaxOrder = 3`, `"heft"` (the setup of § Performance), Cell 5
a cache hit:

| `MaxVertexLegs` | Cells 6+7 | speed-up | UFO vertices dropped |
|---|---|---|---|
| `Automatic` | 200.7 s | 1.00× | — (211 exported) |
| **`6`** | **133.9 s** | **1.50×** | 9 / 211 (4.3 %) |
| `5` | 101.5 s | 1.98× | 22 / 211 (10.4 %) |
| `4` | 97.7 s | 2.05× | 67 / 211 (31.8 %) |

High-multiplicity vertices are combinatorially the most expensive, which is why removing 4 % of
them buys a third of the time. Below 5 legs there is little left to gain.

Not part of the cache key — you can re-export one cached build at several cuts for free.

## The Kappa and Delta frameworks

`KappaFramework` decides how deviations from SM couplings are parameterised, and **which names
are declared as parameters at all**. An exported model contains one side, never both.

| | `KappaFramework = True` | `KappaFramework = False` |
|---|---|---|
| Names | `KappaV`, `Kappa2V`, `Kappa3H`, `Kappa4H`, `KappaQU`… | `DeltaFCn1`, `DeltaFCn2`, `DeltaLam3`, `DeltaLam4`, `DeltaYQU`… |
| Form | multiplicative rescaling | additive shift |
| SM point | `1` | `0` |

In the 2F sector the fermion **mass** and the **single-Higgs (*hff*) vertex** are carried by
two separate tensors — `yu`/`yd`/`yl` for the mass, `yuH`/`ydH`/`ylH` for the vertex — so a
Kappa can vary the coupling *relative* to the mass without shifting the mass away from the
value used for the propagator. Above `n = 1`, the multi-Higgs tower `FQU`/`FQD`/`FLE` carries
`CQUn<n>`/`CQDn<n>`/`CLEn<n>` in both frameworks alike.

## Input scheme (EW)

Before Feynman rules are computed, the mass-basis Lagrangian can be rewritten in terms of
electroweak inputs.

| `EWInputScheme` | Inputs | Lagrangian |
|---|---|---|
| **`"heft"`** *(default)* | `G1`, `GW`, `vev`, `hlambda` themselves — all `External` | Untouched. The Lagrangian and every downstream export stay written natively in `G1`/`GW`/`vev`/`hlambda`. `MZ` and `MW` are **predictions** (`Internal`): `MW = GW vev/2`, and `MZ` is the Lagrangian's Z mass including the one-insertion `P1`/`P12`/`PT` shifts. |
| **`"gf"`** | `Gf`, `MW`, `MZ`, `MH` | Rewritten, with a one-WC-insertion shift on top of the tree relation. |
| **`"aem"`** | `α<sub>EM</sub>`, `Gf`, `MZ`, `MH` | Rewritten, with a one-WC-insertion shift on top of the tree relation. |

**The relations can be found in the associated paper.**


## Wilson coefficients — the WCxf workflow

There is nothing to configure. Three fixed steps:

1. **Cell 3 writes two files** for your operator selection, every coefficient at its default:
   - `wcxf/wcxf_init.json` — an untouched reference copy. The model never reads it; it is there
     to look at, diff against, or copy back from.
   - `wcxf/wcxf_output.json` — **the file the model actually reads**.
2. **Optionally edit `wcxf_output.json`** in any text editor. Deleting a key has the same effect
   as writing `0`, since absent keys are read as zero.
3. **Cell 5 reads it exactly as it stands on disk** and prints every value that differs from the
   default, so you can check at a glance what it picked up.

**Cell 3 rewrites `wcxf_output.json` back to the defaults every time it runs.** Edit *after*
Cell 3, not before; if you re-run it after editing, it lists the values it is about to discard.
After changing `EFTOperators` you *must* re-run Cell 3 — a file written for the old selection
has no keys for the new operators.

**Coefficient counts grow fast.** A 2F operator has `(HiggsMaxOrder+1) × 3²` independent
entries and a 4F operator `(HiggsMaxOrder+1) × 3⁴` — at `HiggsMaxOrder = 2`, `NQ1` contributes
27 keys and `RQ1` contributes 243. Selecting many four-fermion operators makes
`wcxf_output.json` large.

Flavour multiplicity is **fixed at 3 generations**; it is not a configuration option.

## Adding your own operators

Two files are reserved for operators you define yourself, and nothing else in the model has to
change:

- **[`model_files/Lagrangian/Lagrangian_User.fr`](model_files/Lagrangian/Lagrangian_User.fr)** —
  the Lagrangian terms;
- **[`model_files/parameters/parameters_User.fr`](model_files/parameters/parameters_User.fr)** —
  their flare functions and Wilson coefficients.

Both are loaded after the SM and EFT files, so every building block of the model is available
in them. They ship with `PGHD1`, `PGHD2` and `SGHD` as a worked example to copy. **An operator
is four entries in four places.** The steps below follow `PGHD1`.

**Naming.** A label `<label>` (what goes into `EFTOperators`) has a Lagrangian `L<label>`, a
flare function `FC<label>`, and coefficients `C<label>n<n>`, one per power `n` of `h/v`. Never
put the leading `L` into `EFTOperators`.

### Step 1 — the Lagrangian term (`Lagrangian_User.fr`)

```mathematica
LPGHD1 := Block[{mu, nu, ga, a},
  -WCOrder*ChiralOrder^2/LamHEFT^2 1/vev^4 gs^2 1/4 del[H, mu] del[H, nu]
      FS[Gl, mu, ga, a] FS[Gl, nu, ga, a] FCPGHD1[H, NEFT]
];
```

- **Dummy indices** go in the `Block`.
- `ChiralOrder^n` with `n` the operator's chiral, energy scale `LamHEFT` to ensure proper dimansionality. `WCOrder` is what keeps the model at [one insertion per
  vertex](#one-wilson-coefficient-insertion-per-vertex).
- **Multiply by the flare function `FC<label>[H, NEFT]` and by no coefficient of your own** —
  the Wilson coefficients live inside the flare. **One flare per term**: an operator that
  multiplies two of them is refused at load time (see
  [Two derivatives on two flares](#two-derivatives-on-two-flares-one-combined-coefficient)).
- **Do not touch the gauge kinetic terms or the input relations.** Those are the two places the
  model expands to first order in `WCOrder`; an operator that modified them would add a third
  source of coefficient products that nothing re-expands.

### Step 2 — make it selectable (`Lagrangian_User.fr`)

Add one line to **each** of the two selection blocks at the bottom of the file:

```mathematica
If[HEFTPieceActiveQ["PGHD1"], LUseraux += LPGHD1];     (* in the LUseraux block     *)
If[HEFTPieceActiveQ["PGHD1"], aux += LPGHD1];          (* inside HEFTRebuildLUser[] *)
```

`HEFT_Model.fr` rebuilds the user Lagrangian with `HEFTRebuildLUser[]` after the model has
loaded, so **the second line is the one that counts** — forgetting it drops the operator with
no message at all, while its coefficients are still declared and still written to
`wcxf_output.json`, so nothing downstream looks wrong. Check that the coefficients really
appear in `LHEFT` after Cell 5.

### Step 3 — declare the flare and its coefficients (`parameters_User.fr`)

One row in `userScalarFlareSpecs`:

```mathematica
userScalarFlareSpecs = {
  {FCPGHD1,  "PGHD1",  "CPGHD1n",  0},
  ...
};
```

The four fields are the flare symbol, the label, the coefficient prefix and `nmin`. From that
row the model builds

```
FCPGHD1[h, NEFT] = Σ_{n = nmin}^{NEFT} CPGHD1n<n> · (LamF h/vev)^n
```

only when the label is selected, and declares every coefficient as an `External` parameter, so
it appears in the parameter card and in the WCxf files. **Use `nmin = 1` if the flare sits
under a derivative** — a constant there drops out, and the load aborts otherwise. These rows
are for bosonic, flavour-blind operators; a fermionic one needs flavour-tensor flares instead
(`ferm2FFlareSpecs` / `ferm4FFlareSpecs` in `parameters_EFT_2F.fr` / `parameters_EFT_4F.fr`
show how).

### Step 4 — register the label (`wcxf_input.fr`, `heft_notebook_reference.wl`)

```mathematica
(* wcxf_input.fr, in HEFT1604ScalarOpPrefixes — same label, prefix and nmin as Step 3 *)
{"PGHD1", "CPGHD1n", 0},

(* heft_notebook_reference.wl, in HEFT$Catalog1604Higher *)
{"PGHD1", "PGHD2", "SGHD"},

(* heft_notebook_reference.wl, in HEFT$OperatorChiralOrder — the same n as in Step 1 *)
Thread[{"PGHD1", "PGHD2", "SGHD"} -> 2],
```

The first generates the WCxf keys; without it the coefficients never reach
`wcxf_output.json`, and absent keys are read as **0**. The second is the catalogue Cell 3
validates `EFTOperators` against — an unlisted label is refused as unknown. The third is the
chiral-order label printed by the Reference cell and exported as a UFO coupling order; the two
must agree with the power in Step 1, and the load-time check compares the prefix and `nmin` of
Steps 3 and 4 against each other.

### Using user-defined operators

```mathematica
EFTOperators = {"PGHD1"};
```

Then run the notebook as usual. The `_User.fr` files are part of the cache's model digest, so
**any edit to them invalidates every cached `LHEFT`** and the next Cell 5 rebuilds. To check an
operator came out as intended, look at its vertices in the Cell 6 Feynman-rule output before
exporting.

## Exports

There is no `OutputFormat` option — the cell you evaluate *is* the choice.

| Cell | Writes | Notes |
|---|---|---|
| **6** | `output/FeynmanRules/<OutputName>/` | `.mx` (reload with `Get`), `.txt` (every vertex in plain text), `latex/<OutputName>.tex` (a standalone LaTeX document). Optional — Cells 7 and 8 never read it. |
| **7** | `output/UFO/<OutputName>/` | For MadGraph. Carries `ChiralOrder` and `WCOrder` as coupling orders. |
| **8** | `output/FeynArts/<OutputName>/` | `.mod`, `.gen`, `.pars`. For FeynArts / FeynCalc. |

## The LHEFT cache

Cell 5 saves and reloads the evaluated mass-basis Lagrangian under `HEFT_cache/`, one
subfolder per configuration: `<OutputName>__<configHash>/{LHEFT.mx, meta.json}`. The hash is an
8-hex-digit MD5 over every physics setting that goes into the build, including a digest of the
`.fr` sources — **the lookup is by configuration, never by name**; `OutputName` is in the folder
name only so the directory is readable by eye.

1. **Hit under the current name** — loaded.
2. **Hit under a different name** — reported, loaded, and your name is appended to that entry's
   `names` list. The `.mx` is deliberately not copied: one copy is reachable from every name,
   and an `.mx` runs to hundreds of MB with full three-generation Wilson tensors.
3. **Miss** — built fresh, and always saved.

**Cells 3 and 4 report the verdict before you start Cell 5**, so a multi-hour build is never a
surprise; on a miss they also print how long the closest previous build took.

| Change | Rebuild? |
|---|---|
| `EFTOperators`, `HiggsMaxOrder`, `EWInputScheme`, `KappaFramework`, `LOYukawaExpansion`, `Massless`, `DiagonalCKM`, or any `.fr` source | **Yes** — unless that exact configuration was built before, under any name |
| Wilson-coefficient **values**, zeros included | **No.** Every coefficient is an `External` parameter, so a value never enters `LHEFT`; it reaches the export through `M$Parameters`. No coefficient is part of the cache key. |
| `MaxVertexLegs`, `InitialiseWCs`, `OutputName`, export format | **No** |

`ForceRebuildLHEFT = True` is the only override. Editing any model file changes the digest, so
**every existing cache entry is invalidated automatically** by a source edit — including edits
to your own `_User.fr` operators.

## Merging cached models

The expensive step is not `LoadModel` (1–2 s) but the `ExpandIndices` pass, which grows faster
than the operator count. Measured at `HiggsMaxOrder = 2`, `"heft"`: `{P1}` 12 s, `{P12}` 14 s,
`{PW}` 7 s — but a single build of all three takes **45 s**. Merging the three cached pieces takes
**4 s**, and gives the same 105 vertices with identical couplings.

[`heft_fr_merge_models.wl`](heft_fr_merge_models.wl) does exactly that. `ExpandIndices` is
linear in the Lagrangian, so for *N* sub-models

```
LHEFT(A ∪ B ∪ …) = Σ_i LHEFT(i) − (N − 1) · LHEFT(SM baseline)
```

The SM baseline must be subtracted explicitly: each sub-model carries the whole LO Lagrangian,
so adding *N* of them without it would scale every SM vertex by *N*.

Its Cell 3 lists every cached model built with your configuration — **you never need to know a
cache hash**; selection is by name. Cells 6, 7 and 8 are literally the same cells as the main
notebook, `Get` from the same file rather than copied.

**Merging is exact here**, because the model keeps [one EFT insertion per
vertex](#one-wilson-coefficient-insertion-per-vertex): the places where operators would mix
non-linearly — the A–Z rotation and the input-scheme shifts — are themselves linear in
`WCOrder`, so nothing cross-couples two sub-models.

**What must agree:** every cache key except the operator list. **Refused, not warned about:**
any hashed option differing between sub-models, a missing SM baseline, an operator appearing
twice, and a cache entry listed twice.


## Performance

The dominant cost depends on `HiggsMaxOrder`. At `HiggsMaxOrder = 2` the **build** dominates
and merging is the answer. At `HiggsMaxOrder = 3` the **export** does. Measured on
`{PG, PW, P12}`, `HiggsMaxOrder = 3`, `EWInputScheme = "heft"`, `MaxVertexLegs = Automatic`, all
other options at their defaults, all cells in one kernel (Intel i7-9750H, 6 cores, Mathematica
14.0):

| Stage | Seconds (wall) | Result |
|---|---|---|
| Cell 3 — configuration, WCxf files | 12.3 | |
| Cell 5 — build (cache miss) | 26.0 | `LHEFT`: 567 terms |
| Cell 6 — `FeynmanRules` | 82.5 | 183 vertices |
| Cell 7 — `WriteUFO` | 118.2 | 211 vertices in `vertices.py` |
| Cell 8 — `WriteFeynArtsOutput` | 70.7 | 91 couplings in the `.mod` file |

Cells 6, 7 and 8 each read `LHEFT` independently, so an export costs only the cells you run:
UFO alone is ~2 min here, FeynArts alone ~1 min. On a cache hit, Cell 5 takes a second or two.


## Repository layout

```
heft_fr_notebook.wl        THE entry point — open this
heft_fr_merge_models.wl    build a large model by merging cached small ones

model_files/               the model source
  HEFT_Model.fr              master file: loads everything, assembles LHEFTMassBasis
  fields.fr                  field and particle declarations
  definitions.fr             chiral building blocks (U, V_μ, T, field strengths), unitary gauge
  power_counting.fr          the ChiralOrder / WCOrder / LamF bookkeepers
  gauge_normalization.fr     gauge-field normalisations and the A–Z mixing matrix
  input_scheme.fr            EW input schemes, applied at the end of the mass-basis build
  wcxf_input.fr              WCxf reading/writing, key tables and operator activation
  parameters/
    parameters_SM.fr           SM parameters, the Kappa/Delta sets, the WC declaration helpers
    parameters_EFT.fr          shared EFT machinery: flare and coefficient-table builders
    parameters_EFT_Bosonic.fr  bosonic flare and coefficient specs
    parameters_EFT_2F.fr       two-fermion specs
    parameters_EFT_4F.fr       four-fermion specs
    parameters_User.fr         YOUR operators' flares and coefficients
  Lagrangian/
    Lagrangian_SM.fr           the LO (SM-like) Lagrangian
    Lagrangian_EFT_Bosonic.fr  bosonic operators
    Lagrangian_EFT_2F.fr       two-fermion operators
    Lagrangian_EFT_4F.fr       four-fermion operators
    Lagrangian_User.fr         YOUR operators
  heft_fr.wl                 the engine behind notebook Cells 3–8
  heft_fr_merge.wl           the engine behind the merge notebook
  lheft_cache.wl             the build cache
  lheft_merge.wl             the merge arithmetic
  heft_latex_export.wl       LaTeX writer for the Feynman rules
  heft_notebook_reference.wl the Cell 1 reference tables, operator catalogue and chiral orders
  heft_defaults.wl           fallback values for unset options, and the removed-option check

wcxf/                      Wilson coefficients: wcxf_init.json (reference) + wcxf_output.json (read)
restrictions/              Massless.rst, DiagonalCKM.rst
HEFT_cache/                built Lagrangians, one folder per configuration  (generated)
output/                    UFO/, FeynArts/, FeynmanRules/ exports              (generated)
```

`HEFT_cache/` and `output/` are created on demand; nothing needs to exist there beforehand.

## Rules of the road

**One run per kernel.** Quit the kernel (*Evaluation ▸ Quit Kernel*) before every run.
LoadModel is not idempotent: a second call re-declares the model on top of the live
FeynRules state and corrupts it. The notebook therefore refuses rather than resets — Cell 5
refuses a second LoadModel, and Cell 3 refuses to run unless Cell 2 has been evaluated.
Cells 1–4 and 6–8 are safe to re-run; restarting is cheap, since LHEFT is on disk.

## Known limitations

**No general Rξ gauge.** The model is **unitary gauge** only.

**One operator set.** - 1604.06801 only, whichis **not a complete basis**.

**Only single insertions of the EFT Wilson coefficients.** Every vertex is linear in WCs.

**No assumptions on the fermionic Wilson coefficients.** Every flavour entry is an independent
free parameter — 3×3 per 2F operator and 3⁴ per 4F operator, per power of `h/v`. The model
imposes **no** flavour symmetry, no MFV ansatz, no hermiticity or exchange relation between
entries, and no relation between operators; the only assumption is that the coefficients are
real.

**All Wilson coefficients are real.** 

**Flavour is fixed at 3 generations.** 

**One `LoadModel` per kernel.** See [Rules of the road](#rules-of-the-road).

## Authors

**Michał Ryczkowski** — <michaljakub.ryczkowski@unipd.it>

*Dipartimento di Fisica e Astronomia "G. Galilei", Università di Padova, and INFN, Sezione di
Padova, Via F. Marzolo 8, I-35131 Padova, Italy*

Released under the MIT License — see [LICENSE](LICENSE).

---
