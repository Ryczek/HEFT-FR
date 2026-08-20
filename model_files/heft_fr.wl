(* ::Package:: *)

(* Guard: this file is only ever meant to be Get-ed from heft_fr_notebook.wl, which sets
   HEFT$FromNotebook = True in its Cell 3. Evaluating it standalone would run with no
   configuration at all, so quit instead. *)
If[!TrueQ[HEFT$FromNotebook], Quit[]]

(* HEFT FeynRules engine, driven by heft_fr_notebook.wl.  The notebook's Cell 1 (Reference)
   and Cell 2 (Configuration) contain no code from this file; the six cells below are the ones
   that Get it, and each sets HEFT$NotebookCell to its own number first:
   CELL 3  Load FeynRules, echo the configuration, write WCxf templates
   CELL 4  Edit wcxf/wcxf_output.json manually (optional; no code to run)
   CELL 5  LoadModel, build the mass-basis Lagrangian (LHEFT)
   CELL 6  Compute Feynman rules from LHEFT, save to output/FeynmanRules/<OutputName>/ as
           <OutputName>.mx + .txt, and latex/<OutputName>.tex (optional; Cell 7/8 exports
           don't need it)
   CELL 7  UFO export
   CELL 8  FeynArts export
   All user options are set inline in heft_fr_notebook.wl's Configuration section;
   anything left unset falls back to heft_defaults.wl. *)

HEFT$NBShouldRunCell[heftN_Integer] :=
  !ValueQ[HEFT$NotebookCell] || HEFT$NotebookCell === heftN;

(* ---------------------------------------------------------------------------
   MaxVertexLegs \[LongDash] export-time cut on vertex multiplicity (Cells 6, 7 and 8)

   Automatic (the default) leaves every vertex in.  An integer n keeps only vertices with at
   most n legs, in whichever of the three output cells you run.

   It is applied by handing FeynRules its own MaxParticles option, which is NOT specific to
   FeynmanRules: WriteUFO (Interfaces/UFO/PYIntMain.m) and WriteFeynArtsOutput
   (Interfaces/FeynArtsInterface.m) are not given a vertex list, they build one by calling
   FeynmanRules themselves and forward MaxParticles to it, so setting it on the writer really
   does shrink the exported model.  (SmeftFR's option of the same name does not, which is what
   2302.01353 Tab. 3 means by "Does not affect UFO and FeynArts output" - it reaches SmeftFR's
   own Feynman-rule call only.  That caveat is about SmeftFR, not about FeynRules.)

   It is not a filter on the finished vertices either: LagrangianTermSelectionRules
   (Core/VertexRoutine.m) drops Lagrangian TERMS carrying more than n fields after index
   expansion and before the vertex algebra runs, so the cut saves time as well as output size.

   Deliberately NOT part of the HEFT_cache/ key (HEFTLHEFTCacheMeta[] in lheft_cache.wl): it
   changes nothing about LHEFT, only what is read off it at export time, so two exports
   differing only in MaxVertexLegs share one cached Lagrangian.  Same reasoning as
   InitialiseWCs.

   Know what it costs physically before using it.  The quartics it removes first are exactly
   the ones that unitarise VV -> VV; and in HEFT it is the h-expansion (HiggsMaxOrder) that
   generates high multiplicities, so a cut here silently truncates the flare-function tower in
   the output while wcxf_output.json still lists every coefficient.  This is a tool for
   cutting an export down to the vertices one study needs, not a physics option. *)

HEFT$MaxVertexLegsValue[] := If[ValueQ[MaxVertexLegs], MaxVertexLegs, Automatic];

(* Automatic, or an integer >= 3.  Anything smaller is refused rather than honoured: FeynRules
   returns no 1- or 2-point vertices at all (confirmed the hard way), so MaxVertexLegs = 2
   would export an empty model, not a restricted one. *)
HEFT$CheckMaxVertexLegs[] := Module[{heftN = HEFT$MaxVertexLegsValue[]},
  If[heftN === Automatic, Return[True]];
  If[!IntegerQ[heftN] || heftN < 3,
    Print[Style["[HEFT] ERROR: MaxVertexLegs = " <> ToString[heftN, InputForm] <>
      " is not a usable value.", Red, Bold]];
    Print[Style["[HEFT] Use Automatic (no cut) or an integer >= 3. FeynRules returns no 1- " <>
      "or 2-point vertices, so a smaller cut would export an empty model rather than a " <>
      "restricted one.", Darker[Red]]];
    Abort[]
  ];
  True
];

(* =============================================================================
   CELL 3 \[LongDash] Configuration & WCxf template generation
   ============================================================================= *)

If[HEFT$NBShouldRunCell[3],

(* ======================= CONFIGURATION PRESENT? ======================= *)

(* The kernel reset lives in the notebook's Reference cell, not here: it runs before the
   Configuration section, so a quit there costs nothing the user has set.  Cell 3 deliberately
   does NOT quit (a quit at this point would always throw away the Configuration just
   evaluated).  Cell 5 still refuses to load a second model, so the corrupted-state path
   remains closed.

   This check catches the other half of the problem.  After the Reference cell quits, the
   Configuration section has not run - but this cell sets HEFT$FromNotebook /
   HEFT$WorkspaceRoot itself, so without the check Cell 3 would sail on and
   HEFT$ApplyConfigDefaults[] would quietly substitute defaults for every option the user had
   chosen.  The Configuration cell sets HEFT$ConfigEvaluated = True as its last line. *)
If[!TrueQ[HEFT$ConfigEvaluated],
  Print[Style["[HEFT] ERROR: the Configuration section has not been evaluated in this kernel.", Red, Bold]];
  Print[Style["[HEFT] Evaluate the Configuration cell first, then Cell 3. (Running now would " <>
    "silently use the defaults from model_files/heft_defaults.wl, not your settings.)", Red]];
  Abort[]
];

(* ======================= PATHS & FEYNRULES ======================= *)

(* This file lives in model_files/; the workspace root is one level up. *)
If[!ValueQ[HEFT$WorkspaceRoot],
  HEFT$WorkspaceRoot = DirectoryName @ DirectoryName @ ExpandFileName @ $InputFileName
];

(* Single source of default values: fills in any variable the notebook's own
   Configuration section left unset. *)
Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_defaults.wl"}];

HEFT$ApplyConfigDefaults[];

(* Master model file in model_files/ *)
HEFT$ModelFile = FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "HEFT_Model.fr"}];

