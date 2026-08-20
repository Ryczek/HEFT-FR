(* ::Package:: *)

(* Custom LaTeX writer for RulesHEFT, used by heft_fr.wl's Cell 6 instead of FeynRules' own
   FeynmanRules[..., TeXOutput -> file] / FRMakeTeXOut. That built-in writer has no hooks for
   what was actually wanted here: filtering the particle/index tables down to only what
   appears in the computed vertices (its own tables list every class/index declared anywhere
   in the model, physical or not), model-specific display names (capital "A" for the photon,
   "W^+"/"W^-" for the charged W), and explicit spacing between multiplied coupling factors
   (TeXForm separates \text{...}-wrapped factors with a literal space character, which LaTeX
   math mode renders with zero visible gap between two "Ord" atoms - the couplings run
   together unless something inserts real spacing glue). It is also the writer with the
   Gluon$1-style dummy-index bug (see HEFT$LatexCleanDollarSymbols below): FeynRules names an
   internal summed index via Mathematica's own $-suffixed unique-symbol convention, and its
   TeXForm renders the literal "$" unescaped, which breaks compilation of that formula. *)

(* Display name for every physical field this model can ever produce as an external leg -
   fixed by fields_LO.fr's ClassMembers (A, Z, W/Wbar, G, H, and the three-generation
   lepton/quark classes), not run-dependent. Anything not in this table (should not happen
   in unitary gauge - no ghosts/Goldstones reach FeynmanRules) falls back to its raw symbol
   name rather than failing. *)
(* {base, flavour-subscript-or-""} rather than one flat display string: HEFT$LatexLeg has to
   attach a further leg-number subscript to each of these, and a name that already carries its
   own subscript (the neutrinos, \nu_e etc.) cannot just get a second "_{...}" tacked onto it -
   "{\nu_e}_{1}" is fine, but "{\bar{\nu}_e}_{1}" is not: \bar (a math *accent*, unlike a plain
   symbol) does not nest cleanly with a pre-existing subscript once regrouped, and pdflatex
   raises "Double subscript" (confirmed with a minimal standalone reproduction - \bar{\nu}_e
   alone compiles, {\bar{\nu}_e}_{1} does not, {\nu_e}_{1} without the bar does). Keeping base
   and flavour-subscript separate lets HEFT$LatexLeg merge the flavour letter and the leg
   number into one combined subscript group instead, e.g. {\bar{\nu}}_{e,1} - never two nested
   "_" groups on the same base regardless of whether it is barred. *)
HEFT$LatexLegParts = <|
  A -> {"A", ""}, Z -> {"Z", ""}, H -> {"H", ""}, G -> {"g", ""},
  W -> {"W^+", ""}, Wbar -> {"W^-", ""},
  u -> {"u", ""}, ubar -> {"\\bar{u}", ""}, c -> {"c", ""}, cbar -> {"\\bar{c}", ""},
  t -> {"t", ""}, tbar -> {"\\bar{t}", ""},
  d -> {"d", ""}, dbar -> {"\\bar{d}", ""}, s -> {"s", ""}, sbar -> {"\\bar{s}", ""},
  b -> {"b", ""}, bbar -> {"\\bar{b}", ""},
  e -> {"e", ""}, ebar -> {"\\bar{e}", ""}, mu -> {"\\mu", ""}, mubar -> {"\\bar{\\mu}", ""},
  ta -> {"\\tau", ""}, tabar -> {"\\bar{\\tau}", ""},
  ve -> {"\\nu", "e"}, vebar -> {"\\bar{\\nu}", "e"},
  vm -> {"\\nu", "\\mu"}, vmbar -> {"\\bar{\\nu}", "\\mu"},
  vt -> {"\\nu", "\\tau"}, vtbar -> {"\\bar{\\nu}", "\\tau"}
|>;

(* Flat "base_{flavour}" display string, derived from HEFT$LatexLegParts so the two never
   drift apart - used only in the summary table below, which does not append a further
   subscript and so does not hit the nesting issue HEFT$LatexLeg works around. *)
HEFT$LatexParticleName = Association[Map[
  Function[part, part -> With[{parts = HEFT$LatexLegParts[part]},
    If[parts[[2]] === "", parts[[1]], parts[[1]] <> "_" <> parts[[2]]]]],
  Keys[HEFT$LatexLegParts]
]];

