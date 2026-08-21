# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Fri 21 Aug 2026 15:35:16



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
CKMlambda = Parameter(name = 'CKMlambda',
                      nature = 'external',
                      type = 'real',
                      value = 0.2265,
                      texname = '\\lambda _{\\text{CKM}}',
                      lhablock = 'CKMBLOCK',
                      lhacode = [ 1 ])

CKMA = Parameter(name = 'CKMA',
                 nature = 'external',
                 type = 'real',
                 value = 0.79,
                 texname = 'A_{\\text{CKM}}',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 2 ])

CKMrho = Parameter(name = 'CKMrho',
                   nature = 'external',
                   type = 'real',
                   value = 0.141,
                   texname = '\\rho _{\\text{CKM}}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 3 ])

CKMeta = Parameter(name = 'CKMeta',
                   nature = 'external',
                   type = 'real',
                   value = 0.357,
                   texname = '\\eta _{\\text{CKM}}',
                   lhablock = 'CKMBLOCK',
                   lhacode = [ 4 ])

KappaV = Parameter(name = 'KappaV',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{KappaV}',
                   lhablock = 'HEFT',
                   lhacode = [ 1 ])

Kappa2V = Parameter(name = 'Kappa2V',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{Kappa2V}',
                    lhablock = 'HEFT',
                    lhacode = [ 2 ])

Kappa3H = Parameter(name = 'Kappa3H',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{Kappa3H}',
                    lhablock = 'HEFT',
                    lhacode = [ 3 ])

Kappa4H = Parameter(name = 'Kappa4H',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{Kappa4H}',
                    lhablock = 'HEFT',
                    lhacode = [ 4 ])

KappaLE = Parameter(name = 'KappaLE',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{KappaLE}',
                    lhablock = 'HEFT',
                    lhacode = [ 5 ])

KappaLM = Parameter(name = 'KappaLM',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{KappaLM}',
                    lhablock = 'HEFT',
                    lhacode = [ 6 ])

KappaLT = Parameter(name = 'KappaLT',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{KappaLT}',
                    lhablock = 'HEFT',
                    lhacode = [ 7 ])

KappaQU = Parameter(name = 'KappaQU',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{KappaQU}',
                    lhablock = 'HEFT',
                    lhacode = [ 8 ])

KappaQC = Parameter(name = 'KappaQC',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{KappaQC}',
                    lhablock = 'HEFT',
                    lhacode = [ 9 ])

KappaQT = Parameter(name = 'KappaQT',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{KappaQT}',
                    lhablock = 'HEFT',
                    lhacode = [ 10 ])

KappaQD = Parameter(name = 'KappaQD',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{KappaQD}',
                    lhablock = 'HEFT',
                    lhacode = [ 11 ])

KappaQS = Parameter(name = 'KappaQS',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{KappaQS}',
                    lhablock = 'HEFT',
                    lhacode = [ 12 ])

KappaQB = Parameter(name = 'KappaQB',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{KappaQB}',
                    lhablock = 'HEFT',
                    lhacode = [ 13 ])

LamHEFT = Parameter(name = 'LamHEFT',
                    nature = 'external',
                    type = 'real',
                    value = 1000,
                    texname = '\\Lambda _{\\text{HEFT}}',
                    lhablock = 'HEFT',
                    lhacode = [ 14 ])

CFCn3 = Parameter(name = 'CFCn3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CFCn3}',
                  lhablock = 'HEFT',
                  lhacode = [ 15 ])

CFTn0 = Parameter(name = 'CFTn0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CFTn0}',
                  lhablock = 'HEFT',
                  lhacode = [ 16 ])

CFTn1 = Parameter(name = 'CFTn1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CFTn1}',
                  lhablock = 'HEFT',
                  lhacode = [ 17 ])

CFTn2 = Parameter(name = 'CFTn2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CFTn2}',
                  lhablock = 'HEFT',
                  lhacode = [ 18 ])

CFTn3 = Parameter(name = 'CFTn3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CFTn3}',
                  lhablock = 'HEFT',
                  lhacode = [ 19 ])

ChiralOrder = Parameter(name = 'ChiralOrder',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\text{ChiralOrder}',
                        lhablock = 'HEFT',
                        lhacode = [ 20 ])

CGHNLOn0 = Parameter(name = 'CGHNLOn0',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CGHNLOn0}',
                     lhablock = 'HEFT',
                     lhacode = [ 21 ])

