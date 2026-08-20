(* Operator catalogues and reference printing for heft_fr_notebook.wl / heft_fr.wl.

   Entry point: HEFT$PrintNotebookReference[] (called from the notebook's Reference
   section). It always prints the "About" block (what this model is, who wrote it,
   references); the configuration-option table and the operator catalogue are only
   printed when Global`IgnoreReference is not True. *)

HEFT$Version = "0.5";

(* Each group is {title, operator labels, category}; category in {"Bosonic","2F","4F"}. *)

HEFT$Catalog1604NLO = {
  {"Bosonic - scalar / gauge kinetic",
    {"DH", "GHNLO", "GHtildeNLO", "WHNLO", "WtildeHNLO", "BHNLO", "BtildeHNLO"}, "Bosonic"},
  {"Bosonic - cubic gauge",
    {"GGGNLO", "WWWNLO", "WWWtildeNLO", "GGGtildeNLO"}, "Bosonic"},
  {"Bosonic - CP-even (P operators)",
    {"P1NLO", "P2NLO", "P3NLO", "P4NLO", "P5NLO", "P6NLO", "P8NLO", "P11NLO", "P12NLO",
     "P13NLO", "P14NLO", "P17NLO", "P18NLO", "P20NLO", "P21NLO", "P22NLO",
     "P23NLO", "P24NLO", "P26NLO"}, "Bosonic"},
  {"Bosonic - CP-odd (S operators)",
    {"S2DNLO", "S1NLO", "S2NLO", "S3NLO", "S4NLO", "S5NLO", "S6NLO", "S7NLO",
     "S8NLO", "S9NLO", "S15NLO"}, "Bosonic"},
  {"Fermionic 2F - quark (NQ1-NQ36)",
    Table["NQ" <> ToString[heftI] <> "NLO", {heftI, 1, 36}], "2F"},
  {"Fermionic 2F - lepton (NL1-NL17, NLF1-NLF3)",
    Join[Table["NL" <> ToString[heftI] <> "NLO", {heftI, 1, 17}], {"NLF1NLO", "NLF2NLO", "NLF3NLO"}], "2F"},
  {"Fermionic 4F - quark (RQ1-RQ26)",
    Table["RQ" <> ToString[heftI] <> "NLO", {heftI, 1, 26}], "4F"},
  {"Fermionic 4F - quark-lepton (RQL1-RQL23)",
    Table["RQL" <> ToString[heftI] <> "NLO", {heftI, 1, 23}], "4F"},
  {"Fermionic 4F - lepton (RL1-RL7)",
    Table["RL" <> ToString[heftI] <> "NLO", {heftI, 1, 7}], "4F"}
};

(* Not part of the 1604.06801 paper itself - NNLO operators implemented as an extension
   beyond that paper's NLO basis, and shipped as worked examples rather than as a complete
   NNLO basis. Only printed when PrintHigherOrder = True (see Reference cell).
   NNNLO (GHDNNNLO) was dropped from this release. *)
HEFT$Catalog1604Higher = {
  {"NNLO (need HEFTMaxOrder >= 2)",
    {"GHNNLO1", "GHNNLO2", "GHtildeNNLO",
     "WLh2WRD2NNLO", "WLh3D4NNLO"}, "Bosonic"}
};

HEFT$Catalog2206NLO = {
  {"UhD4 operators (UhD4n1 - UhD4n15)",
    Table["UhD4n" <> ToString[heftI], {heftI, 1, 15}], "Bosonic"},
  {"X2Uh operators (X2Uhn1 - X2Uhn10)",
    Table["X2Uhn" <> ToString[heftI], {heftI, 1, 10}], "Bosonic"},
  {"XUhD2 operators (XUhD2n1 - XUhD2n8)",
    Table["XUhD2n" <> ToString[heftI], {heftI, 1, 8}], "Bosonic"},
  {"X3 operators (X3n1 - X3n6)",
    Table["X3n" <> ToString[heftI], {heftI, 1, 6}], "Bosonic"}
};

(* Not part of the 2206.07722 paper itself - see note on HEFT$Catalog1604Higher above. *)
HEFT$Catalog2206Higher = {
  {"NNLO (need HEFTMaxOrder >= 2)",
    {"WL2h2T2D2NNLO", "BL2h2D2NNLO"}, "Bosonic"}
};

HEFT$OperatorCatalogsForBasis[basis_String] := Switch[basis,
  "1604.06801", {HEFT$Catalog1604NLO, HEFT$Catalog1604Higher},
  "2206.07722", {HEFT$Catalog2206NLO, HEFT$Catalog2206Higher},
  _, {{}, {}}
];

HEFTCatalogFlatten[catalog_List] := Join @@ catalog[[All, 2]];

HEFT$RefPrintSubsection[title_String] := Print[
  Style["\n  " <> title, Bold, FontSize -> 14]
];

(* Category grouping: every catalog group carries a "Bosonic"/"2F"/"4F" tag (3rd tuple entry). *)
HEFT$CategoryOrder = {"Bosonic", "2F", "4F"};

HEFT$CategoryLabel = <|
  "Bosonic" -> "Bosonic operators",
  "2F" -> "2-fermion (2F) operators",
  "4F" -> "4-fermion (4F) operators"
|>;

HEFT$CatalogCategory[heftEntry_List] := If[Length[heftEntry] >= 3, heftEntry[[3]], "Bosonic"];

HEFT$RefPrintCategoryTable[groups_List] := Module[{rows, heftHeader},
  If[groups === {}, Return[]];
  heftHeader = {Style["Group", Bold, FontSize -> 12], Style["#", Bold, FontSize -> 12],
    Style["Operators", Bold, FontSize -> 12]};
  rows = Map[
    Function[heftG, {heftG[[1]], Length[heftG[[2]]], Pane[StringJoin[Riffle[heftG[[2]], ", "]], 480]}],
    groups
  ];
  Print @ Grid[
    Prepend[rows, heftHeader],
    Frame -> All,
    Alignment -> {{Left, Center, Left}, Top},
    Spacings -> {1.5, 0.75},
    ItemStyle -> {Automatic, Automatic, Directive[FontFamily -> "Monospace", FontSize -> 10]},
    Background -> {None, {{1 -> GrayLevel[0.88]}}}
  ];
];

HEFT$RefPrintOperatorCatalog[catalog_List] := Module[{total, cat, groups, heftC},
  If[catalog === {}, Return[]];
  total = Total[Length /@ catalog[[All, 2]]];
  Print[Style["    (" <> ToString[total] <> " operators in " <>
    ToString[Length[catalog]] <> " groups)", Gray]];
  Do[
    cat = HEFT$CategoryOrder[[heftC]];
    groups = Select[catalog, HEFT$CatalogCategory[#] === cat &];
    If[groups =!= {},
      HEFT$RefPrintSubsection[HEFT$CategoryLabel[cat] <> "  (" <>
        ToString[Total[Length /@ groups[[All, 2]]]] <> ")"];
      HEFT$RefPrintCategoryTable[groups];
      Print[""];
    ],
    {heftC, Length[HEFT$CategoryOrder]}
  ];
];

HEFT$ConfigOptionReference = {
  {"$FeynRulesPath", "Path to your FeynRules installation."},
  {"HEFTGauge", "\"unitary\" - the only supported value. An R_xi branch exists in the source but is unfinished and unsupported; see README SS \"Deferred configuration options\"."},
  {"HEFTMaxOrder", "Chiral/LamHEFT truncation: 0 = LO only, 1 = NLO, 2 = NNLO. 2 requires EWInputScheme = \"heft\": the derived schemes are NLO-only and the combination is refused (see EWInputScheme below)."},
  {"HiggsMaxOrder", "Max (H/vev)^n order in bosonic F-functions."},
  {"KappaFramework", "True = Kappa* normalisation; False = Delta* (see README)."},
  {"InitialiseWCs", "Default value cell 3 writes for the effective Wilson coefficients: 1 or 0. SM couplings keep their SM value either way (Kappa framework 1, Delta framework 0)."},
  {"LOYukawaExpansion", "True (default) = keep the higher-order fermion-Higgs terms of the LO Yukawa sector (F-functions FQU/FQD/FLE, coefficients CQUn<n>/CQDn<n>/CLEn<n>, n >= 2). False = drop them and do not declare those coefficients at all. The SM Yukawa and its single-Higgs coupling are unaffected either way (they follow KappaQU.../DeltaYQU...)."},
  {"IncludeCustodialT", "True (default) = keep the custodial-symmetry breaking operator PT = Tr[T.V_mu]Tr[T.V^mu] F_T(h) in LGaugeHiggs. False = drop it; its CFTn coefficients are then not declared either, since PT is their only user."},
  {"Combine2Derivatives", "False (default) = unchanged behaviour. True = for DH/P8NLO/P20NLO/P21NLO/P22NLO only (each multiplies two independently h/vev-truncated flare functions via a derivative on each), replace the two WC families with one new combined family per operator (C<op>n<nh>prime, nh = the total number of Higgs fields in that term, the differentiated ones included), so a given vertex's coefficient is a single WC instead of the sum of products of the two originals it would otherwise be. Changes which Wilson coefficients exist for these 5 operators, so it is part of the LHEFT cache key."},
  {"EWInputScheme", "\"heft\" (default) = G1/GW/GS/vev/hlambda are the model's own External inputs and the Lagrangian is left alone. \"gf\" = derived from (Gf, MW, MZ, MH). \"aem\" = derived from (alpha_EM as aEWM1, Gf, MZ, MH); MW is then a prediction, not an input, and is declared Internal. \"gf\"/\"aem\" also rewrite the mass-basis Lagrangian via HEFTEWInputRepl, with an NLO (ChiralOrder) shift when HEFTMaxOrder >= 1. ORDER RESTRICTION: \"heft\" works at any HEFTMaxOrder; \"gf\" and \"aem\" are derived to O(ChiralOrder) only and are REFUSED at HEFTMaxOrder >= 2 - Cell 3 aborts during configuration, and LoadModel aborts again in Cell 5."},
  {"Massless", "True -> load restrictions/Massless.rst before Feynman rules."},
  {"DiagonalCKM", "True -> load restrictions/DiagonalCKM.rst."},
  {"HEFTNLOBasis", "\"1604.06801\" (Brivio et al.) - the only implemented basis. \"2206.07722\" (Sun et al.) is refused as not yet implemented; its catalogue can still be previewed here."},
  {"NLOOperators", "List of active NLO/NNLO labels; {} = LO only. Must match basis."},
  {"OutputName", "Subdirectory name under output/. The export format is not an option: run Cell 7 for UFO or Cell 8 for FeynArts (both, if you want both)."},
  {"MaxVertexLegs", "Automatic (default) = every vertex is exported. An integer n >= 3 keeps only vertices with at most n legs, in all three output cells (6 Feynman rules, 7 UFO, 8 FeynArts) - it is passed on as FeynRules' own MaxParticles, which WriteUFO and WriteFeynArtsOutput forward to the FeynmanRules call they make internally, so it really does shrink the exported model. Values below 3 are refused: FeynRules returns no 1- or 2-point vertices, so a smaller cut would write an empty model. NOT part of the LHEFT cache key - it changes only what is read off the Lagrangian at export time, never the Lagrangian, so switching it never forces a rebuild. It is a way to cut an export down to the vertices a study needs, not a physics option: the quartics it drops first are the ones unitarising VV -> VV, and since the h-expansion is what generates high multiplicities it also truncates the flare tower in the output while wcxf_output.json still lists every coefficient."},
  {"ForceRebuildLHEFT", "The only cache option. False (default) = always look HEFT_cache/ up first and load a matching build if there is one (under any OutputName); True = skip the lookup, rebuild LHEFTMassBasis, overwrite. Every build is saved either way."}
};

HEFT$PrintConfigOptionsReference[] := Module[{idx},
  HEFT$RefPrintSubsection["Configuration options (set in the Configuration section)"];
  Print[Style["    Variable              Meaning", Bold]];
  Print[Style["    " <> StringRepeat["-", 66], Darker[Gray]]];
  Do[
    Print[
      "    ",
      Style[StringPadRight[HEFT$ConfigOptionReference[[idx, 1]], 22], FontFamily -> "Courier"],
      HEFT$ConfigOptionReference[[idx, 2]]
    ],
    {idx, Length[HEFT$ConfigOptionReference]}
  ];
  Print[Style["\n    LO operators are always included. NNLO labels need HEFTMaxOrder >= 2.", Gray]];
  Print[Style["\n    Wilson coefficients have no options: cell 3 always writes wcxf/wcxf_init.json", Gray]];
  Print[Style["    and wcxf/wcxf_output.json with every coefficient at 1; edit wcxf_output.json", Gray]];
  Print[Style["    (cell 4) to change them. A value of 0 is just 0 in the exported model;", Gray]];
  Print[Style["    which operators exist is decided by NLOOperators alone.", Gray]];
];

HEFT$PrintBasisOperatorReference[basis_String] := Module[{nlo, higher},
  {nlo, higher} = HEFT$OperatorCatalogsForBasis[basis];
  HEFT$RefPrintSubsection["Basis " <> basis <> " - NLO (chiral dimension 1)"];
  HEFT$RefPrintOperatorCatalog[nlo];
  If[TrueQ[Global`PrintHigherOrder] && higher =!= {} && HEFTCatalogFlatten[higher] =!= {},
    HEFT$RefPrintSubsection[
      "Higher chiral order operators (NNLO extensions, not part of the " <> basis <> " paper itself)"
    ];
    HEFT$RefPrintOperatorCatalog[higher];
  ];
];