HEFT$LatexParticleFullName = <|
  A -> "photon", Z -> "Z boson", H -> "Higgs", G -> "gluon",
  W -> "W boson", Wbar -> "W boson (conjugate)",
  u -> "up quark", ubar -> "up antiquark", c -> "charm quark", cbar -> "charm antiquark",
  t -> "top quark", tbar -> "top antiquark",
  d -> "down quark", dbar -> "down antiquark", s -> "strange quark", sbar -> "strange antiquark",
  b -> "bottom quark", bbar -> "bottom antiquark",
  e -> "electron", ebar -> "positron", mu -> "muon", mubar -> "antimuon",
  ta -> "tau", tabar -> "antitau",
  ve -> "electron neutrino", vebar -> "electron antineutrino",
  vm -> "muon neutrino", vmbar -> "muon antineutrino",
  vt -> "tau neutrino", vtbar -> "tau antineutrino"
|>;

(* Every index type the model declares (fields_LO.fr's IndexStyle lines, plus FeynRules'
   builtin Lorentz/Spin) - a run only ever uses a subset; which ones is read off the actual
   vertices at export time, not hardcoded per run. *)
HEFT$LatexIndexInfo = <|
  Lorentz    -> {"\\mu", "Lorentz vector index"},
  Gluon      -> {"a", "SU(3) colour-octet (gluon) index, 1..8"},
  Colour     -> {"m", "SU(3) colour-triplet (quark) index, 1..3"},
  Spin       -> {"s", "Dirac spin index, 1..2"},
  Generation -> {"f", "Fermion generation index, 1..3"},
  SU2W       -> {"j", "SU(2)_W index, 1..3"},
  SU2D       -> {"k", "custodial SU(2) index, 1..3"}
|>;

(* FeynRules names some internal summed indices via Mathematica's own $-suffixed
   Unique[]-style symbols (e.g. Gluon$1, from a repeated colour index in a squared
   structure-constant term). TeXForm renders the literal "$" unescaped, which breaks LaTeX
   compilation of that one formula. Renamed before TeXForm ever sees the expression, rather
   than patched up as a string afterwards, so nothing depends on guessing TeXForm's exact
   (and, empirically, not even self-consistent) escaping of "$". *)
HEFT$LatexCleanDollarSymbols[expr_] := expr /.
  s_Symbol /; StringContainsQ[SymbolName[s], "$"] :>
    Symbol[StringReplace[SymbolName[s], "$" -> ""]];

