# Merged by HEFT ufo_merge.py: baseline FB_SM, sources FB_PT, FB_PG, FB_PB, FB_SG, FB_SB, FB_S2D, FB_PDH, FB_P1, FB_P2, FB_P3, FB_P4, FB_P5, FB_P6, FB_P12, FB_P13, FB_P14, FB_P17, FB_P18, FB_P20, FB_P21, FB_P22, FB_P23, FB_P24, FB_P26, FB_S1, FB_S2, FB_S3, FB_S4, FB_S5, FB_S6, FB_S7, FB_S8, FB_S9, FB_S15, FB_PWHD1, FB_PWHD2, FB_SWHDT, FB_PW, FB_SW, FB_SWHD, FB_P11, FB_P8, FB_PGHD1, FB_PGHD2, FB_SGHD, FB_PWWW, FB_SWWW
# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Tue 13 Oct 2026 20:18:42



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.

ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

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

DeltaFCn1 = Parameter(name = 'DeltaFCn1',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{DeltaFCn1}',
                      lhablock = 'HEFT',
                      lhacode = [ 1 ])

DeltaFCn2 = Parameter(name = 'DeltaFCn2',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{DeltaFCn2}',
                      lhablock = 'HEFT',
                      lhacode = [ 2 ])

DeltaLam3 = Parameter(name = 'DeltaLam3',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{DeltaLam3}',
                      lhablock = 'HEFT',
                      lhacode = [ 3 ])

DeltaLam4 = Parameter(name = 'DeltaLam4',
                      nature = 'external',
                      type = 'real',
                      value = 0,
                      texname = '\\text{DeltaLam4}',
                      lhablock = 'HEFT',
                      lhacode = [ 4 ])

DeltaYLE = Parameter(name = 'DeltaYLE',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{DeltaYLE}',
                     lhablock = 'HEFT',
                     lhacode = [ 5 ])

DeltaYLM = Parameter(name = 'DeltaYLM',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{DeltaYLM}',
                     lhablock = 'HEFT',
                     lhacode = [ 6 ])

DeltaYLT = Parameter(name = 'DeltaYLT',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{DeltaYLT}',
                     lhablock = 'HEFT',
                     lhacode = [ 7 ])

DeltaYQU = Parameter(name = 'DeltaYQU',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{DeltaYQU}',
                     lhablock = 'HEFT',
                     lhacode = [ 8 ])

DeltaYQC = Parameter(name = 'DeltaYQC',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{DeltaYQC}',
                     lhablock = 'HEFT',
                     lhacode = [ 9 ])

DeltaYQT = Parameter(name = 'DeltaYQT',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{DeltaYQT}',
                     lhablock = 'HEFT',
                     lhacode = [ 10 ])

DeltaYQD = Parameter(name = 'DeltaYQD',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{DeltaYQD}',
                     lhablock = 'HEFT',
                     lhacode = [ 11 ])

DeltaYQS = Parameter(name = 'DeltaYQS',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{DeltaYQS}',
                     lhablock = 'HEFT',
                     lhacode = [ 12 ])

