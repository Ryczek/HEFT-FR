(* LHEFT disk cache for heft_fr.wl.  Fixed directory: HEFT_cache/  (no option).

   Layout: one subfolder per *configuration*,
     HEFT_cache/<OutputName>__<configHash>/{LHEFT.mx, meta.json}
   <configHash> is an 8-hex-digit MD5 over every physics setting that goes into the build
   (HEFTLHEFTCacheCompareKeys).  <OutputName> is in the folder name only so HEFT_cache/ stays
   readable by eye - the lookup is by hash, never by name.

   Lookup is a single glob for "*__<configHash>" (no per-entry meta.json scan), done by
   HEFTLoadOrBuildLHEFT[] and, non-destructively, by HEFTLHEFTCacheReport[] at the end of
   Cells 3 and 4 so you know before starting Cell 5 whether it will load or build:
     - hit under the current OutputName  -> load it.
     - hit under a different OutputName  -> report which name, load it, and record the current
       OutputName in that entry's meta.json "names" list.  The .mx is deliberately NOT copied:
       the lookup is by configuration, so the one copy is reachable from every name (and an
       .mx runs to hundreds of MB with the full 3-generation Wilson tensors).
     - miss -> build LHEFTMassBasis and save it, always, overwriting the entry for this exact
       configuration if one is there - it can only be another build of the very same thing.

   ForceRebuildLHEFT is the only option left: True skips the lookup and rebuilds.

   Wilson coefficients are NOT part of the key at all.  Every one of them is an External
   FeynRules parameter, so a value never enters LHEFT; it reaches the output through
   M$Parameters when Cell 7 exports.  And since 2026-08-05 values do not decide which operators
   are in the Lagrangian either - that is NLOOperators alone (HEFTPieceActiveQ in wcxf_input.fr
   is now a plain MemberQ, and the LO HEFTLOIf gates are gone).  So *any* edit to
   wcxf/wcxf_output.json, zeros included, is a cache hit: re-run Cell 5 (a LoadModel, seconds)
   and Cell 7, and the new numbers are in the export.

   Cell 5 itself can never be skipped: Cell 7 needs the FeynRules model state that only
   LoadModel builds (fields, M$Parameters -> the UFO/FeynArts parameter tables), and LoadModel
   is also what reads wcxf_output.json.  The cache only ever skips LHEFTMassBasis. *)

HEFTLHEFTCacheDir[] := Module[{dir},
  dir = FileNameJoin[{HEFT$WorkspaceRoot, "HEFT_cache"}];
  Quiet[CreateDirectory[dir, CreateIntermediateDirectories -> True], CreateDirectory::eexist];
  dir
];

HEFTLHEFTFileDigest[path_String] := Module[{h},
  If[!StringQ[path] || !FileExistsQ[path], Return[""]];
  h = Quiet @ Check[FileHash[path, "MD5"], $Failed];
  If[h === $Failed, Return[""]];
  IntegerString[h, 16, 8]
];

(* Every .fr file whose contents can change what LHEFTMassBasis evaluates to.  wcxf_input.fr is
   in the list because HEFTPieceActiveQ lives there and decides which operators enter the
   Lagrangian at all; the parameter files are in it because their `Definitions` are applied by
   the ExpandIndices pass that produces the mass basis.  All five of those were missing before
   2026-08-05, so edits to them left stale cache entries looking valid. *)
