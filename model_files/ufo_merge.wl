(* ::Package:: *)

(* UFO model merging.  Get'd by heft_fr_merge.wl for merge notebook Cells 11 (list the UFO
   exports) and 12 (merge them).  Needs lheft_cache.wl and lheft_merge.wl (loaded by
   HEFT$MergeBootstrap[]) and heft_export_meta.wl (loaded below).  The merge itself is done by
   model_files/ufo_merge.py; this file does what fa_merge.wl does for FeynArts before the merge -
   find the exports, check their heft_export.json records against the Cell 2 configuration, find
   the SM baseline, refuse what cannot be merged - then calls the script and writes the merged
   export's own record.

   WHAT THIS DOES
   Builds output/UFO/<OutputName>/ out of UFO exports already on disk, with no FeynRules and no
   LoadModel: every coupling entry becomes  C(LO) + Sum_i ( C(A_i) - C(LO) ),  exact at one
   Wilson-coefficient insertion.  The UFO writer is the slowest step of the pipeline (about 10 h
   for the full bosonic model), so this lets it run on small models only.  How each UFO file is
   treated: the header of ufo_merge.py.  decays.py is omitted (user decision D2, 2026-10-06).

   WHAT IS REFUSED (here; ufo_merge.py refuses the file-level problems)
   - an export without heft_export.json, or whose record differs from the Cell 2 configuration in
     any hashed option, modelDigest, MaxVertexLegs or the UFO-interface digest;
   - no SM baseline, or several without MergeUFOBaseline naming one;
   - an operator in two sources, a source listed twice, OutputName equal to an input. *)

Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_export_meta.wl"}]];

HEFTUFOError[msg_String] := (Print[Style["[HEFT UFO merge] ERROR: " <> msg, Red, Bold]]; Abort[]);

HEFTUFOExportsDir[] := FileNameJoin[{HEFT$WorkspaceRoot, "output", "UFO"}];

(* The Python 3 interpreter: HEFT$Python if set, else the first one found.  ufo_merge.py needs only
   the standard library (Python >= 3.8). *)
HEFTUFOPython[] := If[StringQ[HEFT$Python], HEFT$Python,
  SelectFirst[{"/usr/local/bin/python3", "/opt/homebrew/bin/python3",
      "/Library/Frameworks/Python.framework/Versions/Current/bin/python3", "/usr/bin/python3"},
    FileExistsQ, "python3"]];


(* ============================================================================
   Index of the exports (Cell 11) and resolving names (Cell 12)
   ============================================================================ *)

HEFTUFOExportIndex[] := Module[{dir = HEFTUFOExportsDir[], dirs, entries = {}, noMeta = {}, m},
  dirs = If[DirectoryQ[dir], Sort @ Select[FileNames["*", dir], DirectoryQ], {}];
  Do[
    m = HEFTExportReadMeta[d];
    If[m === None || Lookup[m, "format", None] =!= "ufo",
      AppendTo[noMeta, FileNameTake[d]],
      AppendTo[entries, <|
        "name"      -> FileNameTake[d],
        "dir"       -> d,
        "meta"      -> m,
        "operators" -> Sort @ Lookup[m, "operators", {}],
        "created"   -> ToString @ Lookup[m, "created", "?"]
      |>]
    ],
    {d, dirs}
  ];
  <|"entries" -> entries, "noMeta" -> noMeta|>
];

