# Merged by HEFT ufo_merge.py: baseline FB_SM, sources FB_PT, FB_PG, FB_PB, FB_SG, FB_SB, FB_S2D, FB_PDH, FB_P1, FB_P2, FB_P3, FB_P4, FB_P5, FB_P6, FB_P12, FB_P13, FB_P14, FB_P17, FB_P18, FB_P20, FB_P21, FB_P22, FB_P23, FB_P24, FB_P26, FB_S1, FB_S2, FB_S3, FB_S4, FB_S5, FB_S6, FB_S7, FB_S8, FB_S9, FB_S15, FB_PWHD1, FB_PWHD2, FB_SWHDT, FB_PW, FB_SW, FB_SWHD, FB_P11, FB_P8, FB_PGHD1, FB_PGHD2, FB_SGHD, FB_PWWW, FB_SWWW
# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Tue 13 Oct 2026 20:18:42


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L

V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_1})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1 ],
             couplings = {(0,0):C.GC_2})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_3})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_4})

V_5 = Vertex(name = 'V_5',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_5})

V_6 = Vertex(name = 'V_6',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV2 ],
             couplings = {(0,0):C.GC_6})

V_7 = Vertex(name = 'V_7',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV1, L.VVVV2, L.VVVV3 ],
             couplings = {(0,0):C.GC_7,(1,1):C.GC_7,(2,2):C.GC_7})

V_8 = Vertex(name = 'V_8',
             particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.FFSS1 ],
             couplings = {(0,0):C.GC_8})

V_9 = Vertex(name = 'V_9',
             particles = [ P.mu__plus__, P.e__minus__, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.FFSS2, L.FFSS3 ],
             couplings = {(0,0):C.GC_9,(0,1):C.GC_10})

V_10 = Vertex(name = 'V_10',
              particles = [ P.ta__plus__, P.e__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_11,(0,1):C.GC_12})

V_11 = Vertex(name = 'V_11',
              particles = [ P.e__plus__, P.mu__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_10,(0,1):C.GC_9})

V_12 = Vertex(name = 'V_12',
              particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1 ],
              couplings = {(0,0):C.GC_13})

V_13 = Vertex(name = 'V_13',
              particles = [ P.ta__plus__, P.mu__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_14,(0,1):C.GC_15})

V_14 = Vertex(name = 'V_14',
              particles = [ P.e__plus__, P.ta__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_12,(0,1):C.GC_11})

V_15 = Vertex(name = 'V_15',
              particles = [ P.mu__plus__, P.ta__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_15,(0,1):C.GC_14})

V_16 = Vertex(name = 'V_16',
              particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSS1, L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_16,(0,1):C.GC_452,(0,2):C.GC_452})

V_17 = Vertex(name = 'V_17',
              particles = [ P.e__plus__, P.e__minus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSSS1, L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_17,(0,1):C.GC_395,(0,2):C.GC_395})

V_18 = Vertex(name = 'V_18',
              particles = [ P.mu__plus__, P.e__minus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_18,(0,1):C.GC_19})

V_19 = Vertex(name = 'V_19',
              particles = [ P.ta__plus__, P.e__minus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_20,(0,1):C.GC_21})

V_20 = Vertex(name = 'V_20',
              particles = [ P.e__plus__, P.mu__minus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_19,(0,1):C.GC_18})

V_21 = Vertex(name = 'V_21',
              particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSSS1, L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_22,(0,1):C.GC_137,(0,2):C.GC_137})

V_22 = Vertex(name = 'V_22',
              particles = [ P.ta__plus__, P.mu__minus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_23,(0,1):C.GC_24})

V_23 = Vertex(name = 'V_23',
              particles = [ P.e__plus__, P.ta__minus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_21,(0,1):C.GC_20})

V_24 = Vertex(name = 'V_24',
              particles = [ P.mu__plus__, P.ta__minus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_24,(0,1):C.GC_23})

V_25 = Vertex(name = 'V_25',
              particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFSSS1, L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_25,(0,1):C.GC_138,(0,2):C.GC_138})

V_26 = Vertex(name = 'V_26',
              particles = [ P.u__tilde__, P.u, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3, L.FFSS1 ],
              couplings = {(0,0):C.GC_26,(0,1):C.GC_26,(0,2):C.GC_242})

V_27 = Vertex(name = 'V_27',
              particles = [ P.c__tilde__, P.u, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_27,(0,1):C.GC_28})

V_28 = Vertex(name = 'V_28',
              particles = [ P.t__tilde__, P.u, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_29,(0,1):C.GC_30})

V_29 = Vertex(name = 'V_29',
              particles = [ P.u__tilde__, P.c, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_28,(0,1):C.GC_27})

V_30 = Vertex(name = 'V_30',
              particles = [ P.c__tilde__, P.c, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_31,(0,1):C.GC_31})

V_31 = Vertex(name = 'V_31',
              particles = [ P.t__tilde__, P.c, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_32,(0,1):C.GC_33})

V_32 = Vertex(name = 'V_32',
              particles = [ P.u__tilde__, P.t, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_30,(0,1):C.GC_29})

V_33 = Vertex(name = 'V_33',
              particles = [ P.c__tilde__, P.t, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_33,(0,1):C.GC_32})

V_34 = Vertex(name = 'V_34',
              particles = [ P.t__tilde__, P.t, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_34,(0,1):C.GC_34})

V_35 = Vertex(name = 'V_35',
              particles = [ P.u__tilde__, P.u, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_35,(0,1):C.GC_35})

V_36 = Vertex(name = 'V_36',
              particles = [ P.c__tilde__, P.u, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_36,(0,1):C.GC_37})

V_37 = Vertex(name = 'V_37',
              particles = [ P.t__tilde__, P.u, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_38,(0,1):C.GC_39})

V_38 = Vertex(name = 'V_38',
              particles = [ P.u__tilde__, P.c, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_37,(0,1):C.GC_36})

V_39 = Vertex(name = 'V_39',
              particles = [ P.c__tilde__, P.c, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_40,(0,1):C.GC_40})

V_40 = Vertex(name = 'V_40',
              particles = [ P.t__tilde__, P.c, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_41,(0,1):C.GC_42})

V_41 = Vertex(name = 'V_41',
              particles = [ P.u__tilde__, P.t, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_39,(0,1):C.GC_38})

V_42 = Vertex(name = 'V_42',
              particles = [ P.c__tilde__, P.t, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_42,(0,1):C.GC_41})

V_43 = Vertex(name = 'V_43',
              particles = [ P.t__tilde__, P.t, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_43,(0,1):C.GC_43})

