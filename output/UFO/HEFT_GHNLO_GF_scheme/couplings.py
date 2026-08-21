# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Fri 21 Aug 2026 15:58:44


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-GS',
                order = {'QCD':1})

GC_2 = Coupling(name = 'GC_2',
                value = 'complex(0,1)*GS',
                order = {'QCD':1})

GC_3 = Coupling(name = 'GC_3',
                value = 'complex(0,1)*GS**2',
                order = {'QCD':2})

GC_4 = Coupling(name = 'GC_4',
                value = '(complex(0,1)*GW)/cmath.sqrt(2)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '(CKM1x1*complex(0,1)*GW)/cmath.sqrt(2)',
                order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = '(CKM1x2*complex(0,1)*GW)/cmath.sqrt(2)',
                order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '(CKM1x3*complex(0,1)*GW)/cmath.sqrt(2)',
                order = {'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '(CKM2x1*complex(0,1)*GW)/cmath.sqrt(2)',
                order = {'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = '(CKM2x2*complex(0,1)*GW)/cmath.sqrt(2)',
                order = {'QED':1})

GC_10 = Coupling(name = 'GC_10',
                 value = '(CKM2x3*complex(0,1)*GW)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '(CKM3x1*complex(0,1)*GW)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '(CKM3x2*complex(0,1)*GW)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(CKM3x3*complex(0,1)*GW)/cmath.sqrt(2)',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-(complex(0,1)*GW**2)',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '(complex(0,1)*G1**2*GW**2)/(G1**2 + GW**2)',
                 order = {'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '(-2*complex(0,1)*G1*GW**3)/(G1**2 + GW**2)',
                 order = {'QED':2})

GC_17 = Coupling(name = 'GC_17',
                 value = '(complex(0,1)*GW**4)/(G1**2 + GW**2)',
                 order = {'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-0.16666666666666666*(complex(0,1)*G1**2)/cmath.sqrt(G1**2 + GW**2)',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(complex(0,1)*G1**2)/(2.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-0.3333333333333333*(complex(0,1)*G1*GW)/cmath.sqrt(G1**2 + GW**2)',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '(2*complex(0,1)*G1*GW)/(3.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-((complex(0,1)*G1*GW)/cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(complex(0,1)*G1*GW)/cmath.sqrt(G1**2 + GW**2)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-0.5*(complex(0,1)*GW**2)/cmath.sqrt(G1**2 + GW**2)',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(complex(0,1)*GW**2)/(2.*cmath.sqrt(G1**2 + GW**2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(complex(0,1)*GW**2)/cmath.sqrt(G1**2 + GW**2)',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(complex(0,1)*cmath.sqrt(G1**2 + GW**2))/2.',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = 'CFTn2*ChiralOrder*complex(0,1)*G1**2 + CFTn2*ChiralOrder*complex(0,1)*GW**2',
                 order = {'ExpansionChiral':1,'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '(complex(0,1)*GW**2*Kappa2V)/2.',
                 order = {'QED':2})

GC_30 = Coupling(name = 'GC_30',
                 value = '(complex(0,1)*G1**2*Kappa2V)/2. + (complex(0,1)*GW**2*Kappa2V)/2.',
                 order = {'QED':2})

GC_31 = Coupling(name = 'GC_31',
                 value = '-6*complex(0,1)*hlambda*Kappa4H',
                 order = {'QED':2})

GC_32 = Coupling(name = 'GC_32',
                 value = '(GS**3*thetaS)/(8.*cmath.pi**2)',
                 order = {'QCD':3})

GC_33 = Coupling(name = 'GC_33',
                 value = '(3*CFCn3*complex(0,1)*G1**2)/(2.*vev) + (3*CFCn3*complex(0,1)*GW**2)/(2.*vev)',
                 order = {'QED':3})

GC_34 = Coupling(name = 'GC_34',
                 value = '(3*CFTn3*ChiralOrder*complex(0,1)*G1**2)/vev + (3*CFTn3*ChiralOrder*complex(0,1)*GW**2)/vev',
                 order = {'ExpansionChiral':1,'QED':3})

GC_35 = Coupling(name = 'GC_35',
                 value = '(-6*CGHNLOn3*ChiralOrder*complex(0,1))/vev**3',
                 order = {'ExpansionChiral':1,'QED':3})

GC_36 = Coupling(name = 'GC_36',
                 value = '(-6*CGHNLOn3*ChiralOrder*GS)/vev**3',
                 order = {'ExpansionChiral':1,'QCD':1,'QED':3})

GC_37 = Coupling(name = 'GC_37',
                 value = '(6*CGHNLOn3*ChiralOrder*complex(0,1)*GS**2)/vev**3',
                 order = {'ExpansionChiral':1,'QCD':2,'QED':3})

GC_38 = Coupling(name = 'GC_38',
                 value = '(-2*CGHNLOn2*ChiralOrder*complex(0,1))/vev**2',
                 order = {'ExpansionChiral':1,'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(-2*CGHNLOn2*ChiralOrder*GS)/vev**2',
                 order = {'ExpansionChiral':1,'QCD':1,'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(2*CGHNLOn2*ChiralOrder*complex(0,1)*GS**2)/vev**2',
                 order = {'ExpansionChiral':1,'QCD':2,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '-((CGHNLOn1*ChiralOrder*complex(0,1))/vev)',
                 order = {'ExpansionChiral':1,'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((CGHNLOn1*ChiralOrder*GS)/vev)',
                 order = {'ExpansionChiral':1,'QCD':1,'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(CGHNLOn1*ChiralOrder*complex(0,1)*GS**2)/vev',
                 order = {'ExpansionChiral':1,'QCD':2,'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(3*CFCn3*complex(0,1)*GW**2)/(2.*vev)',
                 order = {'QED':3})

GC_45 = Coupling(name = 'GC_45',
                 value = '-((complex(0,1)*KappaLE*MLE)/vev)',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-((complex(0,1)*KappaLM*MLM)/vev)',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-((complex(0,1)*KappaLT*MLT)/vev)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((complex(0,1)*KappaQB*MQB)/vev)',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-((complex(0,1)*KappaQC*MQC)/vev)',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-((complex(0,1)*KappaQD*MQD)/vev)',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '-((complex(0,1)*KappaQS*MQS)/vev)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '-((complex(0,1)*KappaQT*MQT)/vev)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '-((complex(0,1)*KappaQU*MQU)/vev)',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '-6*complex(0,1)*hlambda*Kappa3H*vev',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(complex(0,1)*GW**2*KappaV*vev)/2.',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(CFTn1*ChiralOrder*complex(0,1)*G1**2*vev)/2. + (CFTn1*ChiralOrder*complex(0,1)*GW**2*vev)/2.',
                 order = {'ExpansionChiral':1,'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(complex(0,1)*G1**2*KappaV*vev)/2. + (complex(0,1)*GW**2*KappaV*vev)/2.',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(complex(0,1)*GW*complexconjugate(CKM1x1))/cmath.sqrt(2)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(complex(0,1)*GW*complexconjugate(CKM1x2))/cmath.sqrt(2)',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(complex(0,1)*GW*complexconjugate(CKM1x3))/cmath.sqrt(2)',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(complex(0,1)*GW*complexconjugate(CKM2x1))/cmath.sqrt(2)',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(complex(0,1)*GW*complexconjugate(CKM2x2))/cmath.sqrt(2)',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '(complex(0,1)*GW*complexconjugate(CKM2x3))/cmath.sqrt(2)',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(complex(0,1)*GW*complexconjugate(CKM3x1))/cmath.sqrt(2)',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(complex(0,1)*GW*complexconjugate(CKM3x2))/cmath.sqrt(2)',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(complex(0,1)*GW*complexconjugate(CKM3x3))/cmath.sqrt(2)',
                 order = {'QED':1})

