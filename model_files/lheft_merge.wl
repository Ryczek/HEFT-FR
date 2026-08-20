(* ::Package:: *)

(* Model merging from HEFT_cache/ entries.  Get'd by heft_fr_merge.wl (the pipeline behind
   heft_fr_merge_models.wl).  Requires lheft_cache.wl to have been Get first: every cache
   concept here - the directory, the entry layout, the compare keys, the meta reader - is
   reused from there rather than restated, so the two cannot drift apart.

   WHAT THIS DOES
   Builds one big model out of several small ones without re-running the expensive
   LHEFTMassBasis pass.  ExpandIndices is linear in the Lagrangian, so with N sub-models

       LHEFT(A u B)  =  LHEFT(A) + LHEFT(B) - LHEFT(LO)        (generally: sum - (N-1) LO)

   and each LHEFT(x) is already sitting in HEFT_cache/<name>__<hash>/LHEFT.mx from an earlier
   run.  The LO baseline must be subtracted explicitly: every sub-model contains the *whole*
   LO Lagrangian, so adding N of them without it gives N x LO and every SM vertex comes out
   scaled by N.

   WHEN IT IS EXACT
   Only at linear order in ChiralOrder, hence the hard refusal at HEFTMaxOrder > 1.  The model
   mixes operators non-linearly in two places: HEFTUpdateGaugeNormalizations[], where
   eps = -2 chi CP1NLOn0 WnormINV BnormINV P12normINV is a *product* and the kinetic diagonal
   is Wnorm^2 P12norm^2; and the EW input scheme, whose shifts mix CP1/CP12/CFTn0 and the
   RL2/RL5 vev shift jointly.  At O(chi) all of that linearises and the identity above is
   exact; at O(chi^2) a build with only P1NLO genuinely has a different A-Z rotation - i.e.
   different physical fields - than a build with P1NLO + P12NLO, and no merge of separately
   built models can recover the cross term.

   WHY THE MERGE IS PLAIN ARITHMETIC, AND NOT TERM MATCHING
   The obvious implementation - match the LO terms of each sub-model against the baseline and
   drop them - does not work, and the reason is worth recording because it looks like it
   should.  Two things defeat it, both measured on real builds (2026-08-18):

     1. FeynRules names summed dummy indices with Unique-style $-suffixed symbols (a$27410,
        sp2$4536, ...) whose counters diverge between kernels.  Renaming them "in order of
        first appearance" is NOT canonical, because Times is Orderless: Mathematica sorts the
        factors of a product by symbol name, so a different dummy name gives a different
        factor order, which gives a different first-appearance order, which gives a different
        canonical form.  A Yukawa mass term matched this way came out as present in one build
        and absent in the other.
     2. More fundamentally, the LO sector is not written the same way in the two builds.
        Turning on any of P1NLO / P12NLO / WHNLO / BHNLO switches gauge_normalization.fr to
        its other A-Z branch, whose cos/sin are algebraically equal to the LO ones but
        syntactically different (1/Sqrt[1 + G1^2/GW^2] rather than GW/Sqrt[G1^2 + GW^2]).
        Expand does not reconcile those, so 102 of the 149 LO terms of an LO-only build do
        not appear verbatim in a {P1NLO} build at all.

   Plain arithmetic is immune to both: adding expressions never requires matching terms, and
   dummy indices are summed *within* a term, so terms from different sub-models never
   interact.  Algebraically L_i = LO + delta_i whatever form each is written in, so
   sum - (N-1) LO = LO + sum(delta_i) exactly.

   The cost is that nothing cancels syntactically, so the merged Lagrangian is bigger than a
   directly built one - measured +29% in LeafCount (39327 vs 30556) for {P1NLO} + {P12NLO}.
   FeynRules collapses it during vertex extraction, and the vertices are exact: 105 vertices
   both ways, identical field content, and 0 of 105 couplings differing. *)


(* ============================================================================
   Merge group: the configuration that must agree
   ============================================================================ *)

(* Every cache compare key except "operators" - i.e. exactly "same configuration, different
   operator selection".  modelDigest is in here and is the one doing the heavy lifting: it
   pins the .fr sources, so two sub-models built a week apart against different versions of
   gauge_normalization.fr can never be merged. *)