V_44 = Vertex(name = 'V_44',
              particles = [ P.d__tilde__, P.d, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_44,(0,1):C.GC_44})

V_45 = Vertex(name = 'V_45',
              particles = [ P.s__tilde__, P.d, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_45,(0,1):C.GC_46})

V_46 = Vertex(name = 'V_46',
              particles = [ P.b__tilde__, P.d, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_47,(0,1):C.GC_48})

V_47 = Vertex(name = 'V_47',
              particles = [ P.d__tilde__, P.s, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_46,(0,1):C.GC_45})

V_48 = Vertex(name = 'V_48',
              particles = [ P.b__tilde__, P.s, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_49,(0,1):C.GC_50})

V_49 = Vertex(name = 'V_49',
              particles = [ P.d__tilde__, P.b, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_48,(0,1):C.GC_47})

V_50 = Vertex(name = 'V_50',
              particles = [ P.s__tilde__, P.b, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3 ],
              couplings = {(0,0):C.GC_50,(0,1):C.GC_49})

V_51 = Vertex(name = 'V_51',
              particles = [ P.b__tilde__, P.b, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSS2, L.FFSS3, L.FFSS1 ],
              couplings = {(0,0):C.GC_51,(0,1):C.GC_51,(0,2):C.GC_243})

V_52 = Vertex(name = 'V_52',
              particles = [ P.d__tilde__, P.d, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3, L.FFSSS1 ],
              couplings = {(0,0):C.GC_52,(0,1):C.GC_52,(0,2):C.GC_244})

V_53 = Vertex(name = 'V_53',
              particles = [ P.s__tilde__, P.d, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_53,(0,1):C.GC_54})

V_54 = Vertex(name = 'V_54',
              particles = [ P.b__tilde__, P.d, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_55,(0,1):C.GC_56})

V_55 = Vertex(name = 'V_55',
              particles = [ P.d__tilde__, P.s, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_54,(0,1):C.GC_53})

V_56 = Vertex(name = 'V_56',
              particles = [ P.s__tilde__, P.s, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3, L.FFSSS1 ],
              couplings = {(0,0):C.GC_57,(0,1):C.GC_57,(0,2):C.GC_245})

V_57 = Vertex(name = 'V_57',
              particles = [ P.b__tilde__, P.s, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_58,(0,1):C.GC_59})

V_58 = Vertex(name = 'V_58',
              particles = [ P.d__tilde__, P.b, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_56,(0,1):C.GC_55})

V_59 = Vertex(name = 'V_59',
              particles = [ P.s__tilde__, P.b, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3 ],
              couplings = {(0,0):C.GC_59,(0,1):C.GC_58})

V_60 = Vertex(name = 'V_60',
              particles = [ P.b__tilde__, P.b, P.H, P.H, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFSSS2, L.FFSSS3, L.FFSSS1 ],
              couplings = {(0,0):C.GC_60,(0,1):C.GC_60,(0,2):C.GC_246})

V_61 = Vertex(name = 'V_61',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_61,(0,1):C.GC_61,(0,2):C.GC_247})

V_62 = Vertex(name = 'V_62',
              particles = [ P.d__tilde__, P.d, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_62,(0,1):C.GC_62,(0,2):C.GC_248})

V_63 = Vertex(name = 'V_63',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_63,(0,1):C.GC_63,(0,2):C.GC_249})

V_64 = Vertex(name = 'V_64',
              particles = [ P.s__tilde__, P.s, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_64,(0,1):C.GC_64,(0,2):C.GC_250})

V_65 = Vertex(name = 'V_65',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_65,(0,1):C.GC_65,(0,2):C.GC_162})

V_66 = Vertex(name = 'V_66',
              particles = [ P.b__tilde__, P.b, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_66,(0,1):C.GC_66,(0,2):C.GC_163})

V_67 = Vertex(name = 'V_67',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_67,(0,1):C.GC_67,(0,2):C.GC_139})

V_68 = Vertex(name = 'V_68',
              particles = [ P.e__plus__, P.e__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_68,(0,1):C.GC_68,(0,2):C.GC_140})

V_69 = Vertex(name = 'V_69',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_69,(0,1):C.GC_69,(0,2):C.GC_141})

V_70 = Vertex(name = 'V_70',
              particles = [ P.mu__plus__, P.mu__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_70,(0,1):C.GC_70,(0,2):C.GC_142})

V_71 = Vertex(name = 'V_71',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_71,(0,1):C.GC_71,(0,2):C.GC_143})

V_72 = Vertex(name = 'V_72',
              particles = [ P.ta__plus__, P.ta__minus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_72,(0,1):C.GC_72,(0,2):C.GC_144})

V_73 = Vertex(name = 'V_73',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_73,(0,1):C.GC_73,(0,2):C.GC_145})

V_74 = Vertex(name = 'V_74',
              particles = [ P.u__tilde__, P.u, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_74,(0,1):C.GC_74,(0,2):C.GC_146})

V_75 = Vertex(name = 'V_75',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_75,(0,1):C.GC_75,(0,2):C.GC_147})

V_76 = Vertex(name = 'V_76',
              particles = [ P.c__tilde__, P.c, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS1, L.FFS2, L.FFS3 ],
              couplings = {(0,0):C.GC_76,(0,1):C.GC_76,(0,2):C.GC_148})

V_77 = Vertex(name = 'V_77',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_77})

V_78 = Vertex(name = 'V_78',
              particles = [ P.t__tilde__, P.t, P.H ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFS3 ],
              couplings = {(0,0):C.GC_78})

V_79 = Vertex(name = 'V_79',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_79})

V_80 = Vertex(name = 'V_80',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_80})

V_81 = Vertex(name = 'V_81',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_81,(0,1):C.GC_435,(0,2):C.GC_450})

V_82 = Vertex(name = 'V_82',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_82})

V_83 = Vertex(name = 'V_83',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_83,(0,1):C.GC_436,(0,2):C.GC_451})

V_84 = Vertex(name = 'V_84',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS4 ],
              couplings = {(0,0):C.GC_84,(0,1):C.GC_434,(0,2):C.GC_449})

V_85 = Vertex(name = 'V_85',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV4 ],
              couplings = {(0,0):C.GC_85})

V_86 = Vertex(name = 'V_86',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV2 ],
              couplings = {(0,0):C.GC_86})

V_87 = Vertex(name = 'V_87',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV4 ],
              couplings = {(0,0):C.GC_87})

V_88 = Vertex(name = 'V_88',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_88})

V_89 = Vertex(name = 'V_89',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1 ],
              couplings = {(0,0):C.GC_89})

V_90 = Vertex(name = 'V_90',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2, L.VVSS4 ],
              couplings = {(0,0):C.GC_90,(0,1):C.GC_160,(0,2):C.GC_177})