(* ---------------------------------------------------------------------------
   About block - what this model is, who wrote it, what it is built on.
   Printed unconditionally by HEFT$PrintNotebookReference[], whether or not the
   option/operator listing is suppressed via IgnoreReference = True.
   --------------------------------------------------------------------------- *)

HEFT$AboutAuthors = {
  {"Micha\[LSlash] Ryczkowski", "michaljakub.ryczkowski@unipd.it"}
};

HEFT$AboutAffiliation = {
  "Dipartimento di Fisica e Astronomia \"G. Galilei\", Universit\[AGrave] di Padova",
  "and INFN, Sezione di Padova, Via F. Marzolo 8, I-35131 Padova, Italy"
};

HEFT$AboutFeatures = {
  "LO: the Standard Model in HEFT form - Kappa/Delta normalisation, F-functions in H/vev",
  "NLO: the complete 1604.06801 basis - bosonic, 2-fermion (2F) and 4-fermion (4F) operators",
  "Higher orders: example NNLO operators, as an extension beyond that basis",
  "Gauge: unitary - the only gauge implemented (no Goldstone bosons in the spectrum)",
  "Electroweak and CKM input schemes, plus optional restrictions/*.rst",
  "Wilson coefficients read from / written to WCxf JSON files under wcxf/",
  "Mass-basis Lagrangian cached on disk under HEFT_cache/<OutputName>/",
  "Export to UFO (MadGraph) or FeynArts model files under output/"
};