HEFTMergeGroupKeys = {
  "basis", "heftMaxOrder", "higgsMaxOrder", "gauge", "ewScheme",
  "kappaFramework", "loYukawaExpansion", "includeCustodialT", "combine2Derivatives",
  "massless", "diagonalCKM", "modelDigest"
};

(* Drift guard: if a new option is ever added to HEFTLHEFTCacheCompareKeys in lheft_cache.wl
   and not here, merging would stop checking it and would silently combine models that differ
   in it.  Say so loudly rather than let that happen. *)
HEFTMergeCheckKeys[] := Module[{expected, notChecked, notAKey},
  expected   = Complement[HEFTLHEFTCacheCompareKeys, {"operators"}];
  notChecked = Complement[expected, HEFTMergeGroupKeys];
  notAKey    = Complement[HEFTMergeGroupKeys, expected];
  If[notChecked =!= {} || notAKey =!= {},
    Print[Style["[HEFT merge] ERROR: HEFTMergeGroupKeys is out of sync with " <>
      "HEFTLHEFTCacheCompareKeys (lheft_cache.wl).", Red, Bold]];
    If[notChecked =!= {}, Print[Style["  cache keys not checked by the merge: " <>
      ToString[notChecked], Red]]];
    If[notAKey =!= {}, Print[Style["  merge keys that are not cache keys: " <>
      ToString[notAKey], Red]]];
    Print[Style["  Fix HEFTMergeGroupKeys in lheft_merge.wl before merging anything.",
      Red, Bold]];
    Abort[]
  ];
  True
];

HEFTMergeGroupHash[meta_Association] := IntegerString[
  Hash[Sort @ Normal @ KeyTake[meta, HEFTMergeGroupKeys], "MD5"], 16, 8
];

(* Which group keys two metas disagree on.  Used both to refuse a merge with a precise
   reason and to explain near-misses in the catalogue. *)
HEFTMergeDifferingKeys[a_Association, b_Association] := Select[
  HEFTMergeGroupKeys,
  Function[k,
    !KeyExistsQ[a, k] || !KeyExistsQ[b, k] || !HEFTLHEFTMetaValueEqual[a[k], b[k]]
  ]
];


(* ============================================================================
   Indexing the cache
   ============================================================================ *)

(* Scan every HEFT_cache/ subfolder and return the usable entries, plus the list of skipped
   ones with a reason.  Defensive on purpose: real caches contain a zero-byte meta.json next
   to a perfectly good .mx, and pre-2026-08-05 entries whose meta has no configHash at all.
   Local names avoid `dir`, `out`, `entry` and `ref`, which shadow FeynRules internals and
   produce ::shdw noise on every run. *)