CGHNLOn1 = Parameter(name = 'CGHNLOn1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CGHNLOn1}',
                     lhablock = 'HEFT',
                     lhacode = [ 22 ])

CGHNLOn2 = Parameter(name = 'CGHNLOn2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CGHNLOn2}',
                     lhablock = 'HEFT',
                     lhacode = [ 23 ])

CGHNLOn3 = Parameter(name = 'CGHNLOn3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CGHNLOn3}',
                     lhablock = 'HEFT',
                     lhacode = [ 24 ])

LamF = Parameter(name = 'LamF',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{LamF}',
                 lhablock = 'HEFTEXP',
                 lhacode = [ 1 ])

LamGold = Parameter(name = 'LamGold',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{LamGold}',
                    lhablock = 'HEFTGold',
                    lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.95,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.000011663787,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1179,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

thetaS = Parameter(name = 'thetaS',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\theta _s',
                   lhablock = 'SMINPUTS',
                   lhacode = [ 4 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MLE = Parameter(name = 'MLE',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{MLE}',
                lhablock = 'MASS',
                lhacode = [ 11 ])

MLM = Parameter(name = 'MLM',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MLM}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MLT = Parameter(name = 'MLT',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MLT}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MQU = Parameter(name = 'MQU',
                nature = 'external',
                type = 'real',
                value = 0.00216,
                texname = '\\text{MQU}',
                lhablock = 'MASS',
                lhacode = [ 2 ])

MQC = Parameter(name = 'MQC',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{MQC}',
                lhablock = 'MASS',
                lhacode = [ 4 ])

MQT = Parameter(name = 'MQT',
                nature = 'external',
                type = 'real',
                value = 172.76,
                texname = '\\text{MQT}',
                lhablock = 'MASS',
                lhacode = [ 6 ])

MQD = Parameter(name = 'MQD',
                nature = 'external',
                type = 'real',
                value = 0.00467,
                texname = '\\text{MQD}',
                lhablock = 'MASS',
                lhacode = [ 1 ])

MQS = Parameter(name = 'MQS',
                nature = 'external',
                type = 'real',
                value = 0.093,
                texname = '\\text{MQS}',
                lhablock = 'MASS',
                lhacode = [ 3 ])

MQB = Parameter(name = 'MQB',
                nature = 'external',
                type = 'real',
                value = 4.18,
                texname = '\\text{MQB}',
                lhablock = 'MASS',
                lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125.09,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WQT = Parameter(name = 'WQT',
                nature = 'external',
                type = 'real',
                value = 1.33,
                texname = '\\text{WQT}',
                lhablock = 'DECAY',
                lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEWM = Parameter(name = 'aEWM',
                 nature = 'internal',
                 type = 'real',
                 value = '1/aEWM1',
                 texname = '\\text{aEWM}')

Wnorm = Parameter(name = 'Wnorm',
                  nature = 'internal',
                  type = 'real',
                  value = '1',
                  texname = '\\text{Wnorm}')

WnormINV = Parameter(name = 'WnormINV',
                     nature = 'internal',
                     type = 'real',
                     value = '1',
                     texname = '\\text{WnormINV}')

Bnorm = Parameter(name = 'Bnorm',
                  nature = 'internal',
                  type = 'real',
                  value = '1',
                  texname = '\\text{Bnorm}')

BnormINV = Parameter(name = 'BnormINV',
                     nature = 'internal',
                     type = 'real',
                     value = '1',
                     texname = '\\text{BnormINV}')

Gnorm = Parameter(name = 'Gnorm',
                  nature = 'internal',
                  type = 'real',
                  value = '1 + (CGHNLOn0*ChiralOrder)/2.',
                  texname = '\\text{Gnorm}')

GnormINV = Parameter(name = 'GnormINV',
                     nature = 'internal',
                     type = 'real',
                     value = '1 - (CGHNLOn0*ChiralOrder)/2.',
                     texname = '\\text{GnormINV}')

GS = Parameter(name = 'GS',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
               texname = 'G_s')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '1/(2**0.25*cmath.sqrt(Gf))',
                texname = '\\text{vev}')

hlambda = Parameter(name = 'hlambda',
                    nature = 'internal',
                    type = 'real',
                    value = '(Gf*MH**2)/cmath.sqrt(2)',
                    texname = '\\text{hlambda}')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - CKMlambda**2/2.',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMlambda',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**3*(CKMrho - CKMeta*complex(0,1))',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-CKMlambda',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '1 - CKMlambda**2/2.',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**2',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'CKMA*CKMlambda**3*(1 - CKMrho - CKMeta*complex(0,1))',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '-(CKMA*CKMlambda**2)',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(hlambda*vev**2)',
                texname = '\\mu')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt((Gf*MZ**2 + MZ*cmath.sqrt(Gf**2*MZ**2 - 2*aEWM*cmath.pi*Gf*cmath.sqrt(2)))/Gf)/cmath.sqrt(2) - (CFTn0*ChiralOrder*(1 + (Gf*MZ)/cmath.sqrt(Gf**2*MZ**2 - 2*aEWM*cmath.pi*Gf*cmath.sqrt(2)))*cmath.sqrt((Gf*MZ**2 + MZ*cmath.sqrt(Gf**2*MZ**2 - 2*aEWM*cmath.pi*Gf*cmath.sqrt(2)))/Gf))/(2.*cmath.sqrt(2))',
               texname = 'M_W')

G1 = Parameter(name = 'G1',
               nature = 'internal',
               type = 'real',
               value = '2**0.75*cmath.sqrt(Gf*MZ**2 - MZ*cmath.sqrt(Gf**2*MZ**2 - 2*aEWM*cmath.pi*Gf*cmath.sqrt(2))) - (CFTn0*ChiralOrder*(1 - (Gf*MZ)/cmath.sqrt(Gf**2*MZ**2 - 2*aEWM*cmath.pi*Gf*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ**2 - MZ*cmath.sqrt(Gf**2*MZ**2 - 2*aEWM*cmath.pi*Gf*cmath.sqrt(2))))/2**0.25',
               texname = 'G_1')

gs = Parameter(name = 'gs',
               nature = 'internal',
               type = 'real',
               value = 'Gnorm*GS',
               texname = 'g_s')

GW = Parameter(name = 'GW',
               nature = 'internal',
               type = 'real',
               value = '2**0.75*cmath.sqrt(Gf*MZ**2 + MZ*cmath.sqrt(Gf**2*MZ**2 - 2*aEWM*cmath.pi*Gf*cmath.sqrt(2))) - (CFTn0*ChiralOrder*(1 + (Gf*MZ)/cmath.sqrt(Gf**2*MZ**2 - 2*aEWM*cmath.pi*Gf*cmath.sqrt(2)))*cmath.sqrt(Gf*MZ**2 + MZ*cmath.sqrt(Gf**2*MZ**2 - 2*aEWM*cmath.pi*Gf*cmath.sqrt(2))))/2**0.25',
               texname = 'G_W')

AZnorm1x1 = Parameter(name = 'AZnorm1x1',
                      nature = 'internal',
                      type = 'real',
                      value = 'GW/cmath.sqrt(G1**2 + GW**2)',
                      texname = '\\text{AZnorm1x1}')

AZnorm1x2 = Parameter(name = 'AZnorm1x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'G1/cmath.sqrt(G1**2 + GW**2)',
                      texname = '\\text{AZnorm1x2}')

AZnorm2x1 = Parameter(name = 'AZnorm2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '-(G1/cmath.sqrt(G1**2 + GW**2))',
                      texname = '\\text{AZnorm2x1}')

AZnorm2x2 = Parameter(name = 'AZnorm2x2',
                      nature = 'internal',
                      type = 'real',
                      value = 'GW/cmath.sqrt(G1**2 + GW**2)',
                      texname = '\\text{AZnorm2x2}')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'Bnorm*G1',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'GW*Wnorm',
               texname = 'g_W')

