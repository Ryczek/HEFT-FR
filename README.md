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
- [Merging FeynArts exports](#merging-feynarts-exports)
- [Merging UFO exports](#merging-ufo-exports)
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

**One deliberate deviation from 1604.06801:** `PDH` carries a factor `1/(4π)²`. The paper prints
`P_DH = (∂_μF_DH ∂^μF'_DH)²` without it, but its own NDA master formula gives `1/(4π)²` for
four derivatives on four Higgs fields, the same factor the paper puts on `P6`, `P8`, `P11` and
`P20`–`P22`. The model's `CPDHn<nh>prime` are therefore the paper's coefficients times `(4π)²`.


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
`RQ`/`RQL`/`RL` the four-fermion ones. The seven user examples, `PGHD1`, `PGHD2`, `SGHD` and
`PWHD1`, `PWHD2`, `SWHD`, `SWHDT`, are chiral order 2. The SM Lagrangian is always present and carries **no** `ChiralOrder` factor at
all. Cell 1 prints this same catalogue, grouped the same way.

### One Wilson-coefficient insertion per vertex

**Every exported vertex is at most linear in the HEFT Wilson coefficients.** The Lagrangian is
already linear term by term: each EFT operator carries exactly one `WCOrder`, as does each
Delta-framework deviation (`DeltaFCn1/2`, `DeltaLam3/4`, `dyuH`/`dydH`/`dylH`) and each flagged
`h/v` tower (`FFC`, `FVHiggs`, `FQU`/`FQD`/`FLE`). Kappa rescalings multiply interactions the SM
already has, and are deliberately **not** flagged.

Only three substitutions could put a *second* coefficient into a vertex, and all three are expanded to
first order in `WCOrder` and cut there:

1. **The A–Z rotation** — [`gauge_normalization.fr`](model_files/gauge_normalization.fr). `P1` (W³–B kinetic mixing) and `P12` (W³ rescaling) change the gauge kinetic matrix
   at `h⁰`, so `AZnorm` depends on `CP1n0` and `CP12n0` and enters every vertex with a W³ or B
   leg. All such contributions are linearised, so in the end every vertex contains at most one
   insertion of Wilson coefficient.

2. **The input relations** — [`input_scheme.fr`](model_files/input_scheme.fr).
Five HEFT operators change the tree-level relation: `P1`, `P12`, `PT` and
   `RL2`/`RL5`. Again, such contributions are linearised, so in the end every vertex contains at most one insertion of Wilson coefficient.

3. **The `S2D` field redefinition** — [`Lagrangian_EFT_Bosonic.fr`](model_files/Lagrangian/Lagrangian_EFT_Bosonic.fr).
   `S2D`'s `n = 1` term is a Z–h mixing, removed by `U → U e^{−iθσ3}` with `θ ∝ CS2Dn1·h/v`
   (1604.06801 §2.2). `LS2D` carries the result at first order: the redefinition acting on the SM
   `F_C` term and Yukawas (CP-odd Yukawas). Its `CS2Dn1²` terms and `θ` acting on other EFT
   operators (`CS2Dn1 × C_other`) are second order and are not included.

**At the amplitude level** more than one insertion is possible: two EFT vertices glued by a
propagator give `O(c²)`. Those products are exact, **except** where one of the three substitutions
above is involved, because their own second-order terms were cut at the vertex. An `O(c²)`
amplitude is therefore incomplete in products of `CP1n0`, `CP12n0` (A–Z rotation), of `CP1n0`, `CP12n0`, `CPTn0`,
`CRL2n0`, `CRL5n0` (in `"gf"`/`"aem"`), and of `CS2Dn1`, with any coefficient. Everything at `O(c)` is exact. To
keep only `O(c)`, restrict `WCOrder` in MadGraph.

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
  containing `FeynRules.m`. This is the first line of the Configuration cell. An unmodified
  FeynRules is enough: the two corrections HEFT needs in its FeynArts writer are applied in
  memory by Cell 8 (see [Exports](#exports)).

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
| `FeynArtsDiracIndices` | `Automatic` | Fermion form of the FeynArts export: `Automatic` = FeynRules' choice, `True` = explicit Dirac indices always. Needed to merge FeynArts exports with four-fermion operators — see [Exports](#exports). |
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

**Predicted masses in propagators (limitation).** When a gauge-boson mass is a prediction, its declared
value contains the Wilson coefficients, and MadGraph uses it in the **full propagator with the shifted
mass**, `m = m_SM + δm`, `δm` linear in the coefficients. The pole moves, the amplitude is not strictly
linear in the coefficients (`m²` contains `δm²`), and this dependence is not counted by `WCOrder`. This is
the default treatment of SMEFTsim 3.0. Which masses and operators are affected:

| `EWInputScheme` | Shifted mass | Operators |
|---|---|---|
| `"heft"` | `MZ` | `P1`, `P12`, `PT` |
| `"aem"` | `MW` | `P1`, `P12`, `PT`, `RL2`, `RL5` |
| `"gf"` | none | — |

`MW` in `"heft"` is predicted (`GW·vev/2`) but receives no shift. Fermion, Higgs and the remaining gauge
masses are inputs in every scheme, and widths are inputs and never shifted.

**Recommendation: use `"gf"`** (`Gf`, `MW`, `MZ`, `MH`). Both gauge-boson masses are inputs there, so no
Wilson coefficient reaches a propagator — the choice SmeftFR makes in all its schemes and the one SMEFTsim
recommends.


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
in them. They ship with two sets of examples to copy: the gluon-Higgs operators `PGHD1`,
`PGHD2`, `SGHD`, and the W-Higgs operators `PWHD1`, `PWHD2`, `SWHD`, `SWHDT` (below). **An operator
is four entries in four places.** The steps below follow `PGHD1`.

**The W-Higgs examples** are HEFT analogues of SMEFT's `Q_{W²H²D²}`. In each, the covariant
derivative becomes an ordinary one and each Higgs doublet a flare function:

| Label | From | Structure |
|---|---|---|
| `PWHD1` | `Q^{(1)}` | `∂^μF ∂^νF W^I_{μρ} W^{Iρ}_ν` |
| `PWHD2` | `Q^{(2)}` | `∂_μF ∂^μF W^I_{νρ} W^{Iνρ}` |
| `SWHD` | `Q^{(3)}` | `∂_μF ∂^μF W^I_{νρ} W̃^{Iνρ}` |
| `SWHDT` | `Q^{(5)}` | `ε^{IJK} t^I ∂^μF ∂^νF (W^J_{μρ} W̃^{Kρ}_ν − W̃^J_{μρ} W^{Kρ}_ν)`, `t^I = Tr[Tσ^I]/2` |

`∂^μF ∂^νF` is written as one combined flare, like `P8`: `∂^μh ∂^νh FC<label>Combined` with
coefficients `C<label>n<nh>prime`, `nh = 2…2N`. The prefactor is
`WCOrder ChiralOrder²/Λ²`, which with the flare's `1/v²` is the NDA size (2511.23410 eq. 3.2) for `C ~ 1`. `τ^I` of `Q^{(4)}`–`Q^{(6)}` has no doublet to act on, so it
is replaced by the custodial spurion `T`. With that, the analogues of `Q^{(4)}` and `Q^{(6)}`
vanish identically (a symmetric `∂^μF ∂^νF` against an antisymmetric gauge factor) and are not
included; `SWHDT` breaks custodial symmetry. The gluon examples are built the same way:
`PGHD1`, `PGHD2`, `SGHD` are the `Q^{(1)}`–`Q^{(3)}` structures with gluon field strengths.

**Naming.** A label `<label>` (what goes into `EFTOperators`) has a Lagrangian `L<label>`, a
flare function, and coefficients:
- an ordinary flare `FC<label>`, coefficients `C<label>n<n>`, one per power `n` of `h/v`;
- for a derivative on each of two flares, one combined flare `FC<label>Combined`, coefficients
  `C<label>n<nh>prime`, `nh` = the number of Higgs legs.

Never put the leading `L` into `EFTOperators`.

### Step 1 — the Lagrangian term (`Lagrangian_User.fr`)

```mathematica
LPGHD1 := Block[{mu, nu, ga, a},
  WCOrder*ChiralOrder^2/LamHEFT^2 del[H, mu] del[H, nu]
      FS[Gl, mu, ga, a] FS[Gl, nu, ga, a] FCPGHD1Combined[H, NEFT]
];
```

`del[H,mu] del[H,nu] FCPGHD1Combined` is `∂^μF ∂^νF`. Check the mass dimension (4) and the
NDA size: `GG ∂h∂h` has four derivatives and four fields, so 2511.23410 eq. 3.2 gives
`(4π)²/Λ⁴ = 1/((4π)² v⁴)` at `Λ = 4πv`. The combined flare carries `1/v²`, so `1/LamHEFT²`
makes the coefficient `C ~ 1`.

- **Dummy indices** go in the `Block`.
- `ChiralOrder^n` with `n` the operator's chiral, energy scale `LamHEFT` to ensure proper dimansionality. `WCOrder` is what keeps the model at [one insertion per
  vertex](#one-wilson-coefficient-insertion-per-vertex).
- **No coupling constant in front of the operator** (`gs`, `gw`, `g1`, `ee`, a Yukawa, or a mass
  standing in for one): it would change the operator's power counting. Gauge couplings enter only
  through `DC[…]` and `FS[…]`; a coupling the paper writes explicitly (as in the dipoles) is absorbed
  into the coefficient.
- **Multiply by the flare function (`FC<label>[H, NEFT]` or `FC<label>Combined[H, NEFT]`) and by no coefficient of your own** —
  the Wilson coefficients live inside the flare. **One flare per term**: an operator that
  multiplies two of them is refused at load time (see
  [Two derivatives on two flares](#two-derivatives-on-two-flares-one-combined-coefficient)).
- **Do not touch the gauge kinetic terms or the input relations.** Those are the two places the
  model expands to first order in `WCOrder`; an operator that modified them would add a third
  source of coefficient products that nothing re-expands.

### Step 2 — make it selectable (`Lagrangian_User.fr`)

Add one line to **each** of the two selection blocks at the bottom of the file:

```mathematica
If[HEFTPieceActiveQ["PGHD1"], LUseraux += Hold[LPGHD1]];  (* in the LUseraux block  *)
If[HEFTPieceActiveQ["PGHD1"], aux += LPGHD1];          (* inside HEFTRebuildLUser[] *)
```

Keep the `Hold`: an operator evaluated while the file loads comes out unexpanded and can be
expanded wrongly later (`TESTS/T39`). `HEFT_Model.fr` rebuilds the user Lagrangian with
`HEFTRebuildLUser[]` after the model has loaded, so **the second line is the one that counts** — forgetting it drops the operator with
no message at all, while its coefficients are still declared and still written to
`wcxf_output.json`, so nothing downstream looks wrong. Check that the coefficients really
appear in `LHEFT` after Cell 5.

### Step 3 — declare the flare and its coefficients (`parameters_User.fr`)

One row in `userCombinedDerivFlareSpecs`:

```mathematica
userCombinedDerivFlareSpecs = {
  {FCPGHD1Combined,  "PGHD1",  "CPGHD1n",  2},
  ...
};
```

The four fields are the flare symbol, the label, the coefficient prefix and `extraPow`, the
number of differentiated Higgs fields (2 for one `del[H,mu] del[H,nu]`). From that row the model
builds

```
FCPGHD1Combined[h, NEFT] = (LamF/vev)^2 Σ_{nh = 2}^{2 NEFT} CPGHD1n<nh>prime · (LamF h/vev)^(nh−2)
```

only when the label is selected, and declares every coefficient as an `External` parameter, so
it appears in the parameter card and in the WCxf files. **An operator with an ordinary flare**
(no derivative on it, or a derivative on one flare only) goes into `userScalarFlareSpecs` instead,
as `{FC<label>, "<label>", "C<label>n", nmin}`, giving `FC<label>[h, NEFT] = Σ_{n = nmin}^{NEFT}
C<label>n<n> · (LamF h/vev)^n`. **Use `nmin = 1` if that flare sits under a derivative** — a
constant there drops out, and the load aborts otherwise. These rows
are for bosonic, flavour-blind operators; a fermionic one needs flavour-tensor flares instead
(`ferm2FFlareSpecs` / `ferm4FFlareSpecs` in `parameters_EFT_2F.fr` / `parameters_EFT_4F.fr`
show how).

### Step 4 — register the label (`wcxf_input.fr`, `heft_notebook_reference.wl`)

```mathematica
(* wcxf_input.fr, in heft1604CombinedDerivOpPrefixes — same label, prefix and extraPow as Step 3
   (an ordinary flare: HEFT1604ScalarOpPrefixes, with its nmin) *)
{"PGHD1", "CPGHD1n", 2},

(* heft_notebook_reference.wl, in HEFT$Catalog1604Higher *)
{"PGHD1", "PGHD2", "SGHD"},

(* heft_notebook_reference.wl, in HEFT$OperatorChiralOrder — the same n as in Step 1 *)
Thread[{"PGHD1", "PGHD2", "SGHD"} -> 2],
```

The first generates the WCxf keys; without it the coefficients never reach
`wcxf_output.json`, and absent keys are read as **0**. The second is the catalogue Cell 3
validates `EFTOperators` against — an unlisted label is refused as unknown. The third is the
chiral-order label printed by the Reference cell and exported as a UFO coupling order; the two
must agree with the power in Step 1, and the load-time check compares the prefix and `nmin`/
`extraPow` of Steps 3 and 4 against each other.

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
| **8** | `output/FeynArts/<OutputName>/` | `.mod`, `.gen`, `.pars`. For FeynArts / FeynCalc. Plus `heft_export.json`, the configuration it was made with and its fermion form (below), which [merging exports](#merging-feynarts-exports) reads. |

**Two fermion forms.** FeynRules picks the form of the FeynArts files per model: index-free fermion
chains (`NonCommutative[…]`, with flipping rules and `$FermionLines = True`) when no vertex has more
than two fermions, and explicit Dirac indices (`DiracObject[…][di1,di2]`, `$FermionLines = False`)
as soon as one does, i.e. with any four-fermion operator. Cell 8 keeps that default
(`FeynArtsDiracIndices = Automatic`); with `FeynArtsDiracIndices = True` it writes explicit Dirac
indices for every model. `heft_export.json` records the form (`diracIndices`), and exports in
different forms cannot be merged: to merge FeynArts exports that include four-fermion operators,
make **every** export of the merge, the SM-only one included, with `FeynArtsDiracIndices = True`.

**Two FeynRules bugs, corrected by Cell 8.** FeynRules 2.3.49's FeynArts writer (a) silently drops
a vertex whose coupling is a single term when its class of Lorentz structures also holds a
Levi-Civita structure listed before it — with `S1`, `S8`, `SB` or `SG` this removed vertices such
as the SM `hhhW⁺W⁻` — and (b) cannot write `ScalarProduct[p_a,p_b]^2` to the generic file. Before
every export Cell 8 loads [`model_files/feynrules_fixes.wl`](model_files/feynrules_fixes.wl),
which corrects both in the running kernel; FeynRules on disk is not changed. It edits a function
only after checking that the loaded definition is the one it expects, and otherwise prints, in
orange, that it was not applied. The result goes into `heft_export.json` (`feynRulesFixes`).
Exports the bug did not affect come out byte-identical with and without the fix (`TESTS/T38`).

*Which installations this covers.* Both bugs are in FeynRules, not in FeynArts, so the FeynArts
version plays no role. Tested on FeynRules 2.3.49, unmodified and with a local patch: both
corrections apply, and the two installations then write byte-identical files. Other FeynRules
versions are untested. The corrections apply to any version whose two affected functions are
identical to 2.3.49's. Where they differ, nothing is changed, Cell 8 says so in orange, and the
export goes ahead uncorrected. Exports written by different FeynRules installations cannot be
merged together, since the merge compares the digest of `FeynArtsInterface.m`.

### The parameter card (UFO / MadGraph)

The values come from `wcxf/wcxf_output.json` when the model is exported, so the usual route is to edit
that file before Cell 5; the card can also be edited directly. Its blocks:

| Block | Holds |
|---|---|
| `SMINPUTS` | `aEWM1` (1/α), `Gf`, `aS`, `thetaS` — which of them are inputs depends on `EWInputScheme` |
| `MASS` | fermion and Higgs masses; `MZ`/`MW` only where they are inputs (`"gf"`: both; `"aem"`: `MZ`) |
| `HEFTINPUTS` | `"heft"` only: `G1`, `GW`, `GS`, `vev`, `hlambda`. MadGraph lists the first three as `g1__2`, `gw__2`, `gs__2`, because it is case-insensitive and the model also has the gauge couplings `g1`, `gw`, `gs` |
| `CKMBLOCK` | Wolfenstein parameters |
| `HEFT` | the leading-order deviations (13 `Kappa…` or `Delta…` parameters), `LamHEFT`, and the bookkeeping parameters `ChiralOrder` and `WCOrder` (both 1; `WCOrder = 0` switches every EFT contribution off) |
| `HEFTBOSONIC` | the bosonic operator coefficients `C<op>n<n>` (and `C<op>n<nh>prime`), numbered by position — the codes depend on the operator selection, so a card fits only the model it was written for |
| `HEFT<COEFF>` | one block per flavour tensor, e.g. `HEFTCNQ1N0` for `CNQ1n0[i,j]`, entries keyed by the flavour indices (`1 2` = `CNQ1n0[1,2]`, written `CNQ1n01x2`); `NL15`–`NL17` have no diagonal entries |
| `DECAY` | widths; merged UFO models have no `decays.py`, so let MadGraph compute them (`Auto`) |

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
| `EFTOperators`, `HiggsMaxOrder`, `EWInputScheme`, `KappaFramework`, `Massless`, `DiagonalCKM`, or any `.fr` source | **Yes** — unless that exact configuration was built before, under any name |
| Wilson-coefficient **values**, zeros included | **No.** Every coefficient is an `External` parameter, so a value never enters `LHEFT`; it reaches the export through `M$Parameters`. No coefficient is part of the cache key. |
| `MaxVertexLegs`, `FeynArtsDiracIndices`, `InitialiseWCs`, `OutputName`, export format | **No** |

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


## Merging FeynArts exports

Merging cached Lagrangians saves the build, but for large models the **export** is the expensive
step: it grows roughly as terms^2.16, and a FeynArts export of the full bosonic set never finished.
Cells 9 and 10 of [`heft_fr_merge_models.wl`](heft_fr_merge_models.wl) merge one step later, from
FeynArts exports already on disk, so each export is paid only for a small model. No FeynRules, no
`LoadModel` and none of Cells 3–8 are needed: set the configuration in Cell 2, then

1. **Cell 9** lists every export in `output/FeynArts/` made with that configuration, with its
   operators, whether an SM-only export is present, and near-misses with the option they differ in.
2. **Cell 10** takes the names in `MergeFeynArtsSources` and writes
   `output/FeynArts/<OutputName>/`. The SM-only export is found automatically (name it in
   `MergeFeynArtsBaseline` if there are several).

Every coupling becomes

```
C(A ∪ B ∪ …) = C(SM) + Σ_i ( C(i) − C(SM) )
```

which is exact for the same reason as the Lagrangian merge: one Wilson-coefficient insertion per
vertex. To do it, the merger combines each vertex type's Lorentz structures across the exports
(`PDH`, for example, adds momentum structures to the four-Higgs vertex), re-maps every coupling
vector onto the combined list, and gives the `gc` abbreviations one name per distinct definition.
A generic class is declared `G[-1]` when it has a fermion or an `ε` structure and `G[+1]`
otherwise (FeynRules' rule), so CP-even and CP-odd exports differ there; the merged class gets
the sign the rule gives for the combined structures, as a direct export would. The result has its
own `heft_export.json`, so it can be merged again.

**What must agree**, from each export's `heft_export.json`: every cache key except the operator
list, plus `MaxVertexLegs` and the FeynArts interface that wrote it (`FeynArtsInterface.m`, by
its digest). Exports made before 2026-09-29 have no `heft_export.json` and must be re-exported
with Cell 8. Exports made before 2026-10-02, without the FeynRules fixes above, are merged with a
warning: they are correct unless the bug removed vertices from them, which shows as fewer
couplings in the `.mod` than vertices FeynRules reported. **Refused, not warned about:** a missing SM-only export, an operator in two exports, a
name listed twice, an `OutputName` equal to one of the inputs, exports that differ outside their
couplings, and exports in different fermion forms. Under the default `FeynArtsDiracIndices = Automatic` the
SM-only export is index-free, so **a merge with four-fermion operators needs every export, the
SM-only one included, made with `FeynArtsDiracIndices = True`**.

**`.pars` is united, not merged.** FeynArts reads only `.mod` and `.gen`; `.pars` holds FeynRules'
numerical defaults. Where two exports give one parameter different values, the SM-only export's
value is kept and the cell says so.

**Verified** against models exported directly with all the operators at once (`TESTS/T36`):
`{P1}`, `{P12}`, `{PW}` in `"heft"`, and `{P1}`, `{PDH}` in `"aem"` with the Delta framework, give
0 differing couplings, at first order in `WCOrder` and exactly. FeynArts' own `ZZ → hh` amplitude
agrees too.

**The bosonic operators, merged** (`TESTS/T37`, `T38`, `T39`, `HiggsMaxOrder = 3`,
`MaxVertexLegs = 6`, `"heft"`, Delta framework): `output/FeynArts/HEFT_Bosonic_FA/` holds 43
operators, the 42 bosonic ones except `PGGG` and `SGGG` plus the user W-Higgs operators `PWHD1`,
`PWHD2`, `SWHD`. Each was exported on its own, 3.7 h in all (1.5 h of it `SWWW`), and they were
merged in 2 s. A direct FeynArts export of the bosonic set has never finished. `PGGG`'s export
did not finish in 8 h; `SGGG` and `SWHDT` were not included. Three subsets merged this way (one
with the CP-odd `S1`, `S8`, `SB`, `SG`, one with the W-Higgs operators) equal their direct exports
coupling for coupling. Rebuilt on 2026-10-06 after the fix of the quartic gauge vertices of `PW`
and `P12` (`TESTS/T39`, `NOTES.md` §6).


## Merging UFO exports

The UFO writer is the slowest step of the pipeline (about 10 h for the full bosonic model). Cells 11
and 12 of [`heft_fr_merge_models.wl`](heft_fr_merge_models.wl) merge UFO exports already on disk, in
the same way as Cells 9 and 10 merge FeynArts exports: set the configuration in Cell 2, then

1. **Cell 11** lists every export in `output/UFO/` made with that configuration, with its operators,
   whether an SM-only export is present, and near-misses with the option they differ in.
2. **Cell 12** takes the names in `MergeUFOSources` and writes `output/UFO/<OutputName>/`. The
   SM-only export is found automatically (name it in `MergeUFOBaseline` if there are several).

Every coupling entry becomes `C(SM) + Σ_i (C(i) − C(SM))`, exact at one Wilson-coefficient insertion
per vertex. The merge is done by [`model_files/ufo_merge.py`](model_files/ufo_merge.py), so Cells 11
and 12 need a Python 3 interpreter (standard library only, 3.8 or later), found automatically or set
as `HEFT$Python`. No FeynRules and no `LoadModel` are involved.

**How the files are combined:**
- **Vertices and couplings, per entry.** An entry is keyed by particles, colour structure, Lorentz
  structure (by its content) and coupling orders. FeynRules numbers its couplings and Lorentz
  structures per export, so names are never compared. Two exports may decompose a vertex into
  different Lorentz structures; a missing entry counts as zero, so the sum is still right.
- **Values are combined as text.** An entry that only one export changes is copied verbatim; one
  that several change is written as `(C_a) + (C_b) − (m−1)·(C_SM)`, and dropped if it is
  numerically zero. The merged file has one `Vertex` per coupling-order set, where FeynRules
  sometimes combines orders in one `Vertex`; both forms are valid UFO.
- **Parameters.** External parameters are united. An internal parameter that differs between
  exports (`MZ` in `"heft"` with `P1`, `P12` or `PT`; `G1`, `GW`, `vev`, `hlambda`, `MW` in
  `"gf"`/`"aem"`) is merged with the same identity. The LHA block `HEFTBOSONIC`, numbered by
  position in each export, is renumbered; a param card written for a single export does not fit the
  merged model.
- **Copied**, and required to be identical in every export: particles, coupling orders,
  propagators and the UFO library files.
- **`decays.py` is not written.** FeynRules' widths are quadratic in the couplings, so they cannot
  be added. Let MadGraph compute the widths (`compute_widths`, or `Auto` in the param card).

**What must agree**, from each export's `heft_export.json` (written by Cell 7 since 2026-10-06;
older UFO exports must be re-exported): every cache key except the operator list, plus
`MaxVertexLegs` and FeynRules' UFO interface (by its digest). **Refused, not warned about:** a
missing SM-only export, an operator in two exports, a name listed twice, an `OutputName` equal to
one of the inputs, exports that differ in a copied file, a baseline vertex missing from a sub-model,
and a particle set written in two different orders. The result has its own `heft_export.json`, so
it can be merged again.

**Status (2026-10-12): validated for bosonic, two-fermion and four-lepton exports** (`TESTS/T42`):
merged and direct exports agree vertex by vertex and in MadGraph `|M|²` (to 10⁻¹⁵), in `"heft"` and
`"gf"`, and every refusal works. FeynRules names its flavour-sum abbreviations (`I1a11`, …) per export;
where two exports define one name differently, the merge renames it in each (`I1a11_m1`, `I1a11_m2`).
MadGraph converts a Python-2 UFO in place on import, so import a copy of an export, not the export
itself.

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
  lheft_merge.wl             the merge arithmetic (cached Lagrangians)
  fa_merge.wl                the FeynArts export merge (merge notebook Cells 9–10)
  ufo_merge.wl, ufo_merge.py the UFO export merge (merge notebook Cells 11–12)
  heft_export_meta.wl        heft_export.json: what each export was made with
  feynrules_fixes.wl         two corrections to FeynRules' FeynArts writer, applied by Cell 8
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
Amplitudes at `O(c²)` built from two vertices are incomplete in the products involving the A–Z
rotation (`P1`, `P12`), the `"gf"`/`"aem"` input relations (`P1`, `P12`, `PT`, `RL2`, `RL5`) and the
`S2D` field redefinition (`CS2Dn1`); see [One Wilson-coefficient insertion per vertex](#one-wilson-coefficient-insertion-per-vertex).

**Shifted masses in propagators in `"heft"` and `"aem"`.** `MZ` (`"heft"`: `P1`, `P12`, `PT`) and `MW`
(`"aem"`: `P1`, `P12`, `PT`, `RL2`, `RL5`) enter the full propagator with their first-order shift, so the
amplitude is not strictly linear in those coefficients. Use `"gf"` to avoid it; see
[Input scheme (EW)](#input-scheme-ew).

**`QED` coupling orders in `"gf"`/`"aem"`.** FeynRules derives coupling orders from the declared orders of
the parameters, and `Gf` counts as `QED^2`. A coefficient-dependent shift of `vev` goes like `1/√Gf`, so some
`WCOrder` couplings carry the order `QED: −1` (42 in a typical `gf` export). Amplitudes are not affected, but a
MadGraph restriction such as `QED<=n` counts these couplings accordingly; select on `WCOrder` instead.

**No assumptions on the fermionic Wilson coefficients.** Every flavour entry is an independent
free parameter — 3×3 per 2F operator and 3⁴ per 4F operator, per power of `h/v`. The model
imposes **no** flavour symmetry, no MFV ansatz, no hermiticity or exchange relation between
entries, and no relation between operators; the only assumption is that the coefficients are
real.

**All Wilson coefficients are real.** 

**Flavour is fixed at 3 generations.** 

**One `LoadModel` per kernel.** See [Rules of the road](#rules-of-the-road).

**`PGGG`, `SGGG` and `SWWW` are slow to export to FeynArts.** At `HiggsMaxOrder = 3` and
`MaxVertexLegs = 6`, `SWWW` alone takes 2 h and `PGGG` did not finish in 8 h, in FeynRules'
FeynArts writer.

**FeynArts merges with four-fermion operators need `FeynArtsDiracIndices = True` for every export**
(the default fermion forms differ). Alternatively use the [cached-Lagrangian
merge](#merging-cached-models) and one export, or merge the UFO exports
([Merging UFO exports](#merging-ufo-exports)).

## Authors

**Michał Ryczkowski** — <michaljakub.ryczkowski@unipd.it>

*Dipartimento di Fisica e Astronomia "G. Galilei", Università di Padova, and INFN, Sezione di
Padova, Via F. Marzolo 8, I-35131 Padova, Italy*

Released under the MIT License — see [LICENSE](LICENSE).

---
