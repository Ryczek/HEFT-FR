# Merged by HEFT ufo_merge.py: baseline FB_SM, sources FB_PT, FB_PG, FB_PB, FB_SG, FB_SB, FB_S2D, FB_PDH, FB_P1, FB_P2, FB_P3, FB_P4, FB_P5, FB_P6, FB_P12, FB_P13, FB_P14, FB_P17, FB_P18, FB_P20, FB_P21, FB_P22, FB_P23, FB_P24, FB_P26, FB_S1, FB_S2, FB_S3, FB_S4, FB_S5, FB_S6, FB_S7, FB_S8, FB_S9, FB_S15, FB_PWHD1, FB_PWHD2, FB_SWHDT, FB_PW, FB_SW, FB_SWHD, FB_P11, FB_P8, FB_PGHD1, FB_PGHD2, FB_SGHD, FB_PWWW, FB_SWWW
# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Tue 13 Oct 2026 20:18:42


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

GC_1 = Coupling(name = 'GC_1',
                value = '-6*complex(0,1)*hlambda',
                order = {'QED':2})

GC_2 = Coupling(name = 'GC_2',
                value = '-6*DeltaLam4*complex(0,1)*hlambda*WCOrder',
                order = {'QED':2,'WCOrder':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-6*complex(0,1)*hlambda*vev',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = '-6*DeltaLam3*complex(0,1)*hlambda*vev*WCOrder',
                order = {'QED':1,'WCOrder':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-0.125*(GS**3*thetaS)/cmath.pi**2',
                order = {'QCD':3})

GC_6 = Coupling(name = 'GC_6',
                value = 'GS',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*GS**2',
                order = {'QCD':2})

GC_8 = Coupling(name = 'GC_8',
                value = '-((CLEn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                order = {'QED':1,'WCOrder':1})

GC_9 = Coupling(name = 'GC_9',
                value = '-((CLEn22x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                order = {'QED':1,'WCOrder':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '-((CLEn21x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-((CLEn23x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-((CLEn21x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-((CLEn22x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-((CLEn23x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-((CLEn22x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(-((CLEn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev))',
                 order = {'QED':1,'WCOrder':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-4*((-3*CLEn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                 order = {'QED':2,'WCOrder':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '(-3*CLEn32x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(-3*CLEn31x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '(-3*CLEn33x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(-3*CLEn31x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-14*((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                 order = {'QED':2,'WCOrder':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(-3*CLEn33x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(-3*CLEn32x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-19*((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                 order = {'QED':2,'WCOrder':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-20*(-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev))',
                 order = {'QED':1,'WCOrder':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-((CQUn22x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-((CQUn21x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-((CQUn23x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((CQUn21x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '-((CQUn22x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-((CQUn23x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '-((CQUn22x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '-((CQUn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(-3*CQUn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(-3*CQUn32x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(-3*CQUn31x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(-3*CQUn33x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(-3*CQUn31x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(-3*CQUn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '(-3*CQUn33x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '(-3*CQUn32x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(-3*CQUn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((CQDn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-((CQDn22x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-((CQDn21x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-((CQDn23x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((CQDn21x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-((CQDn23x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-((CQDn22x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                 order = {'QED':1,'WCOrder':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-22*(-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev))',
                 order = {'QED':1,'WCOrder':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-22*((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                 order = {'QED':2,'WCOrder':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(-3*CQDn32x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '(-3*CQDn31x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(-3*CQDn33x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(-3*CQDn31x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '-22*((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                 order = {'QED':2,'WCOrder':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(-3*CQDn33x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(-3*CQDn32x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2',
                 order = {'QED':2,'WCOrder':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '-22*((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                 order = {'QED':2,'WCOrder':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '-22*(-((complex(0,1)*MQD)/vev))',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-22*(-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                 order = {'WCOrder':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-22*(-((complex(0,1)*MQS)/vev))',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-22*(-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                 order = {'WCOrder':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-26*(-((complex(0,1)*MQB)/vev))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-26*(-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                 order = {'WCOrder':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-27*(-((complex(0,1)*MLE)/vev))',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-27*(-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                 order = {'WCOrder':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-27*(-((complex(0,1)*MLM)/vev))',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-27*(-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                 order = {'WCOrder':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-37*(-((complex(0,1)*MLT)/vev))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '-37*(-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                 order = {'WCOrder':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '-39*(-((complex(0,1)*MQU)/vev))',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-39*(-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                 order = {'WCOrder':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-39*(-((complex(0,1)*MQC)/vev))',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-39*(-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                 order = {'WCOrder':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((complex(0,1)*MQT)/vev)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((DeltaYQT*complex(0,1)*WCOrder)/cmath.sqrt(2))',
                 order = {'WCOrder':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(-((complex(0,1)*G1**3*GW)/(G1**2 + GW**2)**1.5) - (complex(0,1)*G1*GW**3)/(G1**2 + GW**2)**1.5) + (-((complex(0,1)*G1**3*GW)/(G1**2 + GW**2)**1.5) - (complex(0,1)*G1*GW**3)/(G1**2 + GW**2)**1.5) - (-((complex(0,1)*G1*GW)/cmath.sqrt(G1**2 + GW**2)))',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(complex(0,1)*GW**2)/2.',
                 order = {'QED':2})

GC_81 = Coupling(name = 'GC_81',
                 value = '(DeltaFCn2*complex(0,1)*GW**2*WCOrder)/2.',
                 order = {'QED':2,'WCOrder':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(complex(0,1)*GW**2*vev)/2.',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '(DeltaFCn1*complex(0,1)*GW**2*vev*WCOrder)/2.',
                 order = {'QED':1,'WCOrder':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(3*CFCn3*complex(0,1)*GW**2*WCOrder)/(2.*vev)',
                 order = {'QED':3,'WCOrder':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '((complex(0,1)*G1**4*GW**2)/(G1**2 + GW**2)**2 + (complex(0,1)*G1**2*GW**4)/(G1**2 + GW**2)**2) + ((complex(0,1)*G1**4*GW**2)/(G1**2 + GW**2)**2 + (complex(0,1)*G1**2*GW**4)/(G1**2 + GW**2)**2) - ((complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2))',
                 order = {'QED':2})

GC_86 = Coupling(name = 'GC_86',
                 value = '(-((complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2)**1.5) - (complex(0,1)*GW**4)/(G1**2 + GW**2)**1.5) + (-((complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2)**1.5) - (complex(0,1)*GW**4)/(G1**2 + GW**2)**1.5) - (-((complex(0,1)*GW**2)/cmath.sqrt(G1**2 + GW**2)))',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-(complex(0,1)*GW**2)',
                 order = {'QED':2})

GC_88 = Coupling(name = 'GC_88',
                 value = '((-2*complex(0,1)*G1**3*GW**3)/(G1**2 + GW**2)**2 - (2*complex(0,1)*G1*GW**5)/(G1**2 + GW**2)**2) + ((-2*complex(0,1)*G1**3*GW**3)/(G1**2 + GW**2)**2 - (2*complex(0,1)*G1*GW**5)/(G1**2 + GW**2)**2) + ((2*G1*GW**3)/((complex(0,1)*G1 - GW)*(G1 - complex(0,1)*GW))) + ((-2*complex(0,1)*G1*GW**3)/((G1 - complex(0,1)*GW)*(G1 + complex(0,1)*GW))) - 3*((-2*complex(0,1)*G1*GW**3)/(G1**2 + GW**2))',
                 order = {'QED':2})

GC_89 = Coupling(name = 'GC_89',
                 value = '((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2))) - 10*((complex(0,1)*G1**2)/2. + (complex(0,1)*GW**2)/2.)',
                 order = {'QED':2})

GC_90 = Coupling(name = 'GC_90',
                 value = '(-(CPTn2*complex(0,1)*G1**2*WCOrder) + (DeltaFCn2*complex(0,1)*G1**2*WCOrder)/2. - CPTn2*complex(0,1)*GW**2*WCOrder + (DeltaFCn2*complex(0,1)*GW**2*WCOrder)/2.) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) - (2*CP1n0*complex(0,1)*G1**3*GW*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) - (2*CP1n0*complex(0,1)*G1*GW**3*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (2*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (2*CP12n0*complex(0,1)*GW**4*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn2*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn2*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2) + (DeltaFCn2*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2))) - 11*((DeltaFCn2*complex(0,1)*G1**2*WCOrder)/2. + (DeltaFCn2*complex(0,1)*GW**2*WCOrder)/2.)',
                 order = {'QED':2,'WCOrder':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '((complex(0,1)*G1**4*vev)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2*vev)/(G1**2 + GW**2) + (complex(0,1)*GW**4*vev)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4*vev)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2*vev)/(G1**2 + GW**2) + (complex(0,1)*GW**4*vev)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4*vev)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2*vev)/(G1**2 + GW**2) + (complex(0,1)*GW**4*vev)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4*vev)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2*vev)/(G1**2 + GW**2) + (complex(0,1)*GW**4*vev)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4*vev)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2*vev)/(G1**2 + GW**2) + (complex(0,1)*GW**4*vev)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4*vev)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2*vev)/(G1**2 + GW**2) + (complex(0,1)*GW**4*vev)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4*vev)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2*vev)/(G1**2 + GW**2) + (complex(0,1)*GW**4*vev)/(2.*(G1**2 + GW**2))) + ((complex(0,1)*G1**4*vev)/(2.*(G1**2 + GW**2)) + (complex(0,1)*G1**2*GW**2*vev)/(G1**2 + GW**2) + (complex(0,1)*GW**4*vev)/(2.*(G1**2 + GW**2))) - 7*((complex(0,1)*G1**2*vev)/2. + (complex(0,1)*GW**2*vev)/2.)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(-0.5*(CPTn1*complex(0,1)*G1**2*vev*WCOrder) + (DeltaFCn1*complex(0,1)*G1**2*vev*WCOrder)/2. - (CPTn1*complex(0,1)*GW**2*vev*WCOrder)/2. + (DeltaFCn1*complex(0,1)*GW**2*vev*WCOrder)/2.) + ((DeltaFCn1*complex(0,1)*G1**4*vev*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn1*complex(0,1)*G1**2*GW**2*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*GW**4*vev*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn1*complex(0,1)*G1**4*vev*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn1*complex(0,1)*G1**2*GW**2*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*GW**4*vev*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn1*complex(0,1)*G1**4*vev*WCOrder)/(2.*(G1**2 + GW**2)) - (2*CP1n0*complex(0,1)*G1**3*GW*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*G1**2*GW**2*vev*WCOrder)/(G1**2 + GW**2) - (2*CP1n0*complex(0,1)*G1*GW**3*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*GW**4*vev*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn1*complex(0,1)*G1**4*vev*WCOrder)/(2.*(G1**2 + GW**2)) + (2*CP12n0*complex(0,1)*G1**2*GW**2*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*G1**2*GW**2*vev*WCOrder)/(G1**2 + GW**2) + (2*CP12n0*complex(0,1)*GW**4*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*GW**4*vev*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn1*complex(0,1)*G1**4*vev*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn1*complex(0,1)*G1**2*GW**2*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*GW**4*vev*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn1*complex(0,1)*G1**4*vev*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn1*complex(0,1)*G1**2*GW**2*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*GW**4*vev*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn1*complex(0,1)*G1**4*vev*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn1*complex(0,1)*G1**2*GW**2*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*GW**4*vev*WCOrder)/(2.*(G1**2 + GW**2))) + ((DeltaFCn1*complex(0,1)*G1**4*vev*WCOrder)/(2.*(G1**2 + GW**2)) + (DeltaFCn1*complex(0,1)*G1**2*GW**2*vev*WCOrder)/(G1**2 + GW**2) + (DeltaFCn1*complex(0,1)*GW**4*vev*WCOrder)/(2.*(G1**2 + GW**2))) - 8*((DeltaFCn1*complex(0,1)*G1**2*vev*WCOrder)/2. + (DeltaFCn1*complex(0,1)*GW**2*vev*WCOrder)/2.)',
                 order = {'QED':1,'WCOrder':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '((3*CFCn3*complex(0,1)*G1**2*WCOrder)/(2.*vev) - (3*CPTn3*complex(0,1)*G1**2*WCOrder)/vev + (3*CFCn3*complex(0,1)*GW**2*WCOrder)/(2.*vev) - (3*CPTn3*complex(0,1)*GW**2*WCOrder)/vev) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((3*CFCn3*complex(0,1)*G1**4*WCOrder)/(2.*(G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev) + (3*CFCn3*complex(0,1)*GW**4*WCOrder)/(2.*(G1**2 + GW**2)*vev)) - 11*((3*CFCn3*complex(0,1)*G1**2*WCOrder)/(2.*vev) + (3*CFCn3*complex(0,1)*GW**2*WCOrder)/(2.*vev))',
                 order = {'QED':3,'WCOrder':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '((complex(0,1)*G1**2*GW**4)/(G1**2 + GW**2)**2 + (complex(0,1)*GW**6)/(G1**2 + GW**2)**2) + ((complex(0,1)*G1**2*GW**4)/(G1**2 + GW**2)**2 + (complex(0,1)*GW**6)/(G1**2 + GW**2)**2) - ((complex(0,1)*GW**4)/(G1**2 + GW**2))',
                 order = {'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = '((-2*complex(0,1)*G1**3*GW)/(3.*(G1**2 + GW**2)**1.5) - (2*complex(0,1)*G1*GW**3)/(3.*(G1**2 + GW**2)**1.5)) + ((-2*complex(0,1)*G1**3*GW)/(3.*(G1**2 + GW**2)**1.5) - (2*complex(0,1)*G1*GW**3)/(3.*(G1**2 + GW**2)**1.5)) - ((-2*complex(0,1)*G1*GW)/(3.*cmath.sqrt(G1**2 + GW**2)))',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '((complex(0,1)*G1**4)/(6.*(G1**2 + GW**2)**1.5)) - ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(-0.5*(complex(0,1)*GW**4)/(G1**2 + GW**2)**1.5) + ((complex(0,1)*G1**4)/(6.*(G1**2 + GW**2)**1.5) - (complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5) - (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2)**1.5)) - (-0.5*(complex(0,1)*GW**2)/cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '-11*((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(6.*(G1**2 + GW**2)**1.5) - (complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5) - (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2)**1.5)) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(6.*(G1**2 + GW**2)**1.5) - (complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5) - (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2)**1.5)) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) - 11*(-0.5*(complex(0,1)*GW**2)/cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '-((CKM1x1*complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((CKM1x2*complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '-((CKM1x3*complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '-((CKM2x1*complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '-((CKM2x2*complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '-((CKM2x3*complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '-((CKM3x1*complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-((CKM3x2*complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '-((CKM3x3*complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '-((complex(0,1)*GW*complexconjugate(CKM1x1))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '-((complex(0,1)*GW*complexconjugate(CKM2x1))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '-((complex(0,1)*GW*complexconjugate(CKM3x1))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-((complex(0,1)*GW*complexconjugate(CKM1x2))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-((complex(0,1)*GW*complexconjugate(CKM2x2))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '-((complex(0,1)*GW*complexconjugate(CKM3x2))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((complex(0,1)*GW*complexconjugate(CKM1x3))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '-((complex(0,1)*GW*complexconjugate(CKM2x3))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '-((complex(0,1)*GW*complexconjugate(CKM3x3))/cmath.sqrt(2))',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '((complex(0,1)*G1**3*GW)/(3.*(G1**2 + GW**2)**1.5) + (complex(0,1)*G1*GW**3)/(3.*(G1**2 + GW**2)**1.5)) + ((complex(0,1)*G1**3*GW)/(3.*(G1**2 + GW**2)**1.5) + (complex(0,1)*G1*GW**3)/(3.*(G1**2 + GW**2)**1.5)) - ((complex(0,1)*G1*GW)/(3.*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '-14*((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(6.*(G1**2 + GW**2)**1.5) + (2*complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2)**1.5)) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(6.*(G1**2 + GW**2)**1.5) + (2*complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2)**1.5)) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) - 14*((complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '-20*((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(6.*(G1**2 + GW**2)**1.5) + (2*complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2)**1.5)) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**4)/(6.*(G1**2 + GW**2)**1.5) + (2*complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5) + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2)**1.5)) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + ((complex(0,1)*G1**2)/(6.*cmath.sqrt(G1**2 + GW**2)) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) - 20*((complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) - (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) - (-0.5*(complex(0,1)*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '-((complex(0,1)*GW)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '((complex(0,1)*G1**3*GW)/(G1**2 + GW**2)**1.5 + (complex(0,1)*G1*GW**3)/(G1**2 + GW**2)**1.5) + ((complex(0,1)*G1**3*GW)/(G1**2 + GW**2)**1.5 + (complex(0,1)*G1*GW**3)/(G1**2 + GW**2)**1.5) - ((complex(0,1)*G1*GW)/cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-18*(-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**4)/(G1**2 + GW**2)**1.5 + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2)**1.5)) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**4)/(G1**2 + GW**2)**1.5 + (complex(0,1)*GW**4)/(2.*(G1**2 + GW**2)**1.5)) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2) + (complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))) - 18*((complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '-(complex(0,1)*GS)',
                  order = {'QCD':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(-6*CPGn3*complex(0,1)*WCOrder)/vev**3',
                  order = {'QED':3,'WCOrder':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(-2*CPGn2*complex(0,1)*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-((CPGn1*complex(0,1)*WCOrder)/vev)',
                  order = {'QED':1,'WCOrder':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(6*CPGn3*GS*WCOrder)/vev**3',
                  order = {'QCD':1,'QED':3,'WCOrder':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(2*CPGn2*GS*WCOrder)/vev**2',
                  order = {'QCD':1,'QED':2,'WCOrder':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(CPGn1*GS*WCOrder)/vev',
                  order = {'QCD':1,'QED':1,'WCOrder':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(2*CPGn2*complex(0,1)*GS**2*WCOrder)/vev**2',
                  order = {'QCD':2,'QED':2,'WCOrder':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(CPGn1*complex(0,1)*GS**2*WCOrder)/vev',
                  order = {'QCD':2,'QED':1,'WCOrder':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev)) + (-((complex(0,1)*MLE)/vev))',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLE*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                  order = {'WCOrder':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev)) + (-((complex(0,1)*MLM)/vev))',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLM*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                  order = {'WCOrder':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev)) + (-((complex(0,1)*MLT)/vev))',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYLT*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                  order = {'WCOrder':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '(-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev)) + (-((complex(0,1)*MQU)/vev))',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQU*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                  order = {'WCOrder':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev)) + (-((complex(0,1)*MQC)/vev))',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQC*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                  order = {'WCOrder':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))) + ((2*complex(0,1)*G1**4)/(3.*(G1**2 + GW**2)**1.5) + (2*complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5)) + ((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))) + ((2*complex(0,1)*G1**4)/(3.*(G1**2 + GW**2)**1.5) + (2*complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5)) + ((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))) + ((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))) + ((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))) + ((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))) + ((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))) + ((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))) + ((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2))) + ((2*complex(0,1)*G1**2)/(3.*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**4)/(G1**2 + GW**2)**1.5 - (complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**4)/(G1**2 + GW**2)**1.5 - (complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**4)/(G1**2 + GW**2)**1.5 - (complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**4)/(G1**2 + GW**2)**1.5 - (complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)) + (-0.3333333333333333*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**4)/(G1**2 + GW**2)**1.5) - (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2)**1.5) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**4)/(G1**2 + GW**2)**1.5) - (complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2)**1.5) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2))) + (-((complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '((-6*CPBn3*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((24*CP1n3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((24*CP12n3*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((-6*CPWn3*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**3))',
                  order = {'QED':3,'WCOrder':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '((-2*CPBn2*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((8*CP1n2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((8*CP12n2*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((-2*CPWn2*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**2))',
                  order = {'QED':2,'WCOrder':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(-((CPBn1*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev))) + ((4*CP1n1*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev)) + ((4*CP12n1*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev)) + (-((CPWn1*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev)))',
                  order = {'QED':1,'WCOrder':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '((6*CPBn3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((-12*CP1n3*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**3) + (12*CP1n3*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((24*CP12n3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((-6*CPWn3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3))',
                  order = {'QED':3,'WCOrder':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '((2*CPBn2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((-4*CP1n2*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**2) + (4*CP1n2*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((8*CP12n2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((-2*CPWn2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2))',
                  order = {'QED':2,'WCOrder':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '((CPBn1*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev)) + ((-2*CP1n1*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev) + (2*CP1n1*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev)) + ((4*CP12n1*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev)) + (-((CPWn1*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev)))',
                  order = {'QED':1,'WCOrder':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '((-6*CPBn3*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((-24*CP1n3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((24*CP12n3*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((-6*CPWn3*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**3))',
                  order = {'QED':3,'WCOrder':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '((-2*CPBn2*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((-8*CP1n2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((8*CP12n2*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((-2*CPWn2*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**2))',
                  order = {'QED':2,'WCOrder':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '(-((CPBn1*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev))) + ((-4*CP1n1*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev)) + ((4*CP12n1*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev)) + (-((CPWn1*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev)))',
                  order = {'QED':1,'WCOrder':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '(-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev)) + (-((complex(0,1)*MQB)/vev))',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '(-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQB*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                  order = {'WCOrder':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '(3*CSGn3*complex(0,1)*WCOrder)/(4.*vev**3)',
                  order = {'QED':3,'WCOrder':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '(CSGn2*complex(0,1)*WCOrder)/(4.*vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(CSGn1*complex(0,1)*WCOrder)/(8.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '(-3*CSGn3*GS*WCOrder)/(2.*vev**3)',
                  order = {'QCD':1,'QED':3,'WCOrder':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '-0.5*(CSGn2*GS*WCOrder)/vev**2',
                  order = {'QCD':1,'QED':2,'WCOrder':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-0.25*(CSGn1*GS*WCOrder)/vev',
                  order = {'QCD':1,'QED':1,'WCOrder':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '((3*CSBn3*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((-12*CS1n3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((-12*CS8n3*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((3*CSWn3*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**3))',
                  order = {'QED':3,'WCOrder':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '((CSBn2*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((-4*CS1n2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((-4*CS8n2*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((CSWn2*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**2))',
                  order = {'QED':2,'WCOrder':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '((CSBn1*complex(0,1)*GW**2*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((-2*CS1n1*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev)) + ((-2*CS8n1*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev)) + ((CSWn1*complex(0,1)*G1**2*WCOrder)/(2.*(G1**2 + GW**2)*vev))',
                  order = {'QED':1,'WCOrder':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '((-3*CSBn3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((-12*CS8n3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((3*CSWn3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3))',
                  order = {'QED':3,'WCOrder':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '(-((CSBn2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2))) + ((-4*CS8n2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((CSWn2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2))',
                  order = {'QED':2,'WCOrder':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '(-0.5*(CSBn1*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev)) + ((-2*CS8n1*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev)) + ((CSWn1*complex(0,1)*G1*GW*WCOrder)/(2.*(G1**2 + GW**2)*vev))',
                  order = {'QED':1,'WCOrder':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '((3*CSBn3*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((12*CS1n3*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((-12*CS8n3*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**3)) + ((3*CSWn3*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**3))',
                  order = {'QED':3,'WCOrder':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '((CSBn2*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((4*CS1n2*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((-4*CS8n2*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**2)) + ((CSWn2*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**2))',
                  order = {'QED':2,'WCOrder':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '((CSBn1*complex(0,1)*G1**2*WCOrder)/(2.*(G1**2 + GW**2)*vev)) + ((2*CS1n1*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*vev)) + ((-2*CS8n1*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev)) + ((CSWn1*complex(0,1)*GW**2*WCOrder)/(2.*(G1**2 + GW**2)*vev))',
                  order = {'QED':1,'WCOrder':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '(CS2Dn1*MLE*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '(CS2Dn1*MLM*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '(CS2Dn1*MLT*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '-((CS2Dn1*MQU*WCOrder)/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '(CS2Dn1*MQU*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((CS2Dn1*MQC*WCOrder)/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '(CS2Dn1*MQC*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '-((CS2Dn1*MQT*WCOrder)/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '(CS2Dn1*MQT*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(CS2Dn1*MQD*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '-((CS2Dn1*MQD*WCOrder)/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '(CS2Dn1*MQS*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '-((CS2Dn1*MQS*WCOrder)/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '(CS2Dn1*MQB*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '-((CS2Dn1*MQB*WCOrder)/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '(CS2Dn1*MQD*WCOrder)/(2.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '-0.5*(CS2Dn1*MQD*WCOrder)/vev',
                  order = {'QED':1,'WCOrder':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(CS2Dn1*MQS*WCOrder)/(2.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-0.5*(CS2Dn1*MQS*WCOrder)/vev',
                  order = {'QED':1,'WCOrder':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '(CS2Dn1*MQB*WCOrder)/(2.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-0.5*(CS2Dn1*MQB*WCOrder)/vev',
                  order = {'QED':1,'WCOrder':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(CS2Dn1*MLE*WCOrder)/(2.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '-0.5*(CS2Dn1*MLE*WCOrder)/vev',
                  order = {'QED':1,'WCOrder':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '(CS2Dn1*MLM*WCOrder)/(2.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '-0.5*(CS2Dn1*MLM*WCOrder)/vev',
                  order = {'QED':1,'WCOrder':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '(CS2Dn1*MLT*WCOrder)/(2.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-0.5*(CS2Dn1*MLT*WCOrder)/vev',
                  order = {'QED':1,'WCOrder':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '-0.5*(CS2Dn1*MQU*WCOrder)/vev',
                  order = {'QED':1,'WCOrder':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '(CS2Dn1*MQU*WCOrder)/(2.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-0.5*(CS2Dn1*MQC*WCOrder)/vev',
                  order = {'QED':1,'WCOrder':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(CS2Dn1*MQC*WCOrder)/(2.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '-0.5*(CS2Dn1*MQT*WCOrder)/vev',
                  order = {'QED':1,'WCOrder':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '-0.5*(CS2Dn1*WCOrder*cmath.sqrt(G1**2 + GW**2)) + (CS2Dn2*WCOrder*cmath.sqrt(G1**2 + GW**2))/2.',
                  order = {'QED':1,'WCOrder':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '-0.5*(CS2Dn1*WCOrder*cmath.sqrt(G1**2 + GW**2))/vev + (3*CS2Dn3*WCOrder*cmath.sqrt(G1**2 + GW**2))/(2.*vev)',
                  order = {'QED':2,'WCOrder':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(ChiralOrder**2*CPDHn4prime*complex(0,1)*WCOrder)/(2.*cmath.pi**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(ChiralOrder**2*CPDHn6prime*complex(0,1)*WCOrder)/(cmath.pi**2*vev**6)',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(ChiralOrder**2*CPDHn5prime*complex(0,1)*WCOrder)/(2.*cmath.pi**2*vev**5)',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '((2*CP1n0*complex(0,1)*GW**4*WCOrder)/(G1**2 + GW**2)**1.5) + ((4*CP12n0*complex(0,1)*G1*GW**3*WCOrder)/(G1**2 + GW**2)**1.5)',
                  order = {'QED':1,'WCOrder':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(2*CP1n0*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2)**1.5',
                  order = {'QED':1,'WCOrder':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '((4*CP1n0*complex(0,1)*G1**3*GW**3*WCOrder)/(G1**2 + GW**2)**2) + ((4*CP12n0*complex(0,1)*G1**4*GW**2*WCOrder)/(G1**2 + GW**2)**2)',
                  order = {'QED':2,'WCOrder':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '((12*CP1n3*complex(0,1)*GW**2*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2))) + ((24*CP12n3*complex(0,1)*G1*GW*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':4,'WCOrder':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '((4*CP1n2*complex(0,1)*GW**2*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2))) + ((8*CP12n2*complex(0,1)*G1*GW*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':3,'WCOrder':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '((2*CP1n1*complex(0,1)*GW**2*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2))) + ((4*CP12n1*complex(0,1)*G1*GW*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':2,'WCOrder':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '((2*CP1n0*complex(0,1)*G1**3*GW*WCOrder)/(G1**2 + GW**2)**1.5) + ((-4*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2)**1.5)',
                  order = {'QED':1,'WCOrder':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '(-2*CP1n0*complex(0,1)*G1*GW**3*WCOrder)/(G1**2 + GW**2)**1.5',
                  order = {'QED':1,'WCOrder':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '((-12*CP1n3*complex(0,1)*G1*GW*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2))) + ((24*CP12n3*complex(0,1)*GW**2*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':4,'WCOrder':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '((-4*CP1n2*complex(0,1)*G1*GW*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2))) + ((8*CP12n2*complex(0,1)*GW**2*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':3,'WCOrder':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '((-2*CP1n1*complex(0,1)*G1*GW*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2))) + ((4*CP12n1*complex(0,1)*GW**2*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':2,'WCOrder':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '((4*CP1n0*complex(0,1)*G1**4*GW**2*WCOrder)/(G1**2 + GW**2)**2 - (4*CP1n0*complex(0,1)*G1**2*GW**4*WCOrder)/(G1**2 + GW**2)**2) + ((-12*CP12n0*complex(0,1)*G1**3*GW**3*WCOrder)/(G1**2 + GW**2)**2 - (4*CP12n0*complex(0,1)*G1*GW**5*WCOrder)/(G1**2 + GW**2)**2)',
                  order = {'QED':2,'WCOrder':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '((-4*CP1n0*complex(0,1)*G1**3*GW**3*WCOrder)/(G1**2 + GW**2)**2) + ((8*CP12n0*complex(0,1)*G1**2*GW**4*WCOrder)/(G1**2 + GW**2)**2 + (4*CP12n0*complex(0,1)*GW**6*WCOrder)/(G1**2 + GW**2)**2)',
                  order = {'QED':2,'WCOrder':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '((-4*CP1n0*complex(0,1)*G1**2*GW**2*WCOrder)/(3.*(G1**2 + GW**2)**1.5)) + ((-4*CP12n0*complex(0,1)*G1**3*GW*WCOrder)/(3.*(G1**2 + GW**2)**1.5))',
                  order = {'QED':1,'WCOrder':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '-0.3333333333333333*(complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2)**1.5',
                  order = {'QED':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '-0.3333333333333333*(CP1n0*complex(0,1)*G1*GW**3*WCOrder)/(G1**2 + GW**2)**1.5',
                  order = {'QED':1,'WCOrder':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '((CP1n0*complex(0,1)*G1**3*GW*WCOrder)/(G1**2 + GW**2)**1.5) + ((-7*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(3.*(G1**2 + GW**2)**1.5) - (CP12n0*complex(0,1)*GW**4*WCOrder)/(G1**2 + GW**2)**1.5)',
                  order = {'QED':1,'WCOrder':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '((CP1n0*complex(0,1)*G1**3*GW*WCOrder)/(G1**2 + GW**2)**1.5 - (CP1n0*complex(0,1)*G1*GW**3*WCOrder)/(3.*(G1**2 + GW**2)**1.5)) + ((-7*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(3.*(G1**2 + GW**2)**1.5) - (CP12n0*complex(0,1)*GW**4*WCOrder)/(G1**2 + GW**2)**1.5)',
                  order = {'QED':1,'WCOrder':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '((-4*CP1n0*complex(0,1)*G1*GW**3*WCOrder)/(3.*(G1**2 + GW**2)**1.5)) + ((-4*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(3.*(G1**2 + GW**2)**1.5))',
                  order = {'QED':1,'WCOrder':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '((2*CP1n0*complex(0,1)*G1**2*GW**2*WCOrder)/(3.*(G1**2 + GW**2)**1.5)) + ((2*CP12n0*complex(0,1)*G1**3*GW*WCOrder)/(3.*(G1**2 + GW**2)**1.5))',
                  order = {'QED':1,'WCOrder':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '(-((CP1n0*complex(0,1)*G1**3*GW*WCOrder)/(G1**2 + GW**2)**1.5) - (CP1n0*complex(0,1)*G1*GW**3*WCOrder)/(3.*(G1**2 + GW**2)**1.5)) + ((5*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(3.*(G1**2 + GW**2)**1.5) + (CP12n0*complex(0,1)*GW**4*WCOrder)/(G1**2 + GW**2)**1.5)',
                  order = {'QED':1,'WCOrder':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '((2*CP1n0*complex(0,1)*G1*GW**3*WCOrder)/(3.*(G1**2 + GW**2)**1.5)) + ((2*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(3.*(G1**2 + GW**2)**1.5))',
                  order = {'QED':1,'WCOrder':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '((CP1n0*complex(0,1)*G1*GW*WCOrder)/cmath.sqrt(G1**2 + GW**2)) + (-((CP12n0*complex(0,1)*GW**2*WCOrder)/cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':1,'WCOrder':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '((2*CP1n0*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2)**1.5) + ((2*CP12n0*complex(0,1)*G1**3*GW*WCOrder)/(G1**2 + GW**2)**1.5)',
                  order = {'QED':1,'WCOrder':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '(-((CP1n0*complex(0,1)*G1**3*GW*WCOrder)/(G1**2 + GW**2)**1.5) + (CP1n0*complex(0,1)*G1*GW**3*WCOrder)/(G1**2 + GW**2)**1.5) + ((3*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2)**1.5 + (CP12n0*complex(0,1)*GW**4*WCOrder)/(G1**2 + GW**2)**1.5)',
                  order = {'QED':1,'WCOrder':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '((2*CP1n0*complex(0,1)*G1*GW**3*WCOrder)/(G1**2 + GW**2)**1.5) + ((2*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(G1**2 + GW**2)**1.5)',
                  order = {'QED':1,'WCOrder':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '(-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQUn21x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev))',
                  order = {'QED':1,'WCOrder':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '(-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CQDn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev))',
                  order = {'QED':1,'WCOrder':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn32x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CQDn33x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '(-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev)) + (-((complex(0,1)*MQD)/vev))',
                  order = {'QED':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '(-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQD*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                  order = {'WCOrder':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '(-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev)) + (-((complex(0,1)*MQS)/vev))',
                  order = {'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '(-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2))) + (-((DeltaYQS*complex(0,1)*WCOrder)/cmath.sqrt(2)))',
                  order = {'WCOrder':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '(-0.5*(ChiralOrder*CP2n0*complex(0,1)*GW**3*WCOrder)/(cmath.pi*cmath.sqrt(G1**2 + GW**2))) + (-0.25*(ChiralOrder*CP3n0*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(ChiralOrder*CP13n0*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '((-3*ChiralOrder*CP2n3*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))) + ((-3*ChiralOrder*CP3n3*complex(0,1)*G1*GW**2*WCOrder)/(2.*cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))) + ((-3*ChiralOrder*CP13n3*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '(-((ChiralOrder*CP2n2*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2)))) + (-0.5*(ChiralOrder*CP3n2*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))) + (-((ChiralOrder*CP13n2*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '(-0.5*(ChiralOrder*CP2n1*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))) + (-0.25*(ChiralOrder*CP3n1*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(ChiralOrder*CP13n1*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_255 = Coupling(name = 'GC_255',
                  value = '((ChiralOrder*CP2n0*complex(0,1)*G1*GW**2*WCOrder)/(2.*cmath.pi*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(ChiralOrder*CP13n0*complex(0,1)*GW**3*WCOrder)/(cmath.pi*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '((3*ChiralOrder*CP2n3*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))) + ((-3*ChiralOrder*CP13n3*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '((ChiralOrder*CP2n2*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))) + (-((ChiralOrder*CP13n2*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '((ChiralOrder*CP2n1*complex(0,1)*G1*GW**2*WCOrder)/(2.*cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(ChiralOrder*CP13n1*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_259 = Coupling(name = 'GC_259',
                  value = '-0.25*(ChiralOrder*CP3n0*complex(0,1)*G1**2*GW*WCOrder)/(cmath.pi*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_260 = Coupling(name = 'GC_260',
                  value = '-0.25*(ChiralOrder*CP3n0*complex(0,1)*GW**3*WCOrder)/(cmath.pi*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '(-3*ChiralOrder*CP3n3*complex(0,1)*G1**2*GW*WCOrder)/(2.*cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_262 = Coupling(name = 'GC_262',
                  value = '(-3*ChiralOrder*CP3n3*complex(0,1)*GW**3*WCOrder)/(2.*cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '-0.5*(ChiralOrder*CP3n2*complex(0,1)*G1**2*GW*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '-0.5*(ChiralOrder*CP3n2*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '-0.25*(ChiralOrder*CP3n1*complex(0,1)*G1**2*GW*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '-0.25*(ChiralOrder*CP3n1*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '(-0.5*(ChiralOrder*CP3n0*complex(0,1)*GW**3*WCOrder)/cmath.pi) + (-((ChiralOrder*CP13n0*complex(0,1)*GW**3*WCOrder)/cmath.pi))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '(-((ChiralOrder*CP3n2*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev**2))) + ((-2*ChiralOrder*CP13n2*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev**2))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '(-0.5*(ChiralOrder*CP3n1*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev)) + (-((ChiralOrder*CP13n1*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev)))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-0.5*(ChiralOrder*CP3n0*complex(0,1)*G1**3*GW**2*WCOrder)/(cmath.pi*(G1**2 + GW**2)) - (ChiralOrder*CP3n0*complex(0,1)*G1*GW**4*WCOrder)/(2.*cmath.pi*(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '-((ChiralOrder*CP3n2*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev**2))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '-0.5*(ChiralOrder*CP3n1*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev)',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '(ChiralOrder*CP3n0*complex(0,1)*G1**2*GW**3*WCOrder)/(2.*cmath.pi*(G1**2 + GW**2)) + (ChiralOrder*CP3n0*complex(0,1)*GW**5*WCOrder)/(2.*cmath.pi*(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '(ChiralOrder*CP3n2*complex(0,1)*GW**3*WCOrder)/(cmath.pi*vev**2)',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '(ChiralOrder*CP3n1*complex(0,1)*GW**3*WCOrder)/(2.*cmath.pi*vev)',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '((3*ChiralOrder*CP4n3*complex(0,1)*GW*WCOrder)/(2.*cmath.pi*vev**3)) + ((3*ChiralOrder*CP5n3*complex(0,1)*G1*WCOrder)/(4.*cmath.pi*vev**3)) + ((3*ChiralOrder*CP17n3*complex(0,1)*G1*WCOrder)/(2.*cmath.pi*vev**3))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '((ChiralOrder*CP4n2*complex(0,1)*GW*WCOrder)/(2.*cmath.pi*vev**2)) + ((ChiralOrder*CP5n2*complex(0,1)*G1*WCOrder)/(4.*cmath.pi*vev**2)) + ((ChiralOrder*CP17n2*complex(0,1)*G1*WCOrder)/(2.*cmath.pi*vev**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '((ChiralOrder*CP4n1*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev)) + ((ChiralOrder*CP5n1*complex(0,1)*G1*WCOrder)/(8.*cmath.pi*vev)) + ((ChiralOrder*CP17n1*complex(0,1)*G1*WCOrder)/(4.*cmath.pi*vev))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '((-3*ChiralOrder*CP4n3*complex(0,1)*G1*WCOrder)/(2.*cmath.pi*vev**3)) + ((3*ChiralOrder*CP5n3*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev**3)) + ((3*ChiralOrder*CP17n3*complex(0,1)*GW*WCOrder)/(2.*cmath.pi*vev**3))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '(-0.5*(ChiralOrder*CP4n2*complex(0,1)*G1*WCOrder)/(cmath.pi*vev**2)) + ((ChiralOrder*CP5n2*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev**2)) + ((ChiralOrder*CP17n2*complex(0,1)*GW*WCOrder)/(2.*cmath.pi*vev**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '(-0.25*(ChiralOrder*CP4n1*complex(0,1)*G1*WCOrder)/(cmath.pi*vev)) + ((ChiralOrder*CP5n1*complex(0,1)*GW*WCOrder)/(8.*cmath.pi*vev)) + ((ChiralOrder*CP17n1*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '(3*ChiralOrder*CP5n3*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev**3)',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '(ChiralOrder*CP5n2*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '(ChiralOrder*CP5n1*complex(0,1)*GW*WCOrder)/(8.*cmath.pi*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_285 = Coupling(name = 'GC_285',
                  value = '(-3*ChiralOrder*CP5n3*complex(0,1)*G1*GW**2*WCOrder)/(4.*cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '-0.25*(ChiralOrder*CP5n2*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_287 = Coupling(name = 'GC_287',
                  value = '-0.125*(ChiralOrder*CP5n1*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_288 = Coupling(name = 'GC_288',
                  value = '((3*ChiralOrder*CP5n3*complex(0,1)*G1**2*GW*WCOrder)/(4.*cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))) + ((3*ChiralOrder*CP17n3*complex(0,1)*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(2.*cmath.pi*vev**3))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '((ChiralOrder*CP5n2*complex(0,1)*G1**2*GW*WCOrder)/(4.*cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))) + ((ChiralOrder*CP17n2*complex(0,1)*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(2.*cmath.pi*vev**2))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_290 = Coupling(name = 'GC_290',
                  value = '((ChiralOrder*CP5n1*complex(0,1)*G1**2*GW*WCOrder)/(8.*cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))) + ((ChiralOrder*CP17n1*complex(0,1)*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(4.*cmath.pi*vev))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_291 = Coupling(name = 'GC_291',
                  value = '(ChiralOrder**2*CP6n0*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '(ChiralOrder**2*CP6n2*complex(0,1)*GW**4*WCOrder)/(4.*cmath.pi**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_293 = Coupling(name = 'GC_293',
                  value = '(ChiralOrder**2*CP6n1*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2*vev)',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_294 = Coupling(name = 'GC_294',
                  value = '((ChiralOrder**2*CP6n0*complex(0,1)*G1**4*GW**2*WCOrder)/(8.*cmath.pi**2*(G1**2 + GW**2)) + (ChiralOrder**2*CP6n0*complex(0,1)*G1**2*GW**4*WCOrder)/(4.*cmath.pi**2*(G1**2 + GW**2)) + (ChiralOrder**2*CP6n0*complex(0,1)*GW**6*WCOrder)/(8.*cmath.pi**2*(G1**2 + GW**2))) + ((ChiralOrder**2*CP23n0*complex(0,1)*G1**4*GW**2*WCOrder)/(8.*cmath.pi**2*(G1**2 + GW**2)) + (ChiralOrder**2*CP23n0*complex(0,1)*G1**2*GW**4*WCOrder)/(4.*cmath.pi**2*(G1**2 + GW**2)) + (ChiralOrder**2*CP23n0*complex(0,1)*GW**6*WCOrder)/(8.*cmath.pi**2*(G1**2 + GW**2)))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_295 = Coupling(name = 'GC_295',
                  value = '((ChiralOrder**2*CP6n2*complex(0,1)*G1**2*GW**2*WCOrder)/(4.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP6n2*complex(0,1)*GW**4*WCOrder)/(4.*cmath.pi**2*vev**2)) + ((ChiralOrder**2*CP23n2*complex(0,1)*G1**2*GW**2*WCOrder)/(4.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP23n2*complex(0,1)*GW**4*WCOrder)/(4.*cmath.pi**2*vev**2))',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_296 = Coupling(name = 'GC_296',
                  value = '((ChiralOrder**2*CP6n1*complex(0,1)*G1**2*GW**2*WCOrder)/(8.*cmath.pi**2*vev) + (ChiralOrder**2*CP6n1*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2*vev)) + ((ChiralOrder**2*CP23n1*complex(0,1)*G1**2*GW**2*WCOrder)/(8.*cmath.pi**2*vev) + (ChiralOrder**2*CP23n1*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2*vev))',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_297 = Coupling(name = 'GC_297',
                  value = '((ChiralOrder**2*CP6n0*complex(0,1)*G1**4*WCOrder)/(8.*cmath.pi**2) + (ChiralOrder**2*CP6n0*complex(0,1)*G1**2*GW**2*WCOrder)/(4.*cmath.pi**2) + (ChiralOrder**2*CP6n0*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2)) + ((ChiralOrder**2*CP23n0*complex(0,1)*G1**4*WCOrder)/(4.*cmath.pi**2) + (ChiralOrder**2*CP23n0*complex(0,1)*G1**2*GW**2*WCOrder)/(2.*cmath.pi**2) + (ChiralOrder**2*CP23n0*complex(0,1)*GW**4*WCOrder)/(4.*cmath.pi**2)) + ((ChiralOrder**2*CP24n0*complex(0,1)*G1**4*WCOrder)/(4.*cmath.pi**2) + (ChiralOrder**2*CP24n0*complex(0,1)*G1**2*GW**2*WCOrder)/(2.*cmath.pi**2) + (ChiralOrder**2*CP24n0*complex(0,1)*GW**4*WCOrder)/(4.*cmath.pi**2)) + ((ChiralOrder**2*CP26n0*complex(0,1)*G1**4*WCOrder)/(2.*cmath.pi**2) + (ChiralOrder**2*CP26n0*complex(0,1)*G1**2*GW**2*WCOrder)/cmath.pi**2 + (ChiralOrder**2*CP26n0*complex(0,1)*GW**4*WCOrder)/(2.*cmath.pi**2)) + ((ChiralOrder**2*CP11n0*complex(0,1)*G1**4*WCOrder)/(8.*cmath.pi**2) + (ChiralOrder**2*CP11n0*complex(0,1)*G1**2*GW**2*WCOrder)/(4.*cmath.pi**2) + (ChiralOrder**2*CP11n0*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '((ChiralOrder**2*CP6n2*complex(0,1)*G1**4*WCOrder)/(4.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP6n2*complex(0,1)*G1**2*GW**2*WCOrder)/(2.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP6n2*complex(0,1)*GW**4*WCOrder)/(4.*cmath.pi**2*vev**2)) + ((ChiralOrder**2*CP23n2*complex(0,1)*G1**4*WCOrder)/(2.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP23n2*complex(0,1)*G1**2*GW**2*WCOrder)/(cmath.pi**2*vev**2) + (ChiralOrder**2*CP23n2*complex(0,1)*GW**4*WCOrder)/(2.*cmath.pi**2*vev**2)) + ((ChiralOrder**2*CP24n2*complex(0,1)*G1**4*WCOrder)/(2.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP24n2*complex(0,1)*G1**2*GW**2*WCOrder)/(cmath.pi**2*vev**2) + (ChiralOrder**2*CP24n2*complex(0,1)*GW**4*WCOrder)/(2.*cmath.pi**2*vev**2)) + ((ChiralOrder**2*CP26n2*complex(0,1)*G1**4*WCOrder)/(cmath.pi**2*vev**2) + (2*ChiralOrder**2*CP26n2*complex(0,1)*G1**2*GW**2*WCOrder)/(cmath.pi**2*vev**2) + (ChiralOrder**2*CP26n2*complex(0,1)*GW**4*WCOrder)/(cmath.pi**2*vev**2)) + ((ChiralOrder**2*CP11n2*complex(0,1)*G1**4*WCOrder)/(4.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP11n2*complex(0,1)*G1**2*GW**2*WCOrder)/(2.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP11n2*complex(0,1)*GW**4*WCOrder)/(4.*cmath.pi**2*vev**2))',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_299 = Coupling(name = 'GC_299',
                  value = '((ChiralOrder**2*CP6n1*complex(0,1)*G1**4*WCOrder)/(8.*cmath.pi**2*vev) + (ChiralOrder**2*CP6n1*complex(0,1)*G1**2*GW**2*WCOrder)/(4.*cmath.pi**2*vev) + (ChiralOrder**2*CP6n1*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2*vev)) + ((ChiralOrder**2*CP23n1*complex(0,1)*G1**4*WCOrder)/(4.*cmath.pi**2*vev) + (ChiralOrder**2*CP23n1*complex(0,1)*G1**2*GW**2*WCOrder)/(2.*cmath.pi**2*vev) + (ChiralOrder**2*CP23n1*complex(0,1)*GW**4*WCOrder)/(4.*cmath.pi**2*vev)) + ((ChiralOrder**2*CP24n1*complex(0,1)*G1**4*WCOrder)/(4.*cmath.pi**2*vev) + (ChiralOrder**2*CP24n1*complex(0,1)*G1**2*GW**2*WCOrder)/(2.*cmath.pi**2*vev) + (ChiralOrder**2*CP24n1*complex(0,1)*GW**4*WCOrder)/(4.*cmath.pi**2*vev)) + ((ChiralOrder**2*CP26n1*complex(0,1)*G1**4*WCOrder)/(2.*cmath.pi**2*vev) + (ChiralOrder**2*CP26n1*complex(0,1)*G1**2*GW**2*WCOrder)/(cmath.pi**2*vev) + (ChiralOrder**2*CP26n1*complex(0,1)*GW**4*WCOrder)/(2.*cmath.pi**2*vev)) + ((ChiralOrder**2*CP11n1*complex(0,1)*G1**4*WCOrder)/(8.*cmath.pi**2*vev) + (ChiralOrder**2*CP11n1*complex(0,1)*G1**2*GW**2*WCOrder)/(4.*cmath.pi**2*vev) + (ChiralOrder**2*CP11n1*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2*vev))',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_300 = Coupling(name = 'GC_300',
                  value = '(2*CP12n0*complex(0,1)*G1**3*GW*WCOrder)/(G1**2 + GW**2)**1.5',
                  order = {'QED':1,'WCOrder':1})

GC_301 = Coupling(name = 'GC_301',
                  value = '(-2*CP12n0*complex(0,1)*GW**4*WCOrder)/(G1**2 + GW**2)**1.5',
                  order = {'QED':1,'WCOrder':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '4*CP12n0*complex(0,1)*GW**2*WCOrder',
                  order = {'QED':2,'WCOrder':1})

GC_303 = Coupling(name = 'GC_303',
                  value = '((8*CP12n2*complex(0,1)*GW**2*WCOrder)/vev**2) + ((-2*CPWn2*complex(0,1)*GW**2*WCOrder)/vev**2)',
                  order = {'QED':4,'WCOrder':1})

GC_304 = Coupling(name = 'GC_304',
                  value = '((4*CP12n1*complex(0,1)*GW**2*WCOrder)/vev) + (-((CPWn1*complex(0,1)*GW**2*WCOrder)/vev))',
                  order = {'QED':3,'WCOrder':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '(2*complex(0,1)*G1**4)/(3.*(G1**2 + GW**2)**1.5) + (2*complex(0,1)*G1**2*GW**2)/(3.*(G1**2 + GW**2)**1.5)',
                  order = {'QED':1})

GC_306 = Coupling(name = 'GC_306',
                  value = '(-4*CP12n0*complex(0,1)*G1**2*GW**2*WCOrder)/(3.*(G1**2 + GW**2)**1.5)',
                  order = {'QED':1,'WCOrder':1})

GC_307 = Coupling(name = 'GC_307',
                  value = '-0.25*(ChiralOrder*CP14n0*G1**2*GW*WCOrder)/(cmath.pi*cmath.sqrt(G1**2 + GW**2)) - (ChiralOrder*CP14n0*GW**3*WCOrder)/(4.*cmath.pi*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_308 = Coupling(name = 'GC_308',
                  value = '(-3*ChiralOrder*CP14n3*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(2.*cmath.pi*vev**3)',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_309 = Coupling(name = 'GC_309',
                  value = '-0.5*(ChiralOrder*CP14n2*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi*vev**2)',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_310 = Coupling(name = 'GC_310',
                  value = '-0.25*(ChiralOrder*CP14n1*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_311 = Coupling(name = 'GC_311',
                  value = '-0.5*(ChiralOrder*CP14n0*complex(0,1)*G1**3*GW**2*WCOrder)/(cmath.pi*(complex(0,1)*G1 - GW)*(G1 - complex(0,1)*GW)) - (ChiralOrder*CP14n0*complex(0,1)*G1*GW**4*WCOrder)/(2.*cmath.pi*(complex(0,1)*G1 - GW)*(G1 - complex(0,1)*GW))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_312 = Coupling(name = 'GC_312',
                  value = '-((ChiralOrder*CP14n2*G1*GW**2*WCOrder)/(cmath.pi*vev**2))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_313 = Coupling(name = 'GC_313',
                  value = '-0.5*(ChiralOrder*CP14n1*G1*GW**2*WCOrder)/(cmath.pi*vev)',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '(3*ChiralOrder**2*CP18n3*complex(0,1)*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '(ChiralOrder**2*CP18n2*complex(0,1)*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_316 = Coupling(name = 'GC_316',
                  value = '(ChiralOrder**2*CP18n1*complex(0,1)*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(16.*cmath.pi**2*vev)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '(ChiralOrder**2*CP20n2prime*complex(0,1)*GW**2*WCOrder)/(8.*cmath.pi**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_318 = Coupling(name = 'GC_318',
                  value = '(ChiralOrder**2*CP20n3prime*complex(0,1)*GW**2*WCOrder)/(8.*cmath.pi**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '(ChiralOrder**2*CP20n4prime*complex(0,1)*GW**2*WCOrder)/(4.*cmath.pi**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '((ChiralOrder**2*CP20n2prime*complex(0,1)*G1**2*WCOrder)/(8.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP20n2prime*complex(0,1)*GW**2*WCOrder)/(8.*cmath.pi**2*vev**2)) + ((ChiralOrder**2*CP21n2prime*complex(0,1)*G1**2*WCOrder)/(4.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP21n2prime*complex(0,1)*GW**2*WCOrder)/(4.*cmath.pi**2*vev**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '((ChiralOrder**2*CP20n3prime*complex(0,1)*G1**2*WCOrder)/(8.*cmath.pi**2*vev**3) + (ChiralOrder**2*CP20n3prime*complex(0,1)*GW**2*WCOrder)/(8.*cmath.pi**2*vev**3)) + ((ChiralOrder**2*CP21n3prime*complex(0,1)*G1**2*WCOrder)/(4.*cmath.pi**2*vev**3) + (ChiralOrder**2*CP21n3prime*complex(0,1)*GW**2*WCOrder)/(4.*cmath.pi**2*vev**3))',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '((ChiralOrder**2*CP20n4prime*complex(0,1)*G1**2*WCOrder)/(4.*cmath.pi**2*vev**4) + (ChiralOrder**2*CP20n4prime*complex(0,1)*GW**2*WCOrder)/(4.*cmath.pi**2*vev**4)) + ((ChiralOrder**2*CP21n4prime*complex(0,1)*G1**2*WCOrder)/(2.*cmath.pi**2*vev**4) + (ChiralOrder**2*CP21n4prime*complex(0,1)*GW**2*WCOrder)/(2.*cmath.pi**2*vev**4))',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '((ChiralOrder**2*CP22n2prime*complex(0,1)*G1**2*WCOrder)/(8.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP22n2prime*complex(0,1)*GW**2*WCOrder)/(8.*cmath.pi**2*vev**2)) + ((ChiralOrder**2*CP8n2prime*complex(0,1)*G1**2*WCOrder)/(16.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP8n2prime*complex(0,1)*GW**2*WCOrder)/(16.*cmath.pi**2*vev**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '((ChiralOrder**2*CP22n3prime*complex(0,1)*G1**2*WCOrder)/(8.*cmath.pi**2*vev**3) + (ChiralOrder**2*CP22n3prime*complex(0,1)*GW**2*WCOrder)/(8.*cmath.pi**2*vev**3)) + ((ChiralOrder**2*CP8n3prime*complex(0,1)*G1**2*WCOrder)/(16.*cmath.pi**2*vev**3) + (ChiralOrder**2*CP8n3prime*complex(0,1)*GW**2*WCOrder)/(16.*cmath.pi**2*vev**3))',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '((ChiralOrder**2*CP22n4prime*complex(0,1)*G1**2*WCOrder)/(4.*cmath.pi**2*vev**4) + (ChiralOrder**2*CP22n4prime*complex(0,1)*GW**2*WCOrder)/(4.*cmath.pi**2*vev**4)) + ((ChiralOrder**2*CP8n4prime*complex(0,1)*G1**2*WCOrder)/(8.*cmath.pi**2*vev**4) + (ChiralOrder**2*CP8n4prime*complex(0,1)*GW**2*WCOrder)/(8.*cmath.pi**2*vev**4))',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '((ChiralOrder**2*CP24n0*complex(0,1)*G1**4*GW**2*WCOrder)/(16.*cmath.pi**2*(G1**2 + GW**2)) + (ChiralOrder**2*CP24n0*complex(0,1)*G1**2*GW**4*WCOrder)/(8.*cmath.pi**2*(G1**2 + GW**2)) + (ChiralOrder**2*CP24n0*complex(0,1)*GW**6*WCOrder)/(16.*cmath.pi**2*(G1**2 + GW**2))) + ((ChiralOrder**2*CP11n0*complex(0,1)*G1**4*GW**2*WCOrder)/(16.*cmath.pi**2*(G1**2 + GW**2)) + (ChiralOrder**2*CP11n0*complex(0,1)*G1**2*GW**4*WCOrder)/(8.*cmath.pi**2*(G1**2 + GW**2)) + (ChiralOrder**2*CP11n0*complex(0,1)*GW**6*WCOrder)/(16.*cmath.pi**2*(G1**2 + GW**2)))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '((ChiralOrder**2*CP24n2*complex(0,1)*G1**2*GW**2*WCOrder)/(8.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP24n2*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2*vev**2)) + ((ChiralOrder**2*CP11n2*complex(0,1)*G1**2*GW**2*WCOrder)/(8.*cmath.pi**2*vev**2) + (ChiralOrder**2*CP11n2*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2*vev**2))',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '((ChiralOrder**2*CP24n1*complex(0,1)*G1**2*GW**2*WCOrder)/(16.*cmath.pi**2*vev) + (ChiralOrder**2*CP24n1*complex(0,1)*GW**4*WCOrder)/(16.*cmath.pi**2*vev)) + ((ChiralOrder**2*CP11n1*complex(0,1)*G1**2*GW**2*WCOrder)/(16.*cmath.pi**2*vev) + (ChiralOrder**2*CP11n1*complex(0,1)*GW**4*WCOrder)/(16.*cmath.pi**2*vev))',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '(12*CS1n3*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**3)',
                  order = {'QED':3,'WCOrder':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '(12*CS1n3*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**3)',
                  order = {'QED':3,'WCOrder':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '(4*CS1n2*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '(4*CS1n2*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '(2*CS1n1*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '(2*CS1n1*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '((-2*CS1n0*complex(0,1)*GW**2*WCOrder)/cmath.sqrt(G1**2 + GW**2)) + ((-4*CS8n0*complex(0,1)*G1*GW*WCOrder)/cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':1,'WCOrder':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '((2*CS1n0*complex(0,1)*G1*GW*WCOrder)/cmath.sqrt(G1**2 + GW**2)) + ((-4*CS8n0*complex(0,1)*GW**2*WCOrder)/cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':1,'WCOrder':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '((-12*CS1n3*complex(0,1)*GW**2*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2))) + ((-24*CS8n3*complex(0,1)*G1*GW*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':4,'WCOrder':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '((-4*CS1n2*complex(0,1)*GW**2*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2))) + ((-8*CS8n2*complex(0,1)*G1*GW*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':3,'WCOrder':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '((-2*CS1n1*complex(0,1)*GW**2*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2))) + ((-4*CS8n1*complex(0,1)*G1*GW*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':2,'WCOrder':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '((12*CS1n3*complex(0,1)*G1*GW*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2))) + ((-24*CS8n3*complex(0,1)*GW**2*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':4,'WCOrder':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '((4*CS1n2*complex(0,1)*G1*GW*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2))) + ((-8*CS8n2*complex(0,1)*GW**2*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':3,'WCOrder':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '((2*CS1n1*complex(0,1)*G1*GW*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2))) + ((-4*CS8n1*complex(0,1)*GW**2*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':2,'WCOrder':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '((3*ChiralOrder*CS2n3*complex(0,1)*GW*WCOrder)/(2.*cmath.pi*vev**3)) + ((3*ChiralOrder*CS3n3*complex(0,1)*G1*WCOrder)/(4.*cmath.pi*vev**3)) + ((3*ChiralOrder*CS9n3*complex(0,1)*G1*WCOrder)/(2.*cmath.pi*vev**3))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '((ChiralOrder*CS2n2*complex(0,1)*GW*WCOrder)/(2.*cmath.pi*vev**2)) + ((ChiralOrder*CS3n2*complex(0,1)*G1*WCOrder)/(4.*cmath.pi*vev**2)) + ((ChiralOrder*CS9n2*complex(0,1)*G1*WCOrder)/(2.*cmath.pi*vev**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '((ChiralOrder*CS2n1*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev)) + ((ChiralOrder*CS3n1*complex(0,1)*G1*WCOrder)/(8.*cmath.pi*vev)) + ((ChiralOrder*CS9n1*complex(0,1)*G1*WCOrder)/(4.*cmath.pi*vev))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_346 = Coupling(name = 'GC_346',
                  value = '((-3*ChiralOrder*CS2n3*complex(0,1)*G1*WCOrder)/(2.*cmath.pi*vev**3)) + ((3*ChiralOrder*CS3n3*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev**3)) + ((3*ChiralOrder*CS9n3*complex(0,1)*GW*WCOrder)/(2.*cmath.pi*vev**3))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_347 = Coupling(name = 'GC_347',
                  value = '(-0.5*(ChiralOrder*CS2n2*complex(0,1)*G1*WCOrder)/(cmath.pi*vev**2)) + ((ChiralOrder*CS3n2*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev**2)) + ((ChiralOrder*CS9n2*complex(0,1)*GW*WCOrder)/(2.*cmath.pi*vev**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_348 = Coupling(name = 'GC_348',
                  value = '(-0.25*(ChiralOrder*CS2n1*complex(0,1)*G1*WCOrder)/(cmath.pi*vev)) + ((ChiralOrder*CS3n1*complex(0,1)*GW*WCOrder)/(8.*cmath.pi*vev)) + ((ChiralOrder*CS9n1*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '(3*ChiralOrder*CS3n3*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev**3)',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_350 = Coupling(name = 'GC_350',
                  value = '(ChiralOrder*CS3n2*complex(0,1)*GW*WCOrder)/(4.*cmath.pi*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '(ChiralOrder*CS3n1*complex(0,1)*GW*WCOrder)/(8.*cmath.pi*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(-3*ChiralOrder*CS3n3*complex(0,1)*G1*GW**2*WCOrder)/(2.*cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '-0.5*(ChiralOrder*CS3n2*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_354 = Coupling(name = 'GC_354',
                  value = '-0.25*(ChiralOrder*CS3n1*complex(0,1)*G1*GW**2*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '((-3*ChiralOrder*CS3n3*complex(0,1)*G1**2*GW*WCOrder)/(4.*cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2)) - (9*ChiralOrder*CS3n3*complex(0,1)*GW**3*WCOrder)/(4.*cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))) + ((-3*ChiralOrder*CS9n3*complex(0,1)*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(2.*cmath.pi*vev**3))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '(-0.25*(ChiralOrder*CS3n2*complex(0,1)*G1**2*GW*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2)) - (3*ChiralOrder*CS3n2*complex(0,1)*GW**3*WCOrder)/(4.*cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))) + (-0.5*(ChiralOrder*CS9n2*complex(0,1)*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi*vev**2))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '(-0.125*(ChiralOrder*CS3n1*complex(0,1)*G1**2*GW*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2)) - (3*ChiralOrder*CS3n1*complex(0,1)*GW**3*WCOrder)/(8.*cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))) + (-0.25*(ChiralOrder*CS9n1*complex(0,1)*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi*vev))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '-0.125*(ChiralOrder*CS4n0*G1**2*GW*WCOrder)/(cmath.pi*cmath.sqrt(G1**2 + GW**2)) - (ChiralOrder*CS4n0*GW**3*WCOrder)/(8.*cmath.pi*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '(ChiralOrder*CS4n0*G1**3*GW**2*WCOrder)/(8.*cmath.pi*(G1 - complex(0,1)*GW)*(G1 + complex(0,1)*GW)) + (ChiralOrder*CS4n0*G1*GW**4*WCOrder)/(8.*cmath.pi*(G1 - complex(0,1)*GW)*(G1 + complex(0,1)*GW))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(-3*ChiralOrder*CS4n3*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(4.*cmath.pi*vev**3)',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '-0.25*(ChiralOrder*CS4n2*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi*vev**2)',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '-0.125*(ChiralOrder*CS4n1*GW*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '(ChiralOrder*CS4n2*G1*GW**2*WCOrder)/(4.*cmath.pi*vev**2)',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '(ChiralOrder*CS4n1*G1*GW**2*WCOrder)/(8.*cmath.pi*vev)',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '(-3*ChiralOrder**2*CS5n3*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(16.*cmath.pi**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '-0.0625*(ChiralOrder**2*CS5n2*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '-0.03125*(ChiralOrder**2*CS5n1*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_368 = Coupling(name = 'GC_368',
                  value = '((-3*ChiralOrder**2*CS5n3*G1**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev**3) - (3*ChiralOrder**2*CS5n3*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev**3)) + ((-3*ChiralOrder**2*CS6n3*G1**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev**3) - (3*ChiralOrder**2*CS6n3*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev**3)) + ((-3*ChiralOrder**2*CS15n3*G1**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(4.*cmath.pi**2*vev**3) - (3*ChiralOrder**2*CS15n3*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(4.*cmath.pi**2*vev**3))',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '(-0.125*(ChiralOrder**2*CS5n2*G1**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev**2) - (ChiralOrder**2*CS5n2*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev**2)) + (-0.125*(ChiralOrder**2*CS6n2*G1**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev**2) - (ChiralOrder**2*CS6n2*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev**2)) + (-0.25*(ChiralOrder**2*CS15n2*G1**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev**2) - (ChiralOrder**2*CS15n2*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(4.*cmath.pi**2*vev**2))',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_370 = Coupling(name = 'GC_370',
                  value = '(-0.0625*(ChiralOrder**2*CS5n1*G1**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev) - (ChiralOrder**2*CS5n1*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(16.*cmath.pi**2*vev)) + (-0.0625*(ChiralOrder**2*CS6n1*G1**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev) - (ChiralOrder**2*CS6n1*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(16.*cmath.pi**2*vev)) + (-0.125*(ChiralOrder**2*CS15n1*G1**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev) - (ChiralOrder**2*CS15n1*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_371 = Coupling(name = 'GC_371',
                  value = '(-3*ChiralOrder**2*CS6n3*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(8.*cmath.pi**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_372 = Coupling(name = 'GC_372',
                  value = '-0.125*(ChiralOrder**2*CS6n2*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_373 = Coupling(name = 'GC_373',
                  value = '-0.0625*(ChiralOrder**2*CS6n1*GW**2*WCOrder*cmath.sqrt(G1**2 + GW**2))/(cmath.pi**2*vev)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_374 = Coupling(name = 'GC_374',
                  value = '(3*ChiralOrder*CS7n3*GW*WCOrder)/(2.*cmath.pi*vev**3)',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_375 = Coupling(name = 'GC_375',
                  value = '(ChiralOrder*CS7n2*GW*WCOrder)/(2.*cmath.pi*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_376 = Coupling(name = 'GC_376',
                  value = '(ChiralOrder*CS7n1*GW*WCOrder)/(4.*cmath.pi*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_377 = Coupling(name = 'GC_377',
                  value = '(3*ChiralOrder*CS7n3*G1*GW**2*WCOrder)/(2.*cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_378 = Coupling(name = 'GC_378',
                  value = '(ChiralOrder*CS7n2*G1*GW**2*WCOrder)/(2.*cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '(ChiralOrder*CS7n1*G1*GW**2*WCOrder)/(4.*cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_380 = Coupling(name = 'GC_380',
                  value = '(-3*ChiralOrder*CS7n3*GW**3*WCOrder)/(cmath.pi*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':5,'WCOrder':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '-((ChiralOrder*CS7n2*GW**3*WCOrder)/(cmath.pi*vev**2*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'ChiralOrder':1,'QED':4,'WCOrder':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '-0.5*(ChiralOrder*CS7n1*GW**3*WCOrder)/(cmath.pi*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '(4*ChiralOrder**2*CPWHD1n4prime*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_384 = Coupling(name = 'GC_384',
                  value = '(2*ChiralOrder**2*CPWHD1n3prime*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_385 = Coupling(name = 'GC_385',
                  value = '(2*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_386 = Coupling(name = 'GC_386',
                  value = '(4*ChiralOrder**2*CPWHD1n4prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_387 = Coupling(name = 'GC_387',
                  value = '(2*ChiralOrder**2*CPWHD1n3prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_388 = Coupling(name = 'GC_388',
                  value = '(2*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_389 = Coupling(name = 'GC_389',
                  value = '(4*ChiralOrder**2*CPWHD1n4prime*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_390 = Coupling(name = 'GC_390',
                  value = '(2*ChiralOrder**2*CPWHD1n3prime*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_391 = Coupling(name = 'GC_391',
                  value = '(2*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '(4*ChiralOrder**2*CPWHD1n4prime*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_393 = Coupling(name = 'GC_393',
                  value = '(2*ChiralOrder**2*CPWHD1n3prime*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_394 = Coupling(name = 'GC_394',
                  value = '(2*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_395 = Coupling(name = 'GC_395',
                  value = '((-3*CLEn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2) + ((-3*CLEn31x1*complex(0,1)*WCOrder*cmath.sqrt(2))/vev**2)',
                  order = {'QED':2,'WCOrder':1})

GC_396 = Coupling(name = 'GC_396',
                  value = '(-2*ChiralOrder**2*CPWHD1n3prime*complex(0,1)*G1*GW*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_397 = Coupling(name = 'GC_397',
                  value = '(-2*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*G1*GW*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '(-4*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '(-2*ChiralOrder**2*CPWHD1n3prime*complex(0,1)*GW**2*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '(-2*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*GW**2*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_401 = Coupling(name = 'GC_401',
                  value = '(4*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*GW**2*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '(2*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*G1*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_403 = Coupling(name = 'GC_403',
                  value = '(-4*ChiralOrder**2*CPWHD1n2prime*complex(0,1)*GW**4*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_404 = Coupling(name = 'GC_404',
                  value = '(-16*ChiralOrder**2*CPWHD2n4prime*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_405 = Coupling(name = 'GC_405',
                  value = '(-8*ChiralOrder**2*CPWHD2n3prime*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_406 = Coupling(name = 'GC_406',
                  value = '(-8*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_407 = Coupling(name = 'GC_407',
                  value = '(-16*ChiralOrder**2*CPWHD2n4prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_408 = Coupling(name = 'GC_408',
                  value = '(-8*ChiralOrder**2*CPWHD2n3prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_409 = Coupling(name = 'GC_409',
                  value = '(-8*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_410 = Coupling(name = 'GC_410',
                  value = '(-16*ChiralOrder**2*CPWHD2n4prime*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_411 = Coupling(name = 'GC_411',
                  value = '(-8*ChiralOrder**2*CPWHD2n3prime*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_412 = Coupling(name = 'GC_412',
                  value = '(-8*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_413 = Coupling(name = 'GC_413',
                  value = '(-16*ChiralOrder**2*CPWHD2n4prime*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_414 = Coupling(name = 'GC_414',
                  value = '(-8*ChiralOrder**2*CPWHD2n3prime*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_415 = Coupling(name = 'GC_415',
                  value = '(-8*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_416 = Coupling(name = 'GC_416',
                  value = '(-8*ChiralOrder**2*CPWHD2n3prime*complex(0,1)*G1*GW*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_417 = Coupling(name = 'GC_417',
                  value = '(-8*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*G1*GW*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_418 = Coupling(name = 'GC_418',
                  value = '(8*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_419 = Coupling(name = 'GC_419',
                  value = '(-8*ChiralOrder**2*CPWHD2n3prime*complex(0,1)*GW**2*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_420 = Coupling(name = 'GC_420',
                  value = '(-8*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*GW**2*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_421 = Coupling(name = 'GC_421',
                  value = '(-8*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*GW**2*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_422 = Coupling(name = 'GC_422',
                  value = '(-16*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*G1*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_423 = Coupling(name = 'GC_423',
                  value = '(8*ChiralOrder**2*CPWHD2n2prime*complex(0,1)*GW**4*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_424 = Coupling(name = 'GC_424',
                  value = '(-4*ChiralOrder**2*CSWHDTn4prime*WCOrder)/(LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_425 = Coupling(name = 'GC_425',
                  value = '(-2*ChiralOrder**2*CSWHDTn3prime*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_426 = Coupling(name = 'GC_426',
                  value = '(-2*ChiralOrder**2*CSWHDTn2prime*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_427 = Coupling(name = 'GC_427',
                  value = '(2*ChiralOrder**2*CSWHDTn3prime*G1*GW*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_428 = Coupling(name = 'GC_428',
                  value = '(2*ChiralOrder**2*CSWHDTn2prime*G1*GW*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_429 = Coupling(name = 'GC_429',
                  value = '(4*ChiralOrder**2*CSWHDTn2prime*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_430 = Coupling(name = 'GC_430',
                  value = '(-2*ChiralOrder**2*CSWHDTn3prime*GW**2*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_431 = Coupling(name = 'GC_431',
                  value = '(-2*ChiralOrder**2*CSWHDTn2prime*GW**2*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_432 = Coupling(name = 'GC_432',
                  value = '(4*ChiralOrder**2*CSWHDTn2prime*G1*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_433 = Coupling(name = 'GC_433',
                  value = '(4*ChiralOrder**2*CSWHDTn2prime*GW**4*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '(-6*CPWn3*complex(0,1)*WCOrder)/vev**3',
                  order = {'QED':3,'WCOrder':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '(-2*CPWn2*complex(0,1)*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '-((CPWn1*complex(0,1)*WCOrder)/vev)',
                  order = {'QED':1,'WCOrder':1})

GC_437 = Coupling(name = 'GC_437',
                  value = '(-6*CPWn3*complex(0,1)*G1*GW*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':4,'WCOrder':1})

GC_438 = Coupling(name = 'GC_438',
                  value = '(-2*CPWn2*complex(0,1)*G1*GW*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':3,'WCOrder':1})

GC_439 = Coupling(name = 'GC_439',
                  value = '-((CPWn1*complex(0,1)*G1*GW*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':2,'WCOrder':1})

GC_440 = Coupling(name = 'GC_440',
                  value = '(2*CPWn2*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev**2)',
                  order = {'QED':4,'WCOrder':1})

GC_441 = Coupling(name = 'GC_441',
                  value = '(CPWn1*complex(0,1)*G1**2*GW**2*WCOrder)/((G1**2 + GW**2)*vev)',
                  order = {'QED':3,'WCOrder':1})

GC_442 = Coupling(name = 'GC_442',
                  value = '(-6*CPWn3*complex(0,1)*GW**2*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':4,'WCOrder':1})

GC_443 = Coupling(name = 'GC_443',
                  value = '(-2*CPWn2*complex(0,1)*GW**2*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':3,'WCOrder':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '-((CPWn1*complex(0,1)*GW**2*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2)))',
                  order = {'QED':2,'WCOrder':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '(-4*CPWn2*complex(0,1)*G1*GW**3*WCOrder)/((G1**2 + GW**2)*vev**2)',
                  order = {'QED':4,'WCOrder':1})

GC_446 = Coupling(name = 'GC_446',
                  value = '(-2*CPWn1*complex(0,1)*G1*GW**3*WCOrder)/((G1**2 + GW**2)*vev)',
                  order = {'QED':3,'WCOrder':1})

GC_447 = Coupling(name = 'GC_447',
                  value = '(2*CPWn2*complex(0,1)*GW**4*WCOrder)/((G1**2 + GW**2)*vev**2)',
                  order = {'QED':4,'WCOrder':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '(CPWn1*complex(0,1)*GW**4*WCOrder)/((G1**2 + GW**2)*vev)',
                  order = {'QED':3,'WCOrder':1})

GC_449 = Coupling(name = 'GC_449',
                  value = '(3*CSWn3*complex(0,1)*WCOrder)/vev**3',
                  order = {'QED':3,'WCOrder':1})

GC_450 = Coupling(name = 'GC_450',
                  value = '(CSWn2*complex(0,1)*WCOrder)/vev**2',
                  order = {'QED':2,'WCOrder':1})

GC_451 = Coupling(name = 'GC_451',
                  value = '(CSWn1*complex(0,1)*WCOrder)/(2.*vev)',
                  order = {'QED':1,'WCOrder':1})

GC_452 = Coupling(name = 'GC_452',
                  value = '(-((CLEn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)) + (-((CLEn23x3*complex(0,1)*WCOrder*cmath.sqrt(2))/vev))',
                  order = {'QED':1,'WCOrder':1})

GC_453 = Coupling(name = 'GC_453',
                  value = '(6*CSWn3*complex(0,1)*G1*GW*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':4,'WCOrder':1})

GC_454 = Coupling(name = 'GC_454',
                  value = '(2*CSWn2*complex(0,1)*G1*GW*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':3,'WCOrder':1})

GC_455 = Coupling(name = 'GC_455',
                  value = '(CSWn1*complex(0,1)*G1*GW*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':2,'WCOrder':1})

GC_456 = Coupling(name = 'GC_456',
                  value = '(6*CSWn3*complex(0,1)*GW**2*WCOrder)/(vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':4,'WCOrder':1})

GC_457 = Coupling(name = 'GC_457',
                  value = '(2*CSWn2*complex(0,1)*GW**2*WCOrder)/(vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':3,'WCOrder':1})

GC_458 = Coupling(name = 'GC_458',
                  value = '(CSWn1*complex(0,1)*GW**2*WCOrder)/(vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'QED':2,'WCOrder':1})

GC_459 = Coupling(name = 'GC_459',
                  value = '(8*ChiralOrder**2*CSWHDn4prime*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_460 = Coupling(name = 'GC_460',
                  value = '(4*ChiralOrder**2*CSWHDn3prime*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_461 = Coupling(name = 'GC_461',
                  value = '(4*ChiralOrder**2*CSWHDn2prime*complex(0,1)*G1**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_462 = Coupling(name = 'GC_462',
                  value = '(8*ChiralOrder**2*CSWHDn4prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_463 = Coupling(name = 'GC_463',
                  value = '(4*ChiralOrder**2*CSWHDn3prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_464 = Coupling(name = 'GC_464',
                  value = '(4*ChiralOrder**2*CSWHDn2prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_465 = Coupling(name = 'GC_465',
                  value = '(8*ChiralOrder**2*CSWHDn4prime*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_466 = Coupling(name = 'GC_466',
                  value = '(4*ChiralOrder**2*CSWHDn3prime*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_467 = Coupling(name = 'GC_467',
                  value = '(4*ChiralOrder**2*CSWHDn2prime*complex(0,1)*G1*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_468 = Coupling(name = 'GC_468',
                  value = '(8*ChiralOrder**2*CSWHDn4prime*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '(4*ChiralOrder**2*CSWHDn3prime*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_470 = Coupling(name = 'GC_470',
                  value = '(4*ChiralOrder**2*CSWHDn2prime*complex(0,1)*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_471 = Coupling(name = 'GC_471',
                  value = '(8*ChiralOrder**2*CSWHDn3prime*complex(0,1)*G1*GW*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_472 = Coupling(name = 'GC_472',
                  value = '(8*ChiralOrder**2*CSWHDn2prime*complex(0,1)*G1*GW*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_473 = Coupling(name = 'GC_473',
                  value = '(8*ChiralOrder**2*CSWHDn3prime*complex(0,1)*GW**2*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_474 = Coupling(name = 'GC_474',
                  value = '(8*ChiralOrder**2*CSWHDn2prime*complex(0,1)*GW**2*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_475 = Coupling(name = 'GC_475',
                  value = '(ChiralOrder**2*CP11n0*complex(0,1)*GW**4*WCOrder)/(16.*cmath.pi**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_476 = Coupling(name = 'GC_476',
                  value = '(ChiralOrder**2*CP11n2*complex(0,1)*GW**4*WCOrder)/(8.*cmath.pi**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '(ChiralOrder**2*CP11n1*complex(0,1)*GW**4*WCOrder)/(16.*cmath.pi**2*vev)',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_478 = Coupling(name = 'GC_478',
                  value = '(ChiralOrder**2*CP8n2prime*complex(0,1)*GW**2*WCOrder)/(16.*cmath.pi**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_479 = Coupling(name = 'GC_479',
                  value = '(ChiralOrder**2*CP8n3prime*complex(0,1)*GW**2*WCOrder)/(16.*cmath.pi**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':5,'WCOrder':1})

GC_480 = Coupling(name = 'GC_480',
                  value = '(ChiralOrder**2*CP8n4prime*complex(0,1)*GW**2*WCOrder)/(8.*cmath.pi**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':6,'WCOrder':1})

GC_481 = Coupling(name = 'GC_481',
                  value = '(4*ChiralOrder**2*CPGHD1n4prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_482 = Coupling(name = 'GC_482',
                  value = '(2*ChiralOrder**2*CPGHD1n3prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_483 = Coupling(name = 'GC_483',
                  value = '(2*ChiralOrder**2*CPGHD1n2prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_484 = Coupling(name = 'GC_484',
                  value = '(2*ChiralOrder**2*CPGHD1n3prime*GS*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QCD':1,'QED':3,'WCOrder':1})

GC_485 = Coupling(name = 'GC_485',
                  value = '(2*ChiralOrder**2*CPGHD1n2prime*GS*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QCD':1,'QED':2,'WCOrder':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '(-2*ChiralOrder**2*CPGHD1n2prime*complex(0,1)*GS**2*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QCD':2,'QED':2,'WCOrder':1})

GC_487 = Coupling(name = 'GC_487',
                  value = '(-16*ChiralOrder**2*CPGHD2n4prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '(-8*ChiralOrder**2*CPGHD2n3prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_489 = Coupling(name = 'GC_489',
                  value = '(-8*ChiralOrder**2*CPGHD2n2prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '(8*ChiralOrder**2*CPGHD2n3prime*GS*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QCD':1,'QED':3,'WCOrder':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '(8*ChiralOrder**2*CPGHD2n2prime*GS*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QCD':1,'QED':2,'WCOrder':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '(8*ChiralOrder**2*CPGHD2n2prime*complex(0,1)*GS**2*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QCD':2,'QED':2,'WCOrder':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '(2*ChiralOrder**2*CSGHDn4prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**4)',
                  order = {'ChiralOrder':2,'QED':4,'WCOrder':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '(ChiralOrder**2*CSGHDn3prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QED':3,'WCOrder':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '(ChiralOrder**2*CSGHDn2prime*complex(0,1)*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QED':2,'WCOrder':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '(-2*ChiralOrder**2*CSGHDn3prime*GS*WCOrder)/(LamHEFT**2*vev**3)',
                  order = {'ChiralOrder':2,'QCD':1,'QED':3,'WCOrder':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '(-2*ChiralOrder**2*CSGHDn2prime*GS*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':2,'QCD':1,'QED':2,'WCOrder':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '(24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*G1*WCOrder)/(LamHEFT**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'WCOrder':1})

GC_499 = Coupling(name = 'GC_499',
                  value = '(144*ChiralOrder*CPWWWn3*cmath.pi*complex(0,1)*G1*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_500 = Coupling(name = 'GC_500',
                  value = '(48*ChiralOrder*CPWWWn2*cmath.pi*complex(0,1)*G1*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_501 = Coupling(name = 'GC_501',
                  value = '(24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*G1*WCOrder)/(LamHEFT**2*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_502 = Coupling(name = 'GC_502',
                  value = '(24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'WCOrder':1})

GC_503 = Coupling(name = 'GC_503',
                  value = '(144*ChiralOrder*CPWWWn3*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_504 = Coupling(name = 'GC_504',
                  value = '(48*ChiralOrder*CPWWWn2*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_505 = Coupling(name = 'GC_505',
                  value = '(24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '(-24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*G1**2*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '(-48*ChiralOrder*CPWWWn2*cmath.pi*complex(0,1)*G1**2*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '(-24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*G1**2*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '(24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_510 = Coupling(name = 'GC_510',
                  value = '(48*ChiralOrder*CPWWWn2*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '(24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_512 = Coupling(name = 'GC_512',
                  value = '(-48*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*G1**3*GW**2*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '(-48*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*G1**3*GW**2*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_514 = Coupling(name = 'GC_514',
                  value = '(24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*GW*WCOrder)/LamHEFT**2',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_515 = Coupling(name = 'GC_515',
                  value = '(48*ChiralOrder*CPWWWn2*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_516 = Coupling(name = 'GC_516',
                  value = '(24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_517 = Coupling(name = 'GC_517',
                  value = '(-24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*G1**2*GW**3*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '(-24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*G1**2*GW**3*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_519 = Coupling(name = 'GC_519',
                  value = '(-24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/(LamHEFT**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '(-24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/(LamHEFT**2*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_521 = Coupling(name = 'GC_521',
                  value = '(-96*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*G1**2*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '(-24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_523 = Coupling(name = 'GC_523',
                  value = '(-48*ChiralOrder*CPWWWn2*cmath.pi*complex(0,1)*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_524 = Coupling(name = 'GC_524',
                  value = '(-24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_525 = Coupling(name = 'GC_525',
                  value = '(-24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*G1*GW**4*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_526 = Coupling(name = 'GC_526',
                  value = '(-24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*G1*GW**4*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_527 = Coupling(name = 'GC_527',
                  value = '(-24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*GW**3*WCOrder)/(LamHEFT**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '(-24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*GW**3*WCOrder)/(LamHEFT**2*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_529 = Coupling(name = 'GC_529',
                  value = '(-96*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*G1*GW**4*WCOrder)/((G1**2 + GW**2)*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '(-24*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*GW**5*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '(-24*ChiralOrder*CPWWWn1*cmath.pi*complex(0,1)*GW**5*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '(-96*ChiralOrder*CPWWWn0*cmath.pi*complex(0,1)*GW**5*WCOrder)/((G1**2 + GW**2)*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_533 = Coupling(name = 'GC_533',
                  value = '(-8*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*G1*WCOrder)/(LamHEFT**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'WCOrder':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '(-48*ChiralOrder*CSWWWn3*cmath.pi*complex(0,1)*G1*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '(-16*ChiralOrder*CSWWWn2*cmath.pi*complex(0,1)*G1*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '(-8*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*G1*WCOrder)/(LamHEFT**2*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '(-8*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'WCOrder':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '(-48*ChiralOrder*CSWWWn3*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev**3*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '(-16*ChiralOrder*CSWWWn2*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_540 = Coupling(name = 'GC_540',
                  value = '(-8*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_541 = Coupling(name = 'GC_541',
                  value = '-((CQDn22x2*complex(0,1)*WCOrder*cmath.sqrt(2))/vev)',
                  order = {'QED':1,'WCOrder':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '(8*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*G1**2*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_543 = Coupling(name = 'GC_543',
                  value = '(16*ChiralOrder*CSWWWn2*cmath.pi*complex(0,1)*G1**2*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_544 = Coupling(name = 'GC_544',
                  value = '(8*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*G1**2*GW*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_545 = Coupling(name = 'GC_545',
                  value = '(-8*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '(-16*ChiralOrder*CSWWWn2*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '(-8*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '(-16*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*G1**3*GW**2*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '(-16*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*G1**3*GW**2*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '(-16*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*G1**2*GW**3*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '(-16*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*G1**2*GW**3*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '(-8*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*GW*WCOrder)/LamHEFT**2',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '(-16*ChiralOrder*CSWWWn2*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '(-8*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*GW*WCOrder)/(LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '(16*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/(LamHEFT**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '(16*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*G1*GW**2*WCOrder)/(LamHEFT**2*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '(8*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':1,'WCOrder':1})

GC_558 = Coupling(name = 'GC_558',
                  value = '(16*ChiralOrder*CSWWWn2*cmath.pi*complex(0,1)*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev**2)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '(8*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*GW**3*WCOrder)/((G1**2 + GW**2)*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '(-16*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*G1*GW**4*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '(-16*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*G1*GW**4*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '(-16*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*GW**3*WCOrder)/(LamHEFT**2*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '(-16*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*GW**3*WCOrder)/(LamHEFT**2*vev*cmath.sqrt(G1**2 + GW**2))',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '(-16*ChiralOrder*CSWWWn0*cmath.pi*complex(0,1)*GW**5*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2)',
                  order = {'ChiralOrder':1,'QED':2,'WCOrder':1})

GC_565 = Coupling(name = 'GC_565',
                  value = '(-16*ChiralOrder*CSWWWn1*cmath.pi*complex(0,1)*GW**5*WCOrder)/((G1**2 + GW**2)**1.5*LamHEFT**2*vev)',
                  order = {'ChiralOrder':1,'QED':3,'WCOrder':1})
