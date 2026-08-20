(* Single canonical source of default configuration values.
   Consumed by heft_fr.wl (HEFT$ApplyConfigDefaults[]: fills in any Global
   configuration variable the notebook's Configuration section left unset).
   heft_fr_notebook.wl normally sets every variable inline, so it stays
   self-contained; these defaults are the safety net for anything it omits. *)

(* NLO bases that can actually be built.  "2206.07722" is deliberately NOT here: the basis is
   not implemented in this release and both order gates - heft_fr.wl Cell 3 and
   HEFT_Model.fr's own check inside LoadModel - refuse it.  Re-enabling it means adding the
   operator files under model_files/NLO/basis_2206_07722/, listing the basis here, AND lifting
   the literal check in HEFT_Model.fr, which cannot read this file (it runs inside the
   FeynRules model context, where this symbol would land in the wrong context). *)
HEFT$SupportedNLOBases = {"1604.06801"};

HEFT$DefaultConfig = <|
  "feynRulesPath" -> "/Users/michalryczkowski/Library/Mathematica/Applications/feynrules-current",
  "gauge" -> "unitary", "basis" -> "1604.06801",
  "heftMaxOrder" -> 1, "higgsMaxOrder" -> 3,
  "kappaFramework" -> True, "initialiseWCs" -> 1, "loYukawaExpansion" -> True, "includeCustodialT" -> True,
  "combine2Derivatives" -> False,
  "ewScheme" -> "heft",
  "massless" -> False, "diagonalCKM" -> False,
  "operators" -> {}, "outputName" -> "HEFT_run",
  "maxVertexLegs" -> Automatic,
  "forceRebuild" -> False
|>;

(* Maps each key above to the actual Global configuration symbol used by heft_fr.wl. *)
HEFT$ConfigSymbolForKey = <|
  "feynRulesPath" -> "$FeynRulesPath", "gauge" -> "HEFTGauge", "basis" -> "HEFTNLOBasis",
  "heftMaxOrder" -> "HEFTMaxOrder",
  "higgsMaxOrder" -> "HiggsMaxOrder", "kappaFramework" -> "KappaFramework",
  "initialiseWCs" -> "InitialiseWCs", "loYukawaExpansion" -> "LOYukawaExpansion", "includeCustodialT" -> "IncludeCustodialT",
  "combine2Derivatives" -> "Combine2Derivatives",
  "ewScheme" -> "EWInputScheme",
  "massless" -> "Massless", "diagonalCKM" -> "DiagonalCKM", "operators" -> "NLOOperators",
  "outputName" -> "OutputName",
  "maxVertexLegs" -> "MaxVertexLegs",
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
