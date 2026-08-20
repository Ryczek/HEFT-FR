(* ::Package:: *)

(* ::Title:: *)
(*HEFT-FR -- HEFT FeynRules model*)


(* ::Text:: *)
(*This file is the only entry point of the package: open it in Mathematica and evaluate it section by section. Everything the run needs is set here, in the Configuration section below; the model itself lives in model_files/ and is never edited to configure a run.*)
(**)
(*BEFORE YOU START*)
(*- Install FeynRules and put its path in $FeynRulesPath (first line of Configuration). The directory must contain FeynRules.m.*)
(*- ONE RUN PER KERNEL. Quit the kernel (Evaluation > Quit Kernel) before starting a run, every time.*)
(**)
(*CELL 1 - Reference (no FeynRules, no model loading; safe to re-run at any time)*)
(*  Evaluates in a second and prints:*)
(*   (a) model implementation description*)
(*   (b) the configuration-option table (every variable of Cell 2, what it does, allowed values) and the operator catalogue of the selected basis. *)
(*         Set IgnoreReference = True in that cell to suppress (b) and print only (a).*)
(*         HEFTNLOBasis must be "1604.06801" - it is the only implemented basis. PrintHigherOrder = True also lists the implemented NNLO operators.*)
(**)
(*CELL 2 - Configuration (re-evaluate after every change, before Cell 3)*)
(*One code cell holding every run option. The operator labels in NLOOperators must come from the catalogue of the basis you set in HEFTNLOBasis - Cell 3 aborts with "Unknown operator(s)" if one does not exist.*)
(**)
(*CELL 3 - configuration banner and Wilson-coefficient files*)
(*Loads FeynRules, fills in any option left unset from model_files/heft_defaults.wl, echoes the active configuration and the selected operators, and writes the two Wilson-coefficient files wcxf/wcxf_init.json and wcxf/wcxf_output.json for exactly that operator selection. Nothing is built yet. It closes with the cache lookup, so you already know here whether Cell 5 will load an existing build or start a new one. This cell also defines HEFT$FromNotebook and HEFT$WorkspaceRoot for the whole kernel session, so it must be run before any later cell.*)
(**)
(*CELL 4 - edit Wilson coefficients (OPTIONAL - skip it to run with the defaults)*)
(*There are no flags for this: the model always reads wcxf/wcxf_output.json. Edit the numbers in it to change coefficients, or leave it alone for the defaults Cell 3 just wrote. Cell 4 itself only prints the paths and re-runs the cache lookup for the file as it now stands - the editing happens in a text editor. Re-running Cell 3 resets the file, so edit after it, not before. The Cell 4 section below describes this in full.*)
(**)
(*CELL 5 - load model, build LHEFT*)
(*Runs LoadModel on model_files/HEFT_Model.fr, applies the .rst restrictions if Massless / DiagonalCKM are True, then produces LHEFT, the Lagrangian in the mass basis. Before building it looks HEFT_cache/ up for a build of this exact configuration, saved under any OutputName; only if there is none, is LHEFT built from scratch (minutes to hours, depending on the operator count). Every build is saved. ForceRebuildLHEFT = True is the only way to override this.*)
(*Changing Wilson-coefficient values NEVER costs a rebuild, zeros included: they are External parameters, so a value never enters LHEFT.*)
(**)
(*CELL 6 - compute Feynman rules (OPTIONAL)*)
(*A side branch off Cell 5: computes RulesHEFT = FeynmanRules[LHEFT], prints the vertex count, and saves it to output/FeynmanRules/<OutputName>/ - <OutputName>.mx (a Mathematica-reloadable dump), <OutputName>.txt (a plain-text listing of every vertex), and latex/<OutputName>.tex (a standalone LaTeX document, in its own subfolder). Cell 7 does NOT read RulesHEFT - it computes whatever it needs from LHEFT itself - so this step can always be skipped unless you want the rules themselves.*)
(**)
(*CELLS 7 and 8 - export: Cell 7 (UFO) and/or Cell 8 (FeynArts)*)
(*Both need only LHEFT from Cell 5,  and you may run both. Cell 7 writes output/UFO/<OutputName>/ (with ufo_cleanup.py applied to parameters.py); Cell 8 writes output/FeynArts/<OutputName>/ (.mod/.gen/.pars).*)
(**)
(*WHERE THINGS ARE*)
(*  model_files/    model source (HEFT_Model.fr, LO/, NLO/, heft_fr.wl and helpers)*)
(*  wcxf/           Wilson-coefficient JSON (init template + the one actually read)*)
(*  HEFT_cache/     cached mass-basis Lagrangians, one subfolder per configuration (<OutputName>__<configHash>/)*)
(*  output/         UFO/, FeynArts/ and FeynmanRules/ exports, one subfolder per OutputName*)
(*  restrictions/   Massless.rst, DiagonalCKM.rst*)
(*  README.md       full manual*)