DeltaYQB = Parameter(name = 'DeltaYQB',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{DeltaYQB}',
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

ChiralOrder = Parameter(name = 'ChiralOrder',
                        nature = 'external',
                        type = 'real',
                        value = 1,
                        texname = '\\text{ChiralOrder}',
                        lhablock = 'HEFT',
                        lhacode = [ 16 ])

WCOrder = Parameter(name = 'WCOrder',
                    nature = 'external',
                    type = 'real',
                    value = 1,
                    texname = '\\text{WCOrder}',
                    lhablock = 'HEFT',
                    lhacode = [ 17 ])

CLEn21x1 = Parameter(name = 'CLEn21x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn21x1}',
                     lhablock = 'HEFTCLEN2',
                     lhacode = [ 1, 1 ])

CLEn21x2 = Parameter(name = 'CLEn21x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn21x2}',
                     lhablock = 'HEFTCLEN2',
                     lhacode = [ 1, 2 ])

CLEn21x3 = Parameter(name = 'CLEn21x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn21x3}',
                     lhablock = 'HEFTCLEN2',
                     lhacode = [ 1, 3 ])

CLEn22x1 = Parameter(name = 'CLEn22x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn22x1}',
                     lhablock = 'HEFTCLEN2',
                     lhacode = [ 2, 1 ])

CLEn22x2 = Parameter(name = 'CLEn22x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn22x2}',
                     lhablock = 'HEFTCLEN2',
                     lhacode = [ 2, 2 ])

CLEn22x3 = Parameter(name = 'CLEn22x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn22x3}',
                     lhablock = 'HEFTCLEN2',
                     lhacode = [ 2, 3 ])

CLEn23x1 = Parameter(name = 'CLEn23x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn23x1}',
                     lhablock = 'HEFTCLEN2',
                     lhacode = [ 3, 1 ])

CLEn23x2 = Parameter(name = 'CLEn23x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn23x2}',
                     lhablock = 'HEFTCLEN2',
                     lhacode = [ 3, 2 ])

CLEn23x3 = Parameter(name = 'CLEn23x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn23x3}',
                     lhablock = 'HEFTCLEN2',
                     lhacode = [ 3, 3 ])

CLEn31x1 = Parameter(name = 'CLEn31x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn31x1}',
                     lhablock = 'HEFTCLEN3',
                     lhacode = [ 1, 1 ])

CLEn31x2 = Parameter(name = 'CLEn31x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn31x2}',
                     lhablock = 'HEFTCLEN3',
                     lhacode = [ 1, 2 ])

CLEn31x3 = Parameter(name = 'CLEn31x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn31x3}',
                     lhablock = 'HEFTCLEN3',
                     lhacode = [ 1, 3 ])

CLEn32x1 = Parameter(name = 'CLEn32x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn32x1}',
                     lhablock = 'HEFTCLEN3',
                     lhacode = [ 2, 1 ])

CLEn32x2 = Parameter(name = 'CLEn32x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn32x2}',
                     lhablock = 'HEFTCLEN3',
                     lhacode = [ 2, 2 ])

CLEn32x3 = Parameter(name = 'CLEn32x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn32x3}',
                     lhablock = 'HEFTCLEN3',
                     lhacode = [ 2, 3 ])

CLEn33x1 = Parameter(name = 'CLEn33x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn33x1}',
                     lhablock = 'HEFTCLEN3',
                     lhacode = [ 3, 1 ])

CLEn33x2 = Parameter(name = 'CLEn33x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn33x2}',
                     lhablock = 'HEFTCLEN3',
                     lhacode = [ 3, 2 ])

CLEn33x3 = Parameter(name = 'CLEn33x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CLEn33x3}',
                     lhablock = 'HEFTCLEN3',
                     lhacode = [ 3, 3 ])

CQDn21x1 = Parameter(name = 'CQDn21x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn21x1}',
                     lhablock = 'HEFTCQDN2',
                     lhacode = [ 1, 1 ])

CQDn21x2 = Parameter(name = 'CQDn21x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn21x2}',
                     lhablock = 'HEFTCQDN2',
                     lhacode = [ 1, 2 ])

CQDn21x3 = Parameter(name = 'CQDn21x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn21x3}',
                     lhablock = 'HEFTCQDN2',
                     lhacode = [ 1, 3 ])

CQDn22x1 = Parameter(name = 'CQDn22x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn22x1}',
                     lhablock = 'HEFTCQDN2',
                     lhacode = [ 2, 1 ])

CQDn22x2 = Parameter(name = 'CQDn22x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn22x2}',
                     lhablock = 'HEFTCQDN2',
                     lhacode = [ 2, 2 ])

CQDn22x3 = Parameter(name = 'CQDn22x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn22x3}',
                     lhablock = 'HEFTCQDN2',
                     lhacode = [ 2, 3 ])

CQDn23x1 = Parameter(name = 'CQDn23x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn23x1}',
                     lhablock = 'HEFTCQDN2',
                     lhacode = [ 3, 1 ])

CQDn23x2 = Parameter(name = 'CQDn23x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn23x2}',
                     lhablock = 'HEFTCQDN2',
                     lhacode = [ 3, 2 ])

CQDn23x3 = Parameter(name = 'CQDn23x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn23x3}',
                     lhablock = 'HEFTCQDN2',
                     lhacode = [ 3, 3 ])

CQDn31x1 = Parameter(name = 'CQDn31x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn31x1}',
                     lhablock = 'HEFTCQDN3',
                     lhacode = [ 1, 1 ])

CQDn31x2 = Parameter(name = 'CQDn31x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn31x2}',
                     lhablock = 'HEFTCQDN3',
                     lhacode = [ 1, 2 ])

CQDn31x3 = Parameter(name = 'CQDn31x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn31x3}',
                     lhablock = 'HEFTCQDN3',
                     lhacode = [ 1, 3 ])

CQDn32x1 = Parameter(name = 'CQDn32x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn32x1}',
                     lhablock = 'HEFTCQDN3',
                     lhacode = [ 2, 1 ])

CQDn32x2 = Parameter(name = 'CQDn32x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn32x2}',
                     lhablock = 'HEFTCQDN3',
                     lhacode = [ 2, 2 ])

CQDn32x3 = Parameter(name = 'CQDn32x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn32x3}',
                     lhablock = 'HEFTCQDN3',
                     lhacode = [ 2, 3 ])

CQDn33x1 = Parameter(name = 'CQDn33x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn33x1}',
                     lhablock = 'HEFTCQDN3',
                     lhacode = [ 3, 1 ])

CQDn33x2 = Parameter(name = 'CQDn33x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn33x2}',
                     lhablock = 'HEFTCQDN3',
                     lhacode = [ 3, 2 ])

CQDn33x3 = Parameter(name = 'CQDn33x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQDn33x3}',
                     lhablock = 'HEFTCQDN3',
                     lhacode = [ 3, 3 ])

CQUn21x1 = Parameter(name = 'CQUn21x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn21x1}',
                     lhablock = 'HEFTCQUN2',
                     lhacode = [ 1, 1 ])

CQUn21x2 = Parameter(name = 'CQUn21x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn21x2}',
                     lhablock = 'HEFTCQUN2',
                     lhacode = [ 1, 2 ])

CQUn21x3 = Parameter(name = 'CQUn21x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn21x3}',
                     lhablock = 'HEFTCQUN2',
                     lhacode = [ 1, 3 ])

CQUn22x1 = Parameter(name = 'CQUn22x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn22x1}',
                     lhablock = 'HEFTCQUN2',
                     lhacode = [ 2, 1 ])

CQUn22x2 = Parameter(name = 'CQUn22x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn22x2}',
                     lhablock = 'HEFTCQUN2',
                     lhacode = [ 2, 2 ])

CQUn22x3 = Parameter(name = 'CQUn22x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn22x3}',
                     lhablock = 'HEFTCQUN2',
                     lhacode = [ 2, 3 ])

CQUn23x1 = Parameter(name = 'CQUn23x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn23x1}',
                     lhablock = 'HEFTCQUN2',
                     lhacode = [ 3, 1 ])

CQUn23x2 = Parameter(name = 'CQUn23x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn23x2}',
                     lhablock = 'HEFTCQUN2',
                     lhacode = [ 3, 2 ])

CQUn23x3 = Parameter(name = 'CQUn23x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn23x3}',
                     lhablock = 'HEFTCQUN2',
                     lhacode = [ 3, 3 ])

CQUn31x1 = Parameter(name = 'CQUn31x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn31x1}',
                     lhablock = 'HEFTCQUN3',
                     lhacode = [ 1, 1 ])

CQUn31x2 = Parameter(name = 'CQUn31x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn31x2}',
                     lhablock = 'HEFTCQUN3',
                     lhacode = [ 1, 2 ])

CQUn31x3 = Parameter(name = 'CQUn31x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn31x3}',
                     lhablock = 'HEFTCQUN3',
                     lhacode = [ 1, 3 ])

CQUn32x1 = Parameter(name = 'CQUn32x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn32x1}',
                     lhablock = 'HEFTCQUN3',
                     lhacode = [ 2, 1 ])

CQUn32x2 = Parameter(name = 'CQUn32x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn32x2}',
                     lhablock = 'HEFTCQUN3',
                     lhacode = [ 2, 2 ])

CQUn32x3 = Parameter(name = 'CQUn32x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn32x3}',
                     lhablock = 'HEFTCQUN3',
                     lhacode = [ 2, 3 ])

CQUn33x1 = Parameter(name = 'CQUn33x1',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn33x1}',
                     lhablock = 'HEFTCQUN3',
                     lhacode = [ 3, 1 ])