V_91 = Vertex(name = 'V_91',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_91})

V_92 = Vertex(name = 'V_92',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1, L.VVS2, L.VVS4 ],
              couplings = {(0,0):C.GC_92,(0,1):C.GC_161,(0,2):C.GC_178})

V_93 = Vertex(name = 'V_93',
              particles = [ P.Z, P.Z, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1, L.VVSSS2, L.VVSSS4 ],
              couplings = {(0,0):C.GC_93,(0,1):C.GC_159,(0,2):C.GC_176})

V_94 = Vertex(name = 'V_94',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV4 ],
              couplings = {(0,0):C.GC_94})

V_95 = Vertex(name = 'V_95',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_95})

V_96 = Vertex(name = 'V_96',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_95})

V_97 = Vertex(name = 'V_97',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_95})

V_98 = Vertex(name = 'V_98',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV6 ],
              couplings = {(0,0):C.GC_96,(0,1):C.GC_97,(0,2):C.GC_230,(0,3):C.GC_305})

V_99 = Vertex(name = 'V_99',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3, L.FFV4, L.FFV6 ],
              couplings = {(0,0):C.GC_96,(0,1):C.GC_97,(0,2):C.GC_230,(0,3):C.GC_305})

V_100 = Vertex(name = 'V_100',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_98,(0,1):C.GC_99,(0,2):C.GC_149})

V_101 = Vertex(name = 'V_101',
               particles = [ P.d__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_100})

V_102 = Vertex(name = 'V_102',
               particles = [ P.s__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_101})

V_103 = Vertex(name = 'V_103',
               particles = [ P.b__tilde__, P.u, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_102})

V_104 = Vertex(name = 'V_104',
               particles = [ P.d__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_103})

V_105 = Vertex(name = 'V_105',
               particles = [ P.s__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_104})

V_106 = Vertex(name = 'V_106',
               particles = [ P.b__tilde__, P.c, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_105})

V_107 = Vertex(name = 'V_107',
               particles = [ P.d__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_106})

V_108 = Vertex(name = 'V_108',
               particles = [ P.s__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_107})

V_109 = Vertex(name = 'V_109',
               particles = [ P.b__tilde__, P.t, P.W__minus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_108})

V_110 = Vertex(name = 'V_110',
               particles = [ P.u__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_109})

V_111 = Vertex(name = 'V_111',
               particles = [ P.c__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_110})

V_112 = Vertex(name = 'V_112',
               particles = [ P.t__tilde__, P.d, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_111})

V_113 = Vertex(name = 'V_113',
               particles = [ P.u__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_112})

V_114 = Vertex(name = 'V_114',
               particles = [ P.c__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_113})

V_115 = Vertex(name = 'V_115',
               particles = [ P.t__tilde__, P.s, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_114})

V_116 = Vertex(name = 'V_116',
               particles = [ P.u__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_115})

V_117 = Vertex(name = 'V_117',
               particles = [ P.c__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_116})

V_118 = Vertex(name = 'V_118',
               particles = [ P.t__tilde__, P.b, P.W__plus__ ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_117})

V_119 = Vertex(name = 'V_119',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_118})

V_120 = Vertex(name = 'V_120',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_118})

V_121 = Vertex(name = 'V_121',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_118})

V_122 = Vertex(name = 'V_122',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_119,(0,1):C.GC_120,(0,2):C.GC_150})

V_123 = Vertex(name = 'V_123',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_119,(0,1):C.GC_120,(0,2):C.GC_150})

V_124 = Vertex(name = 'V_124',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV4, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_121,(0,1):C.GC_122,(0,2):C.GC_151})

V_125 = Vertex(name = 'V_125',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_123})

V_126 = Vertex(name = 'V_126',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_123})

V_127 = Vertex(name = 'V_127',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_123})

V_128 = Vertex(name = 'V_128',
               particles = [ P.e__plus__, P.ve, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_124})

V_129 = Vertex(name = 'V_129',
               particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_124})

V_130 = Vertex(name = 'V_130',
               particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_124})

V_131 = Vertex(name = 'V_131',
               particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_124})

V_132 = Vertex(name = 'V_132',
               particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_124})

V_133 = Vertex(name = 'V_133',
               particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_124})

V_134 = Vertex(name = 'V_134',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_125})

V_135 = Vertex(name = 'V_135',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_125})

V_136 = Vertex(name = 'V_136',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_125})

V_137 = Vertex(name = 'V_137',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV5, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_126,(0,1):C.GC_127,(0,2):C.GC_152})

V_138 = Vertex(name = 'V_138',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV5, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_126,(0,1):C.GC_127,(0,2):C.GC_152})

V_139 = Vertex(name = 'V_139',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV5, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_126,(0,1):C.GC_127,(0,2):C.GC_152})

V_140 = Vertex(name = 'V_140',
               particles = [ P.u__tilde__, P.u, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_128})

V_141 = Vertex(name = 'V_141',
               particles = [ P.c__tilde__, P.c, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_128})

V_142 = Vertex(name = 'V_142',
               particles = [ P.t__tilde__, P.t, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_128})

V_143 = Vertex(name = 'V_143',
               particles = [ P.d__tilde__, P.d, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_128})

V_144 = Vertex(name = 'V_144',
               particles = [ P.s__tilde__, P.s, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_128})

