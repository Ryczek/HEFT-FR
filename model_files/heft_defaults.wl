(* Single canonical source of default configuration values.
   Consumed by heft_fr.wl (HEFT$ApplyConfigDefaults[]: fills in any Global
   configuration variable the notebook's Configuration section left unset).
   heft_fr_notebook.wl normally sets every variable inline, so it stays
   self-contained; these defaults are the safety net for anything it omits. *)

(* The gauge (unitary) and the operator basis (Brivio et al. 1604.06801) are hard-coded, not
   configuration options - both switches were removed 2026-09-18.  Nothing to default here. *)

HEFT$DefaultConfig = <|
  "feynRulesPath" -> "",   (* no default: the user sets it in Cell 2 (2026-10-13) *)
  "higgsMaxOrder" -> 3,
  "kappaFramework" -> True, "initialiseWCs" -> 1,
  "ewScheme" -> "heft",
  "massless" -> False, "diagonalCKM" -> False,
  "operators" -> {}, "outputName" -> "HEFT_run",
  "maxVertexLegs" -> Automatic,
  "feynArtsDiracIndices" -> Automatic,
  "forceRebuild" -> False
|>;

(* Maps each key above to the actual Global configuration symbol used by heft_fr.wl. *)
HEFT$ConfigSymbolForKey = <|
  "feynRulesPath" -> "$FeynRulesPath",
  "higgsMaxOrder" -> "HiggsMaxOrder", "kappaFramework" -> "KappaFramework",
  "initialiseWCs" -> "InitialiseWCs",
  "ewScheme" -> "EWInputScheme",
  "massless" -> "Massless", "diagonalCKM" -> "DiagonalCKM", "operators" -> "EFTOperators",
  "outputName" -> "OutputName",
  "maxVertexLegs" -> "MaxVertexLegs",
  "feynArtsDiracIndices" -> "FeynArtsDiracIndices",
  "forceRebuild" -> "ForceRebuildLHEFT"
|>;

(* Both Symbol[name] = val and ValueQ[Symbol[name]] are unsafe for dynamic-name
   assignment/lookup: Set has no special case for a computed Symbol[...] target
   (Set::write - "Tag Symbol ... is Protected"), and ValueQ[Symbol[name]] is
   always True regardless of whether the named symbol has a value (Symbol[name]
   itself "evaluates to something", which is all ValueQ checks). Route both
   through ToExpression on the literal source text instead, so the symbol name
   is parsed directly into position rather than computed. *)
HEFT$SymbolHasValueQ[heftName_String] := ValueQ @@ ToExpression[heftName, InputForm, HoldComplete];

(* Fill in (Global context) any configuration variable not already set - called
   once near the top of heft_fr.wl cell 3, after the notebook's own Configuration
   section has already run. *)
HEFT$ApplyConfigDefaults[] := Do[
  If[!HEFT$SymbolHasValueQ[HEFT$ConfigSymbolForKey[key]],
    ToExpression[HEFT$ConfigSymbolForKey[key] <> " = " <> ToString[HEFT$DefaultConfig[key], InputForm]]
  ],
  {key, Keys[HEFT$DefaultConfig]}
];

(* Removed expansion options, checked right after the defaults are applied (heft_fr.wl Cell 3
   and the merge bootstrap).  A Configuration cell still setting one would otherwise be ignored
   without a word, and the build would run on something else:
     - HEFTMaxOrder (renamed MaxChiralOrder 2026-09-16) was removed 2026-09-17: ChiralOrder is a
       label only, nothing is truncated on it;
     - EFTMaxOrder (renamed MaxEFTInsertions 2026-09-16) was removed 2026-09-17: the model keeps a
       single EFT insertion per vertex, always;
     - Combine2Derivatives was removed 2026-09-17: PDH/P8/P20/P21/P22 always use one combined
       Wilson-coefficient family;
     - LOYukawaExpansion was removed 2026-09-28: the FQU/FQD/FLE tower is always present, and
       setting its coefficients to 0 neglects it. *)
HEFT$RemovedOptionMessages = {
  "HEFTMaxOrder" -> "removed (2026-09-17) - chiral order is a label only, every selected operator is kept; delete the line",
  "MaxChiralOrder" -> "removed (2026-09-17) - chiral order is a label only, every selected operator is kept; delete the line",
  "EFTMaxOrder" -> "removed (2026-09-17) - the model always keeps a single EFT insertion per vertex; delete the line",
  "MaxEFTInsertions" -> "removed (2026-09-17) - the model always keeps a single EFT insertion per vertex; delete the line",
  "Combine2Derivatives" -> "removed (2026-09-17) - PDH/P8/P20/P21/P22 always use one combined coefficient family; delete the line",
  "LOYukawaExpansion" -> "removed (2026-09-28) - the FQU/FQD/FLE Yukawa tower is always in the model; set CQUn/CQDn/CLEn to 0 in wcxf_output.json to neglect it, and delete the line"
};
HEFT$CheckExpansionOptions[] := Module[{set},
  set = Select[Keys[HEFT$RemovedOptionMessages],
    HEFT$SymbolHasValueQ["Global`" <> #] &];
  If[set =!= {},
    Scan[Print[Style["[HEFT] ERROR: " <> # <> " is " <> (# /. HEFT$RemovedOptionMessages) <> ".", Red, Bold]] &, set];
    Print[Style["[HEFT] Fix the Configuration cell, restart the kernel (the old names still hold " <>
      "values in this one), and re-run.", Red]];
    Abort[]
  ];
  True
];