HEFTLHEFTModelDigest[] := Module[{paths, digests},
  paths = Select[
    FileNameJoin[{HEFT$WorkspaceRoot, "model_files", #}] & /@ {
      "HEFT_Model.fr",
      "gauge_normalization.fr",
      "definitions.fr",
      "input_scheme.fr",
      "wcxf_input.fr",
      "power_counting.fr",
      "fields_LO.fr",
      "LO/parameters_LO.fr",
      "LO/Lagrangian_LO.fr",
      "NLO/basis_1604_06801/parameters_NLO.fr",
      "NLO/basis_1604_06801/Lagrangian_Bosonic_NLO.fr",
      "NLO/basis_1604_06801/Lagrangian_Fermionic_2F_NLO.fr",
      "NLO/basis_1604_06801/Lagrangian_Fermionic_4F_NLO.fr",
      "NNLO/parameters_NNLO.fr",
      "NNLO/Lagrangian_Bosonic_NNLO.fr"
    },
    FileExistsQ
  ];
  digests = HEFTLHEFTFileDigest /@ paths;
  IntegerString[Hash[StringJoin[digests], "MD5"], 16, 8]
];

HEFTLHEFTCacheMeta[] := Module[{},
  <|
    "outputName"        -> OutputName,
    "operators"         -> Sort[NLOOperators],
    "basis"             -> HEFTNLOBasis,
    "heftMaxOrder"      -> HEFTMaxOrder,
    "higgsMaxOrder"     -> HiggsMaxOrder,
    "gauge"             -> HEFTGauge,
    "ewScheme"          -> EWInputScheme,
    "kappaFramework"    -> KappaFramework,
    "loYukawaExpansion" -> LOYukawaExpansion,
    "includeCustodialT" -> IncludeCustodialT,
    "combine2Derivatives" -> Combine2Derivatives,
    "massless"          -> Massless,
    "diagonalCKM"       -> DiagonalCKM,
    "modelDigest"       -> HEFTLHEFTModelDigest[]
  |>
];

(* Everything except "outputName": the name is metadata about where output goes, not physics,
   and a match under a different name is exactly what the lookup is for. *)
HEFTLHEFTCacheCompareKeys = {
  "operators", "basis", "heftMaxOrder", "higgsMaxOrder",
  "gauge", "ewScheme", "kappaFramework", "loYukawaExpansion", "includeCustodialT",
  "combine2Derivatives", "massless", "diagonalCKM", "modelDigest"
};

(* Sort[Normal[...]] before hashing: two Associations with the same pairs in a different key
   order are not === in Mathematica, and would hash differently. *)
HEFTLHEFTConfigHash[meta_Association] := IntegerString[
  Hash[Sort @ Normal @ KeyTake[meta, HEFTLHEFTCacheCompareKeys], "MD5"], 16, 8
];

HEFTLHEFTCacheSanitizeName[name_] :=
  StringReplace[ToString[name], {"/" -> "_", "\\" -> "_", " " -> "_"}];

HEFTLHEFTCacheEntryPaths[dir_String] := <|
  "dir"  -> dir,
  "mx"   -> FileNameJoin[{dir, "LHEFT.mx"}],
  "meta" -> FileNameJoin[{dir, "meta.json"}]
|>;

(* Where this configuration is saved under the *current* OutputName. *)
HEFTLHEFTCachePaths[meta_Association] := HEFTLHEFTCacheEntryPaths @ FileNameJoin[{
  HEFTLHEFTCacheDir[],
  HEFTLHEFTCacheSanitizeName[meta["outputName"]] <> "__" <> HEFTLHEFTConfigHash[meta]
}];

(* Existence + basic corruption check only (file present, non-empty .mx, parseable meta.json). *)
HEFTLHEFTCacheExistsQ[metaPath_String, mxPath_String] := Module[{stored},
  If[!FileExistsQ[metaPath] || !FileExistsQ[mxPath], Return[False]];
  If[Quiet[Check[FileByteCount[mxPath], 0]] < 1, Return[False]];
  (* "RawJSON" (not "JSON") - returns Association consistently; "JSON" returns a plain List of
     rules on at least one Mathematica version seen on this machine (14.0.0), which would make
     every downstream Head[...] === Association check below fail silently. *)
  stored = Quiet @ Check[Import[metaPath, "RawJSON"], $Failed];
  stored =!= $Failed && Head[stored] === Association
];

HEFTLHEFTReadMeta[metaPath_String] := Module[{stored},
  stored = Quiet @ Check[Import[metaPath, "RawJSON"], $Failed];
  If[stored === $Failed || Head[stored] =!= Association, None, stored]
];

HEFTLHEFTMetaValueEqual[a_, b_] := Which[
  ListQ[a] && ListQ[b], Sort[a] === Sort[b],
  TrueQ[a] || TrueQ[b] || (a === False || b === False), TrueQ[a] === TrueQ[b],
  True, a === b
];

HEFTLHEFTMetaMatchQ[stored_Association, current_Association] := AllTrue[
  HEFTLHEFTCacheCompareKeys,
  Function[k, KeyExistsQ[stored, k] && HEFTLHEFTMetaValueEqual[stored[k], current[k]]]
];

(* The lookup: one glob, then verify the candidate's meta.json really does match (guards against
   a hash collision or an entry written by an older layout).  The current OutputName's own
   folder wins if it is among the hits, so the common case reports no name change. *)