V_145 = Vertex(name = 'V_145',
               particles = [ P.b__tilde__, P.b, P.g ],
               color = [ 'T(3,2,1)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_128})

V_146 = Vertex(name = 'V_146',
               particles = [ P.g, P.g, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVSSS2, L.VVSSS3 ],
               couplings = {(0,0):C.GC_129,(0,1):C.GC_164})

V_147 = Vertex(name = 'V_147',
               particles = [ P.g, P.g, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVSS2, L.VVSS3 ],
               couplings = {(0,0):C.GC_130,(0,1):C.GC_165})

V_148 = Vertex(name = 'V_148',
               particles = [ P.g, P.g, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVS2, L.VVS3 ],
               couplings = {(0,0):C.GC_131,(0,1):C.GC_166})

V_149 = Vertex(name = 'V_149',
               particles = [ P.g, P.g, P.g, P.H, P.H, P.H ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVVSSS1, L.VVVSSS2 ],
               couplings = {(0,0):C.GC_132,(0,1):C.GC_167})

V_150 = Vertex(name = 'V_150',
               particles = [ P.g, P.g, P.g, P.H, P.H ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVVSS1, L.VVVSS2 ],
               couplings = {(0,0):C.GC_133,(0,1):C.GC_168})

V_151 = Vertex(name = 'V_151',
               particles = [ P.g, P.g, P.g, P.H ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVVS1, L.VVVS2 ],
               couplings = {(0,0):C.GC_134,(0,1):C.GC_169})

V_152 = Vertex(name = 'V_152',
               particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
               color = [ 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
               lorentz = [ L.VVVVSS1, L.VVVVSS2, L.VVVVSS3 ],
               couplings = {(0,0):C.GC_135,(1,1):C.GC_135,(2,2):C.GC_135})

V_153 = Vertex(name = 'V_153',
               particles = [ P.g, P.g, P.g, P.g, P.H ],
               color = [ 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
               lorentz = [ L.VVVVS1, L.VVVVS2, L.VVVVS3 ],
               couplings = {(0,0):C.GC_136,(1,1):C.GC_136,(2,2):C.GC_136})

V_154 = Vertex(name = 'V_154',
               particles = [ P.a, P.a, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS2, L.VVSSS4 ],
               couplings = {(0,0):C.GC_153,(0,1):C.GC_170})

V_155 = Vertex(name = 'V_155',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS2, L.VVSS4 ],
               couplings = {(0,0):C.GC_154,(0,1):C.GC_171})

V_156 = Vertex(name = 'V_156',
               particles = [ P.a, P.a, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS2, L.VVS4 ],
               couplings = {(0,0):C.GC_155,(0,1):C.GC_172})

V_157 = Vertex(name = 'V_157',
               particles = [ P.a, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS2, L.VVSSS4, L.VVSSS9, L.VVSSS10 ],
               couplings = {(0,0):C.GC_156,(0,1):C.GC_173,(0,2):C.GC_329,(0,3):C.GC_330})

V_158 = Vertex(name = 'V_158',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS2, L.VVSS4, L.VVSS9, L.VVSS10 ],
               couplings = {(0,0):C.GC_157,(0,1):C.GC_174,(0,2):C.GC_331,(0,3):C.GC_332})

V_159 = Vertex(name = 'V_159',
               particles = [ P.a, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS2, L.VVS4, L.VVS7, L.VVS8 ],
               couplings = {(0,0):C.GC_158,(0,1):C.GC_175,(0,2):C.GC_333,(0,3):C.GC_334})

V_160 = Vertex(name = 'V_160',
               particles = [ P.e__plus__, P.e__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS4 ],
               couplings = {(0,0):C.GC_179})

V_161 = Vertex(name = 'V_161',
               particles = [ P.mu__plus__, P.mu__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS4 ],
               couplings = {(0,0):C.GC_180})

V_162 = Vertex(name = 'V_162',
               particles = [ P.ta__plus__, P.ta__minus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFSS4 ],
               couplings = {(0,0):C.GC_181})

V_163 = Vertex(name = 'V_163',
               particles = [ P.u__tilde__, P.u, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_182,(0,1):C.GC_183})

V_164 = Vertex(name = 'V_164',
               particles = [ P.c__tilde__, P.c, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_184,(0,1):C.GC_185})

V_165 = Vertex(name = 'V_165',
               particles = [ P.t__tilde__, P.t, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_186,(0,1):C.GC_187})

V_166 = Vertex(name = 'V_166',
               particles = [ P.d__tilde__, P.d, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_188,(0,1):C.GC_189})

V_167 = Vertex(name = 'V_167',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_190,(0,1):C.GC_191})

V_168 = Vertex(name = 'V_168',
               particles = [ P.b__tilde__, P.b, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS2, L.FFSS3 ],
               couplings = {(0,0):C.GC_192,(0,1):C.GC_193})

V_169 = Vertex(name = 'V_169',
               particles = [ P.d__tilde__, P.d, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_194,(0,1):C.GC_195})

V_170 = Vertex(name = 'V_170',
               particles = [ P.s__tilde__, P.s, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_196,(0,1):C.GC_197})

V_171 = Vertex(name = 'V_171',
               particles = [ P.b__tilde__, P.b, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_198,(0,1):C.GC_199})

V_172 = Vertex(name = 'V_172',
               particles = [ P.e__plus__, P.e__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_200,(0,1):C.GC_201})

V_173 = Vertex(name = 'V_173',
               particles = [ P.mu__plus__, P.mu__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_202,(0,1):C.GC_203})

V_174 = Vertex(name = 'V_174',
               particles = [ P.ta__plus__, P.ta__minus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_204,(0,1):C.GC_205})

V_175 = Vertex(name = 'V_175',
               particles = [ P.u__tilde__, P.u, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_206,(0,1):C.GC_207})

V_176 = Vertex(name = 'V_176',
               particles = [ P.c__tilde__, P.c, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS1, L.FFS2 ],
               couplings = {(0,0):C.GC_208,(0,1):C.GC_209})

V_177 = Vertex(name = 'V_177',
               particles = [ P.t__tilde__, P.t, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFS4 ],
               couplings = {(0,0):C.GC_210})

V_178 = Vertex(name = 'V_178',
               particles = [ P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSS1 ],
               couplings = {(0,0):C.GC_211})

V_179 = Vertex(name = 'V_179',
               particles = [ P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VSSS1 ],
               couplings = {(0,0):C.GC_212})

V_180 = Vertex(name = 'V_180',
               particles = [ P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSS2 ],
               couplings = {(0,0):C.GC_213})

V_181 = Vertex(name = 'V_181',
               particles = [ P.H, P.H, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSSSS1 ],
               couplings = {(0,0):C.GC_214})

V_182 = Vertex(name = 'V_182',
               particles = [ P.H, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.SSSSS1 ],
               couplings = {(0,0):C.GC_215})

V_183 = Vertex(name = 'V_183',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV3, L.VVV4, L.VVV7, L.VVV10 ],
               couplings = {(0,0):C.GC_216,(0,1):C.GC_217,(0,2):C.GC_300,(0,3):C.GC_335})

V_184 = Vertex(name = 'V_184',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV4 ],
               couplings = {(0,0):C.GC_218})

V_185 = Vertex(name = 'V_185',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS3, L.VVVSSS9, L.VVVSSS1, L.VVVSSS22 ],
               couplings = {(0,0):C.GC_219,(0,1):C.GC_337,(0,2):C.GC_437,(0,3):C.GC_453})

V_186 = Vertex(name = 'V_186',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS3, L.VVVSS9, L.VVVSS1, L.VVVSS22 ],
               couplings = {(0,0):C.GC_220,(0,1):C.GC_338,(0,2):C.GC_438,(0,3):C.GC_454})

V_187 = Vertex(name = 'V_187',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS3, L.VVVS9, L.VVVS1, L.VVVS18 ],
               couplings = {(0,0):C.GC_221,(0,1):C.GC_339,(0,2):C.GC_439,(0,3):C.GC_455})

