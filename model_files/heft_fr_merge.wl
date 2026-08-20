(* ::Package:: *)

(* Guard: this file is only ever meant to be Get-ed from heft_fr_merge_models.wl, which sets
   HEFT$FromMergeNotebook = True in its Cell 3. Evaluating it standalone would run with no
   configuration at all, so quit instead. *)
If[!TrueQ[HEFT$FromMergeNotebook], Quit[]]

(* HEFT model-merging engine, driven by heft_fr_merge_models.wl.  Mirrors heft_fr.wl cell for
   cell, so the two notebooks read the same way:

   CELL 1  Reference - what merging does, when it is exact, and the rules it enforces
   CELL 2  Configuration (notebook only, no code here) - everything EXCEPT NLOOperators,
           which is not chosen but derived from the sub-models you merge
   CELL 3  Echo the configuration and print every cached model that matches it
   CELL 4  Pick the sub-models by name (MergeSources), write the WCxf files for their union
   CELL 5  LoadModel on the union, merge the cached Lagrangians, cache the result as LHEFT

   CELLS 6, 7, 8 (Feynman rules / UFO / FeynArts) are NOT here.  They need nothing but LHEFT,
   OutputName and HEFT$WorkspaceRoot, so the notebook Get's model_files/heft_fr.wl for them -
   literally the same three cells the ordinary notebook runs, not a copy of them.

   The merge itself lives in model_files/lheft_merge.wl. *)

HEFT$MergeShouldRunCell[heftN_Integer] :=
  !ValueQ[HEFT$MergeCell] || HEFT$MergeCell === heftN;

(* Bootstrap shared by cells 3, 4 and 5; idempotent, so a cell run out of order still works
   as long as Cell 2 (Configuration) has been evaluated in this kernel. *)
HEFT$MergeBootstrap[] := Module[{},
  If[!ValueQ[HEFT$WorkspaceRoot],
    HEFT$WorkspaceRoot = DirectoryName @ DirectoryName @ ExpandFileName @ $InputFileName
  ];
  Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_defaults.wl"}];
  HEFT$ApplyConfigDefaults[];
  HEFT$ModelFile       = FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "HEFT_Model.fr"}];
  HEFT$RestrictionsDir = FileNameJoin[{HEFT$WorkspaceRoot, "restrictions"}];
  Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "lheft_cache.wl"}];
  Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "lheft_merge.wl"}];
  HEFTMergeCheckKeys[];
];

HEFT$MergeEnsureFeynRules[] := Module[{},
  If[!StringQ[$FeynRulesPath] || !DirectoryQ[$FeynRulesPath],
    Print[Style["[HEFT merge] ERROR: FeynRules path not found: " <> ToString[$FeynRulesPath],
      Red, Bold]];
    Abort[]
  ];
  If[!MemberQ[$Packages, "FeynRules`"],
    Get[FileNameJoin[{$FeynRulesPath, "FeynRules.m"}]]
  ]
];

HEFT$MergePrintBanner[title_String] := Print[
  Style["\n" <> StringRepeat["=", 72] <> "\n  " <> title <> "\n" <> StringRepeat["=", 72],
    Bold, FontSize -> 14]
];

HEFT$MergePrintSubsection[title_String] := Print[
  Style["\n  " <> title, Bold, FontSize -> 14]
];

HEFT$MergePrintKV[label_String, heftValue_] := Print[
  "    ", Style[StringPadRight[label <> ":", 22], Bold], ToString[heftValue, InputForm]
];


(* =============================================================================
   CELL 1 \[LongDash] Reference
   ============================================================================= *)

