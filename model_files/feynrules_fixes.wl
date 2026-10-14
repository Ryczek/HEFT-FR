(* ::Package:: *)

(* Two corrections to FeynRules' FeynArts writer (Interfaces/FeynArtsInterface.m), applied in
   memory before every FeynArts export (heft_fr.wl Cell 8).  Nothing on disk is changed, so a
   user with an unmodified FeynRules gets correct FeynArts output.  Checked against FeynRules
   2.3.49.

   How: the definition is taken from the installed FeynArtsInterface.m as text, parsed in the
   context FeynRules loads that file into (PRIVATE`), and compared with the definition
   actually loaded.  Only if the two are identical is the text edited and the function redefined.
   If the faulty code is not there (a FeynRules version that changed it) nothing is touched and
   the status says so.  Status per fix: "applied", "already applied", "present in FeynRules", or
   "not applied: <reason>".

   1. "FAStructure2-eps" - single-term vertices lost next to Levi-Civita structures.
      FAStructure2 projects each vertex onto the Lorentz structures of its generic class with a
      local ReturnConst.  For an Eps structure ReturnConst runs
          If[Not[Head[temp]===Plus],temp={temp}];
      on the vertex itself rather than on a copy.  For a vertex that is a single term, every Eps
      structure wraps it in one more list, so every structure after the class's first Eps one
      gets coefficient 0; a vertex with only zeros is then deleted (DeleteCases ... {{0,0}}).
      Vertices of two or more terms are not affected.  Found 2026-09-30: the exports of S1, S8, SB
      and SG lost 4/4/1/1 vertices, among them the SM hhhW+W- (TESTS/T37, T38).  Fix: the Eps
      branch reads If[Head[temp]===Plus,temp,{temp}] and leaves temp alone.

   2. "WriteStructure-SP2" - ScalarProduct[p_a,p_b]^2 in the generic file.
      WriteStructure (a local function of WriteGenCouplings, which is therefore the definition
      edited) has no case for Power[SP[a,b],2]; such a factor falls through to a warning and is
      not written, leaving a broken .gen.  The HEFT patch of 2026-05-23 to the installed
      FeynArtsInterface.m (original kept as FeynArtsInterface.m.heft_backup) added that case,
      but wrote ToString[aa] inside a Switch, which does not bind aa: its output was the
      literal ScalarProduct[momaa,mombb]^2.  This fix writes the momentum labels from
      struc2[[1,1]], struc2[[1,2]], inserting the case into an unmodified FeynRules and
      replacing the faulty one in a patched FeynRules. *)

HEFTFRFixContext = "PRIVATE`";   (* Begin["PRIVATE`"] in FeynRulesPackage.m:1865 - absolute, not FeynRules`PRIVATE` *)

HEFTFRFixFile[] := FileNameJoin[{$FeynRulesPath, "Interfaces", "FeynArtsInterface.m"}];

(* The text of the definition starting with header: the shortest piece from the header up to a
   "];" at the end of a line that parses as a complete expression. *)
HEFTFRFixDefinitionText[text_String, header_String] := Module[{start, ends},
  start = StringPosition[text, header, 1];
  If[start === {}, Return[$Failed]];
  start = start[[1, 1]];
  ends = Select[StringPosition[text, "];\n"][[All, 1]], # > start &];
  SelectFirst[StringTake[text, {start, # + 1}] & /@ ends, SyntaxQ, $Failed]
];

HEFTFRFixParse[code_String, form___] := Block[{$Context = HEFTFRFixContext,
    $ContextPath = {"FeynRules`", "System`"}},
  ToExpression[code, InputForm, form]];

(* DownValues the definition text would produce. *)
HEFTFRFixDownValues[code_String] := Replace[HEFTFRFixParse[code, Hold], {
  Hold[CompoundExpression[SetDelayed[l_, r_], Null]] :> {HoldPattern[l] :> r},
  Hold[SetDelayed[l_, r_]] :> {HoldPattern[l] :> r}}];

(* fix one function: name, header, a test that the edit is already there, the edit. *)
HEFTFRFixApply[name_String, header_String, doneQ_, edit_] := Module[
  {sym, text, def, new},
  If[!StringQ[$FeynRulesPath] || !FileExistsQ[HEFTFRFixFile[]],
    Return["not applied: FeynArtsInterface.m not found"]];
  If[Names[HEFTFRFixContext <> name] === {},
    Return["not applied: " <> HEFTFRFixContext <> name <> " not defined"]];
  sym = Symbol[HEFTFRFixContext <> name];
  text = ReadString[HEFTFRFixFile[]];
  def = HEFTFRFixDefinitionText[text, header];
  If[def === $Failed, Return["not applied: definition of " <> name <> " not found in the file"]];
  (* Already edited in this kernel: the loaded definition is no longer the file's. *)
  If[doneQ[def, sym], Return["already applied"]];
  If[HEFTFRFixDownValues[def] =!= DownValues[Evaluate[sym]],
    Return["not applied: the loaded " <> name <> " differs from FeynArtsInterface.m"]];
  new = edit[def];   (* the edited text, or a "not applied: ..." status *)
  If[!StringQ[new] || StringStartsQ[new, "not applied"], Return[new]];
  HEFTFRFixParse[new];   (* evaluates the SetDelayed: the redefinition *)
  If[HEFTFRFixDownValues[new] =!= DownValues[Evaluate[sym]],
    Return["not applied: redefinition of " <> name <> " did not take"]];
  "applied"
];

(* 1 *)
HEFTFRFix$EpsBad = "If[Not[Head[temp]===Plus],temp={temp}];";
HEFTFRFix$EpsCases = "Cases[temp,yx_";
HEFTFRFix$EpsGood = "Cases[If[Head[temp]===Plus,temp,{temp}],yx_";

HEFTFRFixEps[] := HEFTFRFixApply["FAStructure2",
  "FAStructure2[vertextype_, FAPartContent_, vertex_, fc_] :=",
  Function[{def, sym}, HEFTFRFixDownValues[
    StringReplace[StringReplace[def, HEFTFRFix$EpsBad -> ""], HEFTFRFix$EpsCases -> HEFTFRFix$EpsGood]
    ] === DownValues[Evaluate[sym]]],
  Function[def,
    If[StringCount[def, HEFTFRFix$EpsBad] =!= 1 || StringCount[def, HEFTFRFix$EpsCases] =!= 2,
      "not applied: the faulty code in FAStructure2 is not in the expected form",
      StringReplace[StringReplace[def, HEFTFRFix$EpsBad -> ""],
        HEFTFRFix$EpsCases -> HEFTFRFix$EpsGood]]]
];

(* 2 *)
HEFTFRFix$SPCase = "SP[__],WriteString[gen,\"ScalarProduct[mom\"<>ToString[struc2[[1]]]<>\",mom\"<>ToString[struc2[[2]]]<>\"]\"];,";
(* The case as the HEFT patch of 2026-05-23 wrote it: Switch does not bind aa/bb, so it wrote the
   literal ScalarProduct[momaa,mombb]^2. *)
HEFTFRFix$SP2Wrong = "\n\t\tPower[SP[aa_,bb_],2],WriteString[gen,\"ScalarProduct[mom\"<>ToString[aa]<>\",mom\"<>ToString[bb]<>\"]^2\"];,";
HEFTFRFix$SP2Case = "\n\t\tPower[SP[_,_],2],WriteString[gen,\"ScalarProduct[mom\"<>ToString[struc2[[1,1]]]<>\",mom\"<>ToString[struc2[[1,2]]]<>\"]^2\"];,";

HEFTFRFixSP2Edit[def_String] := Which[
  StringCount[def, HEFTFRFix$SPCase] =!= 1,
    "not applied: the ScalarProduct case of WriteStructure (in WriteGenCouplings) is not in the expected form",
  StringContainsQ[def, HEFTFRFix$SP2Wrong], StringReplace[def, HEFTFRFix$SP2Wrong -> HEFTFRFix$SP2Case],
  StringContainsQ[def, "Power[SP["], "not applied: WriteStructure already has a ScalarProduct^2 case of unknown form",
  True, StringReplace[def, HEFTFRFix$SPCase -> HEFTFRFix$SPCase <> HEFTFRFix$SP2Case]];

HEFTFRFixSP2[] := HEFTFRFixApply["WriteGenCouplings", "WriteGenCouplings[genfile_,diracIndOpt_]:=",
  Function[{def, sym}, With[{e = HEFTFRFixSP2Edit[def]},
    StringQ[e] && !StringStartsQ[e, "not applied"] &&
      HEFTFRFixDownValues[e] === DownValues[Evaluate[sym]]]],
  HEFTFRFixSP2Edit
];

(* Applies both, prints the result, and keeps it in HEFT$FeynRulesFixes for heft_export.json. *)
HEFTApplyFeynRulesFixes[] := Module[{res},
  res = <|"FAStructure2-eps" -> HEFTFRFixEps[], "WriteStructure-SP2" -> HEFTFRFixSP2[]|>;
  KeyValueMap[Function[{k, v},
    Print[If[StringStartsQ[v, "not applied"], Style["[HEFT] FeynRules fix " <> k <> ": " <> v,
      Orange, Bold], "[HEFT] FeynRules fix " <> k <> ": " <> v]]], res];
  HEFT$FeynRulesFixes = res
];
