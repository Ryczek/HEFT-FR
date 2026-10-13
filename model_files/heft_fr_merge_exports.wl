(* ::Package:: *)

(* Guard: this file is only ever meant to be Get-ed from heft_merging/merge_exports.wl, which sets
   HEFT$FromMergeNotebook = True. Evaluating it standalone would run with no configuration at all,
   so quit instead. *)
If[!TrueQ[HEFT$FromMergeNotebook], Quit[]]

(* HEFT merging of FeynArts and UFO EXPORTS, driven by heft_merging/merge_exports.wl (split off the
   single merge notebook on 2026-10-13, where these were Cells 9-12):

   CELL 1  Reference - what export merging does, what it needs, what it refuses
   CELL 2  Configuration (notebook only, no code here) - the options the exports were made with
   CELL 3  List the FeynArts exports (output/FeynArts/) made with the Cell 2 configuration
   CELL 4  Merge FeynArts exports (MergeFeynArtsSources) into output/FeynArts/<OutputName>/
   CELL 5  List the UFO exports (output/UFO/) made with the Cell 2 configuration
   CELL 6  Merge UFO exports (MergeUFOSources) into output/UFO/<OutputName>/ (decays.py omitted)

   No FeynRules is loaded and no model is built: the cells read heft_export.json records and the
   export files from disk.  $FeynRulesPath is still needed, because every record carries the digest
   of the FeynRules interface that wrote it.  Cells 5-6 need a Python 3 interpreter.
   The FeynArts merge lives in model_files/fa_merge.wl, the UFO merge in model_files/ufo_merge.wl +
   ufo_merge.py, the shared helpers in model_files/heft_merge_common.wl. *)

HEFT$MergeExportShouldRunCell[heftN_Integer] :=
  !ValueQ[HEFT$MergeExportCell] || HEFT$MergeExportCell === heftN;

If[!ValueQ[HEFT$WorkspaceRoot],
  HEFT$WorkspaceRoot = DirectoryName @ DirectoryName @ ExpandFileName @ $InputFileName
];
Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_merge_common.wl"}];

(* Every cell after Cell 2: the configuration must have been evaluated in this kernel, and
   $FeynRulesPath must point at a FeynRules installation (it is read, not loaded). *)
HEFT$MergeExportPrecheck[] := Module[{},
  If[!TrueQ[HEFT$ConfigEvaluated],
    Print[Style["[HEFT merge] ERROR: the Configuration section has not been evaluated in this " <>
      "kernel. Evaluate Cell 2 first, then this cell.", Red, Bold]];
    Abort[]
  ];
  HEFT$MergeCheckFeynRulesPath[];
  HEFT$MergeBootstrap[]
];


(* =============================================================================
   CELL 1 \[LongDash] Reference
   ============================================================================= *)

If[HEFT$MergeExportShouldRunCell[1],

Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_notebook_reference.wl"}];

HEFT$MergePrintBanner["HEFT FeynRules \[LongDash] merging FeynArts and UFO exports"];
HEFT$PrintAbout[];

HEFT$MergePrintSubsection["What this notebook does"];
Print["    Builds one large FeynArts or UFO model out of several small exports already on disk,"];
Print["    without re-running FeynRules. Every coupling of the result is"];
Print[Style["\n        C = C(SM) + (C(A) - C(SM)) + (C(B) - C(SM)) + ...\n", FontFamily -> "Monospace"]];
Print["    - the same arithmetic as merging cached Lagrangians, one step later in the pipeline, so"];
Print["    the expensive export is paid only for the small models. It is exact because the model"];
Print["    keeps one Wilson-coefficient insertion per vertex."];

HEFT$MergePrintSubsection["How to use it"];
Print["    1.  Export every sub-model with heft_fr_notebook.wl (Cell 7 for UFO, Cell 8 for"];
Print["        FeynArts), each with its own EFTOperators and ALL OTHER OPTIONS IDENTICAL,"];
Print["        including MaxVertexLegs, plus one SM-only export (EFTOperators = {})."];
Print["    2.  Cell 2  - set the configuration those exports were made with."];
Print["    3.  Cell 3  - lists the FeynArts exports made with it;"];
Print["        Cell 4  - put their names in MergeFeynArtsSources; writes output/FeynArts/<OutputName>/."];
Print["    4.  Cell 5  - lists the UFO exports made with it;"];
Print["        Cell 6  - put their names in MergeUFOSources; writes output/UFO/<OutputName>/"];
Print["                  (no decays.py: widths are not additive, let MadGraph compute them)."];
Print["    The FeynArts and UFO halves are independent: run either or both."];
Print[""];
Print["    To merge CACHED LAGRANGIANS instead, and export the result, use the other notebook,"];
Print["    heft_merging/merge_cached_models.wl."];

HEFT$MergePrintSubsection["What has to agree, and what is refused"];
Print["    Every export carries heft_export.json: its configuration, the .fr digest (modelDigest),"];
Print["    MaxVertexLegs and the digest of the FeynRules interface that wrote it. Two exports may"];
Print["    be merged only if all of these agree; the operator selection is the one thing allowed"];
Print["    to differ."];
Print[""];
Print["    Refused rather than warned about:"];
Print["      \[Bullet] an export not listed by Cell 3 / Cell 5 (other configuration, no record);"];
Print["      \[Bullet] a missing SM-only export, an operator in two exports, a name listed twice;"];
Print["      \[Bullet] an OutputName equal to one of the inputs;"];
Print["      \[Bullet] exports that differ outside their couplings (FeynArts: .gen and the model"];
Print["        structure; UFO: particles, coupling orders, propagators, library files), a baseline"];
Print["        vertex missing from a sub-model, a particle set written in two orders (UFO);"];
Print["      \[Bullet] FeynArts exports in two fermion forms (FeynArtsDiracIndices): with"];
Print["        four-fermion operators, make every export, the SM-only one included, with True."];

Print[Style["\n[HEFT merge] Cell 1 done. Next: Cell 2 (Configuration).", Bold]];

]; (* end export-merge cell 1 gate *)