(* ::Section:: *)
(*Cell 1 - Reference*)


(* ::Text:: *)
(*Evaluate this cell to print the About block (always) and, unless IgnoreReference = True, the configuration options and the operator catalogue of the basis selected below. Independent of the Configuration section, which runs later - so you can preview either basis here before deciding what to configure. No FeynRules or model loading needed; re-run any time you need to look up a label or an option.*)


HEFT$WorkspaceRoot=DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];
Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_notebook_reference.wl"}];
IgnoreReference=False; (* True = print only the About block (what this model is, authors, references); False = also print the option table and the operator catalogue below *)
HEFTNLOBasis="1604.06801"; (* the only implemented basis; "2206.07722" (Sun et al.) is refused as not yet implemented *)
PrintHigherOrder=False; (* True = also show the implemented NNLO (chiral dimension 2) operators *)
HEFT$PrintNotebookReference[];


(* ::Section:: *)
(*Cell 2 - Configuration*)


(* ::Text:: *)
(*Edit the code cell below, then evaluate it before Cell 3. Every option is explained here and printed in full by Cell 1 (Reference) above; NLOOperators must be chosen from the catalogue for the selected HEFTNLOBasis.*)


(* Path to your local FeynRules installation (must contain FeynRules.m) *)
$FeynRulesPath="/Users/michalryczkowski/Library/Mathematica/Applications/feynrules-current";

(* Physics / expansion *)
HEFTGauge="unitary";                 (* "unitary" - the only gauge implemented. An unfinished R_xi branch exists in the source but is not supported; see README *)
HEFTMaxOrder=1;                      (* ChiralOrder truncation: 0 = LO only, 1 = NLO, 2 = NNLO. NOTE: 2 requires EWInputScheme = "heft" - the derived schemes "gf"/"aem" are NLO-only and Cell 3 aborts if you combine them with HEFTMaxOrder >= 2 *)
HiggsMaxOrder=3;                     (* Max (H/vev)^n order kept in the F-functions *)
KappaFramework=True;                 (* True -> Kappa parameterisation of SM couplings deviation; False = Delta parameterisation (see README) *)
InitialiseWCs=0;                     (* Default value Cell 3 writes for the EFFECTIVE Wilson coefficients: 1 or 0. SM couplings always keep their SM value (Kappa framework 1, Delta framework 0) regardless of this *)
LOYukawaExpansion = False;           (* True = keep the higher-order fermion-Higgs terms of the LO Yukawa sector: FQU/FQD/FLE = Sum_{n>=2} C<X>n<n>[ff1,ff2] (LamF H/vev)^n. False = drop them and do not declare CQUn/CQDn/CLEn at all. The mass and the single-Higgs coupling are unaffected either way *)
IncludeCustodialT = True;              (* True = keep the custodial-symmetry breaking operator PT = Tr[T.V_mu]Tr[T.V^mu] F_T(h) in the LO Lagrangian. False = drop it, and with it the CFTn coefficients (PT is their only user) *)
Combine2Derivatives=True;           (* False (default) = unchanged behaviour. True = for DH/P8NLO/P20NLO/P21NLO/P22NLO only, replace their two independently h/vev-truncated flare-function WC families with one new combined family per operator (C<op>n<nh>prime, nh = number of Higgs fields in that term, derivatives of h included), so each vertex gets a single WC instead of a sum of products of two. See README. *)

