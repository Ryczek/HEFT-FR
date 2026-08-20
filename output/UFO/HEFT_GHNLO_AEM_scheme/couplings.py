# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Thu 20 Aug 2026 17:46:06


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(2**0.25*CGHNLOn1*ChiralOrder*complex(0,1)*cmath.sqrt(Gf))',
                order = {'ExpansionChiral':1,'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '-2*CGHNLOn2*ChiralOrder*complex(0,1)*Gf*cmath.sqrt(2)',
                order = {'ExpansionChiral':1,'QED':2})

GC_3 = Coupling(name = 'GC_3',
                value = '-6*2**0.75*CGHNLOn3*ChiralOrder*complex(0,1)*Gf**1.5',
                order = {'ExpansionChiral':1,'QED':3})

GC_4 = Coupling(name = 'GC_4',
                value = '-3*2**0.25*complex(0,1)*Kappa3H*MH**2*cmath.sqrt(Gf)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '-3*complex(0,1)*Gf*Kappa4H*MH**2*cmath.sqrt(2)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '2**0.25*complex(0,1)*MZ*cmath.sqrt(Gf)',
                order = {'QED':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-(2**0.25*CFTn0*ChiralOrder*complex(0,1)*MZ*cmath.sqrt(Gf))',
                order = {'ExpansionChiral':1,'QED':1})

GC_8 = Coupling(name = 'GC_8',
                value = '6*2**0.75*CFCn3*complex(0,1)*Gf**1.5*MZ**2',
                order = {'QED':3})

GC_9 = Coupling(name = 'GC_9',
                value = '2*complex(0,1)*Gf*Kappa2V*MZ**2*cmath.sqrt(2)',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '2*2**0.25*complex(0,1)*KappaV*MZ**2*cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-12*2**0.75*CFCn3*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*MZ**2 + 12*2**0.75*CFTn3*ChiralOrder*complex(0,1)*Gf**1.5*MZ**2',
                 order = {'ExpansionChiral':1,'QED':3})

GC_12 = Coupling(name = 'GC_12',
                 value = '4*CFTn2*ChiralOrder*complex(0,1)*Gf*MZ**2*cmath.sqrt(2) - 4*CFTn0*ChiralOrder*complex(0,1)*Gf*Kappa2V*MZ**2*cmath.sqrt(2)',
                 order = {'ExpansionChiral':1,'QED':2})

GC_13 = Coupling(name = 'GC_13',
                 value = '2*2**0.25*CFTn1*ChiralOrder*complex(0,1)*MZ**2*cmath.sqrt(Gf) - 4*2**0.25*CFTn0*ChiralOrder*complex(0,1)*KappaV*MZ**2*cmath.sqrt(Gf)',
                 order = {'ExpansionChiral':1,'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
                 order = {'QCD':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '2*complex(0,1)*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
                 order = {'QCD':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-2*2**0.25*CGHNLOn1*ChiralOrder*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)*cmath.sqrt(Gf)',
                 order = {'ExpansionChiral':1,'QCD':1,'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-12*2**0.75*CGHNLOn3*ChiralOrder*Gf**1.5*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
                 order = {'ExpansionChiral':1,'QCD':1,'QED':3})

GC_18 = Coupling(name = 'GC_18',
                 value = '4*aEWM*cmath.pi*complex(0,1)',
                 order = {'QED':2})

GC_19 = Coupling(name = 'GC_19',
                 value = '4*aS*cmath.pi*complex(0,1)',
                 order = {'QCD':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '4*2**0.25*aS*CGHNLOn1*ChiralOrder*cmath.pi*complex(0,1)*cmath.sqrt(Gf)',
                 order = {'ExpansionChiral':1,'QCD':2,'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '8*aS*CGHNLOn2*ChiralOrder*cmath.pi*complex(0,1)*Gf*cmath.sqrt(2)',
                 order = {'ExpansionChiral':1,'QCD':2,'QED':2})

GC_22 = Coupling(name = 'GC_22',
                 value = '24*2**0.75*aS*CGHNLOn3*ChiralOrder*cmath.pi*complex(0,1)*Gf**1.5',
                 order = {'ExpansionChiral':1,'QCD':2,'QED':3})

GC_23 = Coupling(name = 'GC_23',
                 value = '-4*CGHNLOn2*ChiralOrder*Gf*cmath.sqrt(aS)*cmath.sqrt(2*cmath.pi)',
                 order = {'ExpansionChiral':1,'QCD':1,'QED':2})

GC_24 = Coupling(name = 'GC_24',
                 value = '(-2*2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2)/(3.*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(2**0.25*complex(0,1)*Gf**1.5*MZ**3)/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(2**0.25*complex(0,1)*Gf**1.5*MZ**3)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '-0.3333333333333333*(2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*MZ**3)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (2*2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-((2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*MZ**3)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) + (2*2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-0.3333333333333333*(2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*MZ**3)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (2*2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) + (2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2)/(3.*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(2*2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*MZ**3)/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) - (4*2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) + (2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2)/(3.*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-((2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*MZ**3)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) + (2*2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(2**0.25*complex(0,1)*Gf**1.5*MZ**3)/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) + (2*2**0.75*aEWM*cmath.pi*complex(0,1))/(3.*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) - (2**0.25*complex(0,1)*Gf*MZ**2)/(3.*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(-2*2**0.25*complex(0,1)*Gf**1.5*MZ**3)/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) + (4*2**0.75*aEWM*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(3.*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) + (2*2**0.75*aEWM*cmath.pi*complex(0,1))/(3.*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) - (2**0.25*complex(0,1)*Gf*MZ**2)/(3.*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '(-4*2**0.75*aEWM*cmath.pi*complex(0,1))/(3.*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) + (2*2**0.25*complex(0,1)*Gf*MZ**2)/(3.*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'QED':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(2**0.25*complex(0,1)*Gf**1.5*MZ**3)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (2**0.25*complex(0,1)*Gf*MZ**2)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(2*2**0.75*aEWM*cmath.pi*complex(0,1))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2**0.25*complex(0,1)*Gf*MZ**2)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(-12*aEWM*cmath.pi*complex(0,1)*Gf*MZ**2)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (8*aEWM**2*cmath.pi**2*complex(0,1)*cmath.sqrt(2))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (2*complex(0,1)*Gf**2*MZ**4*cmath.sqrt(2))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (2*complex(0,1)*Gf**1.5*MZ**3*cmath.sqrt(2))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (8*aEWM*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':2})

GC_39 = Coupling(name = 'GC_39',
                 value = '(8*aEWM*cmath.pi*complex(0,1)*Gf*MZ**2)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*complex(0,1)*Gf**2*MZ**4*cmath.sqrt(2))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*complex(0,1)*Gf**1.5*MZ**3*cmath.sqrt(2))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (8*aEWM*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':2})

GC_40 = Coupling(name = 'GC_40',
                 value = '(-16*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*Gf*MZ**2)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (4*CFTn0*ChiralOrder*complex(0,1)*Gf**2*MZ**4*cmath.sqrt(2))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (4*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*MZ**3*cmath.sqrt(2))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (8*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'ExpansionChiral':1,'QED':2})

GC_41 = Coupling(name = 'GC_41',
                 value = '(16*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*Gf*MZ**2)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (4*CFTn0*ChiralOrder*complex(0,1)*Gf**2*MZ**4*cmath.sqrt(2))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (4*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*MZ**3*cmath.sqrt(2))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (8*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*MZ*cmath.sqrt(Gf))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'ExpansionChiral':1,'QED':2})

GC_42 = Coupling(name = 'GC_42',
                 value = '(-12*2**0.25*aEWM*CFCn3*cmath.pi*complex(0,1)*Gf**1.5*MZ**2)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (3*2**0.75*CFCn3*complex(0,1)*Gf**2.5*MZ**4)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (12*2**0.25*aEWM*CFCn3*cmath.pi*complex(0,1)*Gf*MZ)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (3*2**0.75*CFCn3*complex(0,1)*Gf**2*MZ**3)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':3})

GC_43 = Coupling(name = 'GC_43',
                 value = '(24*2**0.25*aEWM*CFCn3*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*Gf**1.5*MZ**2)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (6*2**0.75*CFCn3*CFTn0*ChiralOrder*complex(0,1)*Gf**2.5*MZ**4)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (12*2**0.25*aEWM*CFCn3*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*Gf*MZ)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (6*2**0.75*CFCn3*CFTn0*ChiralOrder*complex(0,1)*Gf**2*MZ**3)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'ExpansionChiral':1,'QED':3})

GC_44 = Coupling(name = 'GC_44',
                 value = '(-4*aEWM*cmath.pi*complex(0,1)*Gf*Kappa2V*MZ**2)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (complex(0,1)*Gf**2*Kappa2V*MZ**4*cmath.sqrt(2))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (complex(0,1)*Gf**1.5*Kappa2V*MZ**3*cmath.sqrt(2))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (4*aEWM*cmath.pi*complex(0,1)*Kappa2V*MZ*cmath.sqrt(Gf))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':2})

GC_45 = Coupling(name = 'GC_45',
                 value = '(8*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*Gf*Kappa2V*MZ**2)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*CFTn0*ChiralOrder*complex(0,1)*Gf**2*Kappa2V*MZ**4*cmath.sqrt(2))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*Kappa2V*MZ**3*cmath.sqrt(2))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (4*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*Kappa2V*MZ*cmath.sqrt(Gf))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'ExpansionChiral':1,'QED':2})

GC_46 = Coupling(name = 'GC_46',
                 value = '(2**0.25*complex(0,1)*Gf**1.5*KappaV*MZ**4)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*KappaV*MZ**2*cmath.sqrt(Gf))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*KappaV*MZ)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (2**0.25*complex(0,1)*Gf*KappaV*MZ**3)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '(-2*2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf**1.5*KappaV*MZ**4)/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (4*2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*KappaV*MZ**2*cmath.sqrt(Gf))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (2*2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*KappaV*MZ)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.25*CFTn0*ChiralOrder*complex(0,1)*Gf*KappaV*MZ**3)/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((2**0.25*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(-2*2**0.25*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(3.*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(2**0.25*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(3.*cmath.sqrt(Gf))',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(2**0.25*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/cmath.sqrt(Gf)',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(2**0.25*CKM1x1*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*CKM1x1*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '(2**0.25*CKM1x2*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*CKM1x2*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(2**0.25*CKM1x3*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*CKM1x3*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(2**0.25*CKM2x1*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*CKM2x1*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(2**0.25*CKM2x2*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*CKM2x2*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(2**0.25*CKM2x3*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*CKM2x3*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(2**0.25*CKM3x1*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*CKM3x1*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(2**0.25*CKM3x2*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*CKM3x2*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(2**0.25*CKM3x3*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*CKM3x3*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '-((CFTn0*ChiralOrder*CKM1x1*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*CKM1x1*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*CKM1x1*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '-((CFTn0*ChiralOrder*CKM1x2*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*CKM1x2*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*CKM1x2*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-((CFTn0*ChiralOrder*CKM1x3*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*CKM1x3*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*CKM1x3*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-((CFTn0*ChiralOrder*CKM2x1*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*CKM2x1*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*CKM2x1*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '-((CFTn0*ChiralOrder*CKM2x2*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*CKM2x2*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*CKM2x2*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-((CFTn0*ChiralOrder*CKM2x3*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*CKM2x3*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*CKM2x3*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '-((CFTn0*ChiralOrder*CKM3x1*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*CKM3x1*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*CKM3x1*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-((CFTn0*ChiralOrder*CKM3x2*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*CKM3x2*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*CKM3x2*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-((CFTn0*ChiralOrder*CKM3x3*complex(0,1)*Gf*MZ**2.5*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*CKM3x3*cmath.pi*complex(0,1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*CKM3x3*complex(0,1)*MZ**1.5*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(8*aEWM*CFTn0*ChiralOrder*cmath.pi*MZ*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*CFTn0*ChiralOrder*Gf*MZ**3*cmath.sqrt(2)*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*CFTn0*ChiralOrder*MZ**2*cmath.sqrt(2)*cmath.sqrt(Gf)*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'ExpansionChiral':1,'QED':2})

GC_73 = Coupling(name = 'GC_73',
                 value = '(-8*aEWM*cmath.pi*MZ*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) + (2*Gf*MZ**3*cmath.sqrt(2)*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (8*aEWM*cmath.pi*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))) + (2*MZ**2*cmath.sqrt(2)*cmath.sqrt(Gf)*cmath.sqrt(-(Gf*MZ) + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':2})

GC_74 = Coupling(name = 'GC_74',
                 value = '(aS**1.5*thetaS)/cmath.sqrt(cmath.pi)',
                 order = {'QCD':3})

GC_75 = Coupling(name = 'GC_75',
                 value = '-((complex(0,1)*KappaLE*MLE)/vev)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-((complex(0,1)*KappaLM*MLM)/vev)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-((complex(0,1)*KappaLT*MLT)/vev)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-((complex(0,1)*KappaQB*MQB)/vev)',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-((complex(0,1)*KappaQC*MQC)/vev)',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-((complex(0,1)*KappaQD*MQD)/vev)',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-((complex(0,1)*KappaQS*MQS)/vev)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-((complex(0,1)*KappaQT*MQT)/vev)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-((complex(0,1)*KappaQU*MQU)/vev)',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM1x1)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*complexconjugate(CKM1x1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM1x1)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*complexconjugate(CKM1x1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*complexconjugate(CKM1x1)*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM1x2)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*complexconjugate(CKM1x2)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM1x2)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*complexconjugate(CKM1x2)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*complexconjugate(CKM1x2)*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM1x3)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*complexconjugate(CKM1x3)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM1x3)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*complexconjugate(CKM1x3)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*complexconjugate(CKM1x3)*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM2x1)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*complexconjugate(CKM2x1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM2x1)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*complexconjugate(CKM2x1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*complexconjugate(CKM2x1)*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM2x2)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*complexconjugate(CKM2x2)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM2x2)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*complexconjugate(CKM2x2)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*complexconjugate(CKM2x2)*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM2x3)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*complexconjugate(CKM2x3)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM2x3)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*complexconjugate(CKM2x3)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*complexconjugate(CKM2x3)*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM3x1)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*complexconjugate(CKM3x1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM3x1)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*complexconjugate(CKM3x1)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*complexconjugate(CKM3x1)*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM3x2)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*complexconjugate(CKM3x2)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM3x2)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*complexconjugate(CKM3x2)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*complexconjugate(CKM3x2)*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                 order = {'ExpansionChiral':1,'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(2**0.25*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM3x3)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (2*2**0.75*aEWM*cmath.pi*complex(0,1)*complexconjugate(CKM3x3)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '-((CFTn0*ChiralOrder*complex(0,1)*Gf*MZ**2.5*complexconjugate(CKM3x3)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))) + (2**0.75*aEWM*CFTn0*ChiralOrder*cmath.pi*complex(0,1)*complexconjugate(CKM3x3)*cmath.sqrt(MZ)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)) - (CFTn0*ChiralOrder*complex(0,1)*MZ**1.5*complexconjugate(CKM3x3)*cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ + cmath.sqrt(Gf)*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2))))/(2**0.75*cmath.sqrt(Gf*MZ**2 - 2*aEWM*cmath.pi*cmath.sqrt(2)))',
                  order = {'ExpansionChiral':1,'QED':1})