HEFTUFOCompatible[index_Association, current_Association] :=
  Select[index["entries"], HEFTExportDifferingKeys[#["meta"], current, "ufo"] === {} &];

HEFTUFOPrintCatalog[index_Association, current_Association] := Module[
  {compatible, rest, nearMiss, lo},
  compatible = HEFTUFOCompatible[index, current];
  rest = Complement[index["entries"], compatible];

  Print[Style["\n  UFO exports matching this configuration (MaxVertexLegs = " <>
    ToString[current["maxVertexLegs"]] <> ")", Bold, FontSize -> 14]];
  If[compatible === {},
    Print[Style["    None. Export the sub-models first with heft_fr_notebook.wl (Cells 5 and 7), " <>
      "using these very settings and one operator selection each.", Bold, Darker[Red]]],

    Print @ Grid[
      Prepend[
        MapIndexed[{ToString @ First[#2], #1["name"], HEFTMergeOperatorSummary[#1["operators"]],
          #1["created"]} &, compatible],
        Style[#, Bold] & /@ {"#", "name", "operators", "exported"}],
      Alignment -> Left,
      Dividers -> {False, {False, True, {False}}},
      Spacings -> {2, 0.4},
      ItemStyle -> Directive[FontFamily -> "Monospace", FontSize -> 11]
    ];
    lo = Select[compatible, #["operators"] === {} &];
    Which[
      lo === {},
        Print[Style["\n    No SM baseline among them. Merging needs one: export once with " <>
          "EFTOperators = {} and everything else exactly as configured here.", Bold, Darker[Red]]],
      Length[lo] === 1,
        Print[Style["    SM baseline present: \"" <> First[lo]["name"] <> "\".", Darker[Green]]],
      True,
        Print[Style["    " <> ToString[Length[lo]] <> " SM baselines (" <>
          StringRiffle[#["name"] & /@ lo, ", "] <> "): name one in MergeUFOBaseline, Cell 12.",
          Orange]]
    ]
  ];

  If[rest =!= {},
    nearMiss = Select[{#, HEFTExportDifferingKeys[#["meta"], current, "ufo"]} & /@ rest,
      Length[Last[#]] <= 2 &];
    Print[Style["\n  Other UFO exports with a record: " <> ToString[Length[rest]] <>
      " (not mergeable with this configuration)", Bold]];
    If[nearMiss =!= {},
      Print[Style["    Close matches, and the key(s) they differ in:", Gray]];
      Print @ Grid[
        {"      " <> #[[1]]["name"], HEFTMergeOperatorSummary[#[[1]]["operators"]],
          StringRiffle[#[[2]], ", "]} & /@ Take[nearMiss, UpTo[12]],
        Alignment -> Left, Spacings -> {2, 0.3},
        ItemStyle -> Directive[FontFamily -> "Monospace", FontSize -> 10]
      ]
    ]
  ];

  If[index["noMeta"] =!= {},
    Print[Style["\n  " <> ToString[Length[index["noMeta"]]] <> " UFO folder(s) without a UFO " <>
      "heft_export.json (exported before 2026-10-06) - re-export them with Cell 7 to merge them: " <>
      StringRiffle[Take[index["noMeta"], UpTo[20]], ", "] <>
      If[Length[index["noMeta"]] > 20, ", ...", ""], Gray]]
  ];

  compatible
];

HEFTUFOResolve[spec_, index_Association, compatible_List, current_Association] := Module[{hit, other},
  If[!StringQ[spec], HEFTUFOError["MergeUFOSources must list export names as strings; got " <>
    ToString[spec, InputForm] <> "."]];
  hit   = SelectFirst[compatible, #["name"] === spec &, None];
  other = SelectFirst[index["entries"], #["name"] === spec &, None];
  Which[
    hit =!= None, hit,
    other =!= None, HEFTUFOError["\"" <> spec <> "\" was exported with a different " <>
      StringRiffle[HEFTExportDifferingKeys[other["meta"], current, "ufo"], ", "] <>
      " than the configuration in Cell 2."],
    MemberQ[index["noMeta"], spec], HEFTUFOError["\"" <> spec <> "\" has no UFO heft_export.json " <>
      "(exported before 2026-10-06): re-export it with Cell 7."],
    True, HEFTUFOError["no UFO export called \"" <> spec <> "\" in " <> HEFTUFOExportsDir[] <>
      ". Cell 11 lists the ones available."]
  ]
];

HEFTUFOFindBaseline[compatible_List, spec_] := Module[{lo, hit},
  lo = Select[compatible, #["operators"] === {} &];
  If[StringQ[spec],
    hit = SelectFirst[lo, #["name"] === spec &, None];
    If[hit === None, HEFTUFOError["MergeUFOBaseline = \"" <> spec <> "\" is not an SM-only " <>
      "UFO export of this configuration."]];
    hit,
    Which[
      lo === {}, HEFTUFOError["no SM baseline. Export once with EFTOperators = {} and everything " <>
        "else as configured in Cell 2: every sub-model carries the whole SM, so without " <>
        "subtracting it N sub-models give N x SM."],
      Length[lo] > 1, HEFTUFOError["several SM baselines match (" <>
        StringRiffle[#["name"] & /@ lo, ", "] <> "): set MergeUFOBaseline to one of them."],
      True, First[lo]
    ]
  ]
];


(* ============================================================================
   Driver - merge notebook Cell 12
   ============================================================================ *)

HEFTUFOMergeRun[sourceNames_List, outName_String, baselineSpec_] := Module[
  {t0 = AbsoluteTime[], current, index, compatible, lo, subs, names, ops, dup, outDir, spec,
   specFile, script, py, res, lines, summary, refused},

  current    = HEFTExportCurrentMeta["ufo"];
  index      = HEFTUFOExportIndex[];
  compatible = HEFTUFOCompatible[index, current];

  If[!DuplicateFreeQ[sourceNames], HEFTUFOError["a name is listed twice in MergeUFOSources."]];
  lo   = HEFTUFOFindBaseline[compatible, baselineSpec];
  subs = HEFTUFOResolve[#, index, compatible, current] & /@ sourceNames;
  If[MemberQ[#["name"] & /@ subs, lo["name"]],
    Print[Style["[HEFT UFO merge] " <> lo["name"] <> " is the SM baseline; it is subtracted " <>
      "automatically and was dropped from the sources.", Gray]];
    subs = Select[subs, #["name"] =!= lo["name"] &]
  ];
  If[subs === {}, HEFTUFOError["no sub-model left to merge."]];
  If[AnyTrue[subs, #["operators"] === {} &], HEFTUFOError["a source is an SM-only export; list " <>
    "only exports with operators (the baseline is found automatically)."]];
  ops = Flatten[#["operators"] & /@ subs];
  dup = Select[Tally[ops], Last[#] > 1 &][[All, 1]];
  If[dup =!= {}, HEFTUFOError["operator(s) in more than one source, which would be added twice: " <>
    StringRiffle[dup, ", "] <> "."]];
  names = #["name"] & /@ subs;
  If[MemberQ[Append[names, lo["name"]], outName], HEFTUFOError["OutputName \"" <> outName <>
    "\" is one of the inputs; the merge would overwrite it. Choose another OutputName in Cell 2."]];

  HEFT$MergePrintSubsection["UFO merge plan"];
  Print["    ", Style[StringPadRight["SM baseline", 34], Bold], lo["name"]];
  Do[Print["    ", Style[StringPadRight[s["name"], 34], Bold], HEFTMergeOperatorSummary[s["operators"]]],
    {s, subs}];

  outDir = FileNameJoin[{HEFTUFOExportsDir[], outName}];
  If[DirectoryQ[outDir], Print[Style["[HEFT UFO merge] Replacing " <> outDir, Orange]]];
  spec = <|"baseline" -> lo["dir"], "sources" -> (#["dir"] & /@ subs), "out" -> outDir,
    "overwrite" -> True|>;
  specFile = FileNameJoin[{$TemporaryDirectory, "heft_ufo_merge_" <> outName <> ".json"}];
  Export[specFile, spec, "RawJSON"];
  script = FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "ufo_merge.py"}];
  py = HEFTUFOPython[];
  res = RunProcess[{py, script, specFile}];
  Quiet @ DeleteFile[specFile];
  If[!AssociationQ[res], HEFTUFOError["could not run " <> py <> ". Set HEFT$Python to a Python 3 " <>
    "interpreter (standard library only, version 3.8 or later)."]];
  lines = StringSplit[res["StandardOutput"], "\n"];
  Scan[If[!StringStartsQ[#, "@@"], Print[#]] &, lines];
  refused = SelectFirst[lines, StringStartsQ[#, "@@REFUSED@@"] &, None];
  If[refused =!= None, HEFTUFOError["refused by ufo_merge.py: " <>
    ImportString[StringDrop[refused, 12], "RawJSON"]["reason"]]];
  summary = SelectFirst[lines, StringStartsQ[#, "@@SUMMARY@@"] &, None];
  If[res["ExitCode"] =!= 0 || summary === None,
    HEFTUFOError["ufo_merge.py failed (exit code " <> ToString[res["ExitCode"]] <> "):\n" <>
      res["StandardError"]]];
  summary = ImportString[StringDrop[summary, 12], "RawJSON"];

  (* The merged export is an ordinary export of the union: same record, so it can itself be a
     source of a later merge. *)
  HEFTExportWriteMeta[outDir, "ufo", <|
    "outputName"       -> outName,
    "operators"        -> Sort[ops],
    "mergedFrom"       -> names,
    "mergedLOBaseline" -> lo["name"],
    "decays"           -> "omitted"
  |>];

  Print[Style["[HEFT UFO merge] " <> ToString[summary["vertices"]] <> " vertices, " <>
    ToString[summary["couplings"]] <> " couplings, " <> ToString[Length[ops]] <> " operators, in " <>
    ToString[Round[AbsoluteTime[] - t0, 0.1]] <> " s.", Bold]];
  Print[Style["[HEFT UFO merge] Written to ", Bold], outDir];
  Print["[HEFT UFO merge]   ", FileNameTake /@ Select[FileNames["*", outDir], !DirectoryQ[#] &]];
  Print[Style["[HEFT UFO merge] decays.py is not written (widths are not additive); let MadGraph " <>
    "compute the widths (compute_widths, or Auto in the param card).", Gray]];
  outDir
];