V_188 = Vertex(name = 'V_188',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV5, L.VVV6, L.VVV8, L.VVV11 ],
               couplings = {(0,0):C.GC_222,(0,1):C.GC_223,(0,2):C.GC_301,(0,3):C.GC_336})

V_189 = Vertex(name = 'V_189',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS4, L.VVVSSS10, L.VVVSSS1, L.VVVSSS22 ],
               couplings = {(0,0):C.GC_224,(0,1):C.GC_340,(0,2):C.GC_442,(0,3):C.GC_456})

V_190 = Vertex(name = 'V_190',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS4, L.VVVSS10, L.VVVSS1, L.VVVSS22 ],
               couplings = {(0,0):C.GC_225,(0,1):C.GC_341,(0,2):C.GC_443,(0,3):C.GC_457})

V_191 = Vertex(name = 'V_191',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS4, L.VVVS10, L.VVVS1, L.VVVS18 ],
               couplings = {(0,0):C.GC_226,(0,1):C.GC_342,(0,2):C.GC_444,(0,3):C.GC_458})

V_192 = Vertex(name = 'V_192',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_227})

V_193 = Vertex(name = 'V_193',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV4 ],
               couplings = {(0,0):C.GC_228})

V_194 = Vertex(name = 'V_194',
               particles = [ P.u__tilde__, P.u, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_229})

V_195 = Vertex(name = 'V_195',
               particles = [ P.c__tilde__, P.c, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_229})

V_196 = Vertex(name = 'V_196',
               particles = [ P.t__tilde__, P.t, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_229})

V_197 = Vertex(name = 'V_197',
               particles = [ P.u__tilde__, P.u, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_231,(0,1):C.GC_232,(0,2):C.GC_306})

V_198 = Vertex(name = 'V_198',
               particles = [ P.c__tilde__, P.c, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV2, L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_231,(0,1):C.GC_232,(0,2):C.GC_306})

V_199 = Vertex(name = 'V_199',
               particles = [ P.t__tilde__, P.t, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_233,(0,1):C.GC_234})

V_200 = Vertex(name = 'V_200',
               particles = [ P.d__tilde__, P.d, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_235})

V_201 = Vertex(name = 'V_201',
               particles = [ P.s__tilde__, P.s, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_235})

V_202 = Vertex(name = 'V_202',
               particles = [ P.b__tilde__, P.b, P.a ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_235})

V_203 = Vertex(name = 'V_203',
               particles = [ P.d__tilde__, P.d, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_236,(0,1):C.GC_237})

V_204 = Vertex(name = 'V_204',
               particles = [ P.s__tilde__, P.s, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_236,(0,1):C.GC_237})

V_205 = Vertex(name = 'V_205',
               particles = [ P.b__tilde__, P.b, P.Z ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_236,(0,1):C.GC_237})

V_206 = Vertex(name = 'V_206',
               particles = [ P.ve__tilde__, P.ve, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_238})

V_207 = Vertex(name = 'V_207',
               particles = [ P.vm__tilde__, P.vm, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_238})

V_208 = Vertex(name = 'V_208',
               particles = [ P.vt__tilde__, P.vt, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3 ],
               couplings = {(0,0):C.GC_238})

V_209 = Vertex(name = 'V_209',
               particles = [ P.e__plus__, P.e__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_239})

V_210 = Vertex(name = 'V_210',
               particles = [ P.mu__plus__, P.mu__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_239})

V_211 = Vertex(name = 'V_211',
               particles = [ P.ta__plus__, P.ta__minus__, P.a ],
               color = [ '1' ],
               lorentz = [ L.FFV1 ],
               couplings = {(0,0):C.GC_239})

V_212 = Vertex(name = 'V_212',
               particles = [ P.e__plus__, P.e__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_241})

V_213 = Vertex(name = 'V_213',
               particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_241})

V_214 = Vertex(name = 'V_214',
               particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.FFV3, L.FFV6 ],
               couplings = {(0,0):C.GC_240,(0,1):C.GC_241})

V_215 = Vertex(name = 'V_215',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV3 ],
               couplings = {(0,0):C.GC_251})

V_216 = Vertex(name = 'V_216',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS3, L.VVVSSS6, L.VVVSSS11, L.VVVSSS16 ],
               couplings = {(0,0):C.GC_252,(0,1):C.GC_285,(0,2):C.GC_352,(0,3):C.GC_377})

V_217 = Vertex(name = 'V_217',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS3, L.VVVSS6, L.VVVSS11, L.VVVSS16 ],
               couplings = {(0,0):C.GC_253,(0,1):C.GC_286,(0,2):C.GC_353,(0,3):C.GC_378})

V_218 = Vertex(name = 'V_218',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS3, L.VVVS6, L.VVVS11, L.VVVS16 ],
               couplings = {(0,0):C.GC_254,(0,1):C.GC_287,(0,2):C.GC_354,(0,3):C.GC_379})

V_219 = Vertex(name = 'V_219',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV6, L.VVV5, L.VVV2, L.VVV9, L.VVV12 ],
               couplings = {(0,0):C.GC_255,(0,1):C.GC_259,(0,2):C.GC_260,(0,3):C.GC_307,(0,4):C.GC_358})

V_220 = Vertex(name = 'V_220',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS4, L.VVVSSS5, L.VVVSSS1, L.VVVSSS7, L.VVVSSS8, L.VVVSSS11, L.VVVSSS12, L.VVVSSS17 ],
               couplings = {(0,0):C.GC_256,(0,1):C.GC_261,(0,2):C.GC_262,(0,3):C.GC_288,(0,4):C.GC_308,(0,5):C.GC_355,(0,6):C.GC_360,(0,7):C.GC_380})

V_221 = Vertex(name = 'V_221',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS4, L.VVVSS5, L.VVVSS1, L.VVVSS7, L.VVVSS8, L.VVVSS11, L.VVVSS12, L.VVVSS17 ],
               couplings = {(0,0):C.GC_257,(0,1):C.GC_263,(0,2):C.GC_264,(0,3):C.GC_289,(0,4):C.GC_309,(0,5):C.GC_356,(0,6):C.GC_361,(0,7):C.GC_381})

V_222 = Vertex(name = 'V_222',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS4, L.VVVS5, L.VVVS1, L.VVVS7, L.VVVS8, L.VVVS11, L.VVVS12, L.VVVS17 ],
               couplings = {(0,0):C.GC_258,(0,1):C.GC_265,(0,2):C.GC_266,(0,3):C.GC_290,(0,4):C.GC_310,(0,5):C.GC_357,(0,6):C.GC_362,(0,7):C.GC_382})

