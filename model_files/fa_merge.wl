(* ::Package:: *)

(* FeynArts model merging.  Get'd by heft_fr_merge.wl for merge notebook Cells 9 (list the
   exports) and 10 (merge them).  Needs lheft_cache.wl and lheft_merge.wl (loaded by
   HEFT$MergeBootstrap[]) and heft_export_meta.wl (loaded below).

   WHAT THIS DOES
   Builds output/FeynArts/<OutputName>/ out of FeynArts exports already on disk, with no
   FeynRules and no LoadModel.  At one Wilson-coefficient insertion every coupling is linear in
   the coefficients, so for sub-models A_1..A_N and the SM-only baseline LO, for every C[fields]

       C(A_1 u ... u A_N)  =  C(LO) + Sum_i ( C(A_i) - C(LO) )

   - the identity lheft_merge.wl uses for the Lagrangian, applied one step further down the
   pipeline.  The point is cost: an export takes roughly terms^2.16 (AGENTS.md, 2026-08-19/20),
   so N small exports are far cheaper than one big one, and the full-model FeynArts export never
   finished at all (18 h, 2026-08-22).

   WHY FEYNARTS NEEDS MORE THAN ADDITION
   1. A coupling vector {{c1, ct1}, {c2, ct2}, ...} is positional: row k multiplies the k-th
      kinematic structure of its generic class (FFS, SSSS, VVV, ...) in the model's OWN .gen,
      and FeynRules writes only the structures that model uses (PDH, for instance, adds momentum
      structures to SSSS).  Every vector is therefore re-mapped onto the union of the bases first.
   2. The gc<n> abbreviations of M$FACouplings are numbered per export.  They are renamed
      gcm<k>, one name per distinct definition, so the same abbreviation carries the same name in
      every export and identical SM entries cancel syntactically when the baseline is subtracted.
   3. Unlike UFO, FeynArts does not split a vertex by coupling order: SM and EFT pieces share one
      entry, so the baseline is subtracted from every coupling.
   .pars is NOT a physics merge: FeynArts reads only .mod and .gen, and .pars holds FeynRules'
   numerical defaults.  Its lists are united, the baseline's value winning on a conflict.

   EVERYTHING IS READ INTO A PRIVATE CONTEXT (HEFTFAModel`) with only System` visible.  After
   Cell 5 FeynRules is loaded in the merge kernel, and its IndexDelta / IndexSum have
   definitions; read into Global` or FeynRules`, the exported expressions could evaluate during
   the merge arithmetic.  In the private context nothing in them has a definition.

   WHAT IS REFUSED (not warned about)
   - an export without heft_export.json, or whose record differs from the Cell 2 configuration
     in any hashed option, modelDigest, MaxVertexLegs or the FeynArts-interface digest;
   - exports in different fermion forms (index-free vs explicit Dirac indices, recorded as
     diracIndices in heft_export.json);
   - no SM baseline, or several without MergeFeynArtsBaseline naming one;
   - an operator in two sources, a source listed twice, OutputName equal to an input;
   - exports that differ outside the couplings (particles, indices, propagators, generic rules),
     declare a generic class differently, or write one vertex with its fields in a different
     order;
   - a baseline vertex missing from a sub-model export. *)

Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_export_meta.wl"}]];

HEFTFA$Ctx = "HEFTFAModel`";
HEFTFASym[name_String] := Symbol[HEFTFA$Ctx <> name];

HEFTFAError[msg_String] := (Print[Style["[HEFT FA merge] ERROR: " <> msg, Red, Bold]]; Abort[]);

HEFTFAExportsDir[] := FileNameJoin[{HEFT$WorkspaceRoot, "output", "FeynArts"}];

(* Written with the private context on the path, so names come out unqualified. *)
HEFTFAToString[e_] := Block[{$Context = HEFTFA$Ctx, $ContextPath = {HEFTFA$Ctx, "System`"}},
  ToString[e, InputForm]
];


(* ============================================================================
   Index of the exports (Cell 9) and resolving names (Cell 10)
   ============================================================================ *)

