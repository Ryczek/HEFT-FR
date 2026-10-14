(* ::Package:: *)

(* ::Title:: *)
(*HEFT-FR -- merge FeynArts and UFO exports*)


(* ::Text:: *)
(*One of the two merging notebooks in heft_merging/, beside heft_fr_notebook.wl. Open it in Mathematica and evaluate it section by section. Use it to build one LARGE FeynArts or UFO model out of exports of several SMALL models that you have already made with heft_fr_notebook.wl (Cell 7 for UFO, Cell 8 for FeynArts). Nothing is rebuilt and FeynRules is not loaded: the merge works on the exported files, so the expensive export is paid only for the small models. This matters most for UFO, whose writer is the slowest step of the pipeline.*)
(**)
(*The other notebook, merge_cached_models.wl, merges the cached LAGRANGIANS of the small models instead and then exports the merged model.*)
(**)
(*WHY IT WORKS*)
(*Every coupling of the merged model is*)
(*    C(A u B) = C(SM) + (C(A) - C(SM)) + (C(B) - C(SM))*)
(*the same arithmetic as merging cached Lagrangians, one step later in the pipeline. It is exact because the model keeps one Wilson-coefficient insertion per vertex. The SM-only export has to be subtracted: each export contains the whole SM, so adding N of them naively would scale every SM vertex by N.*)
(**)
(*WHAT YOU NEED FIRST*)
(*- The exports of the sub-models, made with heft_fr_notebook.wl, each with its own EFTOperators and ALL OTHER OPTIONS IDENTICAL, including MaxVertexLegs. Each export folder holds a heft_export.json with the configuration it was made with (FeynArts exports since 2026-09-29, UFO exports since 2026-10-06; older ones must be re-exported).*)
(*- One SM-only export (EFTOperators = {}) with the same options, in each format you merge.*)
(*- FeynArts with four-fermion operators: every export, the SM-only one included, made with FeynArtsDiracIndices = True.*)
(*- UFO: a Python 3 interpreter (standard library only), found automatically or set as HEFT$Python.*)
(**)
(*CELLS*)
(*  1  Reference - what export merging does, what it needs, what it refuses*)
(*  2  Configuration - the options the exports were made with*)
(*  3  Lists the FeynArts exports made with this configuration*)
(*  4  MergeFeynArtsSources - merges those exports into output/FeynArts/<OutputName>/*)
(*  5  Lists the UFO exports made with this configuration*)
(*  6  MergeUFOSources - merges those exports into output/UFO/<OutputName>/*)
(*The FeynArts half (3-4) and the UFO half (5-6) are independent: run either or both. No cell loads FeynRules or a model, so any of them can be re-run in the same kernel.*)


(* ::Section:: *)
(*Cell 1 - Reference*)


(* ::Text:: *)
(*Prints the About block, what export merging does, and the rules it enforces. No FeynRules, no configuration needed - safe to re-run at any time.*)


HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=ParentDirectory@DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];   (* this notebook is in heft_merging/; the package root is its parent *)

HEFT$MergeExportCell=1;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge_exports.wl"}];


(* ::Section:: *)
(*Cell 2 - Configuration*)


(* ::Text:: *)
(*Set the options the exports were made with, then evaluate. Every option below must match the exports exactly: Cells 3 and 5 show only the exports that agree with it, so a mismatch shows up as an empty (or short) list rather than as a wrong model. There is no EFTOperators here: the operators of the merged model are the union of the exports you merge.*)
(**)
(*FeynRules is not loaded, but its folder is needed: every export records the digest of the FeynRules interface that wrote it, and only exports written by the same interface are merged.*)


(* Path to your local FeynRules installation (must contain FeynRules.m); read, not loaded *)
$FeynRulesPath="";   (* SET THIS to your FeynRules folder, e.g. FileNameJoin[{$UserBaseDirectory, "Applications", "feynrules-current"}]; Cells 3-6 refuse to run while it is empty *)

(* Must match the exports *)
HiggsMaxOrder=3;                     (* Max (H/vev)^n order kept in the F-functions *)
KappaFramework=True;                 (* True -> Kappa parameterisation of SM couplings deviation; False = Delta parameterisation (see README) *)
EWInputScheme="heft";                (* "heft" / "gf" / "aem". See README SS "Input scheme (EW)" *)
Massless=False;                      (* True if the exports were made with restrictions/Massless.rst *)
DiagonalCKM=False;                   (* True if the exports were made with restrictions/DiagonalCKM.rst *)
MaxVertexLegs=6;                     (* The vertex-multiplicity cut the exports were made with. Automatic = no cut; an integer n >= 3 *)

OutputName="HEFT_MergedExports";     (* Output subdirectory name under output/FeynArts/ and/or output/UFO/; must differ from the names of the exports you merge *)

(* Must stay last: Cells 3-6 refuse to run without it, so that a cell evaluated in a kernel
   where this section never ran cannot silently fall back to the defaults for everything. *)
HEFT$ConfigEvaluated=True;


(* ::Section:: *)
(*Cell 3 - find the FeynArts exports that match this configuration*)


(* ::Text:: *)
(*Prints every export in output/FeynArts/ made with exactly the configuration of Cell 2 - every option, the .fr digest (modelDigest), MaxVertexLegs and the FeynArts interface that wrote it - with its name and operators. Those names are what you put into MergeFeynArtsSources in Cell 4. It also reports near-misses with the option they differ in, and export folders without a heft_export.json (exported before 2026-09-29: re-export them with Cell 8 of heft_fr_notebook.wl to use them).*)


HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=ParentDirectory@DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$MergeExportCell=3;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge_exports.wl"}];


(* ::Section:: *)
(*Cell 4 - merge FeynArts exports*)


(* ::Text:: *)
(*Builds output/FeynArts/<OutputName>/ (.mod, .gen, .pars and heft_export.json) out of the exports named below. Every coupling becomes SM + the sum of each export's deviation from the SM-only export. Do NOT list the SM-only export: it is found automatically and subtracted. If Cell 3 shows several, name one in MergeFeynArtsBaseline.*)
(**)
(*Refused rather than warned about: an export not listed by Cell 3, an operator in two exports, a name listed twice, an OutputName equal to one of the inputs, exports that differ outside their couplings, and exports in two fermion forms. The result carries its own heft_export.json, so it can itself be a source of a later merge.*)
(**)
(*The .pars file is only united, not merged: FeynArts reads .mod and .gen alone. Where two exports hold different values for one parameter (e.g. a Kappa edited in one wcxf_output.json), the SM-only export's value is kept and the cell says so.*)


MergeFeynArtsSources={};             (* e.g. {"HEFT_P1", "HEFT_P12", "HEFT_PW"} - names from the Cell 3 table *)

MergeFeynArtsBaseline=Automatic;     (* Automatic = the one SM-only export Cell 3 finds; or its name, if there are several *)

HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=ParentDirectory@DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$MergeExportCell=4;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge_exports.wl"}];


(* ::Section:: *)
(*Cell 5 - find the UFO exports that match this configuration*)


(* ::Text:: *)
(*Prints every export in output/UFO/ made with exactly the configuration of Cell 2 - every option, the .fr digest (modelDigest), MaxVertexLegs and the FeynRules UFO interface that wrote it - with its name and operators. Those names are what you put into MergeUFOSources in Cell 6. It also reports near-misses with the option they differ in, and UFO folders without a UFO heft_export.json (exported before 2026-10-06: re-export them with Cell 7 of heft_fr_notebook.wl to use them).*)


HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=ParentDirectory@DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$MergeExportCell=5;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge_exports.wl"}];


(* ::Section:: *)
(*Cell 6 - merge UFO exports*)


(* ::Text:: *)
(*Builds output/UFO/<OutputName>/ (the UFO .py files and heft_export.json) out of the exports named below. Every coupling becomes SM + the sum of each export's deviation from the SM-only export, the same arithmetic as Cell 4. Do NOT list the SM-only export: it is found automatically and subtracted. If Cell 5 shows several, name one in MergeUFOBaseline.*)
(**)
(*Merged: vertices, couplings and Lorentz structures (compared by content, renumbered), parameters (an internal parameter that differs between exports, such as MZ in the heft scheme with P1/P12/PT, is merged the same way; FeynRules' per-export abbreviations are renamed per source; the LHA block HEFTBOSONIC is renumbered). Copied, and required to be identical in every export: particles, coupling orders, propagators and the UFO library files. NOT written: decays.py - FeynRules' widths are quadratic in the couplings and cannot be added; let MadGraph compute the widths (compute_widths, or Auto in the param card).*)
(**)
(*Refused rather than warned about: an export not listed by Cell 5, an operator in two exports, a name listed twice, an OutputName equal to one of the inputs, exports that differ in a copied file, a baseline vertex missing from a sub-model, and a particle set written in two different orders. The result carries its own heft_export.json, so it can itself be a source of a later merge. Needs a Python 3 interpreter (standard library only); set HEFT$Python if it is not found.*)


MergeUFOSources={};                  (* e.g. {"HEFT_P1", "HEFT_P12", "HEFT_PW"} - names from the Cell 5 table *)

MergeUFOBaseline=Automatic;          (* Automatic = the one SM-only export Cell 5 finds; or its name, if there are several *)

HEFT$FromMergeNotebook=True;

HEFT$WorkspaceRoot=ParentDirectory@DirectoryName@If[$Notebooks,NotebookFileName[],ExpandFileName@$InputFileName];

SetDirectory[HEFT$WorkspaceRoot];

HEFT$MergeExportCell=6;

Get@FileNameJoin[{HEFT$WorkspaceRoot,"model_files","heft_fr_merge_exports.wl"}];