V_223 = Vertex(name = 'V_223',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV4 ],
               couplings = {(0,0):C.GC_267})

V_224 = Vertex(name = 'V_224',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS4 ],
               couplings = {(0,0):C.GC_268})

V_225 = Vertex(name = 'V_225',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS4 ],
               couplings = {(0,0):C.GC_269})

V_226 = Vertex(name = 'V_226',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5, L.VVVV9, L.VVVV3 ],
               couplings = {(0,0):C.GC_270,(0,1):C.GC_311,(0,2):C.GC_359})

V_227 = Vertex(name = 'V_227',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS5, L.VVVVSS9, L.VVVVSS3 ],
               couplings = {(0,0):C.GC_271,(0,1):C.GC_312,(0,2):C.GC_363})

V_228 = Vertex(name = 'V_228',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS5, L.VVVVS9, L.VVVVS3 ],
               couplings = {(0,0):C.GC_272,(0,1):C.GC_313,(0,2):C.GC_364})

V_229 = Vertex(name = 'V_229',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV4 ],
               couplings = {(0,0):C.GC_273})

V_230 = Vertex(name = 'V_230',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS4 ],
               couplings = {(0,0):C.GC_274})

V_231 = Vertex(name = 'V_231',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS4 ],
               couplings = {(0,0):C.GC_275})

V_232 = Vertex(name = 'V_232',
               particles = [ P.a, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS5, L.VVSSS11 ],
               couplings = {(0,0):C.GC_276,(0,1):C.GC_343})

V_233 = Vertex(name = 'V_233',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS5, L.VVSS11 ],
               couplings = {(0,0):C.GC_277,(0,1):C.GC_344})

V_234 = Vertex(name = 'V_234',
               particles = [ P.a, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS5, L.VVS9 ],
               couplings = {(0,0):C.GC_278,(0,1):C.GC_345})

V_235 = Vertex(name = 'V_235',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS6, L.VVSSS12 ],
               couplings = {(0,0):C.GC_279,(0,1):C.GC_346})

V_236 = Vertex(name = 'V_236',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS6, L.VVSS12 ],
               couplings = {(0,0):C.GC_280,(0,1):C.GC_347})

V_237 = Vertex(name = 'V_237',
               particles = [ P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS6, L.VVS10 ],
               couplings = {(0,0):C.GC_281,(0,1):C.GC_348})

V_238 = Vertex(name = 'V_238',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS6, L.VVSSS12, L.VVSSS13 ],
               couplings = {(0,0):C.GC_282,(0,1):C.GC_349,(0,2):C.GC_374})

V_239 = Vertex(name = 'V_239',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS6, L.VVSS12, L.VVSS13 ],
               couplings = {(0,0):C.GC_283,(0,1):C.GC_350,(0,2):C.GC_375})

V_240 = Vertex(name = 'V_240',
               particles = [ P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVS6, L.VVS10, L.VVS11 ],
               couplings = {(0,0):C.GC_284,(0,1):C.GC_351,(0,2):C.GC_376})

V_241 = Vertex(name = 'V_241',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV6, L.VVVV10 ],
               couplings = {(0,0):C.GC_291,(0,1):C.GC_475})

V_242 = Vertex(name = 'V_242',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS6, L.VVVVSS17 ],
               couplings = {(0,0):C.GC_292,(0,1):C.GC_476})

V_243 = Vertex(name = 'V_243',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS6, L.VVVVS10 ],
               couplings = {(0,0):C.GC_293,(0,1):C.GC_477})

V_244 = Vertex(name = 'V_244',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV7, L.VVVV6 ],
               couplings = {(0,0):C.GC_294,(0,1):C.GC_326})

V_245 = Vertex(name = 'V_245',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS7, L.VVVVSS6 ],
               couplings = {(0,0):C.GC_295,(0,1):C.GC_327})

V_246 = Vertex(name = 'V_246',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS7, L.VVVVS6 ],
               couplings = {(0,0):C.GC_296,(0,1):C.GC_328})

V_247 = Vertex(name = 'V_247',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV8 ],
               couplings = {(0,0):C.GC_297})

V_248 = Vertex(name = 'V_248',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS8 ],
               couplings = {(0,0):C.GC_298})

V_249 = Vertex(name = 'V_249',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS8 ],
               couplings = {(0,0):C.GC_299})

V_250 = Vertex(name = 'V_250',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV4 ],
               couplings = {(0,0):C.GC_302})

V_251 = Vertex(name = 'V_251',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS4 ],
               couplings = {(0,0):C.GC_303})

V_252 = Vertex(name = 'V_252',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS4 ],
               couplings = {(0,0):C.GC_304})

V_253 = Vertex(name = 'V_253',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS7, L.VVVSSS13, L.VVVSSS15 ],
               couplings = {(0,0):C.GC_314,(0,1):C.GC_365,(0,2):C.GC_371})

V_254 = Vertex(name = 'V_254',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS7, L.VVVSS13, L.VVVSS15 ],
               couplings = {(0,0):C.GC_315,(0,1):C.GC_366,(0,2):C.GC_372})

V_255 = Vertex(name = 'V_255',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS7, L.VVVS13, L.VVVS15 ],
               couplings = {(0,0):C.GC_316,(0,1):C.GC_367,(0,2):C.GC_373})

V_256 = Vertex(name = 'V_256',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS7, L.VVSS8 ],
               couplings = {(0,0):C.GC_317,(0,1):C.GC_478})

V_257 = Vertex(name = 'V_257',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7, L.VVSSS8 ],
               couplings = {(0,0):C.GC_318,(0,1):C.GC_479})

V_258 = Vertex(name = 'V_258',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1, L.VVSSSS2 ],
               couplings = {(0,0):C.GC_319,(0,1):C.GC_480})

V_259 = Vertex(name = 'V_259',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS7, L.VVSS8 ],
               couplings = {(0,0):C.GC_320,(0,1):C.GC_323})

V_260 = Vertex(name = 'V_260',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS7, L.VVSSS8 ],
               couplings = {(0,0):C.GC_321,(0,1):C.GC_324})

V_261 = Vertex(name = 'V_261',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS1, L.VVSSSS2 ],
               couplings = {(0,0):C.GC_322,(0,1):C.GC_325})

V_262 = Vertex(name = 'V_262',
               particles = [ P.Z, P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS14 ],
               couplings = {(0,0):C.GC_368})

V_263 = Vertex(name = 'V_263',
               particles = [ P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS14 ],
               couplings = {(0,0):C.GC_369})