HEFT$AboutReferences = {
  {"HEFT NLO basis", "Brivio et al., \"The complete HEFT Lagrangian after the LHC Run I\", arXiv:1604.06801"},
  {"Alternate basis", "arXiv:2206.07722 (not yet implemented)"},
  {"FeynRules", "Alloul et al., \"FeynRules 2.0\", arXiv:1310.1921"},
  {"WCxf format", "Aebischer et al., \"WCxf: an exchange format for Wilson coefficients\", arXiv:1712.05298"}
};

HEFT$PrintAbout[] := Module[{idx},
  Print[Style["\n" <> StringRepeat["=", 72], Bold]];
  Print[Style["  HEFT-FR \[LongDash] a FeynRules implementation of the HEFT Lagrangian" <>
    "  (v" <> HEFT$Version <> ")", Bold, FontSize -> 14]];
  Print[Style[StringRepeat["=", 72], Bold]];

  HEFT$RefPrintSubsection["What this is"];
  Print["    A modular FeynRules model for the Higgs Effective Field Theory: the"];
  Print["    electroweak chiral Lagrangian with a singlet Higgs, organised as a double"];
  Print["    expansion in chiral dimension (LamHEFT) and in powers of H/vev (LamF)."];
  Print["    It assembles the Lagrangian in the mass basis (LHEFT) from the operators you"];
  Print["    select, and exports it as a UFO or FeynArts model."];

  HEFT$RefPrintSubsection["What is implemented"];
  Do[Print["    \[Bullet] ", HEFT$AboutFeatures[[idx]]], {idx, Length[HEFT$AboutFeatures]}];

  HEFT$RefPrintSubsection[If[Length[HEFT$AboutAuthors] > 1, "Authors", "Author"]];
  Do[
    Print["    ", Style[StringPadRight[HEFT$AboutAuthors[[idx, 1]], 24], Bold],
      Style[HEFT$AboutAuthors[[idx, 2]], FontFamily -> "Courier"]],
    {idx, Length[HEFT$AboutAuthors]}
  ];
  Do[Print["    ", Style[HEFT$AboutAffiliation[[idx]], Darker[Gray]]],
    {idx, Length[HEFT$AboutAffiliation]}];

  HEFT$RefPrintSubsection["Built on / based on"];
  Do[
    Print["    ", Style[StringPadRight[HEFT$AboutReferences[[idx, 1]], 18], Bold],
      HEFT$AboutReferences[[idx, 2]]],
    {idx, Length[HEFT$AboutReferences]}
  ];

  HEFT$RefPrintSubsection["How it is run"];
  Print["    heft_fr_notebook.wl is the only entry point: evaluate its cells in order,"];
  Print["    Cell 1 (Reference) \[Rule] Cell 2 (Configuration) \[Rule] Cells 3-8."];
  Print["    The model source lives in model_files/, the manual in README.md."];
];

