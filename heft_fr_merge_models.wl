(* ::Package:: *)

(* ::Title:: *)
(*HEFT-FR -- merge cached models*)


(* ::Text:: *)
(*The second entry point of the package, beside heft_fr_notebook.wl. Open it in Mathematica and evaluate it section by section. Use it to build one LARGE model out of several SMALL ones you have already built - e.g. a full bosonic model assembled from a handful of few-operator runs - without paying for the expensive mass-basis pass again.*)
(**)
(*WHY IT WORKS*)
(*ExpandIndices is linear in the Lagrangian, so*)
(*    LHEFT(A u B) = LHEFT(LO) + (LHEFT(A) - LHEFT(LO)) + (LHEFT(B) - LHEFT(LO))*)
(*and every LHEFT(x) is already on disk in HEFT_cache/ from an earlier heft_fr_notebook.wl run. Only LoadModel, the Feynman rules and the export are recomputed. The LO baseline has to be subtracted explicitly: each sub-model contains the WHOLE LO Lagrangian, so adding N of them naively would give N x LO and scale every SM vertex by N.*)
(**)
(*WHAT YOU NEED FIRST*)
(*- The sub-models, built with heft_fr_notebook.wl, each with its own NLOOperators and ALL OTHER OPTIONS IDENTICAL.*)
(*- An LO baseline: one build with NLOOperators = {} and the same options. It is the cheapest build there is, and one serves every merge of that configuration.*)
(**)
(*WHAT IS REFUSED (not warned about)*)
(*- Any hashed configuration option differing between two sub-models - including modelDigest, the digest of the .fr sources, so sub-models built either side of a model-file edit never merge.*)
(*- HEFTMaxOrder > 1. Merging is exact only at linear order in ChiralOrder: above it the gauge normalisations (eps is a product, the kinetic diagonal is Wnorm^2 P12norm^2) and the EW input scheme mix operators non-linearly, so a build with one operator has different physical fields than a build with two, and no merge recovers the cross terms.*)
(*- A missing LO baseline, or an operator appearing in two selected sub-models (it would be added once per sub-model that carries it).*)
(**)
(*ONE RUN PER KERNEL. Quit the kernel (Evaluation > Quit Kernel) before starting, every time - Cell 5 calls LoadModel, which is not idempotent.*)
(**)
(*CELLS*)
(*  1  Reference - what merging does, when it is exact, what it refuses*)
(*  2  Configuration - every option EXCEPT NLOOperators, which is derived from your selection*)
(*  3  Lists every cached model built with exactly this configuration: name and operators*)
(*  4  MergeSources - the names you picked; writes the WCxf files for their union*)
(*  5  LoadModel on the union, merge, cache the result as LHEFT*)
(*  6  Feynman rules   |*)
(*  7  UFO export      |  the SAME cells as heft_fr_notebook.wl - they Get the same file*)
(*  8  FeynArts export |*)


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
(*Edit the code cell below, then evaluate it before Cell 3. These are the same options as in heft_fr_notebook.wl with ONE exception: there is no NLOOperators here. The operator selection is not something you choose - it is the union of the sub-models you merge in Cell 4.*)
(**)
(*Every option below must match the value the sub-models were built with, exactly. That is the whole point of the lookup in Cell 3: it shows you only the cached models that agree with what you set here, so a mismatch shows up as an empty (or short) list rather than as a wrong model.*)


(* Path to your local FeynRules installation (must contain FeynRules.m) *)
$FeynRulesPath="/Users/michalryczkowski/Library/Mathematica/Applications/feynrules-current";