V_264 = Vertex(name = 'V_264',
               particles = [ P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS14 ],
               couplings = {(0,0):C.GC_370})

V_265 = Vertex(name = 'V_265',
               particles = [ P.a, P.a, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS3, L.VVSSSS4, L.VVSSSS6 ],
               couplings = {(0,0):C.GC_383,(0,1):C.GC_404,(0,2):C.GC_459})

V_266 = Vertex(name = 'V_266',
               particles = [ P.a, P.a, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS15, L.VVSSS17 ],
               couplings = {(0,0):C.GC_384,(0,1):C.GC_405,(0,2):C.GC_460})

V_267 = Vertex(name = 'V_267',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS15, L.VVSS17 ],
               couplings = {(0,0):C.GC_385,(0,1):C.GC_406,(0,2):C.GC_461})

V_268 = Vertex(name = 'V_268',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS3, L.VVSSSS4, L.VVSSSS5, L.VVSSSS6 ],
               couplings = {(0,0):C.GC_386,(0,1):C.GC_407,(0,2):C.GC_424,(0,3):C.GC_462})

V_269 = Vertex(name = 'V_269',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS15, L.VVSSS16, L.VVSSS17 ],
               couplings = {(0,0):C.GC_387,(0,1):C.GC_408,(0,2):C.GC_425,(0,3):C.GC_463})

V_270 = Vertex(name = 'V_270',
               particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS15, L.VVSS16, L.VVSS17 ],
               couplings = {(0,0):C.GC_388,(0,1):C.GC_409,(0,2):C.GC_426,(0,3):C.GC_464})

V_271 = Vertex(name = 'V_271',
               particles = [ P.a, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS3, L.VVSSSS4, L.VVSSSS6 ],
               couplings = {(0,0):C.GC_389,(0,1):C.GC_410,(0,2):C.GC_465})

V_272 = Vertex(name = 'V_272',
               particles = [ P.a, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS15, L.VVSSS17 ],
               couplings = {(0,0):C.GC_390,(0,1):C.GC_411,(0,2):C.GC_466})

V_273 = Vertex(name = 'V_273',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS15, L.VVSS17 ],
               couplings = {(0,0):C.GC_391,(0,1):C.GC_412,(0,2):C.GC_467})

V_274 = Vertex(name = 'V_274',
               particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSSS3, L.VVSSSS4, L.VVSSSS6 ],
               couplings = {(0,0):C.GC_392,(0,1):C.GC_413,(0,2):C.GC_468})

V_275 = Vertex(name = 'V_275',
               particles = [ P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSSS14, L.VVSSS15, L.VVSSS17 ],
               couplings = {(0,0):C.GC_393,(0,1):C.GC_414,(0,2):C.GC_469})

V_276 = Vertex(name = 'V_276',
               particles = [ P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS14, L.VVSS15, L.VVSS17 ],
               couplings = {(0,0):C.GC_394,(0,1):C.GC_415,(0,2):C.GC_470})

V_277 = Vertex(name = 'V_277',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS18, L.VVVSSS19, L.VVVSSS20, L.VVVSSS23 ],
               couplings = {(0,0):C.GC_396,(0,1):C.GC_416,(0,2):C.GC_427,(0,3):C.GC_471})

V_278 = Vertex(name = 'V_278',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS18, L.VVVSS19, L.VVVSS20, L.VVVSS23 ],
               couplings = {(0,0):C.GC_397,(0,1):C.GC_417,(0,2):C.GC_428,(0,3):C.GC_472})

V_279 = Vertex(name = 'V_279',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS12, L.VVVVSS14 ],
               couplings = {(0,0):C.GC_398,(0,1):C.GC_418,(0,2):C.GC_429})

V_280 = Vertex(name = 'V_280',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS18, L.VVVSSS19, L.VVVSSS21, L.VVVSSS23 ],
               couplings = {(0,0):C.GC_399,(0,1):C.GC_419,(0,2):C.GC_430,(0,3):C.GC_473})

V_281 = Vertex(name = 'V_281',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS18, L.VVVSS19, L.VVVSS21, L.VVVSS23 ],
               couplings = {(0,0):C.GC_400,(0,1):C.GC_420,(0,2):C.GC_431,(0,3):C.GC_474})

V_282 = Vertex(name = 'V_282',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS12 ],
               couplings = {(0,0):C.GC_401,(0,1):C.GC_421})

V_283 = Vertex(name = 'V_283',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS13, L.VVVVSS15 ],
               couplings = {(0,0):C.GC_402,(0,1):C.GC_422,(0,2):C.GC_432})

V_284 = Vertex(name = 'V_284',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS12, L.VVVVSS16 ],
               couplings = {(0,0):C.GC_403,(0,1):C.GC_423,(0,2):C.GC_433})

V_285 = Vertex(name = 'V_285',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS4 ],
               couplings = {(0,0):C.GC_440})

V_286 = Vertex(name = 'V_286',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS4 ],
               couplings = {(0,0):C.GC_441})

V_287 = Vertex(name = 'V_287',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS5 ],
               couplings = {(0,0):C.GC_445})

V_288 = Vertex(name = 'V_288',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS5 ],
               couplings = {(0,0):C.GC_446})

V_289 = Vertex(name = 'V_289',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS4 ],
               couplings = {(0,0):C.GC_447})

V_290 = Vertex(name = 'V_290',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS4 ],
               couplings = {(0,0):C.GC_448})

V_291 = Vertex(name = 'V_291',
               particles = [ P.g, P.g, P.H, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVSSSS3, L.VVSSSS4, L.VVSSSS7 ],
               couplings = {(0,0):C.GC_481,(0,1):C.GC_487,(0,2):C.GC_493})

V_292 = Vertex(name = 'V_292',
               particles = [ P.g, P.g, P.H, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVSSS14, L.VVSSS15, L.VVSSS18 ],
               couplings = {(0,0):C.GC_482,(0,1):C.GC_488,(0,2):C.GC_494})

V_293 = Vertex(name = 'V_293',
               particles = [ P.g, P.g, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.VVSS14, L.VVSS15, L.VVSS18 ],
               couplings = {(0,0):C.GC_483,(0,1):C.GC_489,(0,2):C.GC_495})

V_294 = Vertex(name = 'V_294',
               particles = [ P.g, P.g, P.g, P.H, P.H, P.H ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVVSSS18, L.VVVSSS19, L.VVVSSS24 ],
               couplings = {(0,0):C.GC_484,(0,1):C.GC_490,(0,2):C.GC_496})