If[HEFT$MergeShouldRunCell[1],

If[!ValueQ[HEFT$WorkspaceRoot],
  HEFT$WorkspaceRoot = DirectoryName @ DirectoryName @ ExpandFileName @ $InputFileName
];
Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_notebook_reference.wl"}];

HEFT$MergePrintBanner["HEFT FeynRules \[LongDash] model merging"];
HEFT$PrintAbout[];

HEFT$MergePrintSubsection["What this notebook does"];
Print["    Builds one large model out of several small cached ones, without re-running the"];
Print["    expensive mass-basis pass. ExpandIndices is linear in the Lagrangian, so"];
Print[Style["\n        LHEFT(A u B) = LHEFT(LO) + (LHEFT(A) - LHEFT(LO)) + (LHEFT(B) - LHEFT(LO))\n",
  FontFamily -> "Monospace"]];
Print["    and every LHEFT(x) is already on disk in HEFT_cache/ from an earlier run of"];
Print["    heft_fr_notebook.wl. Only Feynman rules and the export are recomputed."];

HEFT$MergePrintSubsection["How to use it"];
Print["    1.  Cell 2  - set the configuration. NOT the operators: they are derived from"];
Print["                  whichever sub-models you merge."];
Print["    2.  Cell 3  - lists every cached model built with exactly that configuration,"];
Print["                  with its name and its operators."];
Print["    3.  Cell 4  - put those names in MergeSources. Writes the WCxf files for the union."];
Print["    4.  Cell 5  - merges, and leaves the result in LHEFT (also cached, so the ordinary"];
Print["                  notebook finds it later as a normal cache hit)."];
Print["    5.  Cells 6/7/8 - Feynman rules, UFO, FeynArts. The very same cells as in"];
Print["                  heft_fr_notebook.wl."];

HEFT$MergePrintSubsection["What has to agree, and what is refused"];
Print["    Two cached models may be merged only if EVERY hashed configuration option agrees;"];
Print["    the operator selection is the one thing allowed to differ. That includes"];
Print[Style["    modelDigest", Bold], ", the digest of the .fr sources - so sub-models built"];
Print["    before and after an edit to any model file are never merged together."];
Print[""];
Print["    Checked, and refused rather than warned about:"];
Print["      \[Bullet] any hashed option differing between two sub-models;"];
Print[Style["      \[Bullet] HEFTMaxOrder > 1", Bold],
  " - merging is exact only at linear order in ChiralOrder."];
Print["        Above it the gauge normalisations (eps is a product, the kinetic diagonal is"];
Print["        Wnorm^2 P12norm^2) and the EW input scheme mix operators non-linearly, so a"];
Print["        build with one operator has different physical fields than one with two;"];
Print["      \[Bullet] a missing LO baseline - a cached build with NLOOperators = {}. Every"];
Print["        sub-model carries the whole LO Lagrangian, so without subtracting it N"];
Print["        sub-models give N x LO and every SM vertex is scaled by N;"];
Print["      \[Bullet] an operator appearing in two selected sub-models (it would be added twice);"];
Print["      \[Bullet] the same cache entry listed twice in MergeSources."];

HEFT$MergePrintSubsection["Configuration options"];
Print[Style["    The same options as heft_fr_notebook.wl, minus NLOOperators. Their full"]];
Print[Style["    reference table is printed by Cell 1 of that notebook.", Gray]];

Print[Style["\n[HEFT merge] Cell 1 done. Next: Cell 2 (Configuration).", Bold]];

]; (* end merge cell 1 gate *)


(* =============================================================================
   CELL 3 \[LongDash] Configuration echo and cache lookup
   ============================================================================= *)