CQUn33x2 = Parameter(name = 'CQUn33x2',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn33x2}',
                     lhablock = 'HEFTCQUN3',
                     lhacode = [ 3, 2 ])

CQUn33x3 = Parameter(name = 'CQUn33x3',
                     nature = 'external',
                     type = 'real',
                     value = 0,
                     texname = '\\text{CQUn33x3}',
                     lhablock = 'HEFTCQUN3',
                     lhacode = [ 3, 3 ])

G1 = Parameter(name = 'G1',
               nature = 'external',
               type = 'real',
               value = 0.34966947648018554,
               texname = 'G_1',
               lhablock = 'HEFTINPUTS',
               lhacode = [ 1 ])

GW = Parameter(name = 'GW',
               nature = 'external',
               type = 'real',
               value = 0.652969815696888,
               texname = 'G_W',
               lhablock = 'HEFTINPUTS',
               lhacode = [ 2 ])

GS = Parameter(name = 'GS',
               nature = 'external',
               type = 'real',
               value = 1.2171996941475736,
               texname = 'G_s',
               lhablock = 'HEFTINPUTS',
               lhacode = [ 3 ])

vev = Parameter(name = 'vev',
                nature = 'external',
                type = 'real',
                value = 246.21965079413738,
                texname = '\\text{vev}',
                lhablock = 'HEFTINPUTS',
                lhacode = [ 4 ])

