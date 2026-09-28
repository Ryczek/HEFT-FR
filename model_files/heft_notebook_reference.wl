(* Operator catalogues and reference printing for heft_fr_notebook.wl / heft_fr.wl.

   Entry point: HEFT$PrintNotebookReference[] (called from the notebook's Reference
   section). It always prints the "About" block (what this model is, who wrote it,
   references) AND the operator catalogue; only the configuration-option table is
   suppressed, by Global`IgnoreInstructions = True.  (Before 2026-09-22 the flag was
   IgnoreReference and it hid the catalogue too; PrintHigherOrder, which used to gate
   the user-defined operators, is gone - they are always listed.) *)

HEFT$Version = "1.0";

(* Each group is {title, operator labels, category}; category in {"Bosonic","2F","4F"}. *)

HEFT$Catalog1604NLO = {
  {"Bosonic - scalar / gauge kinetic",
    {"PT", "PDH", "PG", "SG", "PW", "SW", "PB", "SB"}, "Bosonic"},
  {"Bosonic - cubic gauge",
    {"PGGG", "PWWW", "SWWW", "SGGG"}, "Bosonic"},
  {"Bosonic - CP-even (P operators)",
    {"P1", "P2", "P3", "P4", "P5", "P6", "P8", "P11", "P12",
     "P13", "P14", "P17", "P18", "P20", "P21", "P22",
     "P23", "P24", "P26"}, "Bosonic"},
  {"Bosonic - CP-odd (S operators)",
    {"S2D", "S1", "S2", "S3", "S4", "S5", "S6", "S7",
     "S8", "S9", "S15"}, "Bosonic"},
  {"Fermionic 2F - quark (NQ1-NQ36)",
    Table["NQ" <> ToString[heftI], {heftI, 1, 36}], "2F"},
  {"Fermionic 2F - lepton (NL1-NL17)",
    Table["NL" <> ToString[heftI], {heftI, 1, 17}], "2F"},
  {"Fermionic 4F - quark (RQ1-RQ26)",
    Table["RQ" <> ToString[heftI], {heftI, 1, 26}], "4F"},
  {"Fermionic 4F - quark-lepton (RQL1-RQL23)",
    Table["RQL" <> ToString[heftI], {heftI, 1, 23}], "4F"},
  {"Fermionic 4F - lepton (RL1-RL7)",
    Table["RL" <> ToString[heftI], {heftI, 1, 7}], "4F"}
};

(* Not part of the 1604.06801 paper itself - the user-defined operators of
   parameters_User.fr / Lagrangian_User.fr, shipped with the gluon-Higgs NNLO operators as the
   worked example.  Add the label of every operator you define there to this list, or Cell 3
   rejects it as unknown.  Always printed with the rest of the catalogue (the PrintHigherOrder
   gate was removed 2026-09-22).  NNNLO (GHDNNNLO) was dropped from this release. *)
HEFT$Catalog1604Higher = {
  {"User-defined - gluon-Higgs examples",
    {"PGHD1", "PGHD2", "SGHD"}, "Bosonic"}
};

(* chiral dimension of every operator label - the power n of ChiralOrder^n the operator carries in the
   Lagrangian, from its W/V/d/D count (bosonic 2 -> 0, 3 -> 1, 4 -> 2; fermionic d Psi^2 phi^4
   class 0, d^2 Psi^2 phi^2 class 1).  A LABEL ONLY: nothing is truncated on it (since 2026-09-17),
   it is printed in the Reference tables and is the UFO coupling order ChiralOrder.
   Must match the Lagrangian files: the ChiralOrder^n factor inside each bosonic L<op>, the
   LEFT2F block a 2F operator is added to (LEFT2F1Lamaux = 1, the others 0), LEFT4F = 0, and
   Lagrangian_User.fr for the user labels.  Add a row for every operator you add. *)
HEFT$OperatorChiralOrder = Association @ Join[
  Thread[{"PT", "PG", "PB", "PW", "P1", "P12", "S2D", "SB", "SW", "SG", "S1", "S8"} -> 0],
  Thread[{"P2", "P3", "P4", "P5", "P13", "P14", "P17", "S2", "S3", "S4", "S7", "S9",
    "PWWW", "PGGG", "SWWW", "SGGG"} -> 1],
  Thread[{"PDH", "P6", "P8", "P11", "P18", "P20", "P21", "P22", "P23", "P24", "P26",
    "S5", "S6", "S15"} -> 2],
  Thread[{"PGHD1", "PGHD2", "SGHD"} -> 2],
  Thread[Table["NQ" <> ToString[heftI], {heftI, Join[Range[1, 8], Range[29, 36]]}] -> 0],
  Thread[Table["NQ" <> ToString[heftI], {heftI, 9, 28}] -> 1],
  Thread[Table["NL" <> ToString[heftI], {heftI, Join[{1, 2}, Range[12, 17]]}] -> 0],
  Thread[Table["NL" <> ToString[heftI], {heftI, 3, 11}] -> 1],
  Thread[Table["RQ" <> ToString[heftI], {heftI, 1, 26}] -> 0],
  Thread[Table["RQL" <> ToString[heftI], {heftI, 1, 23}] -> 0],
  Thread[Table["RL" <> ToString[heftI], {heftI, 1, 7}] -> 0]
];

(* The operator basis is fixed at Brivio et al. 1604.06801 (2026-09-18): no dispatch, no
   basis argument. *)
HEFT$OperatorCatalogs[] := {HEFT$Catalog1604NLO, HEFT$Catalog1604Higher};

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

(* One row per group, one column per chiral dimension that occurs in the category: each operator
   sits in the column of its chiral dimension (HEFT$OperatorChiralOrder).  An operator missing from
   that table is shown under "?" instead of being dropped. *)
HEFT$RefPrintCategoryTable[groups_List] := Module[{orders, heftHeader, rows, cell},
  If[groups === {}, Return[]];
  orders = Union[Lookup[HEFT$OperatorChiralOrder, Flatten[groups[[All, 2]]], "?"]];
  heftHeader = Join[
    {Style["Group", Bold, FontSize -> 12], Style["#", Bold, FontSize -> 12]},
    Style["chiral dimension " <> ToString[#], Bold, FontSize -> 12] & /@ orders];
  cell[ops_List] := Pane[If[ops === {}, "", StringJoin[Riffle[ops, ", "]]], 300];
  rows = Map[
    Function[heftG, Join[{heftG[[1]], Length[heftG[[2]]]},
      Function[o, cell[Select[heftG[[2]], Lookup[HEFT$OperatorChiralOrder, #, "?"] === o &]]] /@ orders]],
    groups
  ];
  Print @ Grid[
    Prepend[rows, heftHeader],
    Frame -> All,
    Alignment -> {Join[{Left, Center}, ConstantArray[Left, Length[orders]]], Top},
    Spacings -> {1.5, 0.75},
    ItemStyle -> {Join[{Automatic, Automatic}, ConstantArray[Directive[FontFamily -> "Monospace", FontSize -> 10], Length[orders]]]},
    Background -> {None, {{1 -> GrayLevel[0.88]}}}
  ];
];

HEFT$RefPrintOperatorCatalog[catalog_List] := Module[{cat, groups, heftC},
  If[catalog === {}, Return[]];
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
  {"$FeynRulesPath", "Path to your FeynRules installation"},
  {"HiggsMaxOrder", "Max (H/vev)^n order in bosonic F-functions"},
  {"KappaFramework", "True = Kappa normalisation; False = Delta (see README and documentation)"},
  {"InitialiseWCs", "Default value cell 3 writes for the effective Wilson coefficients: 1 or 0. SM couplings keep their SM value either way (Kappa framework 1, Delta framework 0)"},
  {"EWInputScheme", "\"heft\" (default) = (G1,GW,vev,hlambda) are the model's External input parameters"},
  {"", "\"gf\" = (G1,GW,vev,hlambda) derived from (Gf, MW, MZ, MH)"},
  {"", "\"aem\" = (G1,GW,vev,hlambda) derived from (alpha_EM, Gf, MZ, MH)"},
  {"Massless", "True -> load restrictions/Massless.rst before Feynman rules"},
  {"DiagonalCKM", "True -> load restrictions/DiagonalCKM.rst"},
  {"EFTOperators", "List of active EFT operator labels, must be chosen from the catalogue below"},
  {"OutputName", "Output directory name under HEFT_Frules/output/"},
  {"MaxVertexLegs", "Automatic (default) = every vertex is exported. An integer n >= 3 keeps only vertices with at most n legs"},
  {"ForceRebuildLHEFT", "The only cache option. False (default) = always look HEFT_cache/ up first and load a matching build if there is one (under any OutputName);"},
  {"", "True = skip the lookup, rebuild LHEFTMassBasis, overwrite. Every build is saved either way"}
};

HEFT$PrintConfigOptionsReference[] := Module[{idx},
  HEFT$RefPrintSubsection["Configuration options - to be set in the Configuration section (Cell 2)"];
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
];

HEFT$PrintBasisOperatorReference[] := Module[{nlo, higher},
  {nlo, higher} = HEFT$OperatorCatalogs[];
  HEFT$RefPrintSubsection["Operators by chiral dimension (1604.06801)"];
  HEFT$RefPrintOperatorCatalog[nlo];
  If[higher =!= {} && HEFTCatalogFlatten[higher] =!= {},
    HEFT$RefPrintSubsection[
      "User-defined operators (extension, not part of the 1604.06801 set)"
    ];
    HEFT$RefPrintOperatorCatalog[higher];
  ];
];

(* ---------------------------------------------------------------------------
   About block - what this model is, who wrote it, what it is built on.
   Printed unconditionally by HEFT$PrintNotebookReference[], whether or not the
   configuration-option table is suppressed via IgnoreInstructions = True.
   --------------------------------------------------------------------------- *)

HEFT$AboutAuthors = {
  {"Micha\[LSlash] Ryczkowski", "michaljakub.ryczkowski@unipd.it"}
};

HEFT$AboutAffiliation = {
  "Dipartimento di Fisica e Astronomia \"G. Galilei\", Universit\[AGrave] di Padova",
  "and INFN, Sezione di Padova, Via F. Marzolo 8, I-35131 Padova, Italy"
};

HEFT$AboutFeatures = {
  "The complete operator set of 1604.06801 - SM, bosonic, 2-fermion (2F) and 4-fermion (4F) operators, inlcuding LO, NLO and NNLO",
  "Gauge: unitary",
  "Electroweak input schemes - heft (default), gf, aem",
  "Wilson coefficients read from / written to WCxf JSON files under wcxf/",
  "Mass-basis Lagrangian cached on disk under HEFT_cache/<OutputName>/",
  "Export to UFO or FeynArts model files under output/"
};

HEFT$AboutReferences = {
  {"HEFT operator set of", "Brivio et al., \"The complete HEFT Lagrangian after the LHC Run I\", arXiv:1604.06801"},
  {"FeynRules", "Alloul et al., \"FeynRules 2.0\", arXiv:1310.1921"}};

HEFT$PrintAbout[] := Module[{idx},
  Print[Style["\n" <> StringRepeat["=", 72], Bold]];
  Print[Style["  HEFT-FR \[LongDash] a FeynRules implementation of the HEFT Lagrangian" <>
    "  (v" <> HEFT$Version <> ")", Bold, FontSize -> 14]];
  Print[Style[StringRepeat["=", 72], Bold]];

  HEFT$RefPrintSubsection["What this is"];
  Print["    A modular FeynRules model for the Higgs Effective Field Theory."];
  Print["    The Lagrangian is assembled from the operators of your choice, can be exported as a UFO or FeynArts model."];

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
  Print["    heft_fr_notebook.wl is the only entry point: evaluate its cells in the following order"];
  Print["    Cell 1 (Reference) \[Rule] Cell 2 (Configuration) \[Rule] Cells 3-8."];
  Print["    The model source lives in model_files/, the detailed description is in README.md and associated publication."];
];

(* Prints the About block and the operator catalogue ALWAYS; only the configuration-option
   table is optional, skipped by IgnoreInstructions = True.  The basis is fixed at 1604.06801,
   so there is nothing to select, and the user-defined operators are always listed. *)
HEFT$PrintNotebookReference[] := Module[{skipOptions},
  skipOptions = TrueQ[Global`IgnoreInstructions];

  HEFT$PrintAbout[];

  If[skipOptions,
    Print[Style["\n[HEFT] Configuration-option descriptions skipped " <>
      "(IgnoreInstructions = True). Set IgnoreInstructions = False to print them.",
      Bold, FontSize -> 13]],
    HEFT$PrintConfigOptionsReference[]
  ];

  HEFT$PrintBasisOperatorReference[];
  Print[Style["\n[HEFT] Reference listing complete.", Bold, FontSize -> 13]];
];
