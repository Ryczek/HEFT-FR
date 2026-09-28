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
(*   (a) the model description, authors and references, and the full operator catalogue (user-defined operators included) - always*)
(*   (b) the configuration-option table: every variable of Cell 2, what it does, allowed values.*)
(*         Set IgnoreInstructions = True in that cell to suppress (b); (a) is printed either way.*)
(**)
(*CELL 2 - Configuration (re-evaluate after every change, before Cell 3)*)
(*One code cell holding every run option, and every path: $FeynRulesPath, and HEFT$WorkspaceRoot (this package's folder, set automatically) for the whole kernel session. The operator labels in EFTOperators must come from the catalogue printed by Cell 1 - Cell 3 aborts with "Unknown operator(s)" if one does not exist.*)
(**)
(*CELL 3 - Configuration banner and Wilson-coefficient files*)
(*Checks the configuration (unset options get their defaults, unknown operators abort), loads FeynRules, prints the active configuration, and writes the two Wilson-coefficient files wcxf/wcxf_init.json and wcxf/wcxf_output.json for exactly that operator selection. Nothing is built yet. It ends with the cache lookup, so you know here whether Cell 5 will load an existing build or start a new one. Must be run before any later cell.*)
(**)
(*CELL 4 - Edit Wilson coefficients (OPTIONAL - skip it to run with the defaults)*)
(*There are no flags for this: the model always reads wcxf/wcxf_output.json. Edit the numbers in it to change coefficients, or leave it alone for the defaults Cell 3 just wrote. Cell 4 itself only prints the paths and re-runs the cache lookup for the file as it now stands - the editing happens in a text editor. Re-running Cell 3 resets the file, so edit after it, not before. The Cell 4 section below describes this in full.*)
(**)
(*CELL 5 - Load model, build LHEFT*)
(*Runs LoadModel on model_files/HEFT_Model.fr, applies the .rst restrictions if Massless / DiagonalCKM are True, then produces LHEFT, the Lagrangian in the mass basis. Before building it checks HEFT_cache/ for a build of this exact configuration, saved under any OutputName; only if there is none, is LHEFT built from scratch (minutes to hours, depending on the operator count). Every build is saved. ForceRebuildLHEFT = True is the only way to override this.*)
(*Changing Wilson-coefficient values NEVER costs a rebuild, zeros included: they are External parameters, so a value never enters LHEFT.*)
(**)
(*CELL 6 - compute Feynman rules (OPTIONAL)*)
(*A side branch off Cell 5: computes RulesHEFT = FeynmanRules[LHEFT], prints the vertex count, and saves it to output/FeynmanRules/<OutputName>/ - <OutputName>.mx (a Mathematica-reloadable dump), <OutputName>.txt (a plain-text listing of every vertex), and latex/<OutputName>.tex (a standalone LaTeX document, in its own subfolder). Cell 7 does NOT read RulesHEFT - it computes whatever it needs from LHEFT itself - so this step can always be skipped unless you want the rules themselves.*)
(**)
(*CELLS 7 and 8 - export: Cell 7 (UFO) and/or Cell 8 (FeynArts)*)
(*Need only LHEFT from Cell 5,  and you may run both. Cell 7 writes output/UFO/<OutputName>/; Cell 8 writes output/FeynArts/<OutputName>/ (.mod/.gen/.pars).*)
(**)
(*WHERE THINGS ARE*)
(*  model_files/    	model source (HEFT_Model.fr, parameters/, Lagrangian/, heft_fr.wl and helpers)*)
(*  wcxf/             	 	Wilson-coefficient JSON (init template + output which is actually read)*)
(*  HEFT_cache/     	cached mass-basis Lagrangians, one subfolder per configuration (<OutputName>__<configHash>/)*)
(*  output/         		UFO/, FeynArts/ and FeynmanRules/ exports, one subfolder per OutputName*)
(*  restrictions/   		Massless.rst, DiagonalCKM.rst*)
(*  README.md       	detailed packade description*)


(* ::Section:: *)
(*Cell 1 - Reference*)


(* ::Text:: *)
(*Evaluate this cell to print the model description, the references and the operator catalogue, and the configuration-options (unless IgnoreInstructions=True). *)
(*Independent of the Configuration section, which runs later, so you can look up operators here before deciding what to configure. No FeynRules or model loading needed; can be re-run anytime.*)


Get@FileNameJoin[{DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName],"model_files","heft_notebook_reference.wl"}];
IgnoreInstructions=False; (* True = skip the description of the configuration options *)
HEFT$PrintNotebookReference[];


(* ::Section:: *)
(*Cell 2 - Configuration *)


(* ::Text:: *)
(*Edit the code cell below, then evaluate it before Cell 3. Every option is explained here and printed in full by Cell 1 (Reference) above; EFTOperators must be chosen from the catalogue printed there.*)


(* Paths *)
(* Path to your local FeynRules installation (must contain FeynRules.m) *)
$FeynRulesPath="/Users/michalryczkowski/Library/Mathematica/Applications/feynrules-current";
(* Location of this package, do not edit!*)
HEFT$WorkspaceRoot=DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];
SetDirectory[HEFT$WorkspaceRoot];

(* Physics / expansion *)
HiggsMaxOrder=3;                     (* Max (H/vev)^n order kept in the F-functions *)
KappaFramework=True;                 (* True -> Kappa parameterisation of SM couplings deviation; False = Delta parameterisation (see README/draft) *)
InitialiseWCs=0;                     (* Default value Cell 3 writes for the Effective Wilson coefficients: 1 or 0. SM couplings always keep their SM value (Kappa framework 1, Delta framework 0) regardless of this *)