V_295 = Vertex(name = 'V_295',
               particles = [ P.g, P.g, P.g, P.H, P.H ],
               color = [ 'f(1,2,3)' ],
               lorentz = [ L.VVVSS18, L.VVVSS19, L.VVVSS24 ],
               couplings = {(0,0):C.GC_485,(0,1):C.GC_491,(0,2):C.GC_497})

V_296 = Vertex(name = 'V_296',
               particles = [ P.g, P.g, P.g, P.g, P.H, P.H ],
               color = [ 'f(-1,1,4)*f(2,3,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,2)*f(3,4,-1)' ],
               lorentz = [ L.VVVVSS18, L.VVVVSS19, L.VVVVSS20, L.VVVVSS21, L.VVVVSS22, L.VVVVSS23 ],
               couplings = {(0,0):C.GC_486,(1,1):C.GC_486,(2,2):C.GC_486,(1,3):C.GC_492,(2,4):C.GC_492,(0,5):C.GC_492})

V_297 = Vertex(name = 'V_297',
               particles = [ P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVV13, L.VVV14 ],
               couplings = {(0,0):C.GC_498,(0,1):C.GC_533})

V_298 = Vertex(name = 'V_298',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS25, L.VVVSSS26 ],
               couplings = {(0,0):C.GC_499,(0,1):C.GC_534})

V_299 = Vertex(name = 'V_299',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS25, L.VVVSS26 ],
               couplings = {(0,0):C.GC_500,(0,1):C.GC_535})

V_300 = Vertex(name = 'V_300',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS19, L.VVVS20 ],
               couplings = {(0,0):C.GC_501,(0,1):C.GC_536})

V_301 = Vertex(name = 'V_301',
               particles = [ P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVV13, L.VVV14 ],
               couplings = {(0,0):C.GC_502,(0,1):C.GC_537})

V_302 = Vertex(name = 'V_302',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSSS25, L.VVVSSS26 ],
               couplings = {(0,0):C.GC_503,(0,1):C.GC_538})

V_303 = Vertex(name = 'V_303',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS25, L.VVVSS26 ],
               couplings = {(0,0):C.GC_504,(0,1):C.GC_539})

V_304 = Vertex(name = 'V_304',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS19, L.VVVS20 ],
               couplings = {(0,0):C.GC_505,(0,1):C.GC_540})

V_305 = Vertex(name = 'V_305',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV11, L.VVVV13 ],
               couplings = {(0,0):C.GC_506,(0,1):C.GC_542})

V_306 = Vertex(name = 'V_306',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS24, L.VVVVSS26 ],
               couplings = {(0,0):C.GC_507,(0,1):C.GC_543})

V_307 = Vertex(name = 'V_307',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS11, L.VVVVS13 ],
               couplings = {(0,0):C.GC_508,(0,1):C.GC_544})

V_308 = Vertex(name = 'V_308',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV12, L.VVVV14 ],
               couplings = {(0,0):C.GC_509,(0,1):C.GC_545})

V_309 = Vertex(name = 'V_309',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS25, L.VVVVSS27 ],
               couplings = {(0,0):C.GC_510,(0,1):C.GC_546})

V_310 = Vertex(name = 'V_310',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS12, L.VVVVS14 ],
               couplings = {(0,0):C.GC_511,(0,1):C.GC_547})

V_311 = Vertex(name = 'V_311',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV1, L.VVVVV7 ],
               couplings = {(0,0):C.GC_512,(0,1):C.GC_548})

V_312 = Vertex(name = 'V_312',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS1, L.VVVVVS7 ],
               couplings = {(0,0):C.GC_513,(0,1):C.GC_549})

V_313 = Vertex(name = 'V_313',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVV11, L.VVVV13 ],
               couplings = {(0,0):C.GC_514,(0,1):C.GC_552})

V_314 = Vertex(name = 'V_314',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS24, L.VVVVSS26 ],
               couplings = {(0,0):C.GC_515,(0,1):C.GC_553})

V_315 = Vertex(name = 'V_315',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS11, L.VVVVS13 ],
               couplings = {(0,0):C.GC_516,(0,1):C.GC_554})

V_316 = Vertex(name = 'V_316',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV2, L.VVVVV8 ],
               couplings = {(0,0):C.GC_517,(0,1):C.GC_550})

V_317 = Vertex(name = 'V_317',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS2, L.VVVVVS8 ],
               couplings = {(0,0):C.GC_518,(0,1):C.GC_551})

V_318 = Vertex(name = 'V_318',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV3, L.VVVVV9 ],
               couplings = {(0,0):C.GC_519,(0,1):C.GC_555})

V_319 = Vertex(name = 'V_319',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS3, L.VVVVVS9 ],
               couplings = {(0,0):C.GC_520,(0,1):C.GC_556})

V_320 = Vertex(name = 'V_320',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV1 ],
               couplings = {(0,0):C.GC_521})

V_321 = Vertex(name = 'V_321',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV11, L.VVVV13 ],
               couplings = {(0,0):C.GC_522,(0,1):C.GC_557})

V_322 = Vertex(name = 'V_322',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS24, L.VVVVSS26 ],
               couplings = {(0,0):C.GC_523,(0,1):C.GC_558})

V_323 = Vertex(name = 'V_323',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS11, L.VVVVS13 ],
               couplings = {(0,0):C.GC_524,(0,1):C.GC_559})

V_324 = Vertex(name = 'V_324',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV4, L.VVVVV10 ],
               couplings = {(0,0):C.GC_525,(0,1):C.GC_560})

V_325 = Vertex(name = 'V_325',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS4, L.VVVVVS10 ],
               couplings = {(0,0):C.GC_526,(0,1):C.GC_561})

V_326 = Vertex(name = 'V_326',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV5, L.VVVVV11 ],
               couplings = {(0,0):C.GC_527,(0,1):C.GC_562})

V_327 = Vertex(name = 'V_327',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS5, L.VVVVVS11 ],
               couplings = {(0,0):C.GC_528,(0,1):C.GC_563})

V_328 = Vertex(name = 'V_328',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV2 ],
               couplings = {(0,0):C.GC_529})

V_329 = Vertex(name = 'V_329',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV6, L.VVVVV12 ],
               couplings = {(0,0):C.GC_530,(0,1):C.GC_564})

V_330 = Vertex(name = 'V_330',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS6, L.VVVVVS12 ],
               couplings = {(0,0):C.GC_531,(0,1):C.GC_565})

V_331 = Vertex(name = 'V_331',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV1 ],
               couplings = {(0,0):C.GC_532})

V_332 = Vertex(name = 'V_332',
               particles = [ P.s__tilde__, P.s, P.H, P.H ],
               color = [ 'Identity(1,2)' ],
               lorentz = [ L.FFSS1 ],
               couplings = {(0,0):C.GC_541})