HEFTMergeCacheIndex[] := Module[
  {cacheDir, cacheDirs, entries = {}, skipped = {}, entryPaths, stored, missingKeys},
  cacheDir  = HEFTLHEFTCacheDir[];
  cacheDirs = Sort @ Select[FileNames["*", cacheDir], DirectoryQ];
  Do[
    entryPaths = HEFTLHEFTCacheEntryPaths[d];
    Which[
      !FileExistsQ[entryPaths["mx"]],
        AppendTo[skipped, {FileNameTake[d], "no LHEFT.mx"}],
      !HEFTLHEFTCacheExistsQ[entryPaths["meta"], entryPaths["mx"]],
        AppendTo[skipped, {FileNameTake[d], "missing / empty / unparseable meta.json"}],
      True,
        stored = HEFTLHEFTReadMeta[entryPaths["meta"]];
        missingKeys = Select[Append[HEFTMergeGroupKeys, "operators"], !KeyExistsQ[stored, #] &];
        If[missingKeys =!= {},
          AppendTo[skipped, {FileNameTake[d],
            "legacy entry, meta.json has no " <> StringRiffle[missingKeys, ", "]}],
          AppendTo[entries, <|
            "folder"    -> FileNameTake[d],
            "dir"       -> d,
            "mx"        -> entryPaths["mx"],
            "meta"      -> entryPaths["meta"],
            "stored"    -> stored,
            "name"      -> ToString @ Lookup[stored, "outputName", "?"],
            "names"     -> Module[{n = Lookup[stored, "names", {}]},
                             If[ListQ[n], ToString /@ n, {}]],
            "operators" -> Sort @ Lookup[stored, "operators", {}],
            "groupHash" -> HEFTMergeGroupHash[stored],
            "builtAt"   -> ToString @ Lookup[stored, "builtAt", "?"],
            "seconds"   -> Lookup[stored, "buildSeconds", None]
          |>]
        ]
    ],
    {d, cacheDirs}
  ];
  <|"entries" -> entries, "skipped" -> skipped|>
];

(* The entries this configuration may be merged from: same group hash as the current config. *)
HEFTMergeCompatibleEntries[index_Association, meta_Association] := Module[{h},
  h = HEFTMergeGroupHash[meta];
  Select[index["entries"], #["groupHash"] === h &]
];

HEFTMergeOperatorSummary[ops_List] :=
  If[ops === {}, "(LO only - baseline)", StringRiffle[ops, ", "]];


(* ============================================================================
   Printing the catalogue
   ============================================================================ *)

HEFTMergePrintCatalog[index_Association, meta_Association] := Module[
  {compatible, rest, rows, nearMiss, header, loEntry},

  compatible = HEFTMergeCompatibleEntries[index, meta];
  rest = Complement[index["entries"], compatible];

  Print[Style["\n  Cached models matching this configuration (group " <>
    HEFTMergeGroupHash[meta] <> ")", Bold, FontSize -> 14]];

  If[compatible === {},
    Print[Style["    None. Nothing in HEFT_cache/ was built with this exact configuration.",
      Bold, Darker[Red]]];
    Print[Style["    Build the sub-models first with heft_fr_notebook.wl, using these very " <>
      "settings and one operator selection each.", Darker[Red]]],

    header = {"#", "name", "operators", "built", "s", "folder"};
    rows = MapIndexed[
      Function[{e, i},
        {ToString @ First[i], e["name"], HEFTMergeOperatorSummary[e["operators"]],
         e["builtAt"],
         If[NumericQ[e["seconds"]], ToString @ Round[e["seconds"]], "?"],
         e["folder"]}],
      compatible
    ];
    Print @ Grid[
      Prepend[rows, Style[#, Bold] & /@ header],
      Alignment -> Left,
      Dividers -> {False, {False, True, {False}}},
      Spacings -> {2, 0.4},
      ItemStyle -> Directive[FontFamily -> "Monospace", FontSize -> 11]
    ];
    Print[Style["    Select with the name column (or the folder column when a name is " <>
      "ambiguous).", Gray]];

    loEntry = SelectFirst[compatible, #["operators"] === {} &, None];
    If[loEntry === None,
      Print[Style["\n    No LO baseline in this group. Merging needs one: build once with " <>
        "NLOOperators = {} and everything else exactly as configured here.", Bold, Darker[Red]]],
      Print[Style["    LO baseline present: \"" <> loEntry["name"] <> "\".", Darker[Green]]]
    ]
  ];

  (* Near-misses are the useful part of the rest: an entry that differs in exactly one key is
     almost always a sub-model built before a .fr edit (modelDigest) or with one option
     flipped by accident. Naming the key saves a long hunt. *)
  If[rest =!= {},
    nearMiss = Select[
      {#, HEFTMergeDifferingKeys[#["stored"], meta]} & /@ rest,
      Length[Last[#]] <= 2 &
    ];
    Print[Style["\n  Other cache entries: " <> ToString[Length[rest]] <>
      " (not mergeable with this configuration)", Bold]];
    If[nearMiss =!= {},
      Print[Style["    Close matches, and the key(s) they differ in:", Gray]];
      Print @ Grid[
        Function[nm, {"      " <> nm[[1]]["folder"],
                      HEFTMergeOperatorSummary[nm[[1]]["operators"]],
                      StringRiffle[nm[[2]], ", "]}] /@ Take[nearMiss, UpTo[12]],
        Alignment -> Left, Spacings -> {2, 0.3},
        ItemStyle -> Directive[FontFamily -> "Monospace", FontSize -> 10]
      ];
      If[Length[nearMiss] > 12,
        Print[Style["      ... and " <> ToString[Length[nearMiss] - 12] <> " more.", Gray]]
      ]
    ]
  ];

  If[index["skipped"] =!= {},
    Print[Style["\n  Skipped " <> ToString[Length[index["skipped"]]] <>
      " cache folder(s):", Gray]];
    Do[Print[Style["      " <> s[[1]] <> "  -  " <> s[[2]], Gray]], {s, index["skipped"]}]
  ];

  compatible
];


(* ============================================================================
   Resolving user-supplied names
   ============================================================================ *)

(* A name may be the OutputName, any alias in the entry's "names" list, or the folder name
   <OutputName>__<configHash>.  Within one merge group an OutputName can still be ambiguous
   (the same name built twice with different operator selections), so an ambiguous match is
   refused with the folder names to use instead - never silently resolved. *)
HEFTMergeResolveSource[spec_String, compatible_List] := Module[{hits},
  hits = Select[compatible,
    #["folder"] === spec || #["name"] === spec || MemberQ[#["names"], spec] &];
  Which[
    Length[hits] === 1, First[hits],
    hits === {},
      Print[Style["[HEFT merge] ERROR: no cached model called \"" <> spec <>
        "\" in this configuration group.", Red, Bold]];
      Print[Style["  Available: " <>
        StringRiffle[DeleteDuplicates[#["name"] & /@ compatible], ", "], Red]];
      $Failed,
    True,
      Print[Style["[HEFT merge] ERROR: \"" <> spec <> "\" is ambiguous - " <>
        ToString[Length[hits]] <> " entries in this group carry that name.", Red, Bold]];
      Print[Style["  Use the folder name instead:", Red]];
      Do[Print[Style["    " <> h["folder"] <> "   " <>
        HEFTMergeOperatorSummary[h["operators"]], Red]], {h, hits}];
      $Failed
  ]
];


(* ============================================================================
   Loading a cached Lagrangian without clobbering the previous one
   ============================================================================ *)

(* lheft_cache.wl writes the .mx with DumpSave[path, "LHEFT"], i.e. it saves the symbol LHEFT
   itself.  Every Get therefore overwrites whatever LHEFT currently holds - including the one
   just loaded from the previous source, and including the merged result.  Clear before and
   after, and hand the expression back by value. *)
HEFTMergeGetLHEFT[entry_Association] := Module[{res},
  Clear[LHEFT];
  Get[entry["mx"]];
  If[!ValueQ[LHEFT],
    Print[Style["[HEFT merge] ERROR: " <> entry["mx"] <> " did not define LHEFT.", Red, Bold]];
    Abort[]
  ];
  res = LHEFT;
  Clear[LHEFT];
  res
];

HEFTMergeTermList[expr_] := Module[{e},
  e = Expand[expr];
  Which[Head[e] === Plus, List @@ e, e === 0, {}, True, {e}]
];


(* ============================================================================
   The merge
   ============================================================================ *)

(* loExpr   the LO-only Lagrangian (the cached build with NLOOperators = {})
   sources  {{label, expr}, ...} for the sub-models to merge

       merged = sum_i L_i - (N - 1) * L_LO

   which is L_LO + sum_i (L_i - L_LO) rearranged so that no expression is ever subtracted
   from itself term by term - see the header for why term matching is the wrong tool here.

   Nothing cancels syntactically, so the result is larger than a directly built Lagrangian;
   the term and leaf counts printed below make that visible rather than surprising. *)
HEFTMergeLagrangians[loExpr_, sources_List] := Module[{merged, nSrc, report = {}},

  nSrc = Length[sources];
  Print["    ", Style[StringPadRight["LO baseline", 38], Bold],
    Length[HEFTMergeTermList[loExpr]], " terms"];

  Do[
    Print["    ", Style[StringPadRight[src[[1]], 38], Bold],
      Length[HEFTMergeTermList[src[[2]]]], " terms"];
    AppendTo[report, <|"label" -> src[[1]],
      "terms" -> Length[HEFTMergeTermList[src[[2]]]]|>],
    {src, sources}
  ];

  merged = Plus @@ (Last /@ sources) - (nSrc - 1) * loExpr;

  Print["    ", Style[StringPadRight["merged", 38], Bold],
    Length[HEFTMergeTermList[merged]], " terms, LeafCount ", LeafCount[merged]];
  If[nSrc > 1,
    Print[Style["    (" <> ToString[nSrc - 1] <> " x the LO baseline subtracted, so the SM " <>
      "sector is counted exactly once)", Gray]]
  ];

  <|"lagrangian" -> merged,
    "terms"      -> Length[HEFTMergeTermList[merged]],
    "loTerms"    -> Length[HEFTMergeTermList[loExpr]],
    "report"     -> report|>
];


(* ============================================================================
   Guards
   ============================================================================ *)

(* Refuse rather than warn.  Every one of these produces a model that looks fine and is
   quietly wrong, which is the failure mode this whole file exists to avoid. *)
HEFTMergeValidate[compatible_List, specs_List, meta_Association] := Module[
  {resolved, loEntry, ops, dupes},

  If[!TrueQ[NumericQ[HEFTMaxOrder]] || HEFTMaxOrder > 1,
    Print[Style["[HEFT merge] ERROR: merging is exact only at linear order in ChiralOrder, " <>
      "but HEFTMaxOrder = " <> ToString[HEFTMaxOrder] <> ".", Red, Bold]];
    Print[Style["  At HEFTMaxOrder >= 2 the gauge normalisations (eps is a product, the " <>
      "kinetic diagonal is Wnorm^2 P12norm^2) and the EW input scheme mix operators " <>
      "non-linearly, so a build with one operator has different physical fields than a " <>
      "build with two. No merge of separately built models recovers the cross terms.", Red]];
    Print[Style["  Use HEFTMaxOrder = 1, or build the full model directly with " <>
      "heft_fr_notebook.wl.", Red, Bold]];
    Return[$Failed]
  ];

  If[specs === {},
    Print[Style["[HEFT merge] ERROR: MergeSources is empty - nothing to merge. " <>
      "Take the names from the table printed by Cell 3.", Red, Bold]];
    Return[$Failed]
  ];

  loEntry = SelectFirst[compatible, #["operators"] === {} &, None];
  If[loEntry === None,
    Print[Style["[HEFT merge] ERROR: no LO baseline (a cached build with " <>
      "NLOOperators = {}) in this configuration group.", Red, Bold]];
    Print[Style["  Every sub-model contains the whole LO Lagrangian, so merging N of them " <>
      "without subtracting LO gives N x LO and every SM vertex is scaled by N.", Red]];
    Print[Style["  Build it once in heft_fr_notebook.wl with NLOOperators = {} and exactly " <>
      "the configuration set in Cell 2 here. It is the cheapest build there is, and one " <>
      "serves every merge in this group.", Red, Bold]];
    Return[$Failed]
  ];

  resolved = HEFTMergeResolveSource[#, compatible] & /@ specs;
  If[MemberQ[resolved, $Failed], Return[$Failed]];

  If[Length[DeleteDuplicates[#["folder"] & /@ resolved]] =!= Length[resolved],
    Print[Style["[HEFT merge] ERROR: the same cache entry is listed more than once in " <>
      "MergeSources. Its operators would be counted twice.", Red, Bold]];
    Return[$Failed]
  ];

  If[MemberQ[resolved, loEntry],
    Print[Style["[HEFT merge] Note: the LO baseline is also listed in MergeSources. It is " <>
      "the baseline and contributes nothing on top of itself; dropping it.", Orange]];
    resolved = DeleteCases[resolved, loEntry]
  ];

  If[resolved === {},
    Print[Style["[HEFT merge] ERROR: nothing left to merge after dropping the LO baseline.",
      Red, Bold]];
    Return[$Failed]
  ];

  (* An operator appearing in two sub-models would contribute twice.  Its coefficients are
     the same symbols in both, so the result is a factor-2 error on exactly those vertices -
     invisible unless you go looking. *)
  ops = #["operators"] & /@ resolved;
  dupes = Select[Tally[Join @@ ops], Last[#] > 1 &][[All, 1]];
  If[dupes =!= {},
    Print[Style["[HEFT merge] ERROR: operator(s) present in more than one selected " <>
      "sub-model: " <> StringRiffle[dupes, ", "], Red, Bold]];
    Print[Style["  Each would be added once per sub-model that carries it. Split the " <>
      "selection so every operator appears exactly once.", Red]];
    Return[$Failed]
  ];

  <|"lo" -> loEntry, "sources" -> resolved, "operators" -> Sort[Join @@ ops]|>
];