If[HEFT$MergeShouldRunCell[3],

If[!TrueQ[HEFT$ConfigEvaluated],
  Print[Style["[HEFT merge] ERROR: the Configuration section has not been evaluated in this " <>
    "kernel.", Red, Bold]];
  Print[Style["[HEFT merge] Evaluate Cell 2 first, then this cell. (Running now would " <>
    "silently use the defaults from model_files/heft_defaults.wl, not your settings.)", Red]];
  Abort[]
];

HEFT$MergeBootstrap[];

HEFT$MergePrintBanner["HEFT FeynRules \[LongDash] model merging"];

HEFT$MergePrintSubsection["Active configuration"];
Print[Style["    " <> StringRepeat["-", 68], Darker[Gray]]];
HEFT$MergePrintKV["Gauge", HEFTGauge];
HEFT$MergePrintKV["NLO basis", HEFTNLOBasis];
HEFT$MergePrintKV["HEFTMaxOrder", HEFTMaxOrder];
HEFT$MergePrintKV["HiggsMaxOrder", HiggsMaxOrder];
HEFT$MergePrintKV["KappaFramework", KappaFramework];
HEFT$MergePrintKV["InitialiseWCs", InitialiseWCs];
HEFT$MergePrintKV["LOYukawaExpansion", LOYukawaExpansion];
HEFT$MergePrintKV["IncludeCustodialT", IncludeCustodialT];
HEFT$MergePrintKV["Combine2Derivatives", Combine2Derivatives];
HEFT$MergePrintKV["EWInputScheme", EWInputScheme];
HEFT$MergePrintKV["Massless.rst", Massless];
HEFT$MergePrintKV["DiagonalCKM.rst", DiagonalCKM];
HEFT$MergePrintKV["OutputName", OutputName];
(* Export-time only, and not hashed, so unlike everything above it it need not match the
   sub-models. Cells 6/7/8 (heft_fr.wl's own) validate it at the point of use. *)
HEFT$MergePrintKV["MaxVertexLegs", MaxVertexLegs];
Print[Style["    " <> StringRepeat["-", 68], Darker[Gray]]];

(* The same order gate the ordinary notebook applies, for the same reason: "gf"/"aem" are
   derived at O(ChiralOrder) only.  It is a stricter bound here anyway - merging itself is
   refused above HEFTMaxOrder = 1 in Cell 5, whatever the scheme. *)
If[MemberQ[{"gf", "aem"}, EWInputScheme] && NumericQ[HEFTMaxOrder] && TrueQ[HEFTMaxOrder > 1],
  Print[Style["\n    EWInputScheme = \"" <> ToString[EWInputScheme] <>
    "\" cannot be used with HEFTMaxOrder = " <> ToString[HEFTMaxOrder] <>
    " (the derived schemes are NLO-only).", Bold, Red]];
  Abort[]
];

(* Merging needs no FeynRules and no loaded model: the cache index is meta.json plus the .fr
   digests, all readable from disk.  So Cell 3 is instant, and you can browse the cache
   without paying for a LoadModel. *)
HEFT$MergeMeta  = HEFTLHEFTCacheMeta[];
HEFT$MergeIndex = HEFTMergeCacheIndex[];

Print[Style["\n  Cache: ", Bold], HEFTLHEFTCacheDir[],
  Style["  (merge group " <> HEFTMergeGroupHash[HEFT$MergeMeta] <> ")", Gray]];

HEFT$MergeCompatible = HEFTMergePrintCatalog[HEFT$MergeIndex, HEFT$MergeMeta];

Print[Style["\n[HEFT merge] Cell 3 done.", Bold]];
Print["[HEFT merge] Next: put the names you want from the table above into MergeSources in " <>
  "Cell 4."];

]; (* end merge cell 3 gate *)


(* =============================================================================
   CELL 4 \[LongDash] Choose the sub-models, write the WCxf files for their union
   ============================================================================= *)

If[HEFT$MergeShouldRunCell[4],

If[!ValueQ[HEFT$WorkspaceRoot],
  Print[Style["[HEFT merge] ERROR: run Cell 3 first.", Red, Bold]]; Abort[]
];
HEFT$MergeBootstrap[];
HEFT$MergeEnsureFeynRules[];

If[!ValueQ[MergeSources] || !ListQ[MergeSources],
  Print[Style["[HEFT merge] ERROR: MergeSources is not set. Set it in this cell to a list " <>
    "of names from the Cell 3 table, e.g. MergeSources = {\"HEFT_bos_1\", \"HEFT_bos_2\"};",
    Red, Bold]];
  Abort[]
];

(* Re-index rather than trusting Cell 3's snapshot: the user may have built another sub-model
   in a different kernel since. *)
HEFT$MergeMeta       = HEFTLHEFTCacheMeta[];
HEFT$MergeIndex      = HEFTMergeCacheIndex[];
HEFT$MergeCompatible = HEFTMergeCompatibleEntries[HEFT$MergeIndex, HEFT$MergeMeta];

HEFT$MergePlan = HEFTMergeValidate[HEFT$MergeCompatible, MergeSources, HEFT$MergeMeta];
If[HEFT$MergePlan === $Failed, Abort[]];

HEFT$MergePrintSubsection["Merge plan"];
Print["    ", Style[StringPadRight["LO baseline", 34], Bold], HEFT$MergePlan["lo"]["folder"]];
Do[
  Print["    ", Style[StringPadRight[e["name"], 34], Bold],
    HEFTMergeOperatorSummary[e["operators"]]],
  {e, HEFT$MergePlan["sources"]}
];

(* NLOOperators is DERIVED here - it is the union of the selected sub-models' operator lists.
   Everything downstream (the cache key of the merged model, the WCxf key generation, and the
   LoadModel in Cell 5) reads it from this point on, exactly as in the ordinary notebook. *)
NLOOperators = HEFT$MergePlan["operators"];

HEFT$MergePrintSubsection["Resulting operator selection"];
Print["    ", Style[ToString[Length[NLOOperators]] <> " operator(s): ", Bold],
  StringRiffle[NLOOperators, ", "]];

(* WCxf files for the union, written exactly the way heft_fr.wl Cell 3 writes them.  They
   must be regenerated here: a file written for one sub-model has no keys for the other's
   operators, and absent keys are read as 0. *)
HEFT$MergePrintSubsection["WCxf \[LongDash] Wilson-coefficient files"];
HEFTWCxfDir        = FileNameJoin[{HEFT$WorkspaceRoot, "wcxf"}];
HEFTWCxfInitFile   = FileNameJoin[{HEFTWCxfDir, "wcxf_init.json"}];
HEFTWCxfOutputFile = FileNameJoin[{HEFTWCxfDir, "wcxf_output.json"}];
Global`KappaFramework      = KappaFramework;
Global`InitialiseWCs       = InitialiseWCs;
Global`LOYukawaExpansion   = LOYukawaExpansion;
Global`IncludeCustodialT   = IncludeCustodialT;
Global`Combine2Derivatives = Combine2Derivatives;
Global`HiggsMaxOrder       = HiggsMaxOrder;
Global`HEFTNLOBasis        = HEFTNLOBasis;
Global`HEFTActiveNLOPieces = NLOOperators;
Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "wcxf_input.fr"}]];
HEFTWriteWCxfPointFiles[HEFTWCxfInitFile, HEFTWCxfOutputFile];