(* Input schemes *)
EWInputScheme="heft";                (* "heft" - (g, g', v, hlambda) treated as external input parameters. "gf" - (g, g', v, hlambda) expressed in terms of (Gf, MW, MZ, MH). "aem" - (g, g', v, hlambda) expressed in terms of (alpha_EM, Gf, MZ, MH) *)
Massless=False;                      (* True -> load restrictions/Massless.rst before Feynman rules (zeroes light fermion masses, only tau, b, and t are massive) *)
DiagonalCKM=False;                   (* True -> load restrictions/DiagonalCKM.rst before Feynman rules (CKM -> identity) *)

(* EFT operators - see Cell 1 (Reference) above for the full catalogue. *)
EFTOperators={"PW","NQ22"};          (* Active EFT operator labels. {} = SM only*)

OutputName="HEFT_Example";           (* Output subdirectory name under HEFT_Frules/output/ *)

MaxVertexLegs=6;                     (* Cut on vertex multiplicity, honoured by Cells 6, 7 and 8. Automatic (default) = no cut. An integer n >= 3 keeps only vertices with at most n legs *)

ForceRebuildLHEFT=False;             (* True = skip the cache lookup, rebuild LHEFTMassBasis and overwrite the entry for this configuration *)

(* Must stay last: Cell 3 refuses to run without it, so that a Cell 3 evaluated in a kernel where this section never ran cannot silently fall back to the defaults for everything. *)
HEFT$ConfigEvaluated=True; 


(* ::Section:: *)
(*Cell 3 - Check configuration, load FeynRules, write Wilson-coefficient files*)


(* ::Text:: *)
(*Checks the configuration, loads FeynRules and writes the Wilson-coefficient files. Nothing is built yet.*)
(*  - Aborts if Cell 2 was not run, or if an operator label is unknown or; unset options get their defaults;*)
(*  - Writes wcxf/wcxf_init.json (defaults, for reference) and wcxf/wcxf_output.json (read by Cell 5), resetting any edits;*)
(*  - Ends with the cache lookup: whether Cell 5 will load an existing build or build a new one.*)
(*Re-run it after every change to Cell 2, and after a kernel restart.*)


HEFT$FromNotebook=True;

HEFT$NotebookCell=3;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 4 - Edit Wilson coefficients (manual)*)


(* ::Text:: *)
(*The Wilson coefficient workflow, in full - there is nothing to configure for it anywhere else.*)
(**)
(*Cell 3 always writes two files, built from the operator selection you configured, with every coefficient at its default value:*)
(*  - wcxf/wcxf_init.json  -  an untouched reference copy of those defaults. The model never reads it; it is there to look at, diff against, or copy back from.*)
(*  - wcxf/wcxf_output.json - the file the model actually reads in Cell 5.*)
(**)
(*To run with the defaults: do nothing - just go to Cell 5.*)
(**)
(*To use your own values: open wcxf/wcxf_output.json in any text editor and change the numbers under "values", then run Cell 5. What you write there is what enters the exported model. Deleting a key has the same effect as writing 0, since absent keys are read as 0. Cell 5 prints every value that differs from the default, so you can check at a glance what it picked up.*)
(**)
(*Warning: Cell 3 rewrites wcxf_output.json back to the defaults every time it runs. Edit after Cell 3, not before, and don't re-run Cell 3 once you have edited (if you do, it prints the values it is about to discard). *)
(*If you change the operator selection, you must re-run Cell 3, because the old file has no keys for the new operators - Cell 5 warns if it finds keys missing.*)
(**)
(*The code cell below prints the two paths as a reminder and re-runs the cache lookup against wcxf_output.json as it now stands on disk - the editing itself happens outside Mathematica. *)


HEFT$NotebookCell=4;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 5 - load model, build LHEFT*)


(* ::Text:: *)
(*Produces LHEFT (the mass-basis Lagrangian). That's all Cell 7 and 8 (UFO and FeynArts exports) need - you can go straight to Cell 7 or 8 from here, skiping Cell 6 entirely.*)


HEFT$NotebookCell=5;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 6 - compute Feynman rules*)


(* ::Text:: *)
(*Optional side branch off Cell 5, not a required step before Cell 7: computes RulesHEFT from LHEFT, prints the vertex count, and saves RulesHEFT to output/FeynmanRules/<OutputName>/RulesHEFT.mx (reload later with Get). Cell 7's WriteUFO/WriteFeynArtsOutput compute whatever Feynman rules they need internally from LHEFT directly - they never read RulesHEFT, so this step can always be skipped unless you want the rules themselves.*)


HEFT$NotebookCell=6;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Text:: *)
(*Print a few example vertices: edit the list below (leg order does not matter)*)


exampleVertices = {
  {H, H, H},
  {W, Wbar, H},
  {Z, Z, H},
  {W, Wbar, H, H},
  {Z, Z, H, H},
  {A, W, Wbar},
  {G, G, H},
  {t, tbar, H}
};

HEFT$PrintVertices[exampleVertices];


(* ::Section:: *)
(*Cell 7 - UFO export*)


(* ::Text:: *)
(*Writes output/UFO/<OutputName>/. Only requires LHEFT from Cell 5 - safe to run right after Cell 5. *)


HEFT$NotebookCell=7;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];


(* ::Section:: *)
(*Cell 8 - FeynArts export*)


(* ::Text:: *)
(*Writes output/FeynArts/<OutputName>/ (.mod, .gen, .pars). Like Cell 7 it needs only LHEFT from Cell 5, and the two are independent - run this one, Cell 7, or both.*)


HEFT$NotebookCell=8;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr.wl"}];