(* Prints the About block, and - unless IgnoreReference = True - the configuration-option
   table plus the operator catalogue for a single basis: the one currently selected via
   HEFTNLOBasis (falls back to "1604.06801" if not set yet). Pass an explicit basis string
   to override, e.g. HEFT$PrintNotebookReference["2206.07722"]. Higher chiral order
   (NNLO) operators are only shown when PrintHigherOrder = True. *)
HEFT$PrintNotebookReference[] := HEFT$PrintNotebookReference[
  If[ValueQ[Global`HEFTNLOBasis] && MemberQ[{"1604.06801", "2206.07722"}, Global`HEFTNLOBasis],
    Global`HEFTNLOBasis,
    "1604.06801"
  ]
];

HEFT$PrintNotebookReference[basis_String] := Module[{},
  HEFT$PrintAbout[];

  If[TrueQ[Global`IgnoreReference],
    Print[Style["\n[HEFT] Option and operator reference skipped (IgnoreReference = True). " <>
      "Set IgnoreReference = False to print it.", Bold, FontSize -> 13]];
    Return[]
  ];

  Print[Style["\n" <> StringRepeat["=", 72], Bold]];
  Print[Style["  Reference \[LongDash] configuration options and operator catalogue", Bold, FontSize -> 14]];
  Print[Style["  (showing basis " <> basis <> " - set HEFTNLOBasis to switch; " <>
    "PrintHigherOrder = True also shows NNLO;\n   IgnoreReference = True prints " <>
    "the About block only)", FontSize -> 11, Darker[Gray]]];
  Print[Style[StringRepeat["=", 72], Bold]];
  HEFT$PrintConfigOptionsReference[];
  HEFT$PrintBasisOperatorReference[basis];
  Print[Style["\n[HEFT] Reference listing complete (basis " <> basis <> ").", Bold, FontSize -> 13]];
];
