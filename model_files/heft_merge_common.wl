(* ::Package:: *)

(* Helpers shared by the two merge engines (2026-10-13, when the merge notebook was split):
     heft_fr_merge.wl          - heft_merging/merge_cached_models.wl (merge cached Lagrangians)
     heft_fr_merge_exports.wl  - heft_merging/merge_exports.wl (merge FeynArts and UFO exports)
   Moved here unchanged from heft_fr_merge.wl, plus HEFT$MergeCheckFeynRulesPath[], the path check
   of HEFT$MergeEnsureFeynRules[] without loading FeynRules (the export merges need the path only for
   the digest of FeynRules' interface files recorded in every heft_export.json). *)

(* Bootstrap shared by every cell that needs the configuration; idempotent, so a cell run out of
   order still works as long as Cell 2 (Configuration) has been evaluated in this kernel. *)
HEFT$MergeBootstrap[] := Module[{},
  If[!ValueQ[HEFT$WorkspaceRoot],
    HEFT$WorkspaceRoot = DirectoryName @ DirectoryName @ ExpandFileName @ $InputFileName
  ];
  Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "heft_defaults.wl"}];
  HEFT$ApplyConfigDefaults[];
  HEFT$CheckExpansionOptions[];
  HEFT$ModelFile       = FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "HEFT_Model.fr"}];
  HEFT$RestrictionsDir = FileNameJoin[{HEFT$WorkspaceRoot, "restrictions"}];
  Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "lheft_cache.wl"}];
  Get @ FileNameJoin[{HEFT$WorkspaceRoot, "model_files", "lheft_merge.wl"}];
  HEFTMergeCheckKeys[];
];

HEFT$MergeCheckFeynRulesPath[] := Module[{},
  If[!StringQ[$FeynRulesPath] || $FeynRulesPath === "",
    Print[Style["[HEFT merge] ERROR: $FeynRulesPath is not set. In Cell 2 (Configuration) set it to the folder of your " <>
      "FeynRules installation, the one containing FeynRules.m.", Red, Bold]];
    Abort[]
  ];
  If[!FileExistsQ[FileNameJoin[{$FeynRulesPath, "FeynRules.m"}]],
    Print[Style["[HEFT merge] ERROR: no FeynRules.m in $FeynRulesPath = " <> $FeynRulesPath <>
      ". Set it in Cell 2 (Configuration) to the folder of your FeynRules installation.", Red, Bold]];
    Abort[]
  ]
];

HEFT$MergeEnsureFeynRules[] := Module[{},
  HEFT$MergeCheckFeynRulesPath[];
  If[!MemberQ[$Packages, "FeynRules`"],
    Get[FileNameJoin[{$FeynRulesPath, "FeynRules.m"}]]
  ]
];

HEFT$MergePrintBanner[title_String] := Print[
  Style["\n" <> StringRepeat["=", 72] <> "\n  " <> title <> "\n" <> StringRepeat["=", 72],
    Bold, FontSize -> 14]
];

HEFT$MergePrintSubsection[title_String] := Print[
  Style["\n  " <> title, Bold, FontSize -> 14]
];

HEFT$MergePrintKV[label_String, heftValue_] := Print[
  "    ", Style[StringPadRight[label <> ":", 22], Bold], ToString[heftValue, InputForm]
];