(* =============================================================================
   CELL 3 \[LongDash] FeynArts exports that match this configuration
   ============================================================================= *)

If[HEFT$MergeExportShouldRunCell[3],

HEFT$MergeExportPrecheck[];
Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "fa_merge.wl"}];

HEFT$MergePrintBanner["HEFT FeynRules \[LongDash] FeynArts exports"];
Print[Style["\n  Exports: ", Bold], HEFTFAExportsDir[]];
HEFT$FAMergeCompatible = HEFTFAPrintCatalog[HEFTFAExportIndex[], HEFTExportCurrentMeta["feynarts"]];

Print[Style["\n[HEFT merge] Cell 3 done.", Bold]];
Print["[HEFT merge] Next: put the names you want from the table above into " <>
  "MergeFeynArtsSources in Cell 4."];

]; (* end export-merge cell 3 gate *)


(* =============================================================================
   CELL 4 \[LongDash] Merge FeynArts exports
   ============================================================================= *)

If[HEFT$MergeExportShouldRunCell[4],

HEFT$MergeExportPrecheck[];
Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "fa_merge.wl"}];

If[!ValueQ[MergeFeynArtsSources] || !ListQ[MergeFeynArtsSources] || MergeFeynArtsSources === {},
  Print[Style["[HEFT merge] ERROR: MergeFeynArtsSources is not set. Set it in Cell 4 to a list " <>
    "of names from the Cell 3 table, e.g. MergeFeynArtsSources = {\"HEFT_P1\", \"HEFT_PW\"};",
    Red, Bold]];
  Abort[]
];

HEFT$MergePrintBanner["HEFT FeynRules \[LongDash] FeynArts merge"];
HEFTFAMergeRun[MergeFeynArtsSources, OutputName,
  If[ValueQ[MergeFeynArtsBaseline], MergeFeynArtsBaseline, Automatic]];

Print["[HEFT merge] Done."];

]; (* end export-merge cell 4 gate *)


(* =============================================================================
   CELL 5 \[LongDash] UFO exports that match this configuration
   ============================================================================= *)

If[HEFT$MergeExportShouldRunCell[5],

HEFT$MergeExportPrecheck[];
Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "ufo_merge.wl"}];

HEFT$MergePrintBanner["HEFT FeynRules \[LongDash] UFO exports"];
Print[Style["\n  Exports: ", Bold], HEFTUFOExportsDir[]];
HEFT$UFOMergeCompatible = HEFTUFOPrintCatalog[HEFTUFOExportIndex[], HEFTExportCurrentMeta["ufo"]];

Print[Style["\n[HEFT merge] Cell 5 done.", Bold]];
Print["[HEFT merge] Next: put the names you want from the table above into " <>
  "MergeUFOSources in Cell 6."];

]; (* end export-merge cell 5 gate *)


(* =============================================================================
   CELL 6 \[LongDash] Merge UFO exports
   ============================================================================= *)

If[HEFT$MergeExportShouldRunCell[6],

HEFT$MergeExportPrecheck[];
Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "ufo_merge.wl"}];

If[!ValueQ[MergeUFOSources] || !ListQ[MergeUFOSources] || MergeUFOSources === {},
  Print[Style["[HEFT merge] ERROR: MergeUFOSources is not set. Set it in Cell 6 to a list " <>
    "of names from the Cell 5 table, e.g. MergeUFOSources = {\"HEFT_P1\", \"HEFT_PW\"};",
    Red, Bold]];
  Abort[]
];

HEFT$MergePrintBanner["HEFT FeynRules \[LongDash] UFO merge"];
HEFTUFOMergeRun[MergeUFOSources, OutputName,
  If[ValueQ[MergeUFOBaseline], MergeUFOBaseline, Automatic]];

Print["[HEFT merge] Done."];

]; (* end export-merge cell 6 gate *)