(* TeXForm separates multiplied \text{...}-wrapped factors with a plain space, which LaTeX
   math mode collapses to zero width between two ordinary atoms - "\text{A} \text{B}" and
   "\text{A}\text{B}" render identically, squashed together. Every run of whitespace in the
   TeXForm output is therefore an implicit-multiplication seam FeynRules/Mathematica meant to
   separate visually; replacing it with "\," (thin space) makes that separation real. Except
   just before a "_" or "^": TeXForm also emits a bare space there for some subscripted bare
   macros (e.g. "\mu _2", "\eta _{...}") - TeX itself silently swallows a space right after a
   control word, so that one already renders fine and is a *subscript* attachment, not a
   multiplication seam; inserting "\," there instead would detach the "_{...}" from its base
   ("\eta\,_{...}" prints an orphaned subscript). The negative lookahead leaves exactly that
   case untouched. The optional leading "\\?" absorbs a lone backslash immediately before the
   whitespace: TeXForm occasionally emits an explicit "\ " (control-space) instead of a bare
   space (seen e.g. between "3" and "2^{3/4}" in a CFTn0 coupling) - without consuming that
   backslash too, "\ " + "\," would leave "\\," in the output, i.e. a literal "\\" line-break
   command followed by a stray comma, which errors outside a tabular/array ("There's no line
   here to end"). Safe to apply broadly otherwise because this string is pure formula content
   - no natural-language text whose incidental spacing needs preserving. *)
HEFT$LatexCoupling[expr_] := Module[{cleaned, tex},
  cleaned = HEFT$LatexCleanDollarSymbols[expr];
  tex = ToString[TeXForm[cleaned]];
  StringReplace[tex, RegularExpression["\\\\?[ \t\n\r]+(?![_^])"] -> "\\,"]
];

(* One subscript group per leg, never two nested ones - see the comment on HEFT$LatexLegParts
   for why "{\bar{\nu}_e}_{1}"-style nesting breaks for the accented (barred) neutrinos. *)
HEFT$LatexLeg[{part_Symbol, n_Integer}] := Module[{base, flavour, sub},
  {base, flavour} = Lookup[HEFT$LatexLegParts, part, {ToString[part], ""}];
  sub = If[flavour === "", ToString[n], flavour <> "," <> ToString[n]];
  "{" <> base <> "}_{" <> sub <> "}"
];

HEFT$WriteLatexRules[rules_List, outFile_String] := Module[
  {strm, usedParticles, usedIndexTypes, byN},

  usedParticles = Sort[Union @@ rules[[All, 1, All, 1]]];
  usedIndexTypes = Sort[Union[Cases[rules[[All, 2]], Index[t_, _] :> t, Infinity]]];
  byN = GroupBy[rules, Length[#[[1]]] &];

  strm = OpenWrite[outFile];

  WriteString[strm, "% Auto-generated by HEFT-FR (model_files/heft_latex_export.wl).\n"];
  WriteString[strm, "\\documentclass[11pt]{article}\n"];
  WriteString[strm, "\\usepackage{amsmath}\n"];
  WriteString[strm, "\\usepackage{amssymb}\n\n"];
  WriteString[strm, "\\newenvironment{respr}{\\sloppy\\begin{flushleft}\\hspace*{0.75cm}\\(}{\\)\\end{flushleft}\\fussy}\n\n"];
  WriteString[strm, "\\setlength{\\topmargin}{-.2cm}\n"];
  WriteString[strm, "\\setlength{\\evensidemargin}{0cm}\n"];
  WriteString[strm, "\\setlength{\\oddsidemargin}{0cm}\n"];
  WriteString[strm, "\\setlength{\\textheight}{8.5in}\n"];
  WriteString[strm, "\\setlength{\\textwidth}{6.4in}\n\n"];
  WriteString[strm, "\\begin{document}\n\n"];

  WriteString[strm, "\\section*{HEFT Feynman rules}\n"];
  WriteString[strm, ToString[Length[rules]], " vertices, generated by FeynRules from \\texttt{LHEFT}.\n\n"];

  WriteString[strm, "\\subsection*{Physical fields}\n\n"];
  WriteString[strm, "\\begin{center}\n\\begin{tabular}{lll}\n\\hline\n"];
  WriteString[strm, "Symbol & \\LaTeX & Description \\\\\n\\hline\n"];
  Do[
    WriteString[strm, "\\texttt{", ToString[p], "} & $", Lookup[HEFT$LatexParticleName, p, ToString[p]],
      "$ & ", Lookup[HEFT$LatexParticleFullName, p, ""], " \\\\\n"],
    {p, usedParticles}
  ];
  WriteString[strm, "\\hline\n\\end{tabular}\n\\end{center}\n\n"];

  WriteString[strm, "\\subsection*{Indices}\n\n"];
  If[usedIndexTypes === {},
    WriteString[strm, "No free tensor/gauge indices appear in this vertex set.\n\n"],
    WriteString[strm, "\\begin{center}\n\\begin{tabular}{lll}\n\\hline\n"];
    WriteString[strm, "Type & Symbol & Description \\\\\n\\hline\n"];
    Do[
      WriteString[strm, ToString[t], " & $", HEFT$LatexIndexInfo[t][[1]], "$ & ", HEFT$LatexIndexInfo[t][[2]], " \\\\\n"],
      {t, usedIndexTypes}
    ];
    WriteString[strm, "\\hline\n\\end{tabular}\n\\end{center}\n\n"];
  ];

  WriteString[strm, "\\subsection*{Vertices}\n\n"];
  Do[
    WriteString[strm, "\\subsubsection*{", ToString[n], "-point vertices}\n\n"];
    WriteString[strm, "\\begin{itemize}\n"];
    Do[
      WriteString[strm, "\\item $", StringRiffle[HEFT$LatexLeg /@ v[[1]], ", "], "$\n"];
      WriteString[strm, "\\begin{respr}\n", HEFT$LatexCoupling[v[[2]]], "\n\\end{respr}\n"],
      {v, byN[n]}
    ];
    WriteString[strm, "\\end{itemize}\n\n"],
    {n, Sort[Keys[byN]]}
  ];

  WriteString[strm, "\\end{document}\n"];
  Close[strm];
];