(* Physics / expansion - must match the sub-models *)
HEFTGauge="unitary";                 (* "unitary" - the only gauge implemented. An unfinished R_xi branch exists in the source but is not supported; see README *)
HEFTMaxOrder=1;                      (* ChiralOrder truncation. MERGING REQUIRES <= 1: at 2 or 3 the operators mix non-linearly through the gauge normalisations and the EW input scheme, and separately built models cannot reproduce the cross terms. Cell 5 refuses above 1 *)
HiggsMaxOrder=3;                     (* Max (H/vev)^n order kept in the F-functions *)
KappaFramework=True;                 (* True -> Kappa parameterisation of SM couplings deviation; False = Delta parameterisation (see README) *)
InitialiseWCs=0;                     (* Default value Cell 4 writes for the EFFECTIVE Wilson coefficients: 1 or 0. SM couplings always keep their SM value regardless of this. NOT part of the cache key, so it need not match the sub-models *)
LOYukawaExpansion = False;           (* True = keep the higher-order fermion-Higgs terms of the LO Yukawa sector. Part of the cache key: must match the sub-models *)
IncludeCustodialT=True;             (* True = keep the custodial-symmetry breaking operator PT in the LO Lagrangian. Part of the cache key: must match the sub-models *)
Combine2Derivatives=True;            (* True = one combined WC family per 2-derivative operator (DH/P8/P20/P21/P22). Part of the cache key: must match the sub-models *)

(* Input schemes - must match the sub-models *)
EWInputScheme="heft";                (* "heft" / "gf" / "aem". The derived schemes are NLO-only, which merging requires anyway. See README SS "Input scheme (EW)" *)
Massless=False;                      (* True -> load restrictions/Massless.rst before Feynman rules *)
DiagonalCKM=False;                   (* True -> load restrictions/DiagonalCKM.rst before Feynman rules *)

(* NLO basis - must match the sub-models. There is deliberately NO NLOOperators here:
   Cell 4 derives it as the union of the sub-models you select. *)
HEFTNLOBasis="1604.06801";           (* the only implemented basis; "2206.07722" (Sun et al.) is refused as not yet implemented *)

OutputName="HEFT_FullModel";            (* Output subdirectory name under output/, and the readable half of the merged model's cache folder name *)

MaxVertexLegs=6;                     (* Export-time cut on vertex multiplicity for Cells 6/7/8. Automatic (default) = no cut; an integer n >= 3 keeps only vertices with at most n legs. NOT part of the cache key, so it need not match the sub-models - like InitialiseWCs. See README *)

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
(*Put the names from the Cell 3 table into MergeSources, then evaluate. Do NOT list the LO baseline - it is found automatically and subtracted; listing it anyway is harmless and reported.*)
(**)
(*A name may be the OutputName, any alias recorded in that entry's names list, or the full folder name <OutputName>__<configHash> if one OutputName is ambiguous within this configuration group. An ambiguous name is refused with the folder names to use instead, never resolved silently.*)
(**)
(*This cell then derives NLOOperators as the union of the selected sub-models and rewrites wcxf/wcxf_init.json and wcxf/wcxf_output.json for that union - they must be regenerated, because a file written for one sub-model has no keys for the other's operators and absent keys are read as 0. Edit wcxf_output.json after this cell if you want non-default Wilson coefficients, exactly as in heft_fr_notebook.wl.*)


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
(*The merge is plain arithmetic - sum of the sub-models minus (N-1) copies of the LO baseline - and not term-by-term matching. Matching cannot work here: FeynRules' $-suffixed dummy index names diverge between kernels and Times is Orderless, so "rename in order of first appearance" is not canonical; and the LO sector is not even written the same way in two builds, since activating P1NLO/P12NLO/WHNLO/BHNLO switches gauge_normalization.fr to an algebraically equal but syntactically different A-Z branch. Arithmetic is immune to both. The price is that nothing cancels syntactically, so the merged Lagrangian is larger than a directly built one (+29% in LeafCount in the verified case); FeynRules collapses it when it extracts the vertices, which come out identical.*)
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
(*Writes output/FeynArts/<OutputName>/ (.mod, .gen, .pars). Independent of Cell 7 - run either or both.*)


HEFT$FromNotebook=True;

HEFT$NotebookCell=8;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];