hlambda = Parameter(name = 'hlambda',
                    nature = 'external',
                    type = 'real',
                    value = 0.12905349405143485,
                    texname = '\\text{hlambda}',
                    lhablock = 'HEFTINPUTS',
                    lhacode = [ 5 ])

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
               value = 1.1663787e-05,
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

CPTn0 = Parameter(name = 'CPTn0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPTn0}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 1 ])

CPTn1 = Parameter(name = 'CPTn1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPTn1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 2 ])

CPTn2 = Parameter(name = 'CPTn2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPTn2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 3 ])

CPTn3 = Parameter(name = 'CPTn3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPTn3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 4 ])

CPGn1 = Parameter(name = 'CPGn1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPGn1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 5 ])

CPGn2 = Parameter(name = 'CPGn2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPGn2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 6 ])

CPGn3 = Parameter(name = 'CPGn3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPGn3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 7 ])

CPBn1 = Parameter(name = 'CPBn1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPBn1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 8 ])

CPBn2 = Parameter(name = 'CPBn2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPBn2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 9 ])

CPBn3 = Parameter(name = 'CPBn3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPBn3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 10 ])

CSGn1 = Parameter(name = 'CSGn1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CSGn1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 11 ])

CSGn2 = Parameter(name = 'CSGn2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CSGn2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 12 ])

CSGn3 = Parameter(name = 'CSGn3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CSGn3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 13 ])

CSBn1 = Parameter(name = 'CSBn1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CSBn1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 14 ])

CSBn2 = Parameter(name = 'CSBn2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CSBn2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 15 ])

CSBn3 = Parameter(name = 'CSBn3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CSBn3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 16 ])

CS2Dn1 = Parameter(name = 'CS2Dn1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CS2Dn1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 17 ])

CS2Dn2 = Parameter(name = 'CS2Dn2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CS2Dn2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 18 ])

CS2Dn3 = Parameter(name = 'CS2Dn3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CS2Dn3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 19 ])

CPDHn4prime = Parameter(name = 'CPDHn4prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CPDHn4prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 20 ])

CPDHn5prime = Parameter(name = 'CPDHn5prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CPDHn5prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 21 ])

CPDHn6prime = Parameter(name = 'CPDHn6prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CPDHn6prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 22 ])

CPDHn7prime = Parameter(name = 'CPDHn7prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CPDHn7prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 23 ])

CPDHn8prime = Parameter(name = 'CPDHn8prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CPDHn8prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 24 ])

CPDHn9prime = Parameter(name = 'CPDHn9prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CPDHn9prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 25 ])

CPDHn10prime = Parameter(name = 'CPDHn10prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CPDHn10prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 26 ])

CPDHn11prime = Parameter(name = 'CPDHn11prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CPDHn11prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 27 ])

CPDHn12prime = Parameter(name = 'CPDHn12prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CPDHn12prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 28 ])

CP1n0 = Parameter(name = 'CP1n0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP1n0}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 29 ])

CP1n1 = Parameter(name = 'CP1n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP1n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 30 ])

CP1n2 = Parameter(name = 'CP1n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP1n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 31 ])

CP1n3 = Parameter(name = 'CP1n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP1n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 32 ])

CP2n0 = Parameter(name = 'CP2n0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP2n0}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 33 ])

CP2n1 = Parameter(name = 'CP2n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP2n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 34 ])

CP2n2 = Parameter(name = 'CP2n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP2n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 35 ])

CP2n3 = Parameter(name = 'CP2n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP2n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 36 ])

CP3n0 = Parameter(name = 'CP3n0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP3n0}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 37 ])

CP3n1 = Parameter(name = 'CP3n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP3n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 38 ])

CP3n2 = Parameter(name = 'CP3n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP3n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 39 ])

CP3n3 = Parameter(name = 'CP3n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP3n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 40 ])

CP4n1 = Parameter(name = 'CP4n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP4n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 41 ])

CP4n2 = Parameter(name = 'CP4n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP4n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 42 ])

CP4n3 = Parameter(name = 'CP4n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP4n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 43 ])

CP5n1 = Parameter(name = 'CP5n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP5n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 44 ])

CP5n2 = Parameter(name = 'CP5n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP5n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 45 ])

CP5n3 = Parameter(name = 'CP5n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP5n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 46 ])

CP6n0 = Parameter(name = 'CP6n0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP6n0}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 47 ])

CP6n1 = Parameter(name = 'CP6n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP6n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 48 ])

CP6n2 = Parameter(name = 'CP6n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP6n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 49 ])

CP6n3 = Parameter(name = 'CP6n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CP6n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 50 ])

CP12n0 = Parameter(name = 'CP12n0',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP12n0}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 51 ])

CP12n1 = Parameter(name = 'CP12n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP12n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 52 ])

CP12n2 = Parameter(name = 'CP12n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP12n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 53 ])

CP12n3 = Parameter(name = 'CP12n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP12n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 54 ])

CP13n0 = Parameter(name = 'CP13n0',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP13n0}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 55 ])

CP13n1 = Parameter(name = 'CP13n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP13n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 56 ])

CP13n2 = Parameter(name = 'CP13n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP13n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 57 ])

CP13n3 = Parameter(name = 'CP13n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP13n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 58 ])

CP14n0 = Parameter(name = 'CP14n0',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP14n0}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 59 ])

CP14n1 = Parameter(name = 'CP14n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP14n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 60 ])

CP14n2 = Parameter(name = 'CP14n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP14n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 61 ])

CP14n3 = Parameter(name = 'CP14n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP14n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 62 ])

CP17n1 = Parameter(name = 'CP17n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP17n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 63 ])

CP17n2 = Parameter(name = 'CP17n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP17n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 64 ])

CP17n3 = Parameter(name = 'CP17n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP17n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 65 ])

CP18n1 = Parameter(name = 'CP18n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP18n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 66 ])

CP18n2 = Parameter(name = 'CP18n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP18n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 67 ])

CP18n3 = Parameter(name = 'CP18n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP18n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 68 ])

CP20n2prime = Parameter(name = 'CP20n2prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP20n2prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 69 ])

CP20n3prime = Parameter(name = 'CP20n3prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP20n3prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 70 ])

CP20n4prime = Parameter(name = 'CP20n4prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP20n4prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 71 ])

CP20n5prime = Parameter(name = 'CP20n5prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP20n5prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 72 ])

CP20n6prime = Parameter(name = 'CP20n6prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP20n6prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 73 ])

CP21n2prime = Parameter(name = 'CP21n2prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP21n2prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 74 ])

CP21n3prime = Parameter(name = 'CP21n3prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP21n3prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 75 ])

CP21n4prime = Parameter(name = 'CP21n4prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP21n4prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 76 ])

CP21n5prime = Parameter(name = 'CP21n5prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP21n5prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 77 ])

CP21n6prime = Parameter(name = 'CP21n6prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP21n6prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 78 ])

CP22n2prime = Parameter(name = 'CP22n2prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP22n2prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 79 ])

CP22n3prime = Parameter(name = 'CP22n3prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP22n3prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 80 ])

CP22n4prime = Parameter(name = 'CP22n4prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP22n4prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 81 ])

CP22n5prime = Parameter(name = 'CP22n5prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP22n5prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 82 ])

CP22n6prime = Parameter(name = 'CP22n6prime',
                        nature = 'external',
                        type = 'real',
                        value = 0,
                        texname = '\\text{CP22n6prime}',
                        lhablock = 'HEFTBOSONIC',
                        lhacode = [ 83 ])

CP23n0 = Parameter(name = 'CP23n0',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP23n0}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 84 ])

CP23n1 = Parameter(name = 'CP23n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP23n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 85 ])

CP23n2 = Parameter(name = 'CP23n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP23n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 86 ])

CP23n3 = Parameter(name = 'CP23n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP23n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 87 ])

CP24n0 = Parameter(name = 'CP24n0',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP24n0}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 88 ])

CP24n1 = Parameter(name = 'CP24n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP24n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 89 ])

CP24n2 = Parameter(name = 'CP24n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP24n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 90 ])

CP24n3 = Parameter(name = 'CP24n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP24n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 91 ])

CP26n0 = Parameter(name = 'CP26n0',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP26n0}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 92 ])

CP26n1 = Parameter(name = 'CP26n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP26n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 93 ])

CP26n2 = Parameter(name = 'CP26n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP26n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 94 ])

CP26n3 = Parameter(name = 'CP26n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP26n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 95 ])

CS1n0 = Parameter(name = 'CS1n0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS1n0}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 96 ])

CS1n1 = Parameter(name = 'CS1n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS1n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 97 ])

CS1n2 = Parameter(name = 'CS1n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS1n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 98 ])

CS1n3 = Parameter(name = 'CS1n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS1n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 99 ])

CS2n1 = Parameter(name = 'CS2n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS2n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 100 ])

CS2n2 = Parameter(name = 'CS2n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS2n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 101 ])

CS2n3 = Parameter(name = 'CS2n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS2n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 102 ])

CS3n1 = Parameter(name = 'CS3n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS3n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 103 ])

CS3n2 = Parameter(name = 'CS3n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS3n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 104 ])

CS3n3 = Parameter(name = 'CS3n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS3n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 105 ])

CS4n0 = Parameter(name = 'CS4n0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS4n0}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 106 ])

CS4n1 = Parameter(name = 'CS4n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS4n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 107 ])

CS4n2 = Parameter(name = 'CS4n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS4n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 108 ])

CS4n3 = Parameter(name = 'CS4n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS4n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 109 ])

CS5n1 = Parameter(name = 'CS5n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS5n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 110 ])

CS5n2 = Parameter(name = 'CS5n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS5n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 111 ])

CS5n3 = Parameter(name = 'CS5n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS5n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 112 ])

CS6n1 = Parameter(name = 'CS6n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS6n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 113 ])

CS6n2 = Parameter(name = 'CS6n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS6n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 114 ])

CS6n3 = Parameter(name = 'CS6n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS6n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 115 ])

CS7n1 = Parameter(name = 'CS7n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS7n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 116 ])

CS7n2 = Parameter(name = 'CS7n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS7n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 117 ])

CS7n3 = Parameter(name = 'CS7n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS7n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 118 ])

CS8n0 = Parameter(name = 'CS8n0',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS8n0}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 119 ])

CS8n1 = Parameter(name = 'CS8n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS8n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 120 ])

CS8n2 = Parameter(name = 'CS8n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS8n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 121 ])

CS8n3 = Parameter(name = 'CS8n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS8n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 122 ])

CS9n1 = Parameter(name = 'CS9n1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS9n1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 123 ])

CS9n2 = Parameter(name = 'CS9n2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS9n2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 124 ])

CS9n3 = Parameter(name = 'CS9n3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CS9n3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 125 ])

CS15n1 = Parameter(name = 'CS15n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CS15n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 126 ])

CS15n2 = Parameter(name = 'CS15n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CS15n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 127 ])

CS15n3 = Parameter(name = 'CS15n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CS15n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 128 ])

CPWHD1n2prime = Parameter(name = 'CPWHD1n2prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD1n2prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 129 ])

CPWHD1n3prime = Parameter(name = 'CPWHD1n3prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD1n3prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 130 ])

CPWHD1n4prime = Parameter(name = 'CPWHD1n4prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD1n4prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 131 ])

CPWHD1n5prime = Parameter(name = 'CPWHD1n5prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD1n5prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 132 ])

CPWHD1n6prime = Parameter(name = 'CPWHD1n6prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD1n6prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 133 ])

CPWHD2n2prime = Parameter(name = 'CPWHD2n2prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD2n2prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 134 ])

CPWHD2n3prime = Parameter(name = 'CPWHD2n3prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD2n3prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 135 ])

CPWHD2n4prime = Parameter(name = 'CPWHD2n4prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD2n4prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 136 ])

CPWHD2n5prime = Parameter(name = 'CPWHD2n5prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD2n5prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 137 ])

CPWHD2n6prime = Parameter(name = 'CPWHD2n6prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPWHD2n6prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 138 ])

CSWHDTn2prime = Parameter(name = 'CSWHDTn2prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CSWHDTn2prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 139 ])

CSWHDTn3prime = Parameter(name = 'CSWHDTn3prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CSWHDTn3prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 140 ])

CSWHDTn4prime = Parameter(name = 'CSWHDTn4prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CSWHDTn4prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 141 ])

CSWHDTn5prime = Parameter(name = 'CSWHDTn5prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CSWHDTn5prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 142 ])

CSWHDTn6prime = Parameter(name = 'CSWHDTn6prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CSWHDTn6prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 143 ])

CPWn1 = Parameter(name = 'CPWn1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPWn1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 144 ])

CPWn2 = Parameter(name = 'CPWn2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPWn2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 145 ])

CPWn3 = Parameter(name = 'CPWn3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CPWn3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 146 ])

CSWn1 = Parameter(name = 'CSWn1',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CSWn1}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 147 ])

CSWn2 = Parameter(name = 'CSWn2',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CSWn2}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 148 ])

CSWn3 = Parameter(name = 'CSWn3',
                  nature = 'external',
                  type = 'real',
                  value = 0,
                  texname = '\\text{CSWn3}',
                  lhablock = 'HEFTBOSONIC',
                  lhacode = [ 149 ])

CSWHDn2prime = Parameter(name = 'CSWHDn2prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSWHDn2prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 150 ])

CSWHDn3prime = Parameter(name = 'CSWHDn3prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSWHDn3prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 151 ])

CSWHDn4prime = Parameter(name = 'CSWHDn4prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSWHDn4prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 152 ])

CSWHDn5prime = Parameter(name = 'CSWHDn5prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSWHDn5prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 153 ])

CSWHDn6prime = Parameter(name = 'CSWHDn6prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSWHDn6prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 154 ])

CP11n0 = Parameter(name = 'CP11n0',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP11n0}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 155 ])

CP11n1 = Parameter(name = 'CP11n1',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP11n1}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 156 ])

CP11n2 = Parameter(name = 'CP11n2',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP11n2}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 157 ])

CP11n3 = Parameter(name = 'CP11n3',
                   nature = 'external',
                   type = 'real',
                   value = 0,
                   texname = '\\text{CP11n3}',
                   lhablock = 'HEFTBOSONIC',
                   lhacode = [ 158 ])

CP8n2prime = Parameter(name = 'CP8n2prime',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{CP8n2prime}',
                       lhablock = 'HEFTBOSONIC',
                       lhacode = [ 159 ])

CP8n3prime = Parameter(name = 'CP8n3prime',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{CP8n3prime}',
                       lhablock = 'HEFTBOSONIC',
                       lhacode = [ 160 ])

CP8n4prime = Parameter(name = 'CP8n4prime',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{CP8n4prime}',
                       lhablock = 'HEFTBOSONIC',
                       lhacode = [ 161 ])

CP8n5prime = Parameter(name = 'CP8n5prime',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{CP8n5prime}',
                       lhablock = 'HEFTBOSONIC',
                       lhacode = [ 162 ])

CP8n6prime = Parameter(name = 'CP8n6prime',
                       nature = 'external',
                       type = 'real',
                       value = 0,
                       texname = '\\text{CP8n6prime}',
                       lhablock = 'HEFTBOSONIC',
                       lhacode = [ 163 ])

CPGHD1n2prime = Parameter(name = 'CPGHD1n2prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD1n2prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 164 ])

CPGHD1n3prime = Parameter(name = 'CPGHD1n3prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD1n3prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 165 ])

CPGHD1n4prime = Parameter(name = 'CPGHD1n4prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD1n4prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 166 ])

CPGHD1n5prime = Parameter(name = 'CPGHD1n5prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD1n5prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 167 ])

CPGHD1n6prime = Parameter(name = 'CPGHD1n6prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD1n6prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 168 ])

CPGHD2n2prime = Parameter(name = 'CPGHD2n2prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD2n2prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 169 ])

CPGHD2n3prime = Parameter(name = 'CPGHD2n3prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD2n3prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 170 ])

CPGHD2n4prime = Parameter(name = 'CPGHD2n4prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD2n4prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 171 ])

CPGHD2n5prime = Parameter(name = 'CPGHD2n5prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD2n5prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 172 ])

CPGHD2n6prime = Parameter(name = 'CPGHD2n6prime',
                          nature = 'external',
                          type = 'real',
                          value = 0,
                          texname = '\\text{CPGHD2n6prime}',
                          lhablock = 'HEFTBOSONIC',
                          lhacode = [ 173 ])

CSGHDn2prime = Parameter(name = 'CSGHDn2prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSGHDn2prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 174 ])

CSGHDn3prime = Parameter(name = 'CSGHDn3prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSGHDn3prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 175 ])

CSGHDn4prime = Parameter(name = 'CSGHDn4prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSGHDn4prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 176 ])

CSGHDn5prime = Parameter(name = 'CSGHDn5prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSGHDn5prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 177 ])

CSGHDn6prime = Parameter(name = 'CSGHDn6prime',
                         nature = 'external',
                         type = 'real',
                         value = 0,
                         texname = '\\text{CSGHDn6prime}',
                         lhablock = 'HEFTBOSONIC',
                         lhacode = [ 178 ])

CPWWWn0 = Parameter(name = 'CPWWWn0',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{CPWWWn0}',
                    lhablock = 'HEFTBOSONIC',
                    lhacode = [ 179 ])

CPWWWn1 = Parameter(name = 'CPWWWn1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{CPWWWn1}',
                    lhablock = 'HEFTBOSONIC',
                    lhacode = [ 180 ])

CPWWWn2 = Parameter(name = 'CPWWWn2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{CPWWWn2}',
                    lhablock = 'HEFTBOSONIC',
                    lhacode = [ 181 ])

CPWWWn3 = Parameter(name = 'CPWWWn3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{CPWWWn3}',
                    lhablock = 'HEFTBOSONIC',
                    lhacode = [ 182 ])

CSWWWn0 = Parameter(name = 'CSWWWn0',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{CSWWWn0}',
                    lhablock = 'HEFTBOSONIC',
                    lhacode = [ 183 ])

CSWWWn1 = Parameter(name = 'CSWWWn1',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{CSWWWn1}',
                    lhablock = 'HEFTBOSONIC',
                    lhacode = [ 184 ])

CSWWWn2 = Parameter(name = 'CSWWWn2',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{CSWWWn2}',
                    lhablock = 'HEFTBOSONIC',
                    lhacode = [ 185 ])

CSWWWn3 = Parameter(name = 'CSWWWn3',
                    nature = 'external',
                    type = 'real',
                    value = 0,
                    texname = '\\text{CSWWWn3}',
                    lhablock = 'HEFTBOSONIC',
                    lhacode = [ 186 ])

aEWM = Parameter(name = 'aEWM',
                 nature = 'internal',
                 type = 'real',
                 value = '1/aEWM1',
                 texname = '\\text{aEWM}')

AZnorm1x1 = Parameter(name = 'AZnorm1x1',
                      nature = 'internal',
                      type = 'real',
                      value = '((-2*CP1n0*G1**3*WCOrder)/(G1**2 + GW**2)**1.5 + GW/cmath.sqrt(G1**2 + GW**2)) + (GW/cmath.sqrt(G1**2 + GW**2) + (2*CP12n0*GW*(1 + G1**2/(G1**2 + GW**2))*WCOrder)/cmath.sqrt(G1**2 + GW**2)) - (GW/cmath.sqrt(G1**2 + GW**2))',
                      texname = '\\text{AZnorm1x1}')

AZnorm1x2 = Parameter(name = 'AZnorm1x2',
                      nature = 'internal',
                      type = 'real',
                      value = '((2*CP1n0*G1**2*GW*WCOrder)/(G1**2 + GW**2)**1.5 + G1/cmath.sqrt(G1**2 + GW**2)) + ((2*CP12n0*G1**3*WCOrder)/(G1**2 + GW**2)**1.5 + G1/cmath.sqrt(G1**2 + GW**2)) - (G1/cmath.sqrt(G1**2 + GW**2))',
                      texname = '\\text{AZnorm1x2}')

AZnorm2x1 = Parameter(name = 'AZnorm2x1',
                      nature = 'internal',
                      type = 'real',
                      value = '((2*CP1n0*GW**3*WCOrder)/(G1**2 + GW**2)**1.5 - G1/cmath.sqrt(G1**2 + GW**2)) + ((2*CP12n0*G1*GW**2*WCOrder)/(G1**2 + GW**2)**1.5 - G1/cmath.sqrt(G1**2 + GW**2)) - (-(G1/cmath.sqrt(G1**2 + GW**2)))',
                      texname = '\\text{AZnorm2x1}')

AZnorm2x2 = Parameter(name = 'AZnorm2x2',
                      nature = 'internal',
                      type = 'real',
                      value = '((2*CP1n0*G1*GW**2*WCOrder)/(G1**2 + GW**2)**1.5 + GW/cmath.sqrt(G1**2 + GW**2)) + ((2*CP12n0*G1**2*GW*WCOrder)/(G1**2 + GW**2)**1.5 + GW/cmath.sqrt(G1**2 + GW**2)) - (GW/cmath.sqrt(G1**2 + GW**2))',
                      texname = '\\text{AZnorm2x2}')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'GW',
               texname = 'g_W')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'G1',
               texname = 'g_1')

gs = Parameter(name = 'gs',
               nature = 'internal',
               type = 'real',
               value = 'GS',
               texname = 'g_s')

MZ = Parameter(name = 'MZ',
               nature = 'internal',
               type = 'real',
               value = '((vev*(1 - CPTn0*WCOrder)*cmath.sqrt(G1**2 + GW**2))/2.) + ((vev*(1 - (2*CP1n0*G1*GW*WCOrder)/(G1**2 + GW**2))*cmath.sqrt(G1**2 + GW**2))/2.) + ((vev*(1 + (2*CP12n0*GW**2*WCOrder)/(G1**2 + GW**2))*cmath.sqrt(G1**2 + GW**2))/2.) - 2*((vev*cmath.sqrt(G1**2 + GW**2))/2.)',
               texname = 'M_Z')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = '(GW*vev)/2.',
               texname = 'M_W')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(hlambda*vev**2)',
                texname = '\\mu')

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

LamF = Parameter(name = 'LamF',
                 nature = 'internal',
                 type = 'real',
                 value = '1',
                 texname = '\\text{LamF}')
