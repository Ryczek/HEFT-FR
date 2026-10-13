(* ::Package:: *)

(* Export metadata: output/<format>/<OutputName>/heft_export.json.

   Written by heft_fr.wl Cell 8 next to every FeynArts export and by Cell 7 next to every UFO
   export (since 2026-10-06), and read by the FeynArts merge (fa_merge.wl, merge notebook Cells 9
   and 10) and the UFO merge (ufo_merge.wl, Cells 11 and 12).  An export directory holds only the .mod / .gen
   / .pars files FeynRules writes, and nothing in them says which configuration or operator
   selection produced them - so without this record two exports could not be checked for
   compatibility before being merged.

   The record is the LHEFT cache meta (HEFTLHEFTCacheMeta[], lheft_cache.wl: operators and every
   hashed option, modelDigest included) plus what only an export has:
     maxVertexLegs         - an export-time cut, not in the cache key, but two exports cut at
                             different multiplicities cannot be merged into a consistent model;
     format                - "feynarts" or "ufo";
     ufoInterfaceMD5       - UFO exports only: digest of FeynRules' Interfaces/UFO/*.m, the writer
                             of the files, so that exports from different FeynRules installations
                             are never combined;
     feynArtsInterfaceMD5  - FeynArts exports only: digest of the FeynArtsInterface.m that wrote the
                             files.  The HEFT
                             patch to that file changes the generic (.gen) structures, so exports
                             from a patched and an unpatched FeynRules must never be combined;
     diracIndices          - the fermion form FeynRules actually wrote, read off the .gen:
                             True = explicit Dirac indices (a vertex with more than two
                             fermions, or FeynArtsDiracIndices = True), False = index-free.  Not
                             a configuration key - it follows the operators and
                             FeynArtsDiracIndices - but exports in the two forms cannot be merged,
                             and fa_merge.wl refuses the mix;
     feynRulesFixes        - what feynrules_fixes.wl did before the export (Cell 8), e.g.
                             <|"FAStructure2-eps" -> "applied", ...|>; "none" for an export made
                             without it (before 2026-10-02).  Not a merge key: an export the
                             FAStructure2 bug did not hit is identical either way (TESTS/T38), so
                             fa_merge.wl warns about such sources instead of refusing them.
   Needs lheft_cache.wl (loaded here if it is not). *)

If[DownValues[HEFTLHEFTCacheMeta] === {},
  Get[FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "lheft_cache.wl"}]]
];

HEFTExportMetaFile[exportDir_String] := FileNameJoin[{exportDir, "heft_export.json"}];

(* The keys two exports must agree on to be merged: every cache compare key except the
   operator selection, plus the export-only ones above. *)
HEFTExportGroupKeys["feynarts"] := Join[
  Complement[HEFTLHEFTCacheCompareKeys, {"operators"}],
  {"maxVertexLegs", "format", "feynArtsInterfaceMD5"}
];
HEFTExportGroupKeys["ufo"] := Join[
  Complement[HEFTLHEFTCacheCompareKeys, {"operators"}],
  {"maxVertexLegs", "format", "ufoInterfaceMD5"}
];

(* The fermion form an export was written in (see the header). *)
HEFTExportDiracIndicesQ[exportDir_String] := AnyTrue[FileNames["*.gen", exportDir],
  StringContainsQ[ReadString[#], "KinematicIndices[ F ] = {Dirac}"] &];

(* JSON has no Automatic: stored as the string "Automatic", an integer otherwise. *)
HEFTExportMaxVertexLegsJSON[] := With[{v = If[ValueQ[MaxVertexLegs], MaxVertexLegs, Automatic]},
  If[IntegerQ[v], v, "Automatic"]
];

HEFTExportFeynArtsInterfaceMD5[] := If[StringQ[$FeynRulesPath],
  HEFTLHEFTFileDigest[FileNameJoin[{$FeynRulesPath, "Interfaces", "FeynArtsInterface.m"}]],
  ""
];

(* One digest for all of FeynRules' UFO writer: the digests of Interfaces/UFO/*.m, in file order. *)
HEFTExportUFOInterfaceMD5[] := If[StringQ[$FeynRulesPath],
  With[{files = Sort @ FileNames["*.m", FileNameJoin[{$FeynRulesPath, "Interfaces", "UFO"}]]},
    If[files === {}, "", IntegerString[Hash[StringJoin[HEFTLHEFTFileDigest /@ files], "MD5"], 16, 8]]],
  ""
];

(* The record for an export written NOW with the current configuration. *)
HEFTExportCurrentMeta["feynarts"] := Join[HEFTLHEFTCacheMeta[], <|
  "maxVertexLegs"        -> HEFTExportMaxVertexLegsJSON[],
  "format"               -> "feynarts",
  "feynArtsInterfaceMD5" -> HEFTExportFeynArtsInterfaceMD5[]
|>];
HEFTExportCurrentMeta["ufo"] := Join[HEFTLHEFTCacheMeta[], <|
  "maxVertexLegs"   -> HEFTExportMaxVertexLegsJSON[],
  "format"          -> "ufo",
  "ufoInterfaceMD5" -> HEFTExportUFOInterfaceMD5[]
|>];

HEFTExportWriteMeta[exportDir_String, format_String, extra_Association : <||>] := Export[
  HEFTExportMetaFile[exportDir],
  Join[HEFTExportCurrentMeta[format], <|"created" -> DateString["ISODateTime"]|>,
    (* diracIndices and feynRulesFixes describe the FeynArts writer only. *)
    If[format === "feynarts", <|
      "diracIndices" -> HEFTExportDiracIndicesQ[exportDir],
      "feynRulesFixes" -> If[AssociationQ[HEFT$FeynRulesFixes], HEFT$FeynRulesFixes, "none"]|>, <||>],
    extra],
  "RawJSON"
];

(* None when absent or unreadable.  "RawJSON", not "JSON": the latter returns a List of rules
   on this machine's 14.0.0 kernel (lheft_cache.wl, 2026-07-30). *)
HEFTExportReadMeta[exportDir_String] := Module[{f = HEFTExportMetaFile[exportDir], m},
  If[!FileExistsQ[f], Return[None]];
  m = Quiet @ Check[Import[f, "RawJSON"], $Failed];
  If[Head[m] === Association, m, None]
];

(* The group keys on which a stored record differs from another one. *)
HEFTExportDifferingKeys[stored_Association, current_Association, format_String] := Select[
  HEFTExportGroupKeys[format],
  !KeyExistsQ[stored, #] || !HEFTLHEFTMetaValueEqual[stored[#], current[#]] &
];

(* True when an export (or, for a merged export, every export it was merged from) was written
   with the FAStructure2 fix of feynrules_fixes.wl in place. *)
HEFTExportEpsFixedQ[x_Association] := If[KeyExistsQ[x, "FAStructure2-eps"],
  MemberQ[{"applied", "already applied"}, x["FAStructure2-eps"]],
  x =!= <||> && AllTrue[Values[x], HEFTExportEpsFixedQ]];
HEFTExportEpsFixedQ[_] := False;