HEFTLHEFTFindCacheEntry[meta_Association] := Module[
  {dir, hash, ownDir, candidates, cand, entry, stored, found = None},
  dir  = HEFTLHEFTCacheDir[];
  hash = HEFTLHEFTConfigHash[meta];
  ownDir = HEFTLHEFTCachePaths[meta]["dir"];
  candidates = Select[FileNames["*__" <> hash, dir], DirectoryQ];
  candidates = Join[Select[candidates, # === ownDir &], Select[candidates, # =!= ownDir &]];
  Do[
    entry = HEFTLHEFTCacheEntryPaths[cand];
    If[HEFTLHEFTCacheExistsQ[entry["meta"], entry["mx"]],
      stored = HEFTLHEFTReadMeta[entry["meta"]];
      If[stored =!= None && HEFTLHEFTMetaMatchQ[stored, meta],
        found = Append[entry, "stored" -> stored];
        Break[]
      ]
    ],
    {cand, candidates}
  ];
  found
];

HEFTLHEFTEntryName[entry_Association] := Lookup[entry["stored"], "outputName", "?"];

HEFTLHEFTEntryDescription[entry_Association] := Module[{stored, built, secs},
  stored = entry["stored"];
  built = Lookup[stored, "builtAt", None];
  secs  = Lookup[stored, "buildSeconds", None];
  StringJoin[
    If[StringQ[built], "built " <> built, "built at an unknown time"],
    If[NumericQ[secs], ", took " <> ToString[Round[secs]] <> " s", ""]
  ]
];

HEFTLHEFTCacheSave[paths_Association, meta_Association, buildSeconds_] := Module[{out},
  Quiet[CreateDirectory[paths["dir"], CreateIntermediateDirectories -> True],
    CreateDirectory::eexist];
  out = Association @ Normal @ Append[meta, <|
    "names"        -> {meta["outputName"]},
    "configHash"   -> HEFTLHEFTConfigHash[meta],
    "builtAt"      -> DateString[{"ISODateTime"}],
    "buildSeconds" -> buildSeconds,
    "mathematica"  -> $Version
  |>];
  Export[paths["meta"], out, "JSON"];
  DumpSave[paths["mx"], "LHEFT"];
];

(* A hit found under another OutputName: nothing is copied, the current name is just recorded in
   the entry's own meta.json so HEFT_cache/ says which runs it has served. *)
HEFTLHEFTCacheRegisterName[entry_Association, name_String] := Module[{stored, names},
  stored = entry["stored"];
  names = Lookup[stored, "names", {Lookup[stored, "outputName", name]}];
  If[!ListQ[names], names = {ToString[names]}];
  If[MemberQ[names, name], Return[names]];
  names = Append[names, name];
  Quiet @ Check[Export[entry["meta"], Append[stored, "names" -> names], "JSON"], $Failed];
  names
];

HEFTLHEFTCacheLoad[paths_Association] := Module[{},
  Get[paths["mx"]];
  If[!ValueQ[LHEFT],
    Print[Style["[HEFT] ERROR: cache file did not define LHEFT: " <> paths["mx"], Red, Bold]];
    Abort[]
  ];
  LHEFT
];

(* Only used when a build is about to start, so scanning every meta.json is free by comparison.
   Scores previous builds by how close their configuration is to this one. *)
HEFTLHEFTEstimateBuildSeconds[meta_Association] := Module[
  {dir, sd, best = None, bestScore = Infinity, stored, score},
  dir = HEFTLHEFTCacheDir[];
  Do[
    stored = HEFTLHEFTReadMeta[FileNameJoin[{sd, "meta.json"}]];
    If[stored =!= None && NumericQ[Lookup[stored, "buildSeconds", None]],
      score =
        Abs[Length[Lookup[stored, "operators", {}]] - Length[meta["operators"]]] +
        If[Lookup[stored, "basis", None] === meta["basis"], 0, 5] +
        If[Lookup[stored, "heftMaxOrder", None] === meta["heftMaxOrder"], 0, 5];
      If[score < bestScore, bestScore = score; best = stored]
    ],
    {sd, Select[FileNames["*", dir], DirectoryQ]}
  ];
  best
];

HEFTLHEFTPrintBuildEstimate[meta_Association] := Module[{ref, secs},
  ref = HEFTLHEFTEstimateBuildSeconds[meta];
  If[ref === None, Return[]];
  secs = Lookup[ref, "buildSeconds", None];
  If[!NumericQ[secs], Return[]];
  Print[Style["[HEFT] For scale: the closest previous build (\"" <>
    ToString[Lookup[ref, "outputName", "?"]] <> "\", " <>
    ToString[Length[Lookup[ref, "operators", {}]]] <> " operator(s)) took " <>
    ToString[Round[secs]] <> " s.", Gray]]
];

(* Non-destructive status report.  Called at the end of Cells 3 and 4 (nothing here needs
   FeynRules or a loaded model) and again at the top of Cell 5.  Returns the matching entry or
   None, so callers can reuse it. *)
HEFTLHEFTCacheReport[] := Module[{meta, entry},
  meta = HEFTLHEFTCacheMeta[];
  Print[Style["[HEFT] Cache: ", Bold], HEFTLHEFTCacheDir[],
    Style["  (config " <> HEFTLHEFTConfigHash[meta] <> ")", Gray]];

  If[TrueQ[ForceRebuildLHEFT],
    Print[Style["[HEFT] ForceRebuildLHEFT = True \[LongDash] Cell 5 will rebuild LHEFT and " <>
      "overwrite the cache entry for this configuration.", Bold]];
    HEFTLHEFTPrintBuildEstimate[meta];
    Return[None]
  ];

  entry = HEFTLHEFTFindCacheEntry[meta];
  If[entry === None,
    Print[Style["[HEFT] No cached build for this configuration \[LongDash] Cell 5 will build " <>
      "it from scratch, then save it.", Bold]];
    HEFTLHEFTPrintBuildEstimate[meta];
    Return[None]
  ];

  If[HEFTLHEFTEntryName[entry] === OutputName,
    Print[Style["[HEFT] Cached build found for this configuration (" <>
      HEFTLHEFTEntryDescription[entry] <> "). Cell 5 will load it, not rebuild it.", Bold]],
    Print[Style["[HEFT] Model already present under the name \"" <>
      ToString[HEFTLHEFTEntryName[entry]] <> "\" (" <> HEFTLHEFTEntryDescription[entry] <>
      "). Cell 5 will load it, not rebuild it \[LongDash] output will be written as \"" <>
      ToString[OutputName] <> "\".", Bold]]
  ];
  Print["[HEFT]   ", entry["mx"]];
  entry
];

HEFTLoadOrBuildLHEFT[] := Module[{meta, entry, paths, t0, dt},

  meta = HEFTLHEFTCacheMeta[];
  Print[Style["[HEFT] Cache: ", Bold], HEFTLHEFTCacheDir[],
    Style["  (config " <> HEFTLHEFTConfigHash[meta] <> ")", Gray]];

  If[!TrueQ[ForceRebuildLHEFT],
    entry = HEFTLHEFTFindCacheEntry[meta];
    If[entry =!= None,
      If[HEFTLHEFTEntryName[entry] === OutputName,
        Print[Style["[HEFT] Cache hit \[LongDash] loading: ", Bold], entry["mx"]],
        Print[Style["[HEFT] Such model exists under the name \"" <>
          ToString[HEFTLHEFTEntryName[entry]] <> "\" \[LongDash] loading it; output will be " <>
          "written as \"" <> ToString[OutputName] <> "\".", Bold]];
        Print["[HEFT]   ", entry["mx"]];
        HEFTLHEFTCacheRegisterName[entry, OutputName]
      ];
      Return[HEFTLHEFTCacheLoad[entry]]
    ]
  ];

  If[TrueQ[ForceRebuildLHEFT],
    Print[Style["[HEFT] ForceRebuildLHEFT = True \[LongDash] rebuilding LHEFT.", Bold]],
    Print[Style["[HEFT] No cached build for this configuration; building LHEFTMassBasis...",
      Bold]]
  ];
  HEFTLHEFTPrintBuildEstimate[meta];

  t0 = TimeUsed[];
  LHEFT = LHEFTMassBasis;
  dt = TimeUsed[] - t0;
  Print[Style["[HEFT] mass basis Lagrangian obtained in ", Bold], dt, " seconds"];

  (* Always saved, overwriting if present: the folder is keyed by configuration, so anything
     already there is a build of exactly this. *)
  paths = HEFTLHEFTCachePaths[meta];
  HEFTLHEFTCacheSave[paths, meta, dt];
  Print[Style["[HEFT] LHEFT cached: ", Bold], paths["mx"]];
  Print[Style["[HEFT] Cache meta: ", Bold], paths["meta"]];

  LHEFT
];
