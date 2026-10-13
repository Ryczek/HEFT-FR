(* ::Package:: *)

(* ::Title:: *)
(*HEFT-FR -- merge cached models*)


(* ::Text:: *)
(*The second entry point of the package, beside heft_fr_notebook.wl. Open it in Mathematica and evaluate it section by section. Use it to build one LARGE model out of several SMALL ones you have already built - e.g. a full bosonic model assembled from a handful of few-operator runs - without paying for the expensive mass-basis pass again.*)
(**)
(*WHY IT WORKS*)
(*ExpandIndices is linear in the Lagrangian, so*)
(*    LHEFT(A u B) = LHEFT(SM) + (LHEFT(A) - LHEFT(SM)) + (LHEFT(B) - LHEFT(SM))*)
(*and every LHEFT(x) is already on disk in HEFT_cache/ from an earlier heft_fr_notebook.wl run. Only LoadModel, the Feynman rules and the export are recomputed. The SM baseline has to be subtracted explicitly: each sub-model contains the WHOLE SM Lagrangian, so adding N of them naively would give N x SM and scale every SM vertex by N.*)
(**)
(*WHAT YOU NEED FIRST*)
(*- The sub-models, built with heft_fr_notebook.wl, each with its own EFTOperators and ALL OTHER OPTIONS IDENTICAL.*)
(*- An SM baseline: one build with EFTOperators = {} and the same options. It is the cheapest build there is, and one serves every merge of that configuration.*)
(**)
(*WHAT IS REFUSED (not warned about)*)
(*- Any hashed configuration option differing between two sub-models - including modelDigest, the digest of the .fr sources, so sub-models built either side of a model-file edit never merge.*)
(*- A missing SM baseline, or an operator appearing in two selected sub-models (it would be added once per sub-model that carries it).*)
(**)
(*ONE RUN PER KERNEL. Quit the kernel (Evaluation > Quit Kernel) before starting, every time - Cell 5 calls LoadModel, which is not idempotent.*)
(**)
(*CELLS*)
(*  1  Reference - what merging does, when it is exact, what it refuses*)
(*  2  Configuration - every option EXCEPT EFTOperators, which is derived from your selection*)
(*  3  Lists every cached model built with exactly this configuration: name and operators*)
(*  4  MergeSources - the names you picked; writes the WCxf files for their union*)
(*  5  LoadModel on the union, merge, cache the result as LHEFT*)
(*  6  Feynman rules   |*)
(*  7  UFO export      |  the SAME cells as heft_fr_notebook.wl - they Get the same file*)
(*  8  FeynArts export |*)
(*  9  Lists the FeynArts exports made with this configuration*)
(* 10  MergeFeynArtsSources - merges those exports into output/FeynArts/<OutputName>/*)
(* 11  Lists the UFO exports made with this configuration*)
(* 12  MergeUFOSources - merges those exports into output/UFO/<OutputName>/*)
(**)
(*MERGING FEYNARTS EXPORTS (Cells 9-10) is the same idea one step later: instead of cached Lagrangians, it adds up FeynArts files you already exported, so the expensive export itself is paid only for the small models. The exports must each have a heft_export.json (written by Cell 8 since 2026-09-29), be made with the configuration of Cell 2 including MaxVertexLegs, and include one SM-only export (EFTOperators = {}). Cells 9-10 need only Cell 2 - no FeynRules, no LoadModel, and none of Cells 3-8.*)
(**)
(*MERGING UFO EXPORTS (Cells 11-12) does the same for UFO exports, which matters most: the UFO writer is the slowest step of the pipeline. The exports need a heft_export.json written by Cell 7 (since 2026-10-06; older UFO exports must be re-exported), the configuration of Cell 2 including MaxVertexLegs, and one SM-only export. The merge itself is done by model_files/ufo_merge.py, so Cells 11-12 need a Python 3 interpreter (standard library only), found automatically or set as HEFT$Python. The merged model has no decays.py: widths are not additive, so let MadGraph compute them.*)


(* ::Section:: *)
(*Cell 1 - Reference*)


(* ::Text:: *)
(*Prints the About block, what merging does, and the rules it enforces. No FeynRules, no model loading, no configuration needed - safe to re-run at any time.*)


HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

HEFT$MergeCell=1;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge.wl"}];


(* ::Section:: *)
(*Cell 2 - Configuration*)


(* ::Text:: *)
(*Edit the code cell below, then evaluate it before Cell 3. These are the same options as in heft_fr_notebook.wl with ONE exception: there is no EFTOperators here. The operator selection is not something you choose - it is the union of the sub-models you merge in Cell 4.*)
(**)
(*Every option below must match the value the sub-models were built with, exactly. That is the whole point of the lookup in Cell 3: it shows you only the cached models that agree with what you set here, so a mismatch shows up as an empty (or short) list rather than as a wrong model.*)


(* Path to your local FeynRules installation (must contain FeynRules.m) *)
$FeynRulesPath="";   (* SET THIS to your FeynRules folder, e.g. FileNameJoin[{$UserBaseDirectory, "Applications", "feynrules-current"}]; Cell 3 refuses to run while it is empty *)

(* Physics / expansion - must match the sub-models *)
HiggsMaxOrder=3;                     (* Max (H/vev)^n order kept in the F-functions *)
KappaFramework=True;                 (* True -> Kappa parameterisation of SM couplings deviation; False = Delta parameterisation (see README) *)
InitialiseWCs=0;                     (* Default value Cell 4 writes for the EFFECTIVE Wilson coefficients: 1 or 0. SM couplings always keep their SM value regardless of this. NOT part of the cache key, so it need not match the sub-models *)

(* Input schemes - must match the sub-models *)
EWInputScheme="heft";                (* "heft" / "gf" / "aem". The derived schemes are NSM-only, which merging requires anyway. See README SS "Input scheme (EW)" *)
Massless=False;                      (* True -> load restrictions/Massless.rst before Feynman rules *)
DiagonalCKM=False;                   (* True -> load restrictions/DiagonalCKM.rst before Feynman rules *)

(* NLO basis - must match the sub-models. There is deliberately NO EFTOperators here:
   Cell 4 derives it as the union of the sub-models you select. *)

OutputName="HEFT_FullModel";            (* Output subdirectory name under HEFT_Frules/output/, and the readable half of the merged model's cache folder name *)

MaxVertexLegs=6;                     (* Export-time cut on vertex multiplicity for Cells 6/7/8. Automatic (default) = no cut; an integer n >= 3 keeps only vertices with at most n legs. NOT part of the cache key, so it need not match the sub-models - like InitialiseWCs. See README *)
FeynArtsDiracIndices=Automatic;      (* Fermion form of the FeynArts export of the merged model (Cell 8). Automatic = FeynRules' choice; True = explicit Dirac indices. FeynArts exports to be merged in Cells 9-10 must all have the same form: with four-fermion operators that means all made with True, the SM-only one included *)

ForceRebuildLHEFT=False;             (* True = ignore an existing cache entry for the MERGED configuration and merge again from the sub-models *)

(* Must stay last: Cell 3 refuses to run without it, so that a Cell 3 evaluated in a kernel
   where this section never ran cannot silently fall back to the defaults for everything. *)
HEFT$ConfigEvaluated=True;


(* ::Section:: *)
(*Cell 3 - find the cached models that match this configuration*)


(* ::Text:: *)
(*Prints every entry in HEFT_cache/ that was built with exactly the configuration above, with its name, its operators and when it was built. Those names are what you put into MergeSources in Cell 4.*)
(**)
(*You never need to know a cache hash: the folder names carry one, but every entry's meta.json holds the full configuration, so the lookup is by content. The folder column is shown only as a tie-breaker, for the case where you built two different operator selections under the same OutputName.*)
(**)
(*The cell also reports entries that ALMOST match, together with the option they differ in - usually modelDigest, meaning that sub-model predates an edit to a .fr file and has to be rebuilt before it can join the merge.*)
(**)
(*No FeynRules and no model loading: this reads meta.json and the .fr digests off disk, so it is instant and safe to re-run.*)


HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$MergeCell=3;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge.wl"}];


(* ::Section:: *)
(*Cell 4 - choose the sub-models*)


(* ::Text:: *)
(*Put the names from the Cell 3 table into MergeSources, then evaluate. Do NOT list the SM baseline - it is found automatically and subtracted; listing it anyway is harmless and reported.*)
(**)
(*A name may be the OutputName, any alias recorded in that entry's names list, or the full folder name <OutputName>__<configHash> if one OutputName is ambiguous within this configuration group. An ambiguous name is refused with the folder names to use instead, never resolved silently.*)
(**)
(*This cell then derives EFTOperators as the union of the selected sub-models and rewrites wcxf/wcxf_init.json and wcxf/wcxf_output.json for that union - they must be regenerated, because a file written for one sub-model has no keys for the other's operators and absent keys are read as 0. Edit wcxf_output.json after this cell if you want non-default Wilson coefficients, exactly as in heft_fr_notebook.wl.*)


MergeSources={};                     (* e.g. {"HEFT_bos_gauge", "HEFT_bos_P"} - names from the Cell 3 table *)

HEFT$MergeCell=4;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge.wl"}];


(* ::Section:: *)
(*Cell 5 - merge and load*)


(* ::Text:: *)
(*LoadModel on the UNION of the operator lists (so every parameter both sub-models need is declared), then the merge itself, leaving the result in LHEFT. That is all Cells 6/7/8 need.*)
(**)
(*The merged Lagrangian is saved as an ordinary HEFT_cache/ entry, keyed by its own configuration exactly like a directly built model - so re-running this cell is a plain cache hit, and heft_fr_notebook.wl configured with the same options and the union operator list will find it too. Its meta.json additionally records mergedFrom / mergedLOBaseline, so you can always see where it came from.*)
(**)
(*The merge is plain arithmetic - sum of the sub-models minus (N-1) copies of the SM baseline - and not term-by-term matching. Matching cannot work here: FeynRules' $-suffixed dummy index names diverge between kernels and Times is Orderless, so "rename in order of first appearance" is not canonical; and the SM sector is not even written the same way in two builds, since activating P1/P12/PW/PB switches gauge_normalization.fr to an algebraically equal but syntactically different A-Z branch. Arithmetic is immune to both. The price is that nothing cancels syntactically, so the merged Lagrangian is larger than a directly built one (+29% in LeafCount in the verified case); FeynRules collapses it when it extracts the vertices, which come out identical - see TESTS.md T19.*)
(**)
(*Like heft_fr_notebook.wl Cell 5, this cell runs at most once per kernel: FeynRules' LoadModel is not idempotent.*)


HEFT$MergeCell=5;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge.wl"}];


(* ::Section:: *)
(*Cell 6 - compute Feynman rules*)


(* ::Text:: *)
(*From here on this notebook is heft_fr_notebook.wl: Cells 6, 7 and 8 Get model_files/heft_fr.wl and run its cells 6, 7 and 8 unchanged. They need nothing but LHEFT, OutputName and HEFT$WorkspaceRoot, all of which Cell 5 has set.*)
(**)
(*Optional side branch: computes RulesHEFT = FeynmanRules[LHEFT] and saves it to output/FeynmanRules/<OutputName>/ as .mx, .txt and latex/.tex. Cells 7 and 8 do not read RulesHEFT, so this can always be skipped.*)


HEFT$FromNotebook=True;

HEFT$NotebookCell=6;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 7 - UFO export*)


(* ::Text:: *)
(*Writes output/UFO/<OutputName>/. Only needs LHEFT from Cell 5, whether or not you ran Cell 6.*)


HEFT$FromNotebook=True;

HEFT$NotebookCell=7;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 8 - FeynArts export*)


(* ::Text:: *)
(*Writes output/FeynArts/<OutputName>/ (.mod, .gen, .pars, plus heft_export.json - its configuration, which Cells 9-10 read). Independent of Cell 7 - run either or both. Before exporting it corrects two bugs in FeynRules' FeynArts writer in memory (model_files/feynrules_fixes.wl: single-term vertices next to Levi-Civita structures were dropped, and ScalarProduct^2 was not written) and prints whether each was applied; FeynRules on disk is not changed, and heft_export.json records the result.*)


HEFT$FromNotebook=True;

HEFT$NotebookCell=8;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 9 - find the FeynArts exports that match this configuration*)


(* ::Text:: *)
(*Prints every export in output/FeynArts/ made with exactly the configuration of Cell 2 - every option, the .fr digest (modelDigest), MaxVertexLegs and the FeynArts interface that wrote it - with its name and operators. Those names are what you put into MergeFeynArtsSources in Cell 10. It also reports near-misses with the option they differ in, and export folders without a heft_export.json (exported before 2026-09-29: re-export them with Cell 8 to use them).*)
(**)
(*Needs only Cell 2: no FeynRules, no model loading, and none of Cells 3-8, so it can run in a fresh kernel.*)


HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$MergeCell=9;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge.wl"}];


(* ::Section:: *)
(*Cell 10 - merge FeynArts exports*)


(* ::Text:: *)
(*Builds output/FeynArts/<OutputName>/ (.mod, .gen, .pars and heft_export.json) out of the exports named below. Every coupling becomes SM + the sum of each export's deviation from the SM-only export, the same arithmetic as Cell 5 one step later; this is exact because the model keeps one Wilson-coefficient insertion per vertex. Do NOT list the SM-only export: it is found automatically and subtracted. If Cell 9 shows several, name one in MergeFeynArtsBaseline.*)
(**)
(*Refused rather than warned about: an export not listed by Cell 9, an operator in two exports, a name listed twice, an OutputName equal to one of the inputs, and exports that differ outside their couplings. The result carries its own heft_export.json, so it can itself be a source of a later merge.*)
(**)
(*The .pars file is only united, not merged: FeynArts reads .mod and .gen alone. Where two exports hold different values for one parameter (e.g. a Kappa edited in one wcxf_output.json), the SM-only export's value is kept and the cell says so.*)


MergeFeynArtsSources={};             (* e.g. {"HEFT_P1", "HEFT_P12", "HEFT_PW"} - names from the Cell 9 table *)

MergeFeynArtsBaseline=Automatic;     (* Automatic = the one SM-only export Cell 9 finds; or its name, if there are several *)

HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$MergeCell=10;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge.wl"}];


(* ::Section:: *)
(*Cell 11 - find the UFO exports that match this configuration*)


(* ::Text:: *)
(*Prints every export in output/UFO/ made with exactly the configuration of Cell 2 - every option, the .fr digest (modelDigest), MaxVertexLegs and the FeynRules UFO interface that wrote it - with its name and operators. Those names are what you put into MergeUFOSources in Cell 12. It also reports near-misses with the option they differ in, and UFO folders without a UFO heft_export.json (exported before 2026-10-06: re-export them with Cell 7 to use them).*)
(**)
(*Needs only Cell 2: no FeynRules, no model loading, and none of Cells 3-10, so it can run in a fresh kernel.*)


HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$MergeCell=11;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge.wl"}];


(* ::Section:: *)
(*Cell 12 - merge UFO exports*)


(* ::Text:: *)
(*Builds output/UFO/<OutputName>/ (the UFO .py files and heft_export.json) out of the exports named below. Every coupling becomes SM + the sum of each export's deviation from the SM-only export, the same arithmetic as Cells 5 and 10; this is exact because the model keeps one Wilson-coefficient insertion per vertex. Do NOT list the SM-only export: it is found automatically and subtracted. If Cell 11 shows several, name one in MergeUFOBaseline.*)
(**)
(*Merged: vertices, couplings and Lorentz structures (compared by content, renumbered), parameters (an internal parameter that differs between exports, such as MZ in the heft scheme with P1/P12/PT, is merged the same way; the LHA block HEFTBOSONIC is renumbered). Copied, and required to be identical in every export: particles, coupling orders, propagators and the UFO library files. NOT written: decays.py - FeynRules' widths are quadratic in the couplings and cannot be added; let MadGraph compute the widths (compute_widths, or Auto in the param card).*)
(**)
(*Refused rather than warned about: an export not listed by Cell 11, an operator in two exports, a name listed twice, an OutputName equal to one of the inputs, exports that differ in a copied file, a baseline vertex missing from a sub-model, and a particle set written in two different orders. The result carries its own heft_export.json, so it can itself be a source of a later merge. Needs a Python 3 interpreter (standard library only); set HEFT$Python if it is not found.*)


MergeUFOSources={};             (* e.g. {"HEFT_P1", "HEFT_P12", "HEFT_PW"} - names from the Cell 11 table *)

MergeUFOBaseline=Automatic;     (* Automatic = the one SM-only export Cell 11 finds; or its name, if there are several *)

HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$MergeCell=12;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge.wl"}];