(* Cache verdict for the MERGED configuration.  A hit means this union has been built or
   merged before and Cell 5 will simply load it. *)
HEFT$MergePrintSubsection["LHEFT cache (merged model)"];
HEFTLHEFTCacheReport[];

Print[Style["\n[HEFT merge] Cell 4 done.", Bold]];
Print["[HEFT merge] Optional: edit Wilson coefficients in ", HEFTWCxfOutputFile];
Print["[HEFT merge] Next: Cell 5 (merge + LoadModel)."];

]; (* end merge cell 4 gate *)


(* =============================================================================
   CELL 5 \[LongDash] LoadModel on the union, merge, cache the result as LHEFT
   ============================================================================= *)

If[HEFT$MergeShouldRunCell[5],

If[!ValueQ[HEFT$WorkspaceRoot] || !ValueQ[HEFT$MergePlan],
  Print[Style["[HEFT merge] ERROR: run Cell 4 first.", Red, Bold]]; Abort[]
];
HEFT$MergeBootstrap[];
HEFT$MergeEnsureFeynRules[];

(* Same non-idempotent-LoadModel guard as heft_fr.wl Cell 5, for the same reason: a second
   LoadModel in one kernel corrupts the model state and can silently ignore EWInputScheme. *)
If[TrueQ[MR$ModelLoaded],
  Print[Style["[HEFT merge] ERROR: a FeynRules model is already loaded in this kernel.",
    Red, Bold]];
  Print[Style["[HEFT merge] Restart the kernel (Evaluation > Quit Kernel), then run: " <>
    "Cell 2 -> Cell 3 -> Cell 4 -> Cell 5.", Red, Bold]];
  Abort[]
];

(* Configuration -> model flags.  HEFTActiveNLOPieces is the UNION, so LoadModel declares
   every parameter both sub-models need; that is what makes one export off the merged
   Lagrangian possible at all. *)
Global`KappaFramework      = KappaFramework;
Global`InitialiseWCs       = InitialiseWCs;
Global`LOYukawaExpansion   = LOYukawaExpansion;
Global`IncludeCustodialT   = IncludeCustodialT;
Global`Combine2Derivatives = Combine2Derivatives;
Global`HEFTMaxOrder        = HEFTMaxOrder;
Global`HiggsMaxOrder       = HiggsMaxOrder;
Global`HEFTActiveNLOPieces = NLOOperators;
Global`HEFTNLOBasis        = HEFTNLOBasis;
Global`HEFTGauge           = HEFTGauge;
Global`EWInputScheme       = EWInputScheme;

HEFTWCxfDir        = FileNameJoin[{HEFT$WorkspaceRoot, "wcxf"}];
HEFTWCxfOutputFile = FileNameJoin[{HEFTWCxfDir, "wcxf_output.json"}];
If[!FileExistsQ[HEFTWCxfOutputFile],
  Print[Style["[HEFT merge] ERROR: WCxf output file not found: " <> HEFTWCxfOutputFile,
    Red, Bold]];
  Print["[HEFT merge] Run Cell 4 to (re)create it."];
  Abort[]
];
Global`HEFTWCxfOutputFile = HEFTWCxfOutputFile;
Print[Style["[HEFT merge WCxf] Wilson coefficients from: ", Bold], HEFTWCxfOutputFile];

CPUTime = TimeUsed[];
LoadModel[HEFT$ModelFile];
Print[Style["\n[HEFT merge] Model loaded in ", Bold], TimeUsed[] - CPUTime, " seconds (",
  Length[NLOOperators], " operator(s) declared)"];

(* Optional parameter restrictions, exactly as heft_fr.wl Cell 5 applies them. *)
HEFT$RestrictionPaths = {};
If[TrueQ[Massless],
  AppendTo[HEFT$RestrictionPaths, FileNameJoin[{HEFT$RestrictionsDir, "Massless.rst"}]]];
If[TrueQ[DiagonalCKM],
  AppendTo[HEFT$RestrictionPaths, FileNameJoin[{HEFT$RestrictionsDir, "DiagonalCKM.rst"}]]];
If[HEFT$RestrictionPaths =!= {},
  Do[If[!FileExistsQ[p],
      Print[Style["[HEFT merge] ERROR: restriction not found: " <> p, Red, Bold]]; Abort[]],
    {p, HEFT$RestrictionPaths}];
  Print[Style["[HEFT merge] Loading restrictions: ", Bold], HEFT$RestrictionPaths];
  M$Restrictions = Fold[
    Function[{acc, path}, LoadRestriction[path]; Join[acc, M$Restrictions]],
    {}, HEFT$RestrictionPaths
  ],
  Print[Style["[HEFT merge] No .rst restrictions.", Bold]]
];

(* ======================= merge (or reuse) the Lagrangian ======================= *)

HEFT$MergeMetaFinal = HEFTLHEFTCacheMeta[];
HEFT$MergeCachedEntry =
  If[TrueQ[ForceRebuildLHEFT], None, HEFTLHEFTFindCacheEntry[HEFT$MergeMetaFinal]];

If[HEFT$MergeCachedEntry =!= None,

  (* The merged configuration is itself an ordinary cache entry, so a repeat run is a plain
     hit - no re-merging, and no distinction from a directly built model. *)
  Print[Style["\n[HEFT merge] This merged configuration is already cached under \"" <>
    ToString[HEFTLHEFTEntryName[HEFT$MergeCachedEntry]] <> "\" (" <>
    HEFTLHEFTEntryDescription[HEFT$MergeCachedEntry] <> ") \[LongDash] loading it.", Bold]];
  HEFTLHEFTCacheRegisterName[HEFT$MergeCachedEntry, OutputName];
  LHEFT = HEFTLHEFTCacheLoad[HEFT$MergeCachedEntry],

  HEFT$MergePrintSubsection["Merging"];
  CPUTime = TimeUsed[];

  HEFT$MergeLO = HEFTMergeGetLHEFT[HEFT$MergePlan["lo"]];
  HEFT$MergeResult = HEFTMergeLagrangians[
    HEFT$MergeLO,
    Function[e, {e["name"] <> "  [" <> HEFTMergeOperatorSummary[e["operators"]] <> "]",
                 HEFTMergeGetLHEFT[e]}] /@ HEFT$MergePlan["sources"]
  ];
  If[HEFT$MergeResult === $Failed, Abort[]];

  LHEFT = HEFT$MergeResult["lagrangian"];
  HEFT$MergeSeconds = TimeUsed[] - CPUTime;
  Print[Style["[HEFT merge] merged in ", Bold], HEFT$MergeSeconds, " seconds"];
  Print[Style["[HEFT merge] LHEFT LeafCount: ", Bold], LeafCount[LHEFT]];

  (* Cached like any other build, with the sources recorded.  configHash is computed from the
     compare keys alone, so the extra provenance fields do not change it and a later direct
     build of the same union finds this entry as a normal hit. *)
  HEFT$MergeMetaFinal = Append[HEFT$MergeMetaFinal, <|
    "mergedFrom" -> (#["folder"] & /@ HEFT$MergePlan["sources"]),
    "mergedLOBaseline" -> HEFT$MergePlan["lo"]["folder"]
  |>];
  Module[{paths},
    paths = HEFTLHEFTCachePaths[HEFT$MergeMetaFinal];
    HEFTLHEFTCacheSave[paths, HEFT$MergeMetaFinal, HEFT$MergeSeconds];
    Print[Style["[HEFT merge] merged LHEFT cached: ", Bold], paths["mx"]];
    Print[Style["[HEFT merge] Cache meta: ", Bold], paths["meta"]]
  ]
];

Print["[HEFT merge] Done."];
Print["[HEFT merge] Next: Cell 6 (Feynman rules), Cell 7 (UFO) and/or Cell 8 (FeynArts) \[LongDash] " <>
  "the same cells as in heft_fr_notebook.wl."];

]; (* end merge cell 5 gate *)
