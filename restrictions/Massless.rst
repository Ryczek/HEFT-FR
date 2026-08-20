(******************************************************************)
(* HEFT restriction: light fermions massless                      *)
(* Same pattern as the classic SM Massless.rst: set first two     *)
(* lepton generations and first four quark Yukawa masses to zero; *)
(* MLT, MQT, MQB (tau, top, bottom) keep their nominal values.    *)
(******************************************************************)

M$Restrictions = {
  MLE -> 0,
  MLM -> 0,
  MQD -> 0,
  MQU -> 0,
  MQS -> 0,
  MQC -> 0
}