HEFTFAExportIndex[] := Module[{faDir = HEFTFAExportsDir[], dirs, entries = {}, noMeta = {}, m},
  dirs = If[DirectoryQ[faDir], Sort @ Select[FileNames["*", faDir], DirectoryQ], {}];
  Do[
    m = HEFTExportReadMeta[d];
    If[m === None || Lookup[m, "format", None] =!= "feynarts",
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

HEFTFACompatible[index_Association, current_Association] :=
  Select[index["entries"], HEFTExportDifferingKeys[#["meta"], current, "feynarts"] === {} &];

HEFTFAPrintCatalog[index_Association, current_Association] := Module[
  {compatible, rest, nearMiss, lo},
  compatible = HEFTFACompatible[index, current];
  rest = Complement[index["entries"], compatible];

  Print[Style["\n  FeynArts exports matching this configuration (MaxVertexLegs = " <>
    ToString[current["maxVertexLegs"]] <> ")", Bold, FontSize -> 14]];
  If[compatible === {},
    Print[Style["    None. Export the sub-models first with heft_fr_notebook.wl (Cells 5 and 8), " <>
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
          StringRiffle[#["name"] & /@ lo, ", "] <> "): name one in MergeFeynArtsBaseline, Cell 10.",
          Orange]]
    ]
  ];

  (* Near-misses: an export that differs in one or two keys is almost always one made before
     a .fr edit (modelDigest) or with a different MaxVertexLegs. *)
  If[rest =!= {},
    nearMiss = Select[{#, HEFTExportDifferingKeys[#["meta"], current, "feynarts"]} & /@ rest,
      Length[Last[#]] <= 2 &];
    Print[Style["\n  Other FeynArts exports with a record: " <> ToString[Length[rest]] <>
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
    Print[Style["\n  " <> ToString[Length[index["noMeta"]]] <> " export folder(s) without " <>
      "heft_export.json (exported before it existed) - re-export them to merge them: " <>
      StringRiffle[index["noMeta"], ", "], Gray]]
  ];

  compatible
];

HEFTFAResolve[spec_, index_Association, compatible_List, current_Association] := Module[{hit, other},
  If[!StringQ[spec], HEFTFAError["MergeFeynArtsSources must list export names as strings; got " <>
    ToString[spec, InputForm] <> "."]];
  hit   = SelectFirst[compatible, #["name"] === spec &, None];
  other = SelectFirst[index["entries"], #["name"] === spec &, None];
  Which[
    hit =!= None, hit,
    other =!= None, HEFTFAError["\"" <> spec <> "\" was exported with a different " <>
      StringRiffle[HEFTExportDifferingKeys[other["meta"], current, "feynarts"], ", "] <>
      " than the configuration in Cell 2."],
    MemberQ[index["noMeta"], spec], HEFTFAError["\"" <> spec <> "\" has no heft_export.json " <>
      "(exported before export records existed): re-export it with Cell 8."],
    True, HEFTFAError["no FeynArts export called \"" <> spec <> "\" in " <> HEFTFAExportsDir[] <>
      ". Cell 9 lists the ones available."]
  ]
];

HEFTFAFindBaseline[compatible_List, spec_] := Module[{lo, hit},
  lo = Select[compatible, #["operators"] === {} &];
  If[StringQ[spec],
    hit = SelectFirst[lo, #["name"] === spec &, None];
    If[hit === None, HEFTFAError["MergeFeynArtsBaseline = \"" <> spec <> "\" is not an SM-only " <>
      "export of this configuration."]];
    hit,
    Which[
      lo === {}, HEFTFAError["no SM baseline. Export once with EFTOperators = {} and everything " <>
        "else as configured in Cell 2: every sub-model carries the whole SM, so without " <>
        "subtracting it N sub-models give N x SM."],
      Length[lo] > 1, HEFTFAError["several SM baselines match (" <>
        StringRiffle[#["name"] & /@ lo, ", "] <> "): set MergeFeynArtsBaseline to one of them."],
      True, First[lo]
    ]
  ]
];


(* ============================================================================
   Step 1 - reading an export without evaluating it
   ============================================================================ *)

(* Every top-level statement, unevaluated.  ReadList rather than Import[..., "HeldExpressions"]:
   Import picks the format from the extension, and .mod / .gen / .pars are not Wolfram formats.
   ReadList parses with the current $Context / $ContextPath, which the Block sets.  A statement
   ending in ";" is read as CompoundExpression[stmt, Null]; it is unwrapped so one pattern finds
   both  x = {...}  and  x = {...}; . *)
HEFTFAReadHeld[file_String] := Replace[
  Block[{$Context = HEFTFA$Ctx, $ContextPath = {"System`"}}, ReadList[file, Hold[Expression]]],
  Hold[CompoundExpression[e_, Null]] :> Hold[e],
  {1}
];

(* The right-hand side of the single top-level  name = rhs  in a held file, evaluated (in the
   private context nothing in it has a definition, so evaluation only tidies arithmetic). *)
HEFTFAGetSet[held_, name_String, file_String] := Module[{sym = HEFTFASym[name], hits},
  If[!ListQ[held], HEFTFAError["could not read " <> file <> "."]];
  hits = Cases[held,
    Hold[Set[s_, rhs_]] /; SameQ[Unevaluated[s], sym] :> Hold[rhs]];
  If[Length[hits] =!= 1, HEFTFAError["expected one " <> name <> " = ... in " <> file <>
    ", found " <> ToString[Length[hits]] <> "."]];
  ReleaseHold[First[hits]]
];

(* "FFS", "SSVV", ... - the field types of a coupling in written order, which is also how the
   .gen names its generic classes. *)
HEFTFAStripSign[f_] := Replace[f, Times[-1, g_] :> g];
HEFTFAFieldClass[fields_List] := StringJoin[(SymbolName @* Head @* HEFTFAStripSign) /@ fields];
HEFTFAGenericField[a_] := Replace[a, HoldPattern[Times[_Symbol, g : _[___]]] :> g];   (* s1 F[j1,...] -> F[...] *)

(* A vertex by its field content alone (signs kept, indices dropped): two exports writing one
   vertex with its fields in a different order give two keys with the same signature. *)
HEFTFAFieldSignature[c_C] := Sort[(# /. h_[n_Integer, _List] :> h[n]) & /@ (List @@ c)];

HEFTFATextBefore[s_String, marker_String, file_String] := With[{p = StringPosition[s, marker, 1]},
  If[p === {}, HEFTFAError[marker <> " not found in " <> file <> "."]];
  StringTake[s, p[[1, 1]] - 1]
];
HEFTFATextFrom[s_String, marker_String, file_String] := With[{p = StringPosition[s, marker, 1]},
  If[p === {}, HEFTFAError[marker <> " not found in " <> file <> "."]];
  StringDrop[s, p[[1, 1]] - 1]
];

(* The one selection-dependent line outside the couplings: FeynArtsInterface.m (line 573) writes
   $FermionLines = True only when no vertex has more than two fermions, so an SM baseline says
   True and any four-fermion export False.  It is taken out of the text compared in Step 2, and
   the merged .gen gets False as soon as one export has it False. *)
HEFTFA$FermionLinesPattern = "$FermionLines = " ~~ ("True" | "False") ~~ ";";
HEFTFA$FermionLinesSlot    = "$FermionLines = `FermionLines`;";

HEFTFAReadExport[entry_Association] := Module[
  {exportDir = entry["dir"], paths, text, modHeld, genHeld, parsHeld, cm, gg, couplings, generic,
   genHead, fermionLines},
  paths = AssociationMap[
    Function[ext, With[{hits = FileNames["*." <> ext, exportDir]},
      If[Length[hits] =!= 1, HEFTFAError[entry["name"] <> " must hold exactly one ." <> ext <>
        " file; it holds " <> ToString[Length[hits]] <> "."]];
      First[hits]]],
    {"mod", "gen", "pars"}
  ];
  text     = ReadString /@ paths;
  modHeld  = HEFTFAReadHeld[paths["mod"]];
  genHeld  = HEFTFAReadHeld[paths["gen"]];
  parsHeld = HEFTFAReadHeld[paths["pars"]];

  cm = HEFTFAGetSet[modHeld, "M$CouplingMatrices", paths["mod"]];
  gg = HEFTFAGetSet[genHeld, "M$GenericCouplings", paths["gen"]];
  couplings = Association @ Cases[cm, HoldPattern[Equal[c_C, rows_List]] :> (c -> rows)];
  generic = Association @ Cases[gg,
    HoldPattern[Equal[lhs : _[args__], Dot[g_, basis_List]]] :> (
      HEFTFAFieldClass[HEFTFAGenericField /@ {args}] -> <|"lhs" -> lhs, "g" -> g, "basis" -> basis|>)];
  If[Length[couplings] =!= Length[cm] || Length[generic] =!= Length[gg],
    HEFTFAError["unrecognised coupling layout in " <> entry["name"] <> " (" <>
      ToString[Length[couplings]] <> "/" <> ToString[Length[cm]] <> " couplings, " <>
      ToString[Length[generic]] <> "/" <> ToString[Length[gg]] <> " generic classes read)."]];
  If[!AllTrue[Values[couplings], MatchQ[#, {{_, _} ..}] &],
    HEFTFAError[entry["name"] <> ": a coupling vector is not a list of {tree, counterterm} pairs."]];

  genHead = HEFTFATextBefore[text["gen"], "M$GenericCouplings", paths["gen"]];
  fermionLines = StringCases[genHead, "$FermionLines = " ~~ v : ("True" | "False") ~~ ";" :> v];
  If[Length[fermionLines] =!= 1, HEFTFAError[entry["name"] <> ": expected one $FermionLines " <>
    "setting in the .gen, found " <> ToString[Length[fermionLines]] <> "."]];

  Join[entry, <|
    "couplings" -> couplings,
    "generic"   -> generic,
    "gc"        -> HEFTFAGetSet[modHeld, "M$FACouplings", paths["mod"]],
    "pars"      -> AssociationMap[
                     Association @ HEFTFAGetSet[parsHeld, "M$" <> #, paths["pars"]] &,
                     {"ExtParams", "Masses", "Widths", "IntParams"}],
    "modHead"   -> HEFTFATextBefore[text["mod"], "M$CouplingMatrices", paths["mod"]],
    "genHead"   -> StringReplace[genHead, HEFTFA$FermionLinesPattern -> HEFTFA$FermionLinesSlot],
    "genTail"   -> HEFTFATextFrom[text["gen"], "(* FlippingRules", paths["gen"]],
    "fermionLines" -> (First[fermionLines] === "True")
  |>]
];


(* ============================================================================
   Step 2 - the exports must come from the same model, written the same way
   ============================================================================ *)

(* models: baseline first. *)
HEFTFACheckStructure[models_List] := Module[{lo = First[models], where, classes, sigs, bad},
  where = <|"modHead" -> ".mod (particles, indices, definitions)",
            "genHead" -> ".gen (kinematic indices, propagators)",
            "genTail" -> ".gen (flipping / truncation rules)"|>;
  Do[
    If[m[k] =!= lo[k], HEFTFAError[m["name"] <> ": its " <> where[k] <> " differs from the " <>
      "baseline " <> lo["name"] <> "'s. The exports do not come from the same model."]],
    {m, Rest[models]}, {k, Keys[where]}
  ];
  classes = DeleteDuplicates @ Flatten[Keys[#["generic"]] & /@ models];
  (* The sign of G[+-1] is not compared: FeynRules derives it from the class's structures
     (HEFTFAGenericSign), so a CP-even and a CP-odd export legitimately differ in it.  What is
     checked is that every export follows that rule, and the merged class gets the sign the rule
     gives for the union basis (HEFTFAWriteGen) - what a direct export would write. *)
  Do[
    If[Length @ DeleteDuplicates[{#["generic"][cls]["lhs"], HEFTFAGSignFree[#["generic"][cls]["g"]]} & /@
          Select[models, KeyExistsQ[#["generic"], cls] &]] > 1,
      HEFTFAError["generic class " <> cls <> " is declared differently in two exports."]],
    {cls, classes}
  ];
  Do[
    If[HEFTFAGSign[m["generic"][cls]["g"]] =!= HEFTFAGenericSign[cls, m["generic"][cls]["basis"]],
      HEFTFAError[m["name"] <> ": generic class " <> cls <> " has G[" <>
        ToString[HEFTFAGSign[m["generic"][cls]["g"]]] <> "], not the sign FeynRules gives it " <>
        "(FeynArtsInterface.m: -1 iff a fermion or an Eps).  The FeynRules version may differ."]],
    {m, models}, {cls, Keys[m["generic"]]}
  ];
  sigs = GroupBy[DeleteDuplicates @ Flatten[Keys[#["couplings"]] & /@ models], HEFTFAFieldSignature];
  bad  = Select[sigs, Length[#] > 1 &];
  If[bad =!= <||>, HEFTFAError["one vertex is written with its fields in different orders in " <>
    "two exports: " <> StringRiffle[HEFTFAToString /@ First[Values[bad]], "  vs  "] <> "."]];
];


(* ============================================================================
   Step 3 - union of the generic bases, and every coupling vector re-mapped onto it
   ============================================================================ *)

(* Per class: the baseline's structures first (models are passed baseline first), then each
   new one in order of appearance.  Structures are compared literally, so one written in two
   index orders would appear twice - a redundant row, not a wrong one. *)
(* FeynRules writes G[-1] for a generic class that has a fermion or any structure with Eps
   (LeviCivita in the .gen), G[+1] otherwise (FeynArtsInterface.m:781-782). *)
HEFTFAGSign[g_] := Replace[g, {_[s_][___] :> s, _ :> None}];
HEFTFAGSignFree[g_] := Replace[g, h_[_][args___] :> h[args]];
HEFTFAGenericSign[cls_String, basis_List] :=
  If[StringContainsQ[cls, "F"] || !FreeQ[basis, s_Symbol /; SymbolName[s] === "LeviCivita"], -1, 1];

HEFTFAUnionBases[models_List] := Merge[#["generic"][[All, "basis"]] & /@ models,
  DeleteDuplicates @* Apply[Join]];

HEFTFARemap[couplings_Association, generic_Association, union_Association, name_String] :=
  Association @ KeyValueMap[
    Function[{c, rows}, Module[{cls = HEFTFAFieldClass[List @@ c], basis, idx, new},
      If[!KeyExistsQ[generic, cls], HEFTFAError[name <> ": no generic class " <> cls <>
        " for " <> HEFTFAToString[c] <> "."]];
      basis = generic[cls]["basis"];
      If[Length[rows] =!= Length[basis], HEFTFAError[name <> ": " <> HEFTFAToString[c] <> " has " <>
        ToString[Length[rows]] <> " rows, its class " <> cls <> " has " <>
        ToString[Length[basis]] <> " structures."]];
      idx = PositionIndex[union[cls]];
      new = ConstantArray[{0, 0}, Length[union[cls]]];
      new[[First[idx[#]] & /@ basis]] = rows;
      c -> new
    ]],
    couplings
  ];


(* ============================================================================
   Step 4 - one name per abbreviation definition
   ============================================================================ *)

(* A gc<n> is identified by its argument patterns and its right-hand side, not by its number.
   The renaming is one ReplaceAll pass per export, so no rename can cascade into another. *)
HEFTFAGCKey[r : (_Rule | _RuleDelayed)] := {Replace[First[r], {_[args___] :> {args}, _ :> None}], Last[r]};
HEFTFAGCHead[r : (_Rule | _RuleDelayed)] := Replace[First[r], h_[___] :> h];

(* The table is keyed by the definition's printed form: a string key cannot be defeated by any
   subtlety of expression identity, and a lookup that still fails aborts instead of writing a
   Missing[...] into the merged .mod (which is what the first T1 run of 2026-09-29 produced). *)
HEFTFAGCKeyString[r_] := HEFTFAToString[HEFTFAGCKey[r]];

HEFTFAAbbreviations[models_List] := Module[{keys, names, rename, lookup},
  keys  = DeleteDuplicates @ Flatten[Map[HEFTFAGCKey, #["gc"]] & /@ models, 1];
  names = AssociationThread[(HEFTFAToString /@ keys) ->
    Table[HEFTFASym["gcm" <> ToString[k]], {k, Length[keys]}]];
  lookup = Function[{r}, Lookup[names, HEFTFAGCKeyString[r],
    HEFTFAError["internal: no merged name for the abbreviation " <> HEFTFAToString[r] <> "."]]];
  rename = Map[
    Function[{model}, Thread[Map[HEFTFAGCHead, model["gc"]] -> Map[lookup, model["gc"]]]],
    models];
  <|"rename" -> rename,
    "rules"  -> MapThread[(If[#1[[1]] === None, #2, #2 @@ #1[[1]]] -> #1[[2]]) &,
                  {keys, Lookup[names, HEFTFAToString /@ keys]}]|>
];


(* ============================================================================
   Step 5 - the merge
   ============================================================================ *)

(* For every C[fields] in any export: LO + Sum_i (C_i - LO), entry by entry, then Expand so
   identical terms cancel.  A vertex absent from a sub-model contributes 0 (C_i = 0 there).  A
   baseline vertex absent from a sub-model is refused instead: it would mean an operator
   cancelled an SM vertex exactly, which is not physics but a broken or cut export.  A vertex
   whose merged vector vanishes is dropped. *)
HEFTFAMergeCouplings[lo_Association, subs_List, union_Association] := Module[
  {keys, zero, loRows, total, merged = {}, nDropped = 0},
  keys = DeleteDuplicates @ Join[Keys[lo], Flatten[Keys /@ subs]];
  Do[
    If[KeyExistsQ[lo, c] && !AllTrue[subs, KeyExistsQ[#, c] &],
      HEFTFAError["the baseline vertex " <> HEFTFAToString[c] <> " is missing from a sub-model export."]];
    zero   = ConstantArray[{0, 0}, Length @ union[HEFTFAFieldClass[List @@ c]]];
    loRows = Lookup[lo, Key[c], zero];
    total  = Map[Expand, loRows + Total[(Lookup[#, Key[c], zero] - loRows) & /@ subs], {2}];
    If[AllTrue[Flatten[total], # === 0 &], nDropped++, AppendTo[merged, c -> total]],
    {c, keys}
  ];
  <|"couplings" -> merged, "dropped" -> nDropped|>
];


(* ============================================================================
   Step 6 - .pars: lists united (bookkeeping, not physics)
   ============================================================================ *)

HEFTFAMergeParLists[models_List] := Module[{out = <||>, warn = {}, acc, new},
  Do[
    acc = Lookup[out, k, <||>];
    new = m["pars"][k];
    KeyValueMap[
      Function[{p, v}, If[KeyExistsQ[acc, p] && !TrueQ[acc[p] == v],
        AppendTo[warn, {k, p, m["name"]}]]],
      new];
    out[k] = Join[new, acc],                       (* acc last: earlier (baseline) values win *)
    {m, models}, {k, {"ExtParams", "Masses", "Widths", "IntParams"}}
  ];
  out["ExtParams"] = KeySortBy[out["ExtParams"], ToLowerCase @* SymbolName];
  If[warn =!= {},
    Print[Style["[HEFT FA merge] " <> ToString[Length[warn]] <> " .pars value(s) differ between " <>
      "exports; the baseline's value was kept (FeynArts itself does not read .pars). First ones: " <>
      HEFTFAToString[Take[warn, UpTo[5]]], Orange]]
  ];
  out
];


(* ============================================================================
   Step 7 - writing the merged model
   ============================================================================ *)

(* Everything outside the coupling lists is the baseline's text verbatim - Step 2 checked it is
   identical in every export. *)
HEFTFAWriteMod[file_String, head_String, couplings_List, gcRules_List] := Export[file, StringJoin[
  head, "M$CouplingMatrices = {\n\n",
  StringRiffle[HEFTFAToString[Equal @@ #] & /@ couplings, ",\n\n"],
  "\n\n}\n\n(* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *)\n\n",
  "(* Parameter replacement lists (merged by HEFT from FeynRules-generated exports) *)\n\n",
  "(* FA Couplings *)\n\nM$FACouplings = {\n     ",
  StringRiffle[HEFTFAToString /@ gcRules, ",\n     "], "};\n"
], "Text"];

HEFTFAWriteGen[file_String, head_String, tail_String, union_Association, generic_Association] :=
  Export[file, StringJoin[
    head, "M$GenericCouplings = {\n",
    StringRiffle[KeyValueMap[
      Function[{cls, basis}, "\n\t (* " <> cls <> " *)\n\n" <>
        HEFTFAToString[Equal[generic[cls]["lhs"], Dot[
          Replace[generic[cls]["g"], h_[_][args___] :> h[HEFTFAGenericSign[cls, basis]][args]],
          basis]]]],
      KeySort[union]], ",\n"],
    "\n}\n\n", tail
  ], "Text"];

HEFTFAWritePars[file_String, pars_Association] := Export[file, StringJoin[
  "(***********************************************)\n",
  "(*   Parameter file merged by HEFT from FeynRules-generated exports   *)\n",
  "(***********************************************)\n\n",
  Table["M$" <> k <> " = {\n\t" <> StringRiffle[HEFTFAToString /@ Normal[pars[k]], ",\n\t"] <>
    "\n};\n\n", {k, {"ExtParams", "Masses", "Widths", "IntParams"}}]
], "Text"];


(* ============================================================================
   Driver - merge notebook Cell 10
   ============================================================================ *)

HEFTFAMergeRun[sourceNames_List, outName_String, baselineSpec_] := Module[
  {t0 = AbsoluteTime[], current, index, compatible, lo, subs, names, ops, dup, models, union,
   generic, abbr, remapped, res, outDir, grown},

  current    = HEFTExportCurrentMeta["feynarts"];
  index      = HEFTFAExportIndex[];
  compatible = HEFTFACompatible[index, current];

  If[!DuplicateFreeQ[sourceNames], HEFTFAError["a name is listed twice in MergeFeynArtsSources."]];
  lo   = HEFTFAFindBaseline[compatible, baselineSpec];
  subs = HEFTFAResolve[#, index, compatible, current] & /@ sourceNames;
  If[MemberQ[#["name"] & /@ subs, lo["name"]],
    Print[Style["[HEFT FA merge] " <> lo["name"] <> " is the SM baseline; it is subtracted " <>
      "automatically and was dropped from the sources.", Gray]];
    subs = Select[subs, #["name"] =!= lo["name"] &]
  ];
  If[subs === {}, HEFTFAError["no sub-model left to merge."]];
  (* One fermion form for all: FeynRules writes index-free chains unless a vertex has more than
     two fermions, explicit Dirac indices otherwise, and the two cannot be added.  Under the default
     FeynArtsDiracIndices = Automatic an SM-only baseline is index-free, so this refuses any merge
     with a four-fermion export; with FeynArtsDiracIndices = True for every export (Cell 8,
     2026-10-13) all are explicit and the merge proceeds. *)
  With[{forms = DeleteDuplicates[Lookup[#["meta"], "diracIndices", "unknown"] & /@ Prepend[subs, lo]]},
    If[Length[forms] > 1, HEFTFAError["the exports mix fermion forms (index-free and explicit " <>
      "Dirac indices: " <> StringRiffle[(#["name"] <> "=" <> ToString[Lookup[#["meta"],
      "diracIndices", "unknown"]]) & /@ Prepend[subs, lo], ", "] <> "). FeynRules writes " <>
      "explicit indices only for models with four-fermion vertices unless FeynArtsDiracIndices = " <>
      "True, and the two forms cannot be merged. Re-export every model of the merge, the SM-only " <>
      "one included, with FeynArtsDiracIndices = True (or merge the UFO exports instead)."]]];
  (* Exports written without feynrules_fixes.wl may have lost single-term vertices next to
     Levi-Civita structures (TESTS/T38).  Not refused: an export the bug did not hit is identical
     either way, and a lost SM vertex is refused below anyway.  Lost operator vertices are not
     detectable here, hence the warning. *)
  With[{unfixed = Select[Prepend[subs, lo], !HEFTExportEpsFixedQ[Lookup[#["meta"], "feynRulesFixes", "none"]] &]},
    If[unfixed =!= {}, Print[Style["[HEFT FA merge] Exported without the FeynRules vertex fix " <>
      "(feynrules_fixes.wl, made before 2026-10-02 or the fix was not applied): " <>
      StringRiffle[#["name"] & /@ unfixed, ", "] <> ". Such an export may lack single-term " <>
      "vertices next to Levi-Civita structures; check that its .mod holds every vertex " <>
      "FeynRules computed, or re-export it (TESTS/T38).", Orange]]]];
  If[AnyTrue[subs, #["operators"] === {} &], HEFTFAError["a source is an SM-only export; list " <>
    "only exports with operators (the baseline is found automatically)."]];
  ops = Flatten[#["operators"] & /@ subs];
  dup = Select[Tally[ops], Last[#] > 1 &][[All, 1]];
  If[dup =!= {}, HEFTFAError["operator(s) in more than one source, which would be added twice: " <>
    StringRiffle[dup, ", "] <> "."]];
  names = #["name"] & /@ subs;
  If[MemberQ[Append[names, lo["name"]], outName], HEFTFAError["OutputName \"" <> outName <>
    "\" is one of the inputs; the merge would overwrite it. Choose another OutputName in Cell 2."]];

  HEFT$MergePrintSubsection["FeynArts merge plan"];
  Print["    ", Style[StringPadRight["SM baseline", 34], Bold], lo["name"]];
  Do[Print["    ", Style[StringPadRight[s["name"], 34], Bold], HEFTMergeOperatorSummary[s["operators"]]],
    {s, subs}];

  models = HEFTFAReadExport /@ Prepend[subs, lo];
  HEFTFACheckStructure[models];

  union    = HEFTFAUnionBases[models];
  generic  = Merge[#["generic"] & /@ models, First];
  abbr     = HEFTFAAbbreviations[models];
  remapped = MapThread[HEFTFARemap[#1["couplings"] /. #2, #1["generic"], union, #1["name"]] &,
    {models, abbr["rename"]}];
  res      = HEFTFAMergeCouplings[First[remapped], Rest[remapped], union];

  grown = Select[Keys[union], Length[union[#]] > Length @ Lookup[
    Lookup[First[models]["generic"], #, <|"basis" -> {}|>], "basis"] &];
  If[grown =!= {}, Print["    generic classes extended beyond the baseline's: ", StringRiffle[
    (# <> " (" <> ToString @ Length @ Lookup[Lookup[First[models]["generic"], #, <|"basis" -> {}|>],
      "basis"] <> " -> " <> ToString @ Length[union[#]] <> ")") & /@ grown, ", "]]];

  outDir = FileNameJoin[{HEFTFAExportsDir[], outName}];
  If[DirectoryQ[outDir],
    Print[Style["[HEFT FA merge] Replacing the files in " <> outDir, Orange]]];
  Quiet[CreateDirectory[outDir, CreateIntermediateDirectories -> True], CreateDirectory::eexist];
  HEFTFAWriteMod[FileNameJoin[{outDir, outName <> ".mod"}], First[models]["modHead"],
    res["couplings"], abbr["rules"]];
  HEFTFAWriteGen[FileNameJoin[{outDir, outName <> ".gen"}],
    StringReplace[First[models]["genHead"], HEFTFA$FermionLinesSlot ->
      "$FermionLines = " <> ToString[AllTrue[models, #["fermionLines"] &]] <> ";"],
    First[models]["genTail"], union, generic];
  HEFTFAWritePars[FileNameJoin[{outDir, outName <> ".pars"}], HEFTFAMergeParLists[models]];
  (* The merged export is an ordinary export of the union: same record, so it can itself be a
     source of a later merge. *)
  HEFTExportWriteMeta[outDir, "feynarts", <|
    "outputName"       -> outName,
    "operators"        -> Sort[ops],
    "mergedFrom"       -> names,
    "mergedLOBaseline" -> lo["name"],
    "feynRulesFixes"   -> AssociationMap[Lookup[SelectFirst[Prepend[subs, lo], Function[e, e["name"] === #]]["meta"],
                            "feynRulesFixes", "none"] &, Append[names, lo["name"]]]
  |>];

  Print[Style["[HEFT FA merge] " <> ToString[Length[res["couplings"]]] <> " couplings (" <>
    ToString[res["dropped"]] <> " cancelled to zero and dropped), " <>
    ToString[Length[abbr["rules"]]] <> " abbreviations, " <> ToString[Length[union]] <>
    " generic classes, " <> ToString[Length[ops]] <> " operators, in " <>
    ToString[Round[AbsoluteTime[] - t0, 0.1]] <> " s.", Bold]];
  Print[Style["[HEFT FA merge] Written to ", Bold], outDir];
  Print["[HEFT FA merge]   ", FileNameTake /@ Select[FileNames["*", outDir], !DirectoryQ[#] &]];
  outDir
];
