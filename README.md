# HEFT-FR

**A FeynRules implementation of the Higgs Effective Field Theory (HEFT).**

HEFT-FR builds the electroweak chiral Lagrangian with a singlet Higgs, in the mass basis,
from an operator set you choose — and exports it as a **UFO** model for MadGraph or as
**FeynArts** model files. It is organised as a double expansion: in **chiral dimension** and
in **powers of `h/v`**.


- **Version 0.5** · MIT licensed · see [Authors](#authors)
- **Entry point:** [`heft_fr_notebook.wl`](heft_fr_notebook.wl) — open it in Mathematica and
  evaluate cell by cell. Nothing else needs editing.

---

## Contents

- [What you get](#what-you-get)
- [References and bases](#references-and-bases)
- [Requirements](#requirements)
- [Quick start](#quick-start)
- [Configuration options](#configuration-options)
- [The Kappa and Delta frameworks](#the-kappa-and-delta-frameworks)
- [Input scheme (EW)](#input-scheme-ew)
- [Wilson coefficients — the WCxf workflow](#wilson-coefficients--the-wcxf-workflow)
- [Operators by Chiral Dimension](#operators-by-chiral-dimension)
- [Exports](#exports)
- [The LHEFT cache](#the-lheft-cache)
- [Merging cached models](#merging-cached-models)
- [Performance](#performance)
- [Repository layout](#repository-layout)
- [Rules of the road](#rules-of-the-road)
- [Known limitations](#known-limitations)
- [Deferred configuration options](#deferred-configuration-options)
- [Authors](#authors)

---

## What you get

- **The complete NLO HEFT basis of [Brivio et al. 1604.06801](https://arxiv.org/abs/1604.06801)** —
  bosonic, two-fermion (2F) *and* four-fermion (4F) operators. That is 41 bosonic, 56 2F and
  56 4F operator labels, each with its own flare-function tower of Wilson coefficients.
- **Example NNLO operators** (chiral dimension 2) as an extension beyond that basis — worked
  examples, not a complete NNLO basis.
- **A pick-and-choose operator selection.** You name the operators you want; everything else
  stays out of the Lagrangian entirely, rather than being present with a zero coefficient.
- **Wilson coefficients in [WCxf](https://arxiv.org/abs/1712.05298) JSON** — written out for
  your selection, edited in a text editor, read back into the export.
- **Three electroweak input schemes**, with the SMINPUTS-style ones derived from the model's
  *own* Lagrangian rather than copied from a paper.
- **A build cache**, so the expensive step happens once per physics configuration, and a
  **merge facility** that assembles a large model out of small cached ones by arithmetic.
- **UFO and FeynArts exports**, plus optional plain-text and LaTeX listings of the Feynman
  rules.

## References and bases

The implementation follows the notation and conventions of Brivio et al. throughout.

| | Reference |
|---|---|
| **NLO operator basis** | I. Brivio, J. Gonzalez-Fraile, M.C. Gonzalez-Garcia, L. Merlo, *The complete HEFT Lagrangian after the LHC Run I*, [arXiv:1604.06801](https://arxiv.org/abs/1604.06801) — **the basis this model implements** |
| Alternative basis | H. Sun, X. Wang, et al., [arXiv:2206.07722](https://arxiv.org/abs/2206.07722) — **not implemented**; the operator catalogue can be previewed in Cell 1, but selecting it is refused |
| Framework | A. Alloul, N. Christensen, C. Degrande, C. Duhr, B. Fuks, *FeynRules 2.0*, [arXiv:1310.1921](https://arxiv.org/abs/1310.1921) |
| Coefficient exchange format | J. Aebischer et al., *WCxf: an exchange format for Wilson coefficients*, [arXiv:1712.05298](https://arxiv.org/abs/1712.05298) |

**Power counting.** Two bookkeeping parameters organise the Lagrangian:

- **`LamHEFT`** — chiral dimension. LO operators carry no factor, NLO carries `LamHEFT^1`,
  NNLO `LamHEFT^2`. `HEFTMaxOrder` truncates the series.
- **`LamF`** — the `h/v` expansion inside every flare function. `HiggsMaxOrder` (internally
  `NEFT`) truncates it.

A flare function is just
`F_op(h) = Σ_n C_op_n<n> · (LamF · h/v)^n`, so **every term of the expanded Lagrangian
carries exactly one Wilson coefficient**, named after its operator and its `h`-power.

## Requirements

- **Mathematica** (any version FeynRules supports).
- **FeynRules** — install it yourself and point `$FeynRulesPath` at the directory containing
  `FeynRules.m`. This is the first line of the Configuration cell.

No installation step: clone the repository and open the notebook.

## Quick start

Open [`heft_fr_notebook.wl`](heft_fr_notebook.wl) in Mathematica and work down it. Every path
is resolved relative to the file itself, so the repository can live anywhere.

> **Quit the kernel before every run.** *Evaluation ▸ Quit Kernel*. See
> [Rules of the road](#rules-of-the-road) — this one matters.

| Cell | What it does |
|------|--------------|
| **1 — Reference** | Prints what this model is, the full configuration-option table, and the operator catalogue of the selected basis. No FeynRules, no model loading; safe to re-run any time you need to look up a label. |
| **2 — Configuration** | The single place every run option is set. Re-evaluate it after every change. |
| **3 — Banner and coefficient files** | Loads FeynRules, echoes the active configuration, and writes `wcxf/wcxf_init.json` and `wcxf/wcxf_output.json` for exactly your operator selection. Closes with the cache verdict, so you know before Cell 5 whether it will load or build. |
| **4 — Edit coefficients** *(optional)* | Skip it for defaults. Otherwise edit `wcxf/wcxf_output.json` in a text editor; this cell just prints the paths and re-runs the cache lookup. |
| **5 — Build** | `LoadModel`, restrictions, then `LHEFT` — the mass-basis Lagrangian. Loads from cache when this exact configuration has been built before; otherwise builds from scratch (minutes to hours). |
| **6 — Feynman rules** *(optional)* | `RulesHEFT = FeynmanRules[LHEFT]`, saved as `.mx`, plain text and a standalone LaTeX document. Cells 7 and 8 do **not** need this. |
| **7 — UFO export** | Writes `output/UFO/<OutputName>/`. |
| **8 — FeynArts export** | Writes `output/FeynArts/<OutputName>/` (`.mod`, `.gen`, `.pars`). |

Cells 7 and 8 are independent — run either, or both. Both need only `LHEFT` from Cell 5.

## Configuration options

Everything below lives in **Cell 2**. Cell 1 prints the same table with the allowed values;
[`model_files/heft_defaults.wl`](model_files/heft_defaults.wl) holds the fallback used for
anything you leave unset.

### Physics and expansion

| Option | Default | Meaning |
|---|---|---|
| `HEFTGauge` | `"unitary"` | The only supported value. See [Known limitations](#known-limitations). |
| `HEFTMaxOrder` | `1` | Chiral-order truncation: `0` = LO only, `1` = NLO, `2` = NNLO. `2` requires `EWInputScheme = "heft"`. |
| `HiggsMaxOrder` | `3` | Highest power of `h/v` kept in every flare function. The single strongest driver of build and export cost. |
| `KappaFramework` | `True` | `True` → Kappa (multiplicative) parameterisation of SM-coupling deviations; `False` → Delta (additive). See [below](#the-kappa-and-delta-frameworks). |
| `LOYukawaExpansion` | `True` | Keep the multi-Higgs tower `FQU`/`FQD`/`FLE` (`n ≥ 2`) on top of the LO Yukawa. `False` drops it *and* does not declare `CQUn`/`CQDn`/`CLEn` at all. The fermion mass and the single-Higgs coupling are unaffected either way. |
| `IncludeCustodialT` | `True` | Keep the custodial-breaking operator `PT = Tr[T·V_μ] Tr[T·V^μ] F_T(h)` in the LO Lagrangian. `False` drops it, and with it the `CFTn` coefficients — `PT` is their only user. |
| `Combine2Derivatives` | `False` | See [below](#combine2derivatives). |
| `NLOOperators` | `{}` | The active operator labels. `{}` means LO only. Must come from the catalogue Cell 1 prints; an unknown label aborts Cell 3. |
| `HEFTNLOBasis` | `"1604.06801"` | The only implemented basis. |

### Inputs and restrictions

| Option | Default | Meaning |
|---|---|---|
| `EWInputScheme` | `"heft"` | `"heft"`, `"gf"` or `"aem"` — see [Input scheme (EW)](#input-scheme-ew). |
| `Massless` | `False` | Load `restrictions/Massless.rst`: light fermion masses set to zero, only τ, b and t stay massive. |
| `DiagonalCKM` | `False` | Load `restrictions/DiagonalCKM.rst`: CKM → identity. |

### Coefficients, output and cache

| Option | Default | Meaning |
|---|---|---|
| `InitialiseWCs` | `1` | Value written for the **effective** coefficients (`1` or `0`). SM couplings always keep their SM value regardless. See [below](#initialisewcs). |
| `OutputName` | — | Subdirectory name under `output/`, and the readable half of the cache folder name. |
| `MaxVertexLegs` | `Automatic` | Export-time cut on vertex multiplicity — see [below](#maxvertexlegs). |
| `ForceRebuildLHEFT` | `False` | Skip the cache lookup and rebuild. |

### `Combine2Derivatives`

Five NLO operators — `DH`, `P8NLO`, `P20NLO`, `P21NLO`, `P22NLO` — multiply **two**
independently truncated flare functions together through a derivative on each,
`∂_μF₁(h)·∂_νF₂(h)`. Expanded to a fixed power of `h/v`, a vertex's coefficient is then an
unavoidable *sum of products* of the two families. That is correct, but it overstates how many
free parameters the vertex really has: it only ever depends on that one fixed combination.

`Combine2Derivatives = True` **replaces** each operator's two families with a single combined
family `C<op>n<nh>prime` (spelled out, because `'` is not a legal UFO/FeynArts/WCxf character),
so each vertex carries one coefficient. The rewrite is exact — verified symbolically term by
term. The index `nh` counts the Higgs fields the term contributes to the vertex, differentiated
ones included, so it starts at 2 for the quadratic operators and at 4 for `DH`.

Neither mode ever declares a coefficient the Lagrangian cannot use. It changes `LHEFT`, so it
is part of the cache key.

### `InitialiseWCs`

Sets the value Cell 3 writes for every **effective** (beyond-SM) coefficient. The 13 SM
couplings (`KappaV`, `Kappa2V`, `Kappa3H`, `Kappa4H`, `KappaLE`…`KappaQB`, or their `Delta*`
counterparts) always keep their SM value — they rescale interactions the SM already has, so
zeroing them would not give you the SM, it would delete SM physics.

Note that the SM point depends on the framework: `κ = 1` with `KappaFramework = True`, `Δ = 0`
with `False`. `InitialiseWCs = 0` is the natural starting point for switching one coefficient
on at a time. It changes numbers in the JSON files and nothing in the Lagrangian, so it is
**not** part of the cache key.

### `MaxVertexLegs`

Caps the number of legs a vertex may have in the output. `Automatic` exports everything; an
integer `n ≥ 3` keeps only vertices with at most `n` legs. Honoured by Cells 6, 7 **and** 8 —
it becomes FeynRules' own `MaxParticles`, which the UFO and FeynArts writers forward to the
`FeynmanRules` call they make internally, so it really does shrink the exported model.

> Not to be confused with SmeftFR's option of the same name, which does *not* reach its UFO and
> FeynArts output. That is a property of SmeftFR, not of FeynRules, and does not apply here.

The cut is applied to Lagrangian *terms* before the vertex algebra, so it is a genuine
speed-up. Measured on `{GHNLO, WHNLO, P12NLO}`, `HiggsMaxOrder = 3`:

| `MaxVertexLegs` | Cells 6+7 | speed-up | vertices dropped |
|---|---|---|---|
| `Automatic` | 419.8 s | 1.00× | — |
| **`6`** | **221.0 s** | **1.90×** | 10 / 157 (6.4 %) |
| `5` | 155.3 s | 2.70× | 23 / 157 (14.6 %) |
| `4` | 123.7 s | 3.39× | 42 / 157 (26.8 %) |

High-multiplicity vertices are combinatorially the most expensive, which is why removing 6.4 %
of them buys 47 % of the time.

**Know what it costs.** The quartics it removes first are exactly the ones that unitarise
*VV → VV* — MadGraph will simply not have the diagram. And because the `h`-expansion is what
generates high multiplicities in HEFT, a leg cut acts as a *second, export-level* truncation of
the flare tower, while `wcxf_output.json` still lists every coefficient. Values below 3 are
refused: FeynRules returns no 1- or 2-point vertices at all, so a smaller cut would write an
empty model rather than a restricted one.

Not part of the cache key — you can re-export one cached build at several cuts for free.

## The Kappa and Delta frameworks

`KappaFramework` decides how deviations from SM couplings are parameterised, and **which names
are declared as parameters at all**. An exported model contains one side, never both.

| | `KappaFramework = True` | `KappaFramework = False` |
|---|---|---|
| Names | `KappaV`, `Kappa2V`, `Kappa3H`, `Kappa4H`, `KappaQU`… | `DeltaV`, `Delta2V`, `DeltaLam3`, `DeltaYQU`… |
| Form | multiplicative rescaling | additive shift |
| SM point | `1` | `0` |

In the 2F sector the fermion **mass** and the **single-Higgs (*hff*) vertex** are carried by
two separate tensors — `yu`/`yd`/`yl` for the mass, `yuH`/`ydH`/`ylH` for the vertex — so a
Kappa can vary the coupling *relative* to the mass without shifting the mass away from the
value used for the propagator. Above `n = 1`, the multi-Higgs tower `FQU`/`FQD`/`FLE` carries
`CQUn<n>`/`CQDn<n>/`CLEn<n>` in both frameworks alike.

## Input scheme (EW)

Before Feynman rules are computed, the mass-basis Lagrangian can be rewritten in terms of
SMINPUTS-style electroweak inputs.

| `EWInputScheme` | Inputs | `MW` | Lagrangian |
|---|---|---|---|
| **`"heft"`** *(default)* | `G1`, `GW`, `GS`, `vev`, `hlambda` themselves — all `External` | `External`, an input | Untouched. The Lagrangian and every downstream export stay written natively in `G1`/`GW`/`vev`/`hlambda`. |
| **`"gf"`** | `Gf`, `MW`, `MZ`, `MH` (+ `aS`) | `External`, an input | Rewritten, with an NLO shift on top of the tree relation. |
| **`"aem"`** | `aEWM1` (= 1/α<sub>EM</sub>), `Gf`, `MZ`, `MH` (+ `aS`) | **`Internal` — a *prediction***, `MW = GW·vev/2` | Same as `"gf"`. |

**The relations are read off the model's own mass-basis Lagrangian**, not copied from a paper,
so they are correct for *this* Lagrangian whatever normalisation convention a given operator
carries here:

```
MZ² = (G1² + GW²) v²/4
      + ChiralOrder · v²/2 · (CFTn0 (G1²+GW²) + 2 CP12NLOn0 GW² − 2 CP1NLOn0 G1 GW)
MW² = GW² v²/4                                       (no NLO shift at all)
e   = G1 GW ((1 + 2 ChiralOrder CP12NLOn0) G1²
             + 2 ChiralOrder CP1NLOn0 G1 GW + GW²) / (G1² + GW²)^(3/2)
```

### Chiral-order restriction — enforced, not advisory

| Scheme | Valid for |
|---|---|
| `"heft"` | **any** `HEFTMaxOrder` |
| `"gf"`, `"aem"` | `HEFTMaxOrder ≤ 1` **only** |

The derived schemes invert an extraction that exists at O(`ChiralOrder`) only. At
`HEFTMaxOrder ≥ 2` the Lagrangian carries NNLO operators the extraction knows nothing about,
so the inputs would come out *silently* NLO-accurate while everything around them is not — no
message, no failure, just wrong numbers in the parameter card and in the Lagrangian.

The combination is refused **twice**, so no entry point can slip past it: once in Cell 3, before
any expensive work, and again inside `LoadModel` (`HEFTEWInputSchemeCheckOrder[]`), which covers
headless scripts that `Get` `HEFT_Model.fr` directly. Use `"heft"` at NNLO and beyond.

There is **no CKM input scheme** — see
[Deferred configuration options](#deferred-configuration-options). `DiagonalCKM` is the only
CKM-related switch.

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
After changing `NLOOperators` you *must* re-run Cell 3 — a file written for the old selection
has no keys for the new operators.

**A zero does not remove an operator.** Operator selection is `NLOOperators` alone. A zeroed
coefficient leaves its operator in `LHEFT` with the value `0`. If you do not want an operator,
leave it out of the list.

**Coefficient counts grow fast.** A 2F operator has `(HiggsMaxOrder+1) × 3²` independent
entries and a 4F operator `(HiggsMaxOrder+1) × 3⁴` — at `HiggsMaxOrder = 2`, `NQ1NLO`
contributes 27 keys and `RQ1NLO` contributes 243. Selecting many four-fermion operators makes
`wcxf_output.json` large.

Flavour multiplicity is **fixed at 3 generations**; it is not a configuration option.

## Operators by Chiral Dimension

Cell 1 prints the full catalogue with `PrintHigherOrder = True` for the NNLO block. The labels
below are exactly what goes into `NLOOperators`.

### Leading order — chiral dimension 0

The Standard Model in HEFT form, always present:

- **Gauge sector** — U(1), SU(2) and SU(3) field strengths, plus the QCD θ term.
- **Gauge–Higgs sector** — the chiral-connection terms with flare functions `F_C` and `F_T`.
  `F_T` belongs to the custodial-breaking `PT`, controlled by `IncludeCustodialT`.
- **Fermion kinetic terms** for all quarks and leptons.
- **Higgs sector** — kinetic term and potential, with the cubic and quartic deviations
  `Kappa3H`/`Kappa4H` (or `DeltaLam3`/`DeltaLam4`) and a flare tower from `h⁵` upward.
- **Yukawa sector** — the fermion mass, the single-Higgs coupling, and the multi-Higgs tower
  `FQU`/`FQD`/`FLE` (`LOYukawaExpansion`).

### Next-to-leading order — chiral dimension 1

The complete 1604.06801 basis. All labels carry the `NLO` suffix.

**Bosonic — scalar and gauge kinetic (7)**
`DH`, `GHNLO`, `GHtildeNLO`, `WHNLO`, `WtildeHNLO`, `BHNLO`, `BtildeHNLO`

**Bosonic — cubic gauge (4)**
`GGGNLO`, `WWWNLO`, `WWWtildeNLO`, `GGGtildeNLO`

**Bosonic — CP-even, the *P* operators (19)**
`P1NLO`, `P2NLO`, `P3NLO`, `P4NLO`, `P5NLO`, `P6NLO`, `P8NLO`, `P11NLO`, `P12NLO`, `P13NLO`,
`P14NLO`, `P17NLO`, `P18NLO`, `P20NLO`, `P21NLO`, `P22NLO`, `P23NLO`, `P24NLO`, `P26NLO`

**Bosonic — CP-odd, the *S* operators (11)**
`S1NLO`, `S2NLO`, `S2DNLO`, `S3NLO`, `S4NLO`, `S5NLO`, `S6NLO`, `S7NLO`, `S8NLO`, `S9NLO`,
`S15NLO`

**Two-fermion (56)**

| Family | Labels | Structure |
|---|---|---|
| Quark | `NQ1NLO`–`NQ36NLO` | `NQ1`–`NQ8` pure **V** chains; `NQ9`–`NQ10` dual-flare (two derivatives of two form factors); `NQ11`–`NQ20` chirality-flipping via the chiral connection; `NQ21`–`NQ28` σ^{μν}V_μ with ∂_ν; `NQ29`–`NQ36` σ^{μν} with field strengths (B, G, W) |
| Lepton | `NL1NLO`–`NL17NLO` | `NL1`–`NL14` follow eq. 2.20; `NL15`–`NL17` are the eq. 2.21 flavour structures, valid only off-diagonal (enforced with `1 − δ_{ff1,ff2}`) |
| Lepton, extra flavour structures | `NLF1NLO`–`NLF3NLO` | eq. 2.21 |

Coefficients carry two flavour indices, `C<op>n<n>[ff1, ff2]`, which FeynRules expands as
`C<op>n<n>x<ff1>x<ff2>`.

**Four-fermion (56)**

| Family | Labels | Indices |
|---|---|---|
| Four-quark | `RQ1NLO`–`RQ26NLO` | `[ff1, ff2, ff3, ff4]` |
| Quark–lepton | `RQL1NLO`–`RQL23NLO` | `ff1`, `ff2` lepton legs; `ff3`, `ff4` quark legs |
| Four-lepton | `RL1NLO`–`RL7NLO` | `[ff1, ff2, ff3, ff4]` |

The dual-flare operators `NQ9`, `NQ10` and `NL3` are the one exception to "one coefficient per
term": each half of `∂_μF · ∂^μF'` carries its own tensor, so a term goes as `C¹_n · C²_m`.
Both halves start at `n = 1`, since a constant under `∂` drops out.

### Next-to-next-to-leading order — chiral dimension 2

Implemented as an extension beyond the 1604.06801 basis, and shipped as **worked examples
rather than a complete NNLO basis**. They need `HEFTMaxOrder ≥ 2`, which in turn forces
`EWInputScheme = "heft"`.

`GHNNLO1`, `GHNNLO2`, `GHtildeNNLO`, `WLh2WRD2NNLO`, `WLh3D4NNLO`

## Exports

There is no `OutputFormat` option — the cell you evaluate *is* the choice.

| Cell | Writes | Notes |
|---|---|---|
| **6** | `output/FeynmanRules/<OutputName>/` | `.mx` (reload with `Get`), `.txt` (every vertex in plain text), `latex/<OutputName>.tex` (a standalone LaTeX document). Optional — Cells 7 and 8 never read it. |
| **7** | `output/UFO/<OutputName>/` | For MadGraph. |
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
| Operators, basis, expansion orders, gauge/scheme, restrictions, `.fr` sources | **Yes** — unless that exact configuration was built before, under any name |
| Wilson-coefficient **values**, zeros included | **No.** Every coefficient is an `External` parameter, so a value never enters `LHEFT`; it reaches the export through `M$Parameters`. No coefficient is part of the cache key. |
| `MaxVertexLegs`, `InitialiseWCs`, `OutputName`, export format | **No** |

`ForceRebuildLHEFT = True` is the only override.

## Merging cached models

The expensive step is not `LoadModel` (1–2 s) but the `ExpandIndices` pass, which grows sharply
with operator count. Measured at `HiggsMaxOrder = 2`: `{P1NLO}` 12 s, `{P12NLO}` 16 s,
`{WHNLO}` 13 s — but a single build of all three takes **168 s**. Merging the three cached
pieces takes **4 s**.

[`heft_fr_merge_models.wl`](heft_fr_merge_models.wl) does exactly that. `ExpandIndices` is
linear in the Lagrangian, so for *N* sub-models

```
LHEFT(A ∪ B ∪ …) = Σ_i LHEFT(i) − (N − 1) · LHEFT(LO)
```

The LO baseline must be subtracted explicitly: each sub-model carries the whole LO Lagrangian,
so adding *N* of them without it would scale every SM vertex by *N*.

Its Cell 3 lists every cached model built with your configuration — **you never need to know a
cache hash**; selection is by name. Cells 6, 7 and 8 are literally the same cells as the main
notebook, `Get` from the same file rather than copied.

**What must agree:** every cache key except the operator list. **Refused, not warned about:**
any hashed option differing between sub-models; `HEFTMaxOrder > 1` (merging is exact only at
linear order in `ChiralOrder`); a missing LO baseline; an operator appearing twice.

**Why arithmetic and not term matching.** FeynRules names summed dummy indices with
`$`-suffixed symbols whose counters diverge between kernels, and `Times` is `Orderless`, so
"rename in order of first appearance" is not canonical. More fundamentally, the LO sector is
not written the same way in two builds: activating `P1NLO`/`P12NLO`/`WHNLO`/`BHNLO` switches
`gauge_normalization.fr` to an algebraically equal but syntactically different A–Z branch, so
102 of 149 LO terms of an LO-only build do not appear verbatim in a `{P1NLO}` build. Addition
is immune to both.

The price: nothing cancels syntactically, so the merged Lagrangian is larger (+29 % in
`LeafCount` for two operators). FeynRules collapses it during vertex extraction and the
vertices come out identical — 105 vertices both ways, 0 of 105 couplings differing.

The result is an ordinary cache entry, with `mergedFrom` and `mergedLOBaseline` recorded in its
`meta.json`.

## Performance

The dominant cost depends on `HiggsMaxOrder`. At `HiggsMaxOrder = 2` the **build** dominates
and merging is the answer. At `HiggsMaxOrder = 3` the **export** does — measured on
`{GHNLO, WHNLO, P12NLO}`:

| Stage | Seconds |
|---|---|
| Cell 5 — build (cache miss) | 115.2 |
| Cell 6 — `FeynmanRules` | 188.8 |
| Cell 7 — `WriteUFO` | 231.0 |
| **Export total** | **419.8** |

Merging removes build cost and nothing else, so above `HiggsMaxOrder = 2` it is necessary but
not sufficient; [`MaxVertexLegs`](#maxvertexlegs) is the only lever on the term that then
dominates.

**Practical advice:** debug physics with a small `HiggsMaxOrder` (1–2) and a minimal operator
list, then widen for the final export — the cache means the expensive build runs once per
configuration. To build many sub-models for a merge, run several `wolframscript` kernels in
parallel: 6 concurrent kernels have been run without hitting a licence ceiling.

## Repository layout

```
heft_fr_notebook.wl        THE entry point — open this
heft_fr_merge_models.wl    build a large model by merging cached small ones

model_files/               the model source
  HEFT_Model.fr              master file: loads everything, assembles LHEFTMassBasis
  fields_LO.fr               field and particle declarations
  definitions.fr             chiral building blocks (U, V_μ, T, field strengths)
  power_counting.fr          LamHEFT / LamF bookkeeping
  gauge_normalization.fr     gauge-field normalisations and A–Z mixing
  input_scheme.fr            EW input schemes, applied at the end of the mass-basis build
  wcxf_input.fr              WCxf reading/writing and operator activation
  LO/                        parameters_LO.fr, Lagrangian_LO.fr
  NLO/basis_1604_06801/      the NLO basis: parameters + bosonic / 2F / 4F Lagrangians
  NNLO/                      chiral-dimension-2 example operators
  heft_fr.wl                 the engine behind notebook Cells 3–8
  heft_fr_merge.wl           the engine behind the merge notebook
  lheft_cache.wl             the build cache
  lheft_merge.wl             the merge arithmetic
  heft_latex_export.wl       LaTeX writer for the Feynman rules
  heft_notebook_reference.wl the Cell 1 reference tables and operator catalogue
  heft_defaults.wl           fallback values for unset configuration options

wcxf/                      Wilson coefficients: wcxf_init.json (reference) + wcxf_output.json (read)
restrictions/              Massless.rst, DiagonalCKM.rst
HEFT_cache/                built Lagrangians, one folder per configuration  (generated)
output/                    UFO/, FeynArts/, FeynmanRules/ exports              (generated)
```

`HEFT_cache/` and `output/` are created on demand; nothing needs to exist there beforehand.

## Rules of the road

**One run per kernel.** Quit the kernel (*Evaluation ▸ Quit Kernel*) before every run. The
notebook deliberately does not reset anything by itself — a partial reset would be worse than
none, since the state at risk is FeynRules' own, in its private contexts.

The reason is that **`LoadModel` is not idempotent**: FeynRules only *warns* on a second call
and then re-declares the model on top of the existing state. That state ends up corrupted —
`MR$GaugeGroupList` stops being a list, parameter definitions recurse to `$RecursionLimit`, and
in the cases that do not die outright you get an `LHEFT` that silently ignores `EWInputScheme`.

So the notebook refuses rather than resets:

- **Cell 5 refuses a second `LoadModel`** in one kernel and tells you to restart.
- **Cell 3 refuses to run** unless Cell 2 has been evaluated, so a Cell 3 pressed after a
  restart cannot silently fall back to defaults for every option you had chosen.

Cells 1, 2, 3, 4, 6, 7 and 8 are all safe to re-run; only Cell 5 carries this restriction.
Restarting costs almost nothing — `LHEFT` is on disk, so Cell 5 reloads it in seconds.

## Known limitations

- **Unitary gauge only.** An Rξ branch exists in the source (`definitions.fr`), with the
  Goldstone expansion pinned at order 1, but it is unfinished and unsupported. Setting
  `HEFTGauge = "rxi"` selects that branch; do not rely on the result.
- **One NLO basis.** Only 1604.06801 is implemented. `"2206.07722"` is refused, twice — at
  configuration time and inside `LoadModel`. Its catalogue can still be previewed in Cell 1.
- **All Wilson coefficients are real.** The CP-odd imaginary parts of the chirality-flipping
  and dipole operators (the `n0IM` tensors of eqs. 2.20/2.22) are not currently implemented.
- **Flavour is fixed at 3 generations** — not configurable.
- **The derived EW schemes are NLO-only.** `"gf"` and `"aem"` are refused above
  `HEFTMaxOrder = 1`; use `"heft"` at NNLO. See [Input scheme (EW)](#input-scheme-ew).
- **Indexed coefficients inside an `Internal` value hit a `WriteUFO` bug.** With `"gf"`/`"aem"`
  *and* `RL2NLO`/`RL5NLO` active, the input-scheme shift carries indexed external parameters
  into an `Internal` value, which `WriteUFO` does not handle. With those two operators
  inactive — the usual case — only scalars appear and the export is clean.
- **The NNLO set is a set of worked examples**, not a complete chiral-dimension-2 basis. NNNLO
  operators are not part of this release.
- **One `LoadModel` per kernel.** See [Rules of the road](#rules-of-the-road).

## Deferred configuration options

Two options were removed from the Configuration cell because the features they parametrised are
not implemented. **Both must be revisited when those features land** — the removal cleaned up a
user-facing surface that could not do anything; it was not a decision about the physics.

| Removed | Why | What to review, and when |
|---|---|---|
| **`GoldstoneMaxOrder`** | Only the Rξ branch reads it, and the model ships unitary gauge only. Now pinned at `1` near the top of `HEFT_Model.fr`; the Rξ code path is untouched and still honours it. | **When Rξ gauge is actually implemented.** Decide then whether order 1 is the right default, whether it should be user-selectable again, and **re-add it to the cache key** — otherwise two builds differing only in Goldstone order would collide on one cache entry. |
| **`CKMInputScheme`** | Its four values did nothing distinct: two were no-ops and the other two only did what `DiagonalCKM = True` does. It was never a CKM *input scheme* in the sense `EWInputScheme` is one — there was no extraction of CKM entries from chosen inputs. | **When a real CKM input scheme is implemented.** `HEFTCKMInputRepl` is now always empty. This costs nothing in practice: `DiagonalCKM = True` removes `CKM` from `LHEFT` anyway, because the restriction zeroes the Wolfenstein inputs and FeynRules substitutes the internal `CKM[i,j]` built from them during expansion. |

## Authors

**Michał Ryczkowski** — <michaljakub.ryczkowski@unipd.it>

*Dipartimento di Fisica e Astronomia "G. Galilei", Università di Padova, and INFN, Sezione di
Padova, Via F. Marzolo 8, I-35131 Padova, Italy*

Released under the MIT License — see [LICENSE](LICENSE).

If you use HEFT-FR in published work, please cite the HEFT basis
([arXiv:1604.06801](https://arxiv.org/abs/1604.06801)) and FeynRules
([arXiv:1310.1921](https://arxiv.org/abs/1310.1921)) alongside this repository.

---

*v0.5 — the complete NLO sector of the 1604.06801 basis, bosonic and fermionic (2F and 4F),
with example operators at chiral dimension 2.*