(* FeynRules .rst restriction files (HEFT-specific; see restrictions/*.rst) *)
HEFT$RestrictionsDir = FileNameJoin[{HEFT$WorkspaceRoot, "restrictions"}];

HEFT$EnsureFeynRulesLoaded[] := Module[{},
  If[!StringQ[$FeynRulesPath] || !DirectoryQ[$FeynRulesPath],
    Print[Style["[HEFT] ERROR: FeynRules path not found: " <> ToString[$FeynRulesPath], Red, Bold]];
    Abort[]
  ];
  If[!MemberQ[$Packages, "FeynRules`"],
    Get[FileNameJoin[{$FeynRulesPath, "FeynRules.m"}]]
  ]
];

HEFT$EnsureFeynRulesLoaded[];

(* --------------------------------------------------------------------------- *)
(* Display helpers                                                             *)
(* --------------------------------------------------------------------------- *)

HEFTPrintBanner[title_String] := Print[
  Style["\n" <> StringRepeat["=", 72] <> "\n  " <> title <> "\n" <> StringRepeat["=", 72],
    Bold, FontSize -> 14]
];

HEFTPrintSubsection[title_String] := Print[
  Style["\n  " <> title, Bold, FontSize -> 14]
];

HEFTPrintDivider[] := Print[Style["  " <> StringRepeat["-", 68], Darker[Gray]]];

HEFTPrintKV[label_String, heftValue_] := Print[
  "    ",
  Style[StringPadRight[label <> ":", 22], Bold],
  ToString[heftValue, InputForm]
];

HEFTPrintOptions[rules_List] := Module[{heftIdx},
  HEFTPrintDivider[];
  Do[HEFTPrintKV[rules[[heftIdx, 1]], rules[[heftIdx, 2]]], {heftIdx, Length[rules]}];
  HEFTPrintDivider[];
];

HEFTPrintOperatorGrid[ops_List, cols_Integer: 4] := Module[{padded, rows},
  If[ops === {}, Return[]];
  padded = PadRight[ops, Ceiling[Length[ops]/cols]*cols, ""];
  rows = Partition[padded, cols];
  Print @ Grid[
    rows,
    Alignment -> {Left, Baseline},
    Spacings -> {3, 0.35},
    ItemStyle -> Directive[FontFamily -> "Monospace", FontSize -> 11]
  ]
];

HEFTCatalogFlatten[catalog_List] := Join @@ catalog[[All, 2]];

(* All configuration variables (HEFTNLOBasis, NLOOperators, OutputName,
   ForceRebuildLHEFT, HEFTGauge, HEFTMaxOrder, HiggsMaxOrder,
   KappaFramework, InitialiseWCs, LOYukawaExpansion, IncludeCustodialT, EWInputScheme, Massless, DiagonalCKM,
   MaxVertexLegs) are
   already defaulted above by
   HEFT$ApplyConfigDefaults[] if still unset at this point. *)

Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_notebook_reference.wl"}];

{HEFT$OperatorCatalogNLO, HEFT$OperatorCatalogHigher} =
  HEFT$OperatorCatalogsForBasis[HEFTNLOBasis];

(* The 2206.07722 basis is not implemented in this release - refused here at configuration
   time, and again inside LoadModel (HEFT_Model.fr), so headless entry points that never run
   this cell cannot slip past it.  HEFT$SupportedNLOBases (heft_defaults.wl) is the list this
   check reads. *)
If[HEFTNLOBasis === "2206.07722",
  (
    Print[Style["[HEFT] ERROR: NLO basis \"2206.07722\" is not yet implemented.", Red, Bold]];
    Print[Style["        Use HEFTNLOBasis = \"1604.06801\"; the 2206.07722 " <>
      "operator files are not part of this release.", Red]];
    Abort[];
  )
];

If[!MemberQ[HEFT$SupportedNLOBases, HEFTNLOBasis],
  (
    Print[Style["[HEFT] ERROR: unknown NLO basis: " <> ToString[HEFTNLOBasis] <>
      ". Supported: " <> StringRiffle[HEFT$SupportedNLOBases, ", "] <> ".", Red, Bold]];
    Abort[];
  )
];

HEFTAvailableOperatorsNLO    = HEFTCatalogFlatten[HEFT$OperatorCatalogNLO];
HEFTAvailableOperatorsHigher = HEFTCatalogFlatten[HEFT$OperatorCatalogHigher];
HEFTAvailableOperators       = Join[HEFTAvailableOperatorsNLO, HEFTAvailableOperatorsHigher];

HEFTPrintBanner["HEFT FeynRules"];

HEFTPrintSubsection["Active configuration"];
HEFTPrintOptions[{
  {"Gauge", HEFTGauge},
  {"NLO basis", HEFTNLOBasis},
  {"HEFTMaxOrder", HEFTMaxOrder},
  {"HiggsMaxOrder", HiggsMaxOrder},
  {"KappaFramework", KappaFramework},
  {"InitialiseWCs", InitialiseWCs},
  {"LOYukawaExpansion", LOYukawaExpansion},
  {"IncludeCustodialT", IncludeCustodialT},
  {"Combine2Derivatives", Combine2Derivatives},
  {"EWInputScheme", EWInputScheme},
  {"Massless.rst", Massless},
  {"DiagonalCKM.rst", DiagonalCKM},
  {"ForceRebuildLHEFT", ForceRebuildLHEFT}
}];

(* ======================= INPUT SCHEME vs CHIRAL ORDER ======================= *)

(* Supported combinations:
     EWInputScheme = "heft"         -> any HEFTMaxOrder (0, 1, 2, 3)
     EWInputScheme = "gf" / "aem"   -> HEFTMaxOrder <= 1 only

   The "gf" and "aem" EW input schemes are derived at NLO only: every shift they apply is
   linear in ChiralOrder (the muon-decay extraction of Gf, the gauge-mixing corrections).
   At HEFTMaxOrder >= 2 the Lagrangian carries NNLO operators the extraction knows nothing
   about, so the EW inputs would be silently NLO-accurate while everything around them is
   not.  Caught here, during configuration, rather than after an expensive LoadModel.
   "heft" is exempt: it replaces nothing, so there is nothing to be inconsistent - it is
   the scheme to use at NNLO and beyond.

   input_scheme.fr carries the same rule as HEFTEWInputSchemeCheckOrder[], which fires during
   LoadModel and so also covers entry points that never run this file (headless scripts that
   Get HEFT_Model.fr directly).  This check is the early, cheap one; the two bounds must move
   together if the O(ChiralOrder^2) extraction is ever implemented. *)
If[MemberQ[{"gf", "aem"}, EWInputScheme] && NumericQ[HEFTMaxOrder] && TrueQ[HEFTMaxOrder > 1],
  HEFTPrintSubsection["Configuration error"];
  Print[Style["    EWInputScheme = \"" <> ToString[EWInputScheme] <>
    "\" cannot be used with HEFTMaxOrder = " <> ToString[HEFTMaxOrder] <> ".", Bold, Red]];
  Print[Style["    The EW input schemes are derived at NLO only \[LongDash] every shift is " <>
    "linear in ChiralOrder.  At HEFTMaxOrder >= 2 the Lagrangian contains NNLO operators " <>
    "the extraction does not account for, so the inputs would be silently NLO-accurate.",
    Darker[Red]]];
  Print[Style["    Supported: \"heft\" at any HEFTMaxOrder; \"gf\"/\"aem\" at HEFTMaxOrder <= 1.",
    Darker[Red]]];
  Print[Style["    Use EWInputScheme = \"heft\" for NNLO and beyond, or set HEFTMaxOrder = 1, " <>
    "then re-run Cell 2 (Configuration) and this cell.", Bold, Red]];
  Abort[]
];

unknownOps = Complement[NLOOperators, HEFTAvailableOperators];
If[NLOOperators =!= {} && unknownOps =!= {},
  HEFTPrintSubsection["Selection error"];
  Print[Style["    Unknown operator(s): ", Bold, Red], unknownOps];
  Print[Style["    See the Reference section above for valid labels.", Darker[Red]]];
  Abort[]
];

HEFTPrintSubsection["Selected operators"];
If[NLOOperators === {},
  Print[Style["    (none \[LongDash] LO only)", Gray]],
  HEFTPrintOperatorGrid[NLOOperators, 3];
  Print[Style["    " <> ToString[Length[NLOOperators]] <> " operator(s) active", Gray]]
];

(* Checked here, during configuration, so a typo costs nothing: Cells 6/7/8 check it again at
   the point of use, since either may be run in a kernel where this cell was not. *)
HEFT$CheckMaxVertexLegs[];

HEFTPrintSubsection["Output"];
HEFTPrintOptions[{
  {"OutputName", OutputName},
  {"MaxVertexLegs", HEFT$MaxVertexLegsValue[]}
}];
If[HEFT$MaxVertexLegsValue[] =!= Automatic,
  Print[Style["    Cells 6/7/8 will keep only vertices with at most " <>
    ToString[HEFT$MaxVertexLegsValue[]] <> " legs. Not part of the cache key \[LongDash] " <>
    "Cell 5 builds the full Lagrangian either way, and the WCxf files still carry every " <>
    "coefficient, including those of the dropped vertices.", Gray]]
];

HEFTWCxfDir        = FileNameJoin[{HEFT$WorkspaceRoot, "wcxf"}];
HEFTWCxfInitFile   = FileNameJoin[{HEFTWCxfDir, "wcxf_init.json"}];
HEFTWCxfOutputFile = FileNameJoin[{HEFTWCxfDir, "wcxf_output.json"}];

(* Both WCxf files are (re)written from the current operator selection on every Cell 3 run,
   with every Wilson coefficient at its default of 1. wcxf_output.json is the one the model
   reads in Cell 5, so editing it (Cell 4) is the only step needed to change coefficients -
   and re-running Cell 3 deliberately resets it back to defaults (it says so when the file
   it is about to overwrite contained edits). *)
HEFTPrintSubsection["WCxf \[LongDash] Wilson-coefficient files"];
Global`KappaFramework = KappaFramework;
Global`InitialiseWCs = InitialiseWCs;
Global`LOYukawaExpansion = LOYukawaExpansion;
Global`IncludeCustodialT = IncludeCustodialT;
Global`Combine2Derivatives = Combine2Derivatives;
Global`HiggsMaxOrder = HiggsMaxOrder;
Global`HEFTNLOBasis = HEFTNLOBasis;
Global`HEFTActiveNLOPieces = NLOOperators;
Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "wcxf_input.fr"}]];
HEFTWriteWCxfPointFiles[HEFTWCxfInitFile, HEFTWCxfOutputFile];

(* Cache lookup, reported here so you know before starting Cell 5 whether it will load an
   existing build or start a new one. Nothing here needs FeynRules or a loaded model - the
   cache key is the configuration plus digests of the .fr sources and of the WCxf support.
   Note this verdict is for wcxf_output.json as HEFTWriteWCxfPointFiles just rewrote it, i.e.
   every coefficient at 1; re-run Cell 4 after editing it to get the verdict for your edits. *)
HEFTPrintSubsection["LHEFT cache"];
Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "lheft_cache.wl"}]];
HEFTLHEFTCacheReport[];

Print[Style["\n[HEFT] Cell 3 done.", Bold]];
Print["[HEFT] Next: edit Wilson coefficients in cell 4 (optional), then run cell 5."];
Print["[HEFT]   defaults (reference, never read by the model): ", HEFTWCxfInitFile];
Print["[HEFT]   values used by the model \[LongDash] edit this one: ", HEFTWCxfOutputFile];

]; (* end cell 3 notebook gate *)


(* =============================================================================
   CELL 4 \[LongDash] Edit Wilson coefficients (manual step, no code to run)
   ============================================================================= *)

If[HEFT$NBShouldRunCell[4],

If[!ValueQ[HEFTWCxfOutputFile],
  HEFTWCxfDir = FileNameJoin[{HEFT$WorkspaceRoot, "wcxf"}];
  HEFTWCxfInitFile = FileNameJoin[{HEFTWCxfDir, "wcxf_init.json"}];
  HEFTWCxfOutputFile = FileNameJoin[{HEFTWCxfDir, "wcxf_output.json"}]
];
Print[Style["\n[HEFT] Cell 4: edit Wilson coefficients in:\n  ", Bold], HEFTWCxfOutputFile];
Print["[HEFT] Defaults for reference (regenerated in cell 3): ", HEFTWCxfInitFile];
Print["[HEFT] Every coefficient starts at 1. A value of 0 is simply 0 in the exported model \[LongDash]"];
Print["[HEFT] it does not remove anything; which operators exist is NLOOperators alone."];
Print["[HEFT] Leave the file untouched to run with the defaults."];
Print[Style["[HEFT] When finished editing, run cell 5 \[LongDash] do not re-run cell 3, " <>
  "it rewrites this file back to defaults.", Bold]];

(* Re-run this cell after editing wcxf_output.json: it is free, and the cache report below is
   then the one that applies to your edited coefficients. Changing a non-zero value keeps the
   cache hit (Wilson coefficients are External parameters - the value never enters LHEFT, only
   M$Parameters at export); zeroing a coefficient removes an operator from the Lagrangian, so
   that one does force a rebuild. *)
If[!ValueQ[HEFT$WorkspaceRoot],
  Print[Style["[HEFT] ERROR: Run cell 3 first.", Red, Bold]]; Abort[]
];
Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "lheft_cache.wl"}]];
Print[""];
HEFTLHEFTCacheReport[];

]; (* end cell 4 notebook gate *)


(* =============================================================================
   CELL 5 \[LongDash] Load model, build the mass-basis Lagrangian (LHEFT)
   ============================================================================= *)

If[HEFT$NBShouldRunCell[5],

If[!ValueQ[HEFT$WorkspaceRoot],
  Print[Style["[HEFT] ERROR: Run cell 3 first.", Red, Bold]]; Abort[]
];

HEFT$EnsureFeynRulesLoaded[];

(* Configuration -> model flags (Global` survives FeynRules model context during LoadModel). *)
Global`KappaFramework = KappaFramework;
Global`InitialiseWCs = InitialiseWCs;
Global`LOYukawaExpansion = LOYukawaExpansion;
Global`IncludeCustodialT = IncludeCustodialT;
Global`Combine2Derivatives = Combine2Derivatives;
Global`HEFTMaxOrder = HEFTMaxOrder;
Global`HiggsMaxOrder = HiggsMaxOrder;
Global`HEFTActiveNLOPieces = NLOOperators;
Global`HEFTNLOBasis = HEFTNLOBasis;
Global`HEFTGauge = HEFTGauge;
Global`EWInputScheme = EWInputScheme;

(* WCxf: the model always reads its Wilson coefficients from wcxf_output.json, exactly as it
   is on disk right now - defaults if Cell 3 just wrote it, your values if you edited it. *)
If[!ValueQ[HEFT$WorkspaceRoot],
  Print[Style["[HEFT] ERROR: HEFT$WorkspaceRoot undefined. Run cell 3 first.", Red, Bold]]; Abort[]
];
HEFTWCxfDir = FileNameJoin[{HEFT$WorkspaceRoot, "wcxf"}];
HEFTWCxfInitFile = FileNameJoin[{HEFTWCxfDir, "wcxf_init.json"}];
HEFTWCxfOutputFile = FileNameJoin[{HEFTWCxfDir, "wcxf_output.json"}];
If[!FileExistsQ[HEFTWCxfOutputFile],
  Print[Style["[HEFT] ERROR: WCxf output file not found: " <> HEFTWCxfOutputFile, Red, Bold]];
  Print["[HEFT] Run cell 3 to (re)create it, then optionally edit it in cell 4."];
  Abort[]
];
Global`HEFTWCxfOutputFile = HEFTWCxfOutputFile;
Print[Style["[HEFT WCxf] Will load Wilson coefficients from: ", Bold], HEFTWCxfOutputFile];

(* Report what is actually about to be used. The helpers live in wcxf_input.fr, which cell 3
   already Get'd into Global context; re-Get only if this cell is run in a kernel where it
   isn't defined (e.g. straight after the Reference section). *)
If[DownValues[HEFTWCxfCompareToDefaults] === {},
  Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "wcxf_input.fr"}]]
];
HEFT$WCxfDiff = HEFTWCxfCompareToDefaults[HEFTWCxfOutputFile];
If[HEFT$WCxfDiff["changed"] === {} && HEFT$WCxfDiff["missing"] === {},
  Print[Style["[HEFT WCxf] All coefficients at their default value of 1.", Gray]],
  If[HEFT$WCxfDiff["changed"] =!= {},
    Print[Style["[HEFT WCxf] Using " <> ToString[Length[HEFT$WCxfDiff["changed"]]] <>
      " edited value(s):", Bold]]
  ];
  HEFTWCxfPrintDiff[HEFT$WCxfDiff]
];

(* ======================= LOAD MODEL ======================= *)

(* FeynRules' LoadModel is NOT idempotent.  Core/ClassDeclarations.m only warns on a second
   call (LoadModel::Loaded, gated on MR$ModelLoaded) and then re-declares everything on top of
   the existing model state.  In practice that state ends up corrupted: MR$GaugeGroupList stops
   being a list, so Flatten[MR$GaugeGroupList, 1] and the ReplaceAll/Inner calls built on it
   fail, and the parameter Definitions recurse until $RecursionLimit is hit.  The build then
   either dies or - worse - produces an LHEFT that silently ignores EWInputScheme.
   Reproduced 2026-08-06 for both "gf" and "heft": a single Cell 5 run is clean, running
   Cell 5 twice in one kernel gives $RecursionLimit::reclim / Flatten::normal / ReplaceAll::reps.
   So refuse to build rather than build something wrong.  There is no supported way to unload a
   FeynRules model; a fresh kernel is the only fix. *)
If[TrueQ[MR$ModelLoaded],
  Print[Style["[HEFT] ERROR: a FeynRules model is already loaded in this kernel.", Red, Bold]];
  Print[Style["[HEFT] Cell 5 cannot run twice in one kernel - FeynRules' LoadModel is not "  <>
    "idempotent, and a second load corrupts the model state (recursion errors, and an LHEFT "  <>
    "that can silently ignore EWInputScheme).", Red]];
  Print[Style["[HEFT] Restart the kernel (Evaluation > Quit Kernel), then run: Configuration "  <>
    "-> Cell 3 -> [edit wcxf/wcxf_output.json] -> Cell 5.", Red, Bold]];
  Abort[]
];

CPUTime = TimeUsed[];
LoadModel[HEFT$ModelFile];
Print[Style["\n[HEFT] Model loaded in ", Bold], TimeUsed[] - CPUTime, " seconds"];
If[NLOOperators === {},
  Print[Style["[HEFT] Lagrangian: LO only (no NLO operators selected).", Bold]],
  Print[Style["[HEFT] Lagrangian: LO + ", Bold], Length[NLOOperators], Style[" NLO piece(s).", Bold]]
];

(* Optional parameter restrictions (FeynRules LoadRestriction) *)
HEFT$RestrictionPaths = {};
If[TrueQ[Massless],
  Module[{p = FileNameJoin[{HEFT$RestrictionsDir, "Massless.rst"}]},
    If[!FileExistsQ[p],
      Print[Style["[HEFT] ERROR: Massless.rst not found: " <> p, Red, Bold]]; Abort[],
      AppendTo[HEFT$RestrictionPaths, p]
    ]
  ]
];
If[TrueQ[DiagonalCKM],
  Module[{p = FileNameJoin[{HEFT$RestrictionsDir, "DiagonalCKM.rst"}]},
    If[!FileExistsQ[p],
      Print[Style["[HEFT] ERROR: DiagonalCKM.rst not found: " <> p, Red, Bold]]; Abort[],
      AppendTo[HEFT$RestrictionPaths, p]
    ]
  ]
];
If[HEFT$RestrictionPaths =!= {},
  Print[Style["[HEFT] Loading restrictions: ", Bold], HEFT$RestrictionPaths];
  (* Each .rst sets M$Restrictions = {...}; merge so the last file does not drop earlier rules. *)
  M$Restrictions = Fold[
    Function[{acc, path},
      LoadRestriction[path];
      Join[acc, M$Restrictions]
    ],
    {},
    HEFT$RestrictionPaths
  ];
  Print[Style["[HEFT] M$Restrictions: ", Bold], M$Restrictions],
  Print[Style["[HEFT] No .rst restrictions (Massless / DiagonalCKM both False).", Bold]]
];

(* ======================= Lagrangian in the mass basis ======================= *)

If[!ValueQ[HEFTWCxfOutputFile],
  HEFTWCxfDir = FileNameJoin[{HEFT$WorkspaceRoot, "wcxf"}];
  HEFTWCxfInitFile = FileNameJoin[{HEFTWCxfDir, "wcxf_init.json"}];
  HEFTWCxfOutputFile = FileNameJoin[{HEFTWCxfDir, "wcxf_output.json"}]
];

(* No HEFTLHEFTCacheReport[] here: Cells 3 and 4 print the forecast, and HEFTLoadOrBuildLHEFT
   prints what it actually does (hit / hit under another name / build). *)
Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "lheft_cache.wl"}]];
LHEFT = HEFTLoadOrBuildLHEFT[];

Print["[HEFT] Done."];

]; (* end cell 5 notebook gate *)


(* -----------------------------------------------------------------------------
   MaxVertexLegs -> the FeynRules option, spliced into all three output cells below.

   Defined HERE, below Cell 5's block rather than at the top of the file, and that placement
   is load-bearing.  Get parses and evaluates one expression at a time, so by this point Cell
   3's block has run HEFT$EnsureFeynRulesLoaded[] and FeynRules` sits on $ContextPath.
   Written any earlier, the literal MaxParticles below would be read into Global` instead -
   a different symbol from the FeynRules` one that FeynmanRules / WriteUFO /
   WriteFeynArtsOutput pattern-match against - and the option would then be accepted in
   silence and do nothing whatsoever.  The MemberQ guard turns that into a loud failure if the
   ordering here is ever disturbed.
   ----------------------------------------------------------------------------- *)

HEFT$VertexLegOptions[] := Module[{heftN},
  HEFT$CheckMaxVertexLegs[];
  heftN = HEFT$MaxVertexLegsValue[];
  If[heftN === Automatic, Return[{}]];
  If[!MemberQ[First /@ Options[FeynmanRules], MaxParticles],
    Print[Style["[HEFT] ERROR: the MaxParticles read here is not FeynRules' option symbol " <>
      "(context " <> Context[MaxParticles] <> "). MaxVertexLegs would be ignored silently, " <>
      "so the export is refused instead.", Red, Bold]];
    Abort[]
  ];
  Print[Style["[HEFT] MaxVertexLegs = " <> ToString[heftN] <> ": keeping only vertices with " <>
    "at most " <> ToString[heftN] <> " legs.", Bold]];
  {MaxParticles -> heftN}
];


(* =============================================================================
   CELL 6 \[LongDash] Compute Feynman rules from LHEFT
   ============================================================================= *)

If[HEFT$NBShouldRunCell[6],

If[!ValueQ[LHEFT],
  Print[Style["[HEFT] ERROR: LHEFT undefined. Run cell 5 first.", Red, Bold]]; Abort[]
];

outputDir[what_] :=
  If[Head[what] === List,
    FileNameJoin[{HEFT$WorkspaceRoot, "output", Sequence @@ what}],
    FileNameJoin[{HEFT$WorkspaceRoot, "output", what}]
  ];
Quiet[CreateDirectory[outputDir["."], CreateIntermediateDirectories -> True],
  CreateDirectory::eexist];

Module[{feynRulesOutDir, latexOutDir, texFile, txtFile, strm, i},
  feynRulesOutDir = outputDir[{"FeynmanRules", OutputName}];
  If[DirectoryQ[feynRulesOutDir], DeleteDirectory[feynRulesOutDir, DeleteContents -> True]];
  CreateDirectory[feynRulesOutDir, CreateIntermediateDirectories -> True];
  latexOutDir = FileNameJoin[{feynRulesOutDir, "latex"}];
  CreateDirectory[latexOutDir, CreateIntermediateDirectories -> True];

  (* Evaluate LHEFT once so FeynmanRules receives the truncated Lagrangian (ChiralOrder and
     LamGold truncations are already applied inside LHEFT). *)
  CPUTime = TimeUsed[];
  RulesHEFT = FeynmanRules[LHEFT, FlavorExpand -> True, Sequence @@ HEFT$VertexLegOptions[]];
  Print[Style["[HEFT] Feynman rules computed in ", Bold], TimeUsed[] - CPUTime, " seconds"];
  Print["[HEFT] Number of vertices: ", Length[RulesHEFT]];

  (* .mx: saved via DumpSave, the same format lheft_cache.wl uses for LHEFT itself - RulesHEFT
     carries FeynRules-internal heads that only round-trip faithfully through Mathematica's own
     binary dump, not through a text Put/Export. Reload with Get[".../<OutputName>.mx"]. *)
  DumpSave[FileNameJoin[{feynRulesOutDir, OutputName <> ".mx"}], "RulesHEFT"];

  (* .txt: a plain-text listing of every vertex (legs -> coupling). FeynRules has no built-in
     writer for this, so it is written by hand rather than via PrintScreenOutput - that function
     is broken in the installed FeynRules 2.3.49 (a context-binding bug means PrintOutputCreaList
     silently never fires; confirmed directly, it prints nothing at all). *)
  txtFile = FileNameJoin[{feynRulesOutDir, OutputName <> ".txt"}];
  strm = OpenWrite[txtFile];
  WriteString[strm, "HEFT Feynman rules -- ", OutputName, "\n"];
  WriteString[strm, Length[RulesHEFT], " vertices\n\n"];
  Do[
    WriteString[strm, "Vertex ", i, ": ", ToString[RulesHEFT[[i, 1, All, 1]], OutputForm], "\n"];
    WriteString[strm, "  ", ToString[RulesHEFT[[i, 2]], OutputForm], "\n\n"],
    {i, Length[RulesHEFT]}
  ];
  Close[strm];

  (* .tex: hand-written (heft_latex_export.wl), not FeynRules' own TeXOutput/FRMakeTeXOut -
     that writer lists every class/index declared anywhere in the model rather than what
     actually appears in RulesHEFT, has no model-specific naming hooks (photon prints
     lower-case, W+ isn't superscripted), leaves zero visible spacing between multiplied
     \text{...}-wrapped coupling factors, and breaks compilation on its own Gluon$1-style
     dummy-index names. Written into its own latex/ subfolder so compiling it there leaves
     the .aux/.log/.pdf byproducts alongside it, not next to the .mx/.txt. *)
  Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_latex_export.wl"}]];
  texFile = FileNameJoin[{latexOutDir, OutputName <> ".tex"}];
  HEFT$WriteLatexRules[RulesHEFT, texFile];

  Print[Style["[HEFT] Feynman rules written to " <> feynRulesOutDir <> " (.mx, .txt, latex/.tex)", Bold]];
];

Print["[HEFT] Done."];

]; (* end cell 6 notebook gate *)


(* =============================================================================
   CELL 7 \[LongDash] UFO export
   ============================================================================= *)

If[HEFT$NBShouldRunCell[7],

If[!ValueQ[LHEFT],
  Print[Style["[HEFT] ERROR: LHEFT undefined. Run cell 5 first.", Red, Bold]]; Abort[]
];

outputDir[what_] :=
  If[Head[what] === List,
    FileNameJoin[{HEFT$WorkspaceRoot, "output", Sequence @@ what}],
    FileNameJoin[{HEFT$WorkspaceRoot, "output", what}]
  ];
(* Quiet: output/ normally already exists, and CreateDirectory::eexist on an existing
   directory is not a problem worth printing on every single export. *)
Quiet[CreateDirectory[outputDir["."], CreateIntermediateDirectories -> True],
  CreateDirectory::eexist];

(* The export format is not a configuration option: Cell 7 writes UFO, Cell 8 writes
   FeynArts.  Run whichever you want - or both, which the old single Switch[OutputFormat]
   could not do without re-running Configuration. *)
Module[{ufoOutDir},
      ufoOutDir = outputDir[{"UFO", OutputName}];
      (* Say so when an earlier export is really being replaced - this is the only case worth a
         message, and it used to be drowned out by a spurious CreateDirectory::eexist below. *)
      If[DirectoryQ[ufoOutDir],
        Print[Style["[HEFT] Replacing the existing UFO export at " <> ufoOutDir, Orange]];
        DeleteDirectory[ufoOutDir, DeleteContents -> True]
      ];
      (* Create only the PARENT (output/UFO/), never <OutputName> itself: WriteUFO creates its
         own Output directory, and FeynRules' guard for that is broken for absolute paths -
         Interfaces/UFO/PYIntMain.m does
             If[Not[MemberQ[FileNames[], OptionValue[Output]]], CreateDirectory[...]]
         where FileNames[] lists the cwd's contents as RELATIVE names, so an absolute Output is
         never a member, the test is always False, and CreateDirectory runs unconditionally.
         Pre-creating the directory here therefore produced CreateDirectory::eexist on every
         single export, including the very first one for a brand-new OutputName. *)
      Quiet[CreateDirectory[outputDir["UFO"], CreateIntermediateDirectories -> True],
        CreateDirectory::eexist];
      CPUTime = TimeUsed[];
      WriteUFO[LHEFT, Output -> ufoOutDir, Sequence @@ HEFT$VertexLegOptions[]];
      (* ufo_cleanup.py lives in additional_scripts/, not at the workspace root. *)
      Module[{cleanup = FileNameJoin[{HEFT$WorkspaceRoot, "additional_scripts", "ufo_cleanup.py"}]},
        If[FileExistsQ[cleanup],
          Run["python3 \"" <> cleanup <> "\" \"" <>
            FileNameJoin[{ufoOutDir, "parameters.py"}] <> "\""],
          Print[Style["[HEFT] WARNING: ufo_cleanup.py not found at " <> cleanup <>
            "; parameters.py left as written by WriteUFO.", Orange, Bold]]
        ]
      ];
      Print[Style["[HEFT] UFO written to " <> ufoOutDir <> " in ", Bold], TimeUsed[] - CPUTime, " seconds"];
];

Print["[HEFT] Done."];

]; (* end cell 7 notebook gate *)


(* =============================================================================
   CELL 8 \[LongDash] FeynArts export
   ============================================================================= *)

If[HEFT$NBShouldRunCell[8],

If[!ValueQ[LHEFT],
  Print[Style["[HEFT] ERROR: LHEFT undefined. Run cell 5 first.", Red, Bold]]; Abort[]
];

If[!ValueQ[HEFT$WorkspaceRoot],
  HEFT$WorkspaceRoot = DirectoryName @ DirectoryName @ ExpandFileName @ $InputFileName
];

outputDir[what_] := If[ListQ[what],
    FileNameJoin[Join[{HEFT$WorkspaceRoot, "output"}, what]],
    FileNameJoin[{HEFT$WorkspaceRoot, "output", what}]
  ];
Quiet[CreateDirectory[outputDir["."], CreateIntermediateDirectories -> True],
  CreateDirectory::eexist];

    (* WriteFeynArtsOutput's Output -> is a file basename-with-path, not a target directory, and
       it is doubly awkward about it (FeynArtsInterface.m ~line 1142): it CreateDirectory's
       <Output> itself, SetDirectory's into it, and then writes <Output>.mod / .gen / .pars as
       *siblings* of that directory. Passing feynArtsOutDir/OutputName therefore lands the three
       files in output/FeynArts/<OutputName>/ as intended, but always leaves a stray nested
       <OutputName>/ behind - and because it never restores the working directory, a later
       export in the same kernel inherits that nested directory as its cwd and the files end up
       one level too deep instead. So: restore the working directory afterwards, then flatten
       anything that did land in the nested folder and remove it. *)
    Module[{feynArtsOutDir, cput, faBase, cwd, nestedFiles, target},
      feynArtsOutDir = outputDir[{"FeynArts", OutputName}];
      Quiet[CreateDirectory[feynArtsOutDir, CreateIntermediateDirectories -> True],
        CreateDirectory::eexist];
      faBase = FileNameJoin[{feynArtsOutDir, OutputName}];
      cput = TimeUsed[];
      cwd = Directory[];
      WriteFeynArtsOutput[LHEFT, Output -> faBase, Sequence @@ HEFT$VertexLegOptions[]];
      Quiet @ SetDirectory[cwd];
      If[DirectoryQ[faBase],
        nestedFiles = Select[FileNames["*", faBase], !DirectoryQ[#] &];
        Scan[
          Function[f,
            target = FileNameJoin[{feynArtsOutDir, FileNameTake[f]}];
            If[FileExistsQ[target], DeleteFile[target]];
            RenameFile[f, target]
          ],
          nestedFiles
        ];
        (* Only succeeds once the directory is empty, which is exactly when it should go. *)
        Quiet @ DeleteDirectory[faBase]
      ];
      Print[Style["[HEFT] FeynArts export in ", Bold], TimeUsed[] - cput, " seconds"];
      Print[Style["[HEFT] FeynArts written to ", Bold], feynArtsOutDir];
      Print["[HEFT]   ", FileNameTake /@ Select[FileNames["*", feynArtsOutDir], !DirectoryQ[#] &]];
];

Print["[HEFT] Done."];

]; (* end cell 8 notebook gate *)