(* Input schemes *)
(* CHIRAL-ORDER RESTRICTION - enforced, not advisory:
     "heft"        -> any HEFTMaxOrder (0, 1, 2)
     "gf" / "aem"  -> HEFTMaxOrder <= 1 ONLY
   The derived schemes invert a muon-decay / gauge-mixing extraction that exists at O(ChiralOrder)
   only, so at HEFTMaxOrder >= 2 they would hand you silently NLO-accurate inputs inside an NNLO
   Lagrangian. Cell 3 aborts on that combination, and so does LoadModel in Cell 5. Use "heft" at
   NNLO and beyond. *)
EWInputScheme="aem";                (* "heft" - (g, g', v, hlambda) treated as external parameters. "gf" - expressed in terms of (Gf, MW, MZ, MH). "aem" - expressed in terms of (alpha_EM, Gf, MZ, MH), with MW then a PREDICTION rather than an input. "gf"/"aem" rewrite the Lagrangian via HEFTEWInputRepl and are NLO-only (see the note above); see README SS "Input scheme (EW)" *)
Massless=False;                      (* True -> load restrictions/Massless.rst before Feynman rules (zeroes light fermion masses, only tau, b, and t are massive) *)
DiagonalCKM=False;                   (* True -> load restrictions/DiagonalCKM.rst before Feynman rules (CKM -> identity) *)

(* NLO basis and operators - see Cell 1 (Reference) above for the full catalogue per basis *)
HEFTNLOBasis="1604.06801";           (* the only implemented basis; "2206.07722" (Sun et al.) is refused as not yet implemented *)
NLOOperators={"GHNLO"}; (* Active NLO/NNLO operator labels; {} = LO only. Must be a subset of the catalogue printed above; NNLO labels need HEFTMaxOrder >= 2 *)

OutputName="HEFT_GHNLO_AEM_scheme";              (* Output subdirectory name under output/ *)

MaxVertexLegs=Automatic;             (* Export-time cut on vertex multiplicity, honoured by Cells 6, 7 AND 8. Automatic (default) = no cut. An integer n >= 3 keeps only vertices with at most n legs (it becomes FeynRules' MaxParticles, which the UFO and FeynArts writers forward to their internal FeynmanRules call - unlike SmeftFR's option of the same name, this one does reach the exported model). NOT part of the cache key: Cell 5 builds the full Lagrangian either way, so changing this never forces a rebuild. Beware: quartics are the vertices that unitarise VV->VV, and in HEFT the h-expansion is what makes high multiplicities, so a cut also truncates the flare tower in the output while the WCxf files still list every coefficient. See README *)

ForceRebuildLHEFT=False;             (* True = skip the cache lookup, rebuild LHEFTMassBasis and overwrite the entry for this configuration *)

(* Must stay last: Cell 3 refuses to run without it, so that a Cell 3 evaluated in a kernel
   where this section never ran cannot silently fall back to the defaults for everything. *)
HEFT$ConfigEvaluated=True; 


(* ::Section:: *)
(*Cell 3 - configuration banner and Wilson-coefficient files*)


(* ::Text:: *)
(*These two only need to be set here - they stay set in Global context for the rest of this*)
(*kernel session, so Cells 4-8 below don't repeat them. If you restart the kernel, re-run*)
(*Cell 2 (Configuration) then this cell before jumping to a later one.*)
(**)
(*HEFT$FromNotebook - model_files/heft_fr.wl's very first statement quits the kernel unless*)
(*this flag is True. It is a guard against evaluating heft_fr.wl on its own, outside this*)
(*notebook, where none of the Configuration variables would be set. Setting it here is*)
(*what lets heft_fr.wl proceed at all.*)
(**)
(*HEFT$WorkspaceRoot - absolute path to the repository root, used to locate every model_files/**)
(*file Get'd below (heft_fr.wl, heft_notebook _reference.wl, HEFT_Model.fr, ...). *)*)


HEFT$FromNotebook=True;

HEFT$WorkspaceRoot=DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$NotebookCell=3;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 4 - edit Wilson coefficients (manual)*)


(* ::Text:: *)
(*The Wilson-coefficient workflow, in full - there is nothing to configure for it anywhere else.*)
(**)
(*Cell 3 always writes two files, built from the operator selection you configured, with every coefficient at its default value:*)
(*  - wcxf/wcxf_init.json  -  an untouched reference copy of those defaults. The model never reads it; it is there to look at, diff against, or copy back from.*)
(*  - wcxf/wcxf_output.json - the file the model actually reads in Cell 5.*)
(**)
(*To run with the defaults: do nothing - just go to Cell 5.*)
(**)
(*To use your own values: open wcxf/wcxf_output.json in any text editor and change the numbers under "values", then run Cell 5. What you write there is what enters the exported model. Deleting a key has the same effect as writing 0, since absent keys are read as 0. Cell 5 prints every value that differs from the default, so you can check at a glance what it picked up.*)
(**)
(*Careful: Cell 3 rewrites wcxf_output.json back to the defaults every time it runs. Edit after Cell 3, not before, and don't re-run Cell 3 once you have edited (if you do, it prints the values it is about to discard). Change the operator selection and you must re-run Cell 3, because the old file has no keys for the new operators - Cell 5 warns if it finds keys missing.*)
(**)
(*The code cell below prints the two paths as a reminder and re-runs the cache lookup against wcxf_output.json as it now stands on disk - the editing itself happens outside Mathematica. Editing values can never turn a cache hit into a rebuild, zeros included: Wilson coefficients are External parameters, so a value never enters LHEFT (it goes into the export through M$Parameters), and none of them is part of the cache key. Only the settings in Cell 2 and the .fr sources decide that.*)


HEFT$NotebookCell=4;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 5 - load model, build LHEFT*)
(**)


(* ::Text:: *)
(*Produces LHEFT (the mass-basis Lagrangian). That's all Cell 7 (export) needs - you can go straight to Cell 7 from here and skip Cell 6 entirely.*)


HEFT$NotebookCell=5;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 6 - compute Feynman rules*)


(* ::Text:: *)
(*Optional side branch off Cell 5, not a required step before Cell 7: computes RulesHEFT from LHEFT, prints the vertex count, and saves RulesHEFT to output/FeynmanRules/<OutputName>/RulesHEFT.mx (reload later with Get). Cell 7's WriteUFO/WriteFeynArtsOutput compute whatever Feynman rules they need internally from LHEFT directly - they never read RulesHEFT, so this step can always be skipped unless you want the rules themselves.*)


HEFT$NotebookCell=6;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


Print["W-W-H-H vertex: ",
SelectVertices[RulesHEFT, SelectParticles -> {W, Wbar, H, H}]];


(* ::Section:: *)
(*Cell 7 - UFO export*)


(* ::Text:: *)
(*Writes output/UFO/<OutputName>/. Only requires LHEFT from Cell 5 - safe to run right after Cell 5, whether or not you ran Cell 6. There is no OutputFormat option: this cell is the UFO export, Cell 8 below is the FeynArts one, and you may run either or both.*)


HEFT$NotebookCell=7;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 8 - FeynArts export*)


(* ::Text:: *)
(*Writes output/FeynArts/<OutputName>/ (.mod, .gen, .pars). Like Cell 7 it needs only LHEFT from Cell 5, and the two are independent - run this one, Cell 7, or both.*)


HEFT$NotebookCell=8;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];
