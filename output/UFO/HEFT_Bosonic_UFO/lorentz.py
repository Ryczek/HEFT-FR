# Merged by HEFT ufo_merge.py: baseline FB_SM, sources FB_PT, FB_PG, FB_PB, FB_SG, FB_SB, FB_S2D, FB_PDH, FB_P1, FB_P2, FB_P3, FB_P4, FB_P5, FB_P6, FB_P12, FB_P13, FB_P14, FB_P17, FB_P18, FB_P20, FB_P21, FB_P22, FB_P23, FB_P24, FB_P26, FB_S1, FB_S2, FB_S3, FB_S4, FB_S5, FB_S6, FB_S7, FB_S8, FB_S9, FB_S15, FB_PWHD1, FB_PWHD2, FB_SWHDT, FB_PW, FB_SW, FB_SWHD, FB_P11, FB_P8, FB_PGHD1, FB_PGHD2, FB_SGHD, FB_PWWW, FB_SWWW
# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.0.0 for Mac OS X x86 (64-bit) (December 13, 2023)
# Date: Tue 13 Oct 2026 20:18:42


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = '-4*Epsilon(1,2,3,-1)*P(-1,1) - 4*Epsilon(1,2,3,-1)*P(-1,2) - 4*Epsilon(1,2,3,-1)*P(-1,3)')

VVV2 = Lorentz(name = 'VVV2',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

FFSS1 = Lorentz(name = 'FFSS1',
                spins = [ 2, 2, 1, 1 ],
                structure = 'ProjM(2,1) + ProjP(2,1)')

FFSS2 = Lorentz(name = 'FFSS2',
                spins = [ 2, 2, 1, 1 ],
                structure = 'ProjM(2,1)')

FFSS3 = Lorentz(name = 'FFSS3',
                spins = [ 2, 2, 1, 1 ],
                structure = 'ProjP(2,1)')

FFSSS1 = Lorentz(name = 'FFSSS1',
                 spins = [ 2, 2, 1, 1, 1 ],
                 structure = 'ProjM(2,1) + ProjP(2,1)')

FFSSS2 = Lorentz(name = 'FFSSS2',
                 spins = [ 2, 2, 1, 1, 1 ],
                 structure = 'ProjM(2,1)')

FFSSS3 = Lorentz(name = 'FFSSS3',
                 spins = [ 2, 2, 1, 1, 1 ],
                 structure = 'ProjP(2,1)')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1)')

FFS2 = Lorentz(name = 'FFS2',
               spins = [ 2, 2, 1 ],
               structure = 'ProjP(2,1)')

FFS3 = Lorentz(name = 'FFS3',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVSSS1 = Lorentz(name = 'VVSSS1',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'Metric(1,2)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

VVSSS2 = Lorentz(name = 'VVSSS2',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVS2 = Lorentz(name = 'VVS2',
               spins = [ 3, 3, 1 ],
               structure = 'P(1,2)*P(2,1) - P(-1,1)*P(-1,2)*Metric(1,2)')

VVVSSS1 = Lorentz(name = 'VVVSSS1',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVSS1 = Lorentz(name = 'VVVSS1',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVS1 = Lorentz(name = 'VVVS1',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVVSS1 = Lorentz(name = 'VVVVSS1',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVVSS2 = Lorentz(name = 'VVVVSS2',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVVSS3 = Lorentz(name = 'VVVVSS3',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVVS1 = Lorentz(name = 'VVVVS1',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVVS2 = Lorentz(name = 'VVVVS2',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVVS3 = Lorentz(name = 'VVVVS3',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

FFV6 = Lorentz(name = 'FFV6',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjP(-1,1)')

VVSSS3 = Lorentz(name = 'VVSSS3',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = '-4*Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1) + 4*Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVSS3 = Lorentz(name = 'VVSS3',
                spins = [ 3, 3, 1, 1 ],
                structure = '-4*Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1) + 4*Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS3 = Lorentz(name = 'VVS3',
               spins = [ 3, 3, 1 ],
               structure = '-4*Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1) + 4*Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVVSSS2 = Lorentz(name = 'VVVSSS2',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = '-4*Epsilon(1,2,3,-1)*P(-1,1) - 4*Epsilon(1,2,3,-1)*P(-1,2) - 4*Epsilon(1,2,3,-1)*P(-1,3)')

VVVSS2 = Lorentz(name = 'VVVSS2',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = '-4*Epsilon(1,2,3,-1)*P(-1,1) - 4*Epsilon(1,2,3,-1)*P(-1,2) - 4*Epsilon(1,2,3,-1)*P(-1,3)')

VVVS2 = Lorentz(name = 'VVVS2',
                spins = [ 3, 3, 3, 1 ],
                structure = '-4*Epsilon(1,2,3,-1)*P(-1,1) - 4*Epsilon(1,2,3,-1)*P(-1,2) - 4*Epsilon(1,2,3,-1)*P(-1,3)')

VVSSS4 = Lorentz(name = 'VVSSS4',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVSS4 = Lorentz(name = 'VVSS4',
                spins = [ 3, 3, 1, 1 ],
                structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS4 = Lorentz(name = 'VVS4',
               spins = [ 3, 3, 1 ],
               structure = '-(Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)) + Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

FFSS4 = Lorentz(name = 'FFSS4',
                spins = [ 2, 2, 1, 1 ],
                structure = 'ProjM(2,1) - ProjP(2,1)')

FFS4 = Lorentz(name = 'FFS4',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) - ProjP(2,1)')

VSS1 = Lorentz(name = 'VSS1',
               spins = [ 3, 1, 1 ],
               structure = 'P(1,2) + P(1,3)')

VSSS1 = Lorentz(name = 'VSSS1',
                spins = [ 3, 1, 1, 1 ],
                structure = 'P(1,2) + P(1,3) + P(1,4)')

SSSS2 = Lorentz(name = 'SSSS2',
                spins = [ 1, 1, 1, 1 ],
                structure = 'P(-2,3)*P(-2,4)*P(-1,1)*P(-1,2) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,3) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,4)')

SSSSSS1 = Lorentz(name = 'SSSSSS1',
                  spins = [ 1, 1, 1, 1, 1, 1 ],
                  structure = 'P(-2,3)*P(-2,4)*P(-1,1)*P(-1,2) + P(-2,3)*P(-2,5)*P(-1,1)*P(-1,2) + P(-2,4)*P(-2,5)*P(-1,1)*P(-1,2) + P(-2,3)*P(-2,6)*P(-1,1)*P(-1,2) + P(-2,4)*P(-2,6)*P(-1,1)*P(-1,2) + P(-2,5)*P(-2,6)*P(-1,1)*P(-1,2) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,3) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,3) + P(-2,4)*P(-2,5)*P(-1,1)*P(-1,3) + P(-2,2)*P(-2,6)*P(-1,1)*P(-1,3) + P(-2,4)*P(-2,6)*P(-1,1)*P(-1,3) + P(-2,5)*P(-2,6)*P(-1,1)*P(-1,3) + P(-2,4)*P(-2,5)*P(-1,2)*P(-1,3) + P(-2,4)*P(-2,6)*P(-1,2)*P(-1,3) + P(-2,5)*P(-2,6)*P(-1,2)*P(-1,3) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,4) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,4) + P(-2,3)*P(-2,5)*P(-1,1)*P(-1,4) + P(-2,2)*P(-2,6)*P(-1,1)*P(-1,4) + P(-2,3)*P(-2,6)*P(-1,1)*P(-1,4) + P(-2,5)*P(-2,6)*P(-1,1)*P(-1,4) + P(-2,3)*P(-2,5)*P(-1,2)*P(-1,4) + P(-2,3)*P(-2,6)*P(-1,2)*P(-1,4) + P(-2,5)*P(-2,6)*P(-1,2)*P(-1,4) + P(-2,5)*P(-2,6)*P(-1,3)*P(-1,4) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,5) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,5) + P(-2,3)*P(-2,4)*P(-1,1)*P(-1,5) + P(-2,2)*P(-2,6)*P(-1,1)*P(-1,5) + P(-2,3)*P(-2,6)*P(-1,1)*P(-1,5) + P(-2,4)*P(-2,6)*P(-1,1)*P(-1,5) + P(-2,3)*P(-2,4)*P(-1,2)*P(-1,5) + P(-2,3)*P(-2,6)*P(-1,2)*P(-1,5) + P(-2,4)*P(-2,6)*P(-1,2)*P(-1,5) + P(-2,4)*P(-2,6)*P(-1,3)*P(-1,5) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,6) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,6) + P(-2,3)*P(-2,4)*P(-1,1)*P(-1,6) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,6) + P(-2,3)*P(-2,5)*P(-1,1)*P(-1,6) + P(-2,4)*P(-2,5)*P(-1,1)*P(-1,6) + P(-2,3)*P(-2,4)*P(-1,2)*P(-1,6) + P(-2,3)*P(-2,5)*P(-1,2)*P(-1,6) + P(-2,4)*P(-2,5)*P(-1,2)*P(-1,6) + P(-2,4)*P(-2,5)*P(-1,3)*P(-1,6)')

SSSSS1 = Lorentz(name = 'SSSSS1',
                 spins = [ 1, 1, 1, 1, 1 ],
                 structure = 'P(-2,3)*P(-2,4)*P(-1,1)*P(-1,2) + P(-2,3)*P(-2,5)*P(-1,1)*P(-1,2) + P(-2,4)*P(-2,5)*P(-1,1)*P(-1,2) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,3) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,3) + P(-2,4)*P(-2,5)*P(-1,1)*P(-1,3) + P(-2,4)*P(-2,5)*P(-1,2)*P(-1,3) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,4) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,4) + P(-2,3)*P(-2,5)*P(-1,1)*P(-1,4) + P(-2,3)*P(-2,5)*P(-1,2)*P(-1,4) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,5) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,5) + P(-2,3)*P(-2,4)*P(-1,1)*P(-1,5) + P(-2,3)*P(-2,4)*P(-1,2)*P(-1,5)')

VVV3 = Lorentz(name = 'VVV3',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(2,1)*Metric(1,3)')

VVV4 = Lorentz(name = 'VVV4',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,2)*Metric(1,2) - P(2,3)*Metric(1,3) - P(1,2)*Metric(2,3) + P(1,3)*Metric(2,3)')

VVVSSS3 = Lorentz(name = 'VVVSSS3',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = 'P(3,1)*Metric(1,2) - P(2,1)*Metric(1,3)')

VVVSS3 = Lorentz(name = 'VVVSS3',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,1)*Metric(1,2) - P(2,1)*Metric(1,3)')

VVVS3 = Lorentz(name = 'VVVS3',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) - P(2,1)*Metric(1,3)')

VVV5 = Lorentz(name = 'VVV5',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(1,2)*Metric(2,3)')

VVV6 = Lorentz(name = 'VVV6',
               spins = [ 3, 3, 3 ],
               structure = 'P(2,3)*Metric(1,3) - P(1,3)*Metric(2,3)')

VVVSSS4 = Lorentz(name = 'VVVSSS4',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = 'P(2,3)*Metric(1,3) - P(1,3)*Metric(2,3)')

VVVSS4 = Lorentz(name = 'VVVSS4',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(2,3)*Metric(1,3) - P(1,3)*Metric(2,3)')

VVVS4 = Lorentz(name = 'VVVS4',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(2,3)*Metric(1,3) - P(1,3)*Metric(2,3)')

VVVSSS5 = Lorentz(name = 'VVVSSS5',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(1,2)*Metric(2,3)')

VVVSS5 = Lorentz(name = 'VVVSS5',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(1,2)*Metric(2,3)')

VVVS5 = Lorentz(name = 'VVVS5',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(1,2)*Metric(2,3)')

VVVVSS4 = Lorentz(name = 'VVVVSS4',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVVS4 = Lorentz(name = 'VVVVS4',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVVSS5 = Lorentz(name = 'VVVVSS5',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVVS5 = Lorentz(name = 'VVVVS5',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVSSS5 = Lorentz(name = 'VVSSS5',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'P(1,3)*P(2,1) + P(1,4)*P(2,1) + P(1,5)*P(2,1) - P(-1,1)*P(-1,3)*Metric(1,2) - P(-1,1)*P(-1,4)*Metric(1,2) - P(-1,1)*P(-1,5)*Metric(1,2)')

VVSS5 = Lorentz(name = 'VVSS5',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,3)*P(2,1) + P(1,4)*P(2,1) - P(-1,1)*P(-1,3)*Metric(1,2) - P(-1,1)*P(-1,4)*Metric(1,2)')

VVS5 = Lorentz(name = 'VVS5',
               spins = [ 3, 3, 1 ],
               structure = 'P(1,3)*P(2,1) - P(-1,1)*P(-1,3)*Metric(1,2)')

VVSSS6 = Lorentz(name = 'VVSSS6',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'P(1,3)*P(2,1) + P(1,4)*P(2,1) + P(1,5)*P(2,1) + P(1,2)*P(2,3) + P(1,2)*P(2,4) + P(1,2)*P(2,5) - P(-1,1)*P(-1,3)*Metric(1,2) - P(-1,2)*P(-1,3)*Metric(1,2) - P(-1,1)*P(-1,4)*Metric(1,2) - P(-1,2)*P(-1,4)*Metric(1,2) - P(-1,1)*P(-1,5)*Metric(1,2) - P(-1,2)*P(-1,5)*Metric(1,2)')

VVSS6 = Lorentz(name = 'VVSS6',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,3)*P(2,1) + P(1,4)*P(2,1) + P(1,2)*P(2,3) + P(1,2)*P(2,4) - P(-1,1)*P(-1,3)*Metric(1,2) - P(-1,2)*P(-1,3)*Metric(1,2) - P(-1,1)*P(-1,4)*Metric(1,2) - P(-1,2)*P(-1,4)*Metric(1,2)')

VVS6 = Lorentz(name = 'VVS6',
               spins = [ 3, 3, 1 ],
               structure = 'P(1,3)*P(2,1) + P(1,2)*P(2,3) - P(-1,1)*P(-1,3)*Metric(1,2) - P(-1,2)*P(-1,3)*Metric(1,2)')

VVVSSS6 = Lorentz(name = 'VVVSSS6',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) + P(3,6)*Metric(1,2) - P(2,4)*Metric(1,3) - P(2,5)*Metric(1,3) - P(2,6)*Metric(1,3)')

VVVSS6 = Lorentz(name = 'VVVSS6',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) - P(2,4)*Metric(1,3) - P(2,5)*Metric(1,3)')

VVVS6 = Lorentz(name = 'VVVS6',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,4)*Metric(1,2) - P(2,4)*Metric(1,3)')

VVVSSS7 = Lorentz(name = 'VVVSSS7',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = 'P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) + P(2,6)*Metric(1,3) - P(1,4)*Metric(2,3) - P(1,5)*Metric(2,3) - P(1,6)*Metric(2,3)')

VVVSS7 = Lorentz(name = 'VVVSS7',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) - P(1,4)*Metric(2,3) - P(1,5)*Metric(2,3)')

VVVS7 = Lorentz(name = 'VVVS7',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(2,4)*Metric(1,3) - P(1,4)*Metric(2,3)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4)')

VVVVSS6 = Lorentz(name = 'VVVVSS6',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4)')

VVVVS6 = Lorentz(name = 'VVVVS6',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4)')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,2)*Metric(3,4)')

VVVVSS7 = Lorentz(name = 'VVVVSS7',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,2)*Metric(3,4)')

VVVVS7 = Lorentz(name = 'VVVVS7',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,2)*Metric(3,4)')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVVSS8 = Lorentz(name = 'VVVVSS8',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVVS8 = Lorentz(name = 'VVVVS8',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVV7 = Lorentz(name = 'VVV7',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) + P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(2,3)*Metric(1,3) - P(1,2)*Metric(2,3) + P(1,3)*Metric(2,3)')

VVV8 = Lorentz(name = 'VVV8',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) + P(1,3)*Metric(2,3)')

VVV9 = Lorentz(name = 'VVV9',
               spins = [ 3, 3, 3 ],
               structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) + Epsilon(1,2,3,-1)*P(-1,2)')

VVVSSS8 = Lorentz(name = 'VVVSSS8',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) + Epsilon(1,2,3,-1)*P(-1,2)')

VVVSS8 = Lorentz(name = 'VVVSS8',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) + Epsilon(1,2,3,-1)*P(-1,2)')

VVVS8 = Lorentz(name = 'VVVS8',
                spins = [ 3, 3, 3, 1 ],
                structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) + Epsilon(1,2,3,-1)*P(-1,2)')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Epsilon(1,2,3,4)')

VVVVSS9 = Lorentz(name = 'VVVVSS9',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Epsilon(1,2,3,4)')

VVVVS9 = Lorentz(name = 'VVVVS9',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Epsilon(1,2,3,4)')

VVSS7 = Lorentz(name = 'VVSS7',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(-1,3)*P(-1,4)*Metric(1,2)')

VVSSS7 = Lorentz(name = 'VVSSS7',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'P(-1,3)*P(-1,4)*Metric(1,2) + P(-1,3)*P(-1,5)*Metric(1,2) + P(-1,4)*P(-1,5)*Metric(1,2)')

VVSSSS1 = Lorentz(name = 'VVSSSS1',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'P(-1,3)*P(-1,4)*Metric(1,2) + P(-1,3)*P(-1,5)*Metric(1,2) + P(-1,4)*P(-1,5)*Metric(1,2) + P(-1,3)*P(-1,6)*Metric(1,2) + P(-1,4)*P(-1,6)*Metric(1,2) + P(-1,5)*P(-1,6)*Metric(1,2)')

VVSS8 = Lorentz(name = 'VVSS8',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,4)*P(2,3) + P(1,3)*P(2,4)')

VVSSS8 = Lorentz(name = 'VVSSS8',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'P(1,4)*P(2,3) + P(1,5)*P(2,3) + P(1,3)*P(2,4) + P(1,5)*P(2,4) + P(1,3)*P(2,5) + P(1,4)*P(2,5)')

VVSSSS2 = Lorentz(name = 'VVSSSS2',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'P(1,4)*P(2,3) + P(1,5)*P(2,3) + P(1,6)*P(2,3) + P(1,3)*P(2,4) + P(1,5)*P(2,4) + P(1,6)*P(2,4) + P(1,3)*P(2,5) + P(1,4)*P(2,5) + P(1,6)*P(2,5) + P(1,3)*P(2,6) + P(1,4)*P(2,6) + P(1,5)*P(2,6)')

VVSSS9 = Lorentz(name = 'VVSSS9',
                 spins = [ 3, 3, 1, 1, 1 ],
                 structure = 'Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVSSS10 = Lorentz(name = 'VVSSS10',
                  spins = [ 3, 3, 1, 1, 1 ],
                  structure = 'Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)')

VVSS9 = Lorentz(name = 'VVSS9',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVSS10 = Lorentz(name = 'VVSS10',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)')

VVS7 = Lorentz(name = 'VVS7',
               spins = [ 3, 3, 1 ],
               structure = 'Epsilon(1,2,-1,-2)*P(-2,1)*P(-1,2)')

VVS8 = Lorentz(name = 'VVS8',
               spins = [ 3, 3, 1 ],
               structure = 'Epsilon(1,2,-1,-2)*P(-2,2)*P(-1,1)')

VVV10 = Lorentz(name = 'VVV10',
                spins = [ 3, 3, 3 ],
                structure = '-(Epsilon(1,2,3,-1)*P(-1,1))')

VVV11 = Lorentz(name = 'VVV11',
                spins = [ 3, 3, 3 ],
                structure = '-(Epsilon(1,2,3,-1)*P(-1,3))')

VVVSSS9 = Lorentz(name = 'VVVSSS9',
                  spins = [ 3, 3, 3, 1, 1, 1 ],
                  structure = '-(Epsilon(1,2,3,-1)*P(-1,1))')

VVVSS9 = Lorentz(name = 'VVVSS9',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = '-(Epsilon(1,2,3,-1)*P(-1,1))')

VVVS9 = Lorentz(name = 'VVVS9',
                spins = [ 3, 3, 3, 1 ],
                structure = '-(Epsilon(1,2,3,-1)*P(-1,1))')

VVVSSS10 = Lorentz(name = 'VVVSSS10',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = '-(Epsilon(1,2,3,-1)*P(-1,3))')

VVVSS10 = Lorentz(name = 'VVVSS10',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = '-(Epsilon(1,2,3,-1)*P(-1,3))')

VVVS10 = Lorentz(name = 'VVVS10',
                 spins = [ 3, 3, 3, 1 ],
                 structure = '-(Epsilon(1,2,3,-1)*P(-1,3))')

VVSSS11 = Lorentz(name = 'VVSSS11',
                  spins = [ 3, 3, 1, 1, 1 ],
                  structure = 'Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1) + Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,1)')

VVSS11 = Lorentz(name = 'VVSS11',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)')

VVS9 = Lorentz(name = 'VVS9',
               spins = [ 3, 3, 1 ],
               structure = 'Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)')

VVSSS12 = Lorentz(name = 'VVSSS12',
                  spins = [ 3, 3, 1, 1, 1 ],
                  structure = 'Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1) + Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,1) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2) - Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,2)')

VVSS12 = Lorentz(name = 'VVSS12',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)')

VVS10 = Lorentz(name = 'VVS10',
                spins = [ 3, 3, 1 ],
                structure = 'Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)')

VVVSSS11 = Lorentz(name = 'VVVSSS11',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = '-(Epsilon(1,2,3,-1)*P(-1,4)) - Epsilon(1,2,3,-1)*P(-1,5) - Epsilon(1,2,3,-1)*P(-1,6)')

VVVSS11 = Lorentz(name = 'VVVSS11',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = '-(Epsilon(1,2,3,-1)*P(-1,4)) - Epsilon(1,2,3,-1)*P(-1,5)')

VVVS11 = Lorentz(name = 'VVVS11',
                 spins = [ 3, 3, 3, 1 ],
                 structure = '-(Epsilon(1,2,3,-1)*P(-1,4))')

VVV12 = Lorentz(name = 'VVV12',
                spins = [ 3, 3, 3 ],
                structure = 'P(3,1)*Metric(1,2) + P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(1,2)*Metric(2,3)')

VVVSSS12 = Lorentz(name = 'VVVSSS12',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = 'P(3,1)*Metric(1,2) + P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(1,2)*Metric(2,3)')

VVVSS12 = Lorentz(name = 'VVVSS12',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = 'P(3,1)*Metric(1,2) + P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(1,2)*Metric(2,3)')

VVVS12 = Lorentz(name = 'VVVS12',
                 spins = [ 3, 3, 3, 1 ],
                 structure = 'P(3,1)*Metric(1,2) + P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(1,2)*Metric(2,3)')

VVVSSS13 = Lorentz(name = 'VVVSSS13',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = 'P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) + P(2,6)*Metric(1,3) + P(1,4)*Metric(2,3) + P(1,5)*Metric(2,3) + P(1,6)*Metric(2,3)')

VVVSS13 = Lorentz(name = 'VVVSS13',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = 'P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) + P(1,4)*Metric(2,3) + P(1,5)*Metric(2,3)')

VVVS13 = Lorentz(name = 'VVVS13',
                 spins = [ 3, 3, 3, 1 ],
                 structure = 'P(2,4)*Metric(1,3) + P(1,4)*Metric(2,3)')

VVVSSS14 = Lorentz(name = 'VVVSSS14',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) + P(3,6)*Metric(1,2) + P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) + P(2,6)*Metric(1,3) + P(1,4)*Metric(2,3) + P(1,5)*Metric(2,3) + P(1,6)*Metric(2,3)')

VVVSS14 = Lorentz(name = 'VVVSS14',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) + P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) + P(1,4)*Metric(2,3) + P(1,5)*Metric(2,3)')

VVVS14 = Lorentz(name = 'VVVS14',
                 spins = [ 3, 3, 3, 1 ],
                 structure = 'P(3,4)*Metric(1,2) + P(2,4)*Metric(1,3) + P(1,4)*Metric(2,3)')

VVVSSS15 = Lorentz(name = 'VVVSSS15',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) + P(3,6)*Metric(1,2)')

VVVSS15 = Lorentz(name = 'VVVSS15',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2)')

VVVS15 = Lorentz(name = 'VVVS15',
                 spins = [ 3, 3, 3, 1 ],
                 structure = 'P(3,4)*Metric(1,2)')

VVSSS13 = Lorentz(name = 'VVSSS13',
                  spins = [ 3, 3, 1, 1, 1 ],
                  structure = 'P(1,3)*P(2,1) + P(1,4)*P(2,1) + P(1,5)*P(2,1) - P(1,2)*P(2,3) - P(1,2)*P(2,4) - P(1,2)*P(2,5) - P(-1,1)*P(-1,3)*Metric(1,2) + P(-1,2)*P(-1,3)*Metric(1,2) - P(-1,1)*P(-1,4)*Metric(1,2) + P(-1,2)*P(-1,4)*Metric(1,2) - P(-1,1)*P(-1,5)*Metric(1,2) + P(-1,2)*P(-1,5)*Metric(1,2)')

VVSS13 = Lorentz(name = 'VVSS13',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'P(1,3)*P(2,1) + P(1,4)*P(2,1) - P(1,2)*P(2,3) - P(1,2)*P(2,4) - P(-1,1)*P(-1,3)*Metric(1,2) + P(-1,2)*P(-1,3)*Metric(1,2) - P(-1,1)*P(-1,4)*Metric(1,2) + P(-1,2)*P(-1,4)*Metric(1,2)')

VVS11 = Lorentz(name = 'VVS11',
                spins = [ 3, 3, 1 ],
                structure = 'P(1,3)*P(2,1) - P(1,2)*P(2,3) - P(-1,1)*P(-1,3)*Metric(1,2) + P(-1,2)*P(-1,3)*Metric(1,2)')

VVVSSS16 = Lorentz(name = 'VVVSSS16',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) + P(3,6)*Metric(1,2) + P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) + P(2,6)*Metric(1,3) - 2*P(1,4)*Metric(2,3) - 2*P(1,5)*Metric(2,3) - 2*P(1,6)*Metric(2,3)')

VVVSS16 = Lorentz(name = 'VVVSS16',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) + P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) - 2*P(1,4)*Metric(2,3) - 2*P(1,5)*Metric(2,3)')

VVVS16 = Lorentz(name = 'VVVS16',
                 spins = [ 3, 3, 3, 1 ],
                 structure = 'P(3,4)*Metric(1,2) + P(2,4)*Metric(1,3) - 2*P(1,4)*Metric(2,3)')

VVVSSS17 = Lorentz(name = 'VVVSSS17',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) + P(3,6)*Metric(1,2) - (P(2,4)*Metric(1,3))/2. - (P(2,5)*Metric(1,3))/2. - (P(2,6)*Metric(1,3))/2. - (P(1,4)*Metric(2,3))/2. - (P(1,5)*Metric(2,3))/2. - (P(1,6)*Metric(2,3))/2.')

VVVSS17 = Lorentz(name = 'VVVSS17',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) - (P(2,4)*Metric(1,3))/2. - (P(2,5)*Metric(1,3))/2. - (P(1,4)*Metric(2,3))/2. - (P(1,5)*Metric(2,3))/2.')

VVVS17 = Lorentz(name = 'VVVS17',
                 spins = [ 3, 3, 3, 1 ],
                 structure = 'P(3,4)*Metric(1,2) - (P(2,4)*Metric(1,3))/2. - (P(1,4)*Metric(2,3))/2.')

VVSSSS3 = Lorentz(name = 'VVSSSS3',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = '-(P(-1,2)*P(-1,4)*P(1,3)*P(2,1)) - P(-1,2)*P(-1,5)*P(1,3)*P(2,1) - P(-1,2)*P(-1,6)*P(1,3)*P(2,1) - P(-1,2)*P(-1,3)*P(1,4)*P(2,1) - P(-1,2)*P(-1,5)*P(1,4)*P(2,1) - P(-1,2)*P(-1,6)*P(1,4)*P(2,1) - P(-1,2)*P(-1,3)*P(1,5)*P(2,1) - P(-1,2)*P(-1,4)*P(1,5)*P(2,1) - P(-1,2)*P(-1,6)*P(1,5)*P(2,1) - P(-1,2)*P(-1,3)*P(1,6)*P(2,1) - P(-1,2)*P(-1,4)*P(1,6)*P(2,1) - P(-1,2)*P(-1,5)*P(1,6)*P(2,1) - P(-1,1)*P(-1,4)*P(1,2)*P(2,3) - P(-1,1)*P(-1,5)*P(1,2)*P(2,3) - P(-1,1)*P(-1,6)*P(1,2)*P(2,3) + P(-1,1)*P(-1,2)*P(1,4)*P(2,3) + P(-1,1)*P(-1,2)*P(1,5)*P(2,3) + P(-1,1)*P(-1,2)*P(1,6)*P(2,3) - P(-1,1)*P(-1,3)*P(1,2)*P(2,4) - P(-1,1)*P(-1,5)*P(1,2)*P(2,4) - P(-1,1)*P(-1,6)*P(1,2)*P(2,4) + P(-1,1)*P(-1,2)*P(1,3)*P(2,4) + P(-1,1)*P(-1,2)*P(1,5)*P(2,4) + P(-1,1)*P(-1,2)*P(1,6)*P(2,4) - P(-1,1)*P(-1,3)*P(1,2)*P(2,5) - P(-1,1)*P(-1,4)*P(1,2)*P(2,5) - P(-1,1)*P(-1,6)*P(1,2)*P(2,5) + P(-1,1)*P(-1,2)*P(1,3)*P(2,5) + P(-1,1)*P(-1,2)*P(1,4)*P(2,5) + P(-1,1)*P(-1,2)*P(1,6)*P(2,5) - P(-1,1)*P(-1,3)*P(1,2)*P(2,6) - P(-1,1)*P(-1,4)*P(1,2)*P(2,6) - P(-1,1)*P(-1,5)*P(1,2)*P(2,6) + P(-1,1)*P(-1,2)*P(1,3)*P(2,6) + P(-1,1)*P(-1,2)*P(1,4)*P(2,6) + P(-1,1)*P(-1,2)*P(1,5)*P(2,6) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,3)*Metric(1,2) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,3)*Metric(1,2) + P(-2,2)*P(-2,6)*P(-1,1)*P(-1,3)*Metric(1,2) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,4)*Metric(1,2) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,4)*Metric(1,2) + P(-2,2)*P(-2,6)*P(-1,1)*P(-1,4)*Metric(1,2) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,5)*Metric(1,2) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,5)*Metric(1,2) + P(-2,2)*P(-2,6)*P(-1,1)*P(-1,5)*Metric(1,2) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,6)*Metric(1,2) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,6)*Metric(1,2) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,6)*Metric(1,2)')

VVSSS14 = Lorentz(name = 'VVSSS14',
                  spins = [ 3, 3, 1, 1, 1 ],
                  structure = '-(P(-1,2)*P(-1,4)*P(1,3)*P(2,1)) - P(-1,2)*P(-1,5)*P(1,3)*P(2,1) - P(-1,2)*P(-1,3)*P(1,4)*P(2,1) - P(-1,2)*P(-1,5)*P(1,4)*P(2,1) - P(-1,2)*P(-1,3)*P(1,5)*P(2,1) - P(-1,2)*P(-1,4)*P(1,5)*P(2,1) - P(-1,1)*P(-1,4)*P(1,2)*P(2,3) - P(-1,1)*P(-1,5)*P(1,2)*P(2,3) + P(-1,1)*P(-1,2)*P(1,4)*P(2,3) + P(-1,1)*P(-1,2)*P(1,5)*P(2,3) - P(-1,1)*P(-1,3)*P(1,2)*P(2,4) - P(-1,1)*P(-1,5)*P(1,2)*P(2,4) + P(-1,1)*P(-1,2)*P(1,3)*P(2,4) + P(-1,1)*P(-1,2)*P(1,5)*P(2,4) - P(-1,1)*P(-1,3)*P(1,2)*P(2,5) - P(-1,1)*P(-1,4)*P(1,2)*P(2,5) + P(-1,1)*P(-1,2)*P(1,3)*P(2,5) + P(-1,1)*P(-1,2)*P(1,4)*P(2,5) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,3)*Metric(1,2) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,3)*Metric(1,2) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,4)*Metric(1,2) + P(-2,2)*P(-2,5)*P(-1,1)*P(-1,4)*Metric(1,2) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,5)*Metric(1,2) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,5)*Metric(1,2)')

VVSS14 = Lorentz(name = 'VVSS14',
                 spins = [ 3, 3, 1, 1 ],
                 structure = '-(P(-1,2)*P(-1,4)*P(1,3)*P(2,1)) - P(-1,2)*P(-1,3)*P(1,4)*P(2,1) - P(-1,1)*P(-1,4)*P(1,2)*P(2,3) + P(-1,1)*P(-1,2)*P(1,4)*P(2,3) - P(-1,1)*P(-1,3)*P(1,2)*P(2,4) + P(-1,1)*P(-1,2)*P(1,3)*P(2,4) + P(-2,2)*P(-2,4)*P(-1,1)*P(-1,3)*Metric(1,2) + P(-2,2)*P(-2,3)*P(-1,1)*P(-1,4)*Metric(1,2)')

VVVSSS18 = Lorentz(name = 'VVVSSS18',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = 'P(1,5)*P(2,4)*P(3,1) + P(1,6)*P(2,4)*P(3,1) + P(1,4)*P(2,5)*P(3,1) + P(1,6)*P(2,5)*P(3,1) + P(1,4)*P(2,6)*P(3,1) + P(1,5)*P(2,6)*P(3,1) - P(1,5)*P(2,4)*P(3,2) - P(1,6)*P(2,4)*P(3,2) - P(1,4)*P(2,5)*P(3,2) - P(1,6)*P(2,5)*P(3,2) - P(1,4)*P(2,6)*P(3,2) - P(1,5)*P(2,6)*P(3,2) - P(1,5)*P(2,1)*P(3,4) - P(1,6)*P(2,1)*P(3,4) + P(1,5)*P(2,3)*P(3,4) + P(1,6)*P(2,3)*P(3,4) + P(1,2)*P(2,5)*P(3,4) - P(1,3)*P(2,5)*P(3,4) + P(1,2)*P(2,6)*P(3,4) - P(1,3)*P(2,6)*P(3,4) - P(1,4)*P(2,1)*P(3,5) - P(1,6)*P(2,1)*P(3,5) + P(1,4)*P(2,3)*P(3,5) + P(1,6)*P(2,3)*P(3,5) + P(1,2)*P(2,4)*P(3,5) - P(1,3)*P(2,4)*P(3,5) + P(1,2)*P(2,6)*P(3,5) - P(1,3)*P(2,6)*P(3,5) - P(1,4)*P(2,1)*P(3,6) - P(1,5)*P(2,1)*P(3,6) + P(1,4)*P(2,3)*P(3,6) + P(1,5)*P(2,3)*P(3,6) + P(1,2)*P(2,4)*P(3,6) - P(1,3)*P(2,4)*P(3,6) + P(1,2)*P(2,5)*P(3,6) - P(1,3)*P(2,5)*P(3,6) + P(-1,1)*P(-1,5)*P(3,4)*Metric(1,2) - P(-1,2)*P(-1,5)*P(3,4)*Metric(1,2) + P(-1,1)*P(-1,6)*P(3,4)*Metric(1,2) - P(-1,2)*P(-1,6)*P(3,4)*Metric(1,2) + P(-1,1)*P(-1,4)*P(3,5)*Metric(1,2) - P(-1,2)*P(-1,4)*P(3,5)*Metric(1,2) + P(-1,1)*P(-1,6)*P(3,5)*Metric(1,2) - P(-1,2)*P(-1,6)*P(3,5)*Metric(1,2) + P(-1,1)*P(-1,4)*P(3,6)*Metric(1,2) - P(-1,2)*P(-1,4)*P(3,6)*Metric(1,2) + P(-1,1)*P(-1,5)*P(3,6)*Metric(1,2) - P(-1,2)*P(-1,5)*P(3,6)*Metric(1,2) - P(-1,1)*P(-1,5)*P(2,4)*Metric(1,3) + P(-1,3)*P(-1,5)*P(2,4)*Metric(1,3) - P(-1,1)*P(-1,6)*P(2,4)*Metric(1,3) + P(-1,3)*P(-1,6)*P(2,4)*Metric(1,3) - P(-1,1)*P(-1,4)*P(2,5)*Metric(1,3) + P(-1,3)*P(-1,4)*P(2,5)*Metric(1,3) - P(-1,1)*P(-1,6)*P(2,5)*Metric(1,3) + P(-1,3)*P(-1,6)*P(2,5)*Metric(1,3) - P(-1,1)*P(-1,4)*P(2,6)*Metric(1,3) + P(-1,3)*P(-1,4)*P(2,6)*Metric(1,3) - P(-1,1)*P(-1,5)*P(2,6)*Metric(1,3) + P(-1,3)*P(-1,5)*P(2,6)*Metric(1,3) + P(-1,2)*P(-1,5)*P(1,4)*Metric(2,3) - P(-1,3)*P(-1,5)*P(1,4)*Metric(2,3) + P(-1,2)*P(-1,6)*P(1,4)*Metric(2,3) - P(-1,3)*P(-1,6)*P(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*P(1,5)*Metric(2,3) - P(-1,3)*P(-1,4)*P(1,5)*Metric(2,3) + P(-1,2)*P(-1,6)*P(1,5)*Metric(2,3) - P(-1,3)*P(-1,6)*P(1,5)*Metric(2,3) + P(-1,2)*P(-1,4)*P(1,6)*Metric(2,3) - P(-1,3)*P(-1,4)*P(1,6)*Metric(2,3) + P(-1,2)*P(-1,5)*P(1,6)*Metric(2,3) - P(-1,3)*P(-1,5)*P(1,6)*Metric(2,3)')

VVVSS18 = Lorentz(name = 'VVVSS18',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = 'P(1,5)*P(2,4)*P(3,1) + P(1,4)*P(2,5)*P(3,1) - P(1,5)*P(2,4)*P(3,2) - P(1,4)*P(2,5)*P(3,2) - P(1,5)*P(2,1)*P(3,4) + P(1,5)*P(2,3)*P(3,4) + P(1,2)*P(2,5)*P(3,4) - P(1,3)*P(2,5)*P(3,4) - P(1,4)*P(2,1)*P(3,5) + P(1,4)*P(2,3)*P(3,5) + P(1,2)*P(2,4)*P(3,5) - P(1,3)*P(2,4)*P(3,5) + P(-1,1)*P(-1,5)*P(3,4)*Metric(1,2) - P(-1,2)*P(-1,5)*P(3,4)*Metric(1,2) + P(-1,1)*P(-1,4)*P(3,5)*Metric(1,2) - P(-1,2)*P(-1,4)*P(3,5)*Metric(1,2) - P(-1,1)*P(-1,5)*P(2,4)*Metric(1,3) + P(-1,3)*P(-1,5)*P(2,4)*Metric(1,3) - P(-1,1)*P(-1,4)*P(2,5)*Metric(1,3) + P(-1,3)*P(-1,4)*P(2,5)*Metric(1,3) + P(-1,2)*P(-1,5)*P(1,4)*Metric(2,3) - P(-1,3)*P(-1,5)*P(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*P(1,5)*Metric(2,3) - P(-1,3)*P(-1,4)*P(1,5)*Metric(2,3)')

VVVVSS10 = Lorentz(name = 'VVVVSS10',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(3,6)*P(4,5)*Metric(1,2) + P(3,5)*P(4,6)*Metric(1,2) - (P(2,6)*P(4,5)*Metric(1,3))/2. - (P(2,5)*P(4,6)*Metric(1,3))/2. - (P(2,6)*P(3,5)*Metric(1,4))/2. - (P(2,5)*P(3,6)*Metric(1,4))/2. - (P(1,6)*P(4,5)*Metric(2,3))/2. - (P(1,5)*P(4,6)*Metric(2,3))/2. - (P(1,6)*P(3,5)*Metric(2,4))/2. - (P(1,5)*P(3,6)*Metric(2,4))/2. + P(1,6)*P(2,5)*Metric(3,4) + P(1,5)*P(2,6)*Metric(3,4)')

VVVVSS11 = Lorentz(name = 'VVVVSS11',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(3,6)*P(4,5)*Metric(1,2) + P(3,5)*P(4,6)*Metric(1,2) + P(2,6)*P(4,5)*Metric(1,3) + P(2,5)*P(4,6)*Metric(1,3) - 2*P(2,6)*P(3,5)*Metric(1,4) - 2*P(2,5)*P(3,6)*Metric(1,4) - 2*P(1,6)*P(4,5)*Metric(2,3) - 2*P(1,5)*P(4,6)*Metric(2,3) + P(1,6)*P(3,5)*Metric(2,4) + P(1,5)*P(3,6)*Metric(2,4) + P(1,6)*P(2,5)*Metric(3,4) + P(1,5)*P(2,6)*Metric(3,4)')

VVSSSS4 = Lorentz(name = 'VVSSSS4',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = 'P(-1,3)*P(-1,4)*P(1,2)*P(2,1) + P(-1,3)*P(-1,5)*P(1,2)*P(2,1) + P(-1,4)*P(-1,5)*P(1,2)*P(2,1) + P(-1,3)*P(-1,6)*P(1,2)*P(2,1) + P(-1,4)*P(-1,6)*P(1,2)*P(2,1) + P(-1,5)*P(-1,6)*P(1,2)*P(2,1) - P(-2,3)*P(-2,4)*P(-1,1)*P(-1,2)*Metric(1,2) - P(-2,3)*P(-2,5)*P(-1,1)*P(-1,2)*Metric(1,2) - P(-2,4)*P(-2,5)*P(-1,1)*P(-1,2)*Metric(1,2) - P(-2,3)*P(-2,6)*P(-1,1)*P(-1,2)*Metric(1,2) - P(-2,4)*P(-2,6)*P(-1,1)*P(-1,2)*Metric(1,2) - P(-2,5)*P(-2,6)*P(-1,1)*P(-1,2)*Metric(1,2)')

VVSSS15 = Lorentz(name = 'VVSSS15',
                  spins = [ 3, 3, 1, 1, 1 ],
                  structure = 'P(-1,3)*P(-1,4)*P(1,2)*P(2,1) + P(-1,3)*P(-1,5)*P(1,2)*P(2,1) + P(-1,4)*P(-1,5)*P(1,2)*P(2,1) - P(-2,3)*P(-2,4)*P(-1,1)*P(-1,2)*Metric(1,2) - P(-2,3)*P(-2,5)*P(-1,1)*P(-1,2)*Metric(1,2) - P(-2,4)*P(-2,5)*P(-1,1)*P(-1,2)*Metric(1,2)')

VVSS15 = Lorentz(name = 'VVSS15',
                 spins = [ 3, 3, 1, 1 ],
                 structure = 'P(-1,3)*P(-1,4)*P(1,2)*P(2,1) - P(-2,3)*P(-2,4)*P(-1,1)*P(-1,2)*Metric(1,2)')

VVVSSS19 = Lorentz(name = 'VVVSSS19',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = 'P(-1,4)*P(-1,5)*P(3,1)*Metric(1,2) + P(-1,4)*P(-1,6)*P(3,1)*Metric(1,2) + P(-1,5)*P(-1,6)*P(3,1)*Metric(1,2) - P(-1,4)*P(-1,5)*P(3,2)*Metric(1,2) - P(-1,4)*P(-1,6)*P(3,2)*Metric(1,2) - P(-1,5)*P(-1,6)*P(3,2)*Metric(1,2) - P(-1,4)*P(-1,5)*P(2,1)*Metric(1,3) - P(-1,4)*P(-1,6)*P(2,1)*Metric(1,3) - P(-1,5)*P(-1,6)*P(2,1)*Metric(1,3) + P(-1,4)*P(-1,5)*P(2,3)*Metric(1,3) + P(-1,4)*P(-1,6)*P(2,3)*Metric(1,3) + P(-1,5)*P(-1,6)*P(2,3)*Metric(1,3) + P(-1,4)*P(-1,5)*P(1,2)*Metric(2,3) + P(-1,4)*P(-1,6)*P(1,2)*Metric(2,3) + P(-1,5)*P(-1,6)*P(1,2)*Metric(2,3) - P(-1,4)*P(-1,5)*P(1,3)*Metric(2,3) - P(-1,4)*P(-1,6)*P(1,3)*Metric(2,3) - P(-1,5)*P(-1,6)*P(1,3)*Metric(2,3)')

VVVSS19 = Lorentz(name = 'VVVSS19',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = 'P(-1,4)*P(-1,5)*P(3,1)*Metric(1,2) - P(-1,4)*P(-1,5)*P(3,2)*Metric(1,2) - P(-1,4)*P(-1,5)*P(2,1)*Metric(1,3) + P(-1,4)*P(-1,5)*P(2,3)*Metric(1,3) + P(-1,4)*P(-1,5)*P(1,2)*Metric(2,3) - P(-1,4)*P(-1,5)*P(1,3)*Metric(2,3)')

VVVVSS12 = Lorentz(name = 'VVVVSS12',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(-1,5)*P(-1,6)*Metric(1,4)*Metric(2,3) + P(-1,5)*P(-1,6)*Metric(1,3)*Metric(2,4) - 2*P(-1,5)*P(-1,6)*Metric(1,2)*Metric(3,4)')

VVVVSS13 = Lorentz(name = 'VVVVSS13',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(-1,5)*P(-1,6)*Metric(1,4)*Metric(2,3) - (P(-1,5)*P(-1,6)*Metric(1,3)*Metric(2,4))/2. - (P(-1,5)*P(-1,6)*Metric(1,2)*Metric(3,4))/2.')

VVSSSS5 = Lorentz(name = 'VVSSSS5',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = '-(Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,2)*P(-1,1)*P(-1,3)) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,2)*P(-1,1)*P(-1,3) - Epsilon(1,2,-2,-3)*P(-3,6)*P(-2,2)*P(-1,1)*P(-1,3) - Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(1,2,-2,-3)*P(-3,6)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,2)*P(-1,1)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,6)*P(-2,2)*P(-1,1)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,1)*P(-1,2)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,6)*P(-2,1)*P(-1,2)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,2)*P(-1,1)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,6)*P(-2,2)*P(-1,1)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,1)*P(-1,2)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,6)*P(-2,1)*P(-1,2)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*P(-1,6) - Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,2)*P(-1,1)*P(-1,6) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,2)*P(-1,1)*P(-1,6) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*P(-1,6) - Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,1)*P(-1,2)*P(-1,6) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,1)*P(-1,2)*P(-1,6) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,4)*P(-1,2)*P(1,3) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,5)*P(-1,2)*P(1,3) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,6)*P(-1,2)*P(1,3) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*P(1,4) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,5)*P(-1,2)*P(1,4) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,6)*P(-1,2)*P(1,4) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*P(1,5) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,4)*P(-1,2)*P(1,5) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,6)*P(-1,2)*P(1,5) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*P(1,6) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,4)*P(-1,2)*P(1,6) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,5)*P(-1,2)*P(1,6) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,4)*P(-1,1)*P(2,3) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,5)*P(-1,1)*P(2,3) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,6)*P(-1,1)*P(2,3) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*P(2,4) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,5)*P(-1,1)*P(2,4) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,6)*P(-1,1)*P(2,4) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*P(2,5) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,4)*P(-1,1)*P(2,5) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,6)*P(-1,1)*P(2,5) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*P(2,6) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,4)*P(-1,1)*P(2,6) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,5)*P(-1,1)*P(2,6)')

VVSSS16 = Lorentz(name = 'VVSSS16',
                  spins = [ 3, 3, 1, 1, 1 ],
                  structure = '-(Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,2)*P(-1,1)*P(-1,3)) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,2)*P(-1,1)*P(-1,3) - Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,2)*P(-1,1)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,5)*P(-2,1)*P(-1,2)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,2)*P(-1,1)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,1)*P(-1,2)*P(-1,5) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,4)*P(-1,2)*P(1,3) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,5)*P(-1,2)*P(1,3) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*P(1,4) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,5)*P(-1,2)*P(1,4) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*P(1,5) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,4)*P(-1,2)*P(1,5) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,4)*P(-1,1)*P(2,3) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,5)*P(-1,1)*P(2,3) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*P(2,4) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,5)*P(-1,1)*P(2,4) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*P(2,5) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,4)*P(-1,1)*P(2,5)')

VVSS16 = Lorentz(name = 'VVSS16',
                 spins = [ 3, 3, 1, 1 ],
                 structure = '-(Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,2)*P(-1,1)*P(-1,3)) - Epsilon(1,2,-2,-3)*P(-3,4)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*P(-1,4) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,4)*P(-1,2)*P(1,3) - Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*P(1,4) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,4)*P(-1,1)*P(2,3) + Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*P(2,4)')

VVVSSS20 = Lorentz(name = 'VVVSSS20',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = '-(Epsilon(1,2,3,-2)*P(-2,5)*P(-1,2)*P(-1,4)) - Epsilon(1,2,3,-2)*P(-2,6)*P(-1,2)*P(-1,4) + Epsilon(1,2,3,-2)*P(-2,5)*P(-1,3)*P(-1,4) + Epsilon(1,2,3,-2)*P(-2,6)*P(-1,3)*P(-1,4) - Epsilon(1,2,3,-2)*P(-2,4)*P(-1,2)*P(-1,5) - Epsilon(1,2,3,-2)*P(-2,6)*P(-1,2)*P(-1,5) + Epsilon(1,2,3,-2)*P(-2,4)*P(-1,3)*P(-1,5) + Epsilon(1,2,3,-2)*P(-2,6)*P(-1,3)*P(-1,5) - Epsilon(1,2,3,-2)*P(-2,4)*P(-1,2)*P(-1,6) - Epsilon(1,2,3,-2)*P(-2,5)*P(-1,2)*P(-1,6) + Epsilon(1,2,3,-2)*P(-2,4)*P(-1,3)*P(-1,6) + Epsilon(1,2,3,-2)*P(-2,5)*P(-1,3)*P(-1,6) - Epsilon(2,3,-1,-2)*P(-2,5)*P(-1,2)*P(1,4) - Epsilon(2,3,-1,-2)*P(-2,6)*P(-1,2)*P(1,4) + Epsilon(2,3,-1,-2)*P(-2,5)*P(-1,3)*P(1,4) + Epsilon(2,3,-1,-2)*P(-2,6)*P(-1,3)*P(1,4) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*P(1,5) - Epsilon(2,3,-1,-2)*P(-2,6)*P(-1,2)*P(1,5) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,3)*P(1,5) + Epsilon(2,3,-1,-2)*P(-2,6)*P(-1,3)*P(1,5) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*P(1,6) - Epsilon(2,3,-1,-2)*P(-2,5)*P(-1,2)*P(1,6) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,3)*P(1,6) + Epsilon(2,3,-1,-2)*P(-2,5)*P(-1,3)*P(1,6) - Epsilon(1,3,-1,-2)*P(-2,5)*P(-1,3)*P(2,4) - Epsilon(1,3,-1,-2)*P(-2,6)*P(-1,3)*P(2,4) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,5)*P(2,4) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,6)*P(2,4) - Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,3)*P(2,5) - Epsilon(1,3,-1,-2)*P(-2,6)*P(-1,3)*P(2,5) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*P(2,5) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,6)*P(2,5) - Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,3)*P(2,6) - Epsilon(1,3,-1,-2)*P(-2,5)*P(-1,3)*P(2,6) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*P(2,6) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,5)*P(2,6) - Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,2)*P(3,4) - Epsilon(1,2,-1,-2)*P(-2,6)*P(-1,2)*P(3,4) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,5)*P(3,4) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,6)*P(3,4) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*P(3,5) - Epsilon(1,2,-1,-2)*P(-2,6)*P(-1,2)*P(3,5) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,4)*P(3,5) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,6)*P(3,5) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*P(3,6) - Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,2)*P(3,6) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,4)*P(3,6) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,5)*P(3,6)')

VVVSS20 = Lorentz(name = 'VVVSS20',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = '-(Epsilon(1,2,3,-2)*P(-2,5)*P(-1,2)*P(-1,4)) + Epsilon(1,2,3,-2)*P(-2,5)*P(-1,3)*P(-1,4) - Epsilon(1,2,3,-2)*P(-2,4)*P(-1,2)*P(-1,5) + Epsilon(1,2,3,-2)*P(-2,4)*P(-1,3)*P(-1,5) - Epsilon(2,3,-1,-2)*P(-2,5)*P(-1,2)*P(1,4) + Epsilon(2,3,-1,-2)*P(-2,5)*P(-1,3)*P(1,4) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*P(1,5) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,3)*P(1,5) - Epsilon(1,3,-1,-2)*P(-2,5)*P(-1,3)*P(2,4) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,5)*P(2,4) - Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,3)*P(2,5) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*P(2,5) - Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,2)*P(3,4) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,5)*P(3,4) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*P(3,5) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,4)*P(3,5)')

VVVVSS14 = Lorentz(name = 'VVVVSS14',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = '-(Epsilon(2,3,4,-1)*P(-1,6)*P(1,5)) - Epsilon(2,3,4,-1)*P(-1,5)*P(1,6) - Epsilon(1,3,4,-1)*P(-1,6)*P(2,5) - Epsilon(1,3,4,-1)*P(-1,5)*P(2,6)')

VVVSSS21 = Lorentz(name = 'VVVSSS21',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = 'Epsilon(1,2,3,-2)*P(-2,5)*P(-1,1)*P(-1,4) + Epsilon(1,2,3,-2)*P(-2,6)*P(-1,1)*P(-1,4) - Epsilon(1,2,3,-2)*P(-2,5)*P(-1,2)*P(-1,4) - Epsilon(1,2,3,-2)*P(-2,6)*P(-1,2)*P(-1,4) + Epsilon(1,2,3,-2)*P(-2,4)*P(-1,1)*P(-1,5) + Epsilon(1,2,3,-2)*P(-2,6)*P(-1,1)*P(-1,5) - Epsilon(1,2,3,-2)*P(-2,4)*P(-1,2)*P(-1,5) - Epsilon(1,2,3,-2)*P(-2,6)*P(-1,2)*P(-1,5) + Epsilon(1,2,3,-2)*P(-2,4)*P(-1,1)*P(-1,6) + Epsilon(1,2,3,-2)*P(-2,5)*P(-1,1)*P(-1,6) - Epsilon(1,2,3,-2)*P(-2,4)*P(-1,2)*P(-1,6) - Epsilon(1,2,3,-2)*P(-2,5)*P(-1,2)*P(-1,6) - Epsilon(2,3,-1,-2)*P(-2,5)*P(-1,2)*P(1,4) - Epsilon(2,3,-1,-2)*P(-2,6)*P(-1,2)*P(1,4) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,5)*P(1,4) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,6)*P(1,4) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*P(1,5) - Epsilon(2,3,-1,-2)*P(-2,6)*P(-1,2)*P(1,5) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,4)*P(1,5) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,6)*P(1,5) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*P(1,6) - Epsilon(2,3,-1,-2)*P(-2,5)*P(-1,2)*P(1,6) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,4)*P(1,6) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,5)*P(1,6) - Epsilon(1,3,-1,-2)*P(-2,5)*P(-1,1)*P(2,4) - Epsilon(1,3,-1,-2)*P(-2,6)*P(-1,1)*P(2,4) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,5)*P(2,4) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,6)*P(2,4) - Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,1)*P(2,5) - Epsilon(1,3,-1,-2)*P(-2,6)*P(-1,1)*P(2,5) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*P(2,5) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,6)*P(2,5) - Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,1)*P(2,6) - Epsilon(1,3,-1,-2)*P(-2,5)*P(-1,1)*P(2,6) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*P(2,6) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,5)*P(2,6) + Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,1)*P(3,4) + Epsilon(1,2,-1,-2)*P(-2,6)*P(-1,1)*P(3,4) - Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,2)*P(3,4) - Epsilon(1,2,-1,-2)*P(-2,6)*P(-1,2)*P(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)*P(3,5) + Epsilon(1,2,-1,-2)*P(-2,6)*P(-1,1)*P(3,5) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*P(3,5) - Epsilon(1,2,-1,-2)*P(-2,6)*P(-1,2)*P(3,5) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)*P(3,6) + Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,1)*P(3,6) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*P(3,6) - Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,2)*P(3,6)')

VVVSS21 = Lorentz(name = 'VVVSS21',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = 'Epsilon(1,2,3,-2)*P(-2,5)*P(-1,1)*P(-1,4) - Epsilon(1,2,3,-2)*P(-2,5)*P(-1,2)*P(-1,4) + Epsilon(1,2,3,-2)*P(-2,4)*P(-1,1)*P(-1,5) - Epsilon(1,2,3,-2)*P(-2,4)*P(-1,2)*P(-1,5) - Epsilon(2,3,-1,-2)*P(-2,5)*P(-1,2)*P(1,4) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,5)*P(1,4) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*P(1,5) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,4)*P(1,5) - Epsilon(1,3,-1,-2)*P(-2,5)*P(-1,1)*P(2,4) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,5)*P(2,4) - Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,1)*P(2,5) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*P(2,5) + Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,1)*P(3,4) - Epsilon(1,2,-1,-2)*P(-2,5)*P(-1,2)*P(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)*P(3,5) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*P(3,5)')

VVVVSS15 = Lorentz(name = 'VVVVSS15',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = '-(Epsilon(2,3,4,-1)*P(-1,6)*P(1,5)) - Epsilon(2,3,4,-1)*P(-1,5)*P(1,6) - Epsilon(1,2,3,-1)*P(-1,6)*P(4,5) - Epsilon(1,2,3,-1)*P(-1,5)*P(4,6)')

VVVVSS16 = Lorentz(name = 'VVVVSS16',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = '-(Epsilon(1,2,4,-1)*P(-1,6)*P(3,5)) - Epsilon(1,2,4,-1)*P(-1,5)*P(3,6) - Epsilon(1,2,3,-1)*P(-1,6)*P(4,5) - Epsilon(1,2,3,-1)*P(-1,5)*P(4,6)')

VVVSSS22 = Lorentz(name = 'VVVSSS22',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVVSS22 = Lorentz(name = 'VVVSS22',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVVS18 = Lorentz(name = 'VVVS18',
                 spins = [ 3, 3, 3, 1 ],
                 structure = '-(Epsilon(1,2,3,-1)*P(-1,1)) - Epsilon(1,2,3,-1)*P(-1,2) - Epsilon(1,2,3,-1)*P(-1,3)')

VVSSSS6 = Lorentz(name = 'VVSSSS6',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = '-(Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,4)) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,5) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,4)*P(-1,5) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,4)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,6) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,6) - Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,4)*P(-1,6) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,4)*P(-1,6) - Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,5)*P(-1,6) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,5)*P(-1,6)')

VVSSS17 = Lorentz(name = 'VVSSS17',
                  spins = [ 3, 3, 1, 1, 1 ],
                  structure = '-(Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,4)) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,4) - Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,5) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,5) - Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,4)*P(-1,5) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,4)*P(-1,5)')

VVSS17 = Lorentz(name = 'VVSS17',
                 spins = [ 3, 3, 1, 1 ],
                 structure = '-(Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,4)) + Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,4)')

VVVSSS23 = Lorentz(name = 'VVVSSS23',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = '-(Epsilon(1,2,3,-2)*P(-2,1)*P(-1,4)*P(-1,5)) - Epsilon(1,2,3,-2)*P(-2,2)*P(-1,4)*P(-1,5) - Epsilon(1,2,3,-2)*P(-2,3)*P(-1,4)*P(-1,5) - Epsilon(1,2,3,-2)*P(-2,1)*P(-1,4)*P(-1,6) - Epsilon(1,2,3,-2)*P(-2,2)*P(-1,4)*P(-1,6) - Epsilon(1,2,3,-2)*P(-2,3)*P(-1,4)*P(-1,6) - Epsilon(1,2,3,-2)*P(-2,1)*P(-1,5)*P(-1,6) - Epsilon(1,2,3,-2)*P(-2,2)*P(-1,5)*P(-1,6) - Epsilon(1,2,3,-2)*P(-2,3)*P(-1,5)*P(-1,6)')

VVVSS23 = Lorentz(name = 'VVVSS23',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = '-(Epsilon(1,2,3,-2)*P(-2,1)*P(-1,4)*P(-1,5)) - Epsilon(1,2,3,-2)*P(-2,2)*P(-1,4)*P(-1,5) - Epsilon(1,2,3,-2)*P(-2,3)*P(-1,4)*P(-1,5)')

VVVV10 = Lorentz(name = 'VVVV10',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + 2*Metric(1,2)*Metric(3,4)')

VVVVSS17 = Lorentz(name = 'VVVVSS17',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + 2*Metric(1,2)*Metric(3,4)')

VVVVS10 = Lorentz(name = 'VVVVS10',
                  spins = [ 3, 3, 3, 3, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + 2*Metric(1,2)*Metric(3,4)')

VVVVSS18 = Lorentz(name = 'VVVVSS18',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(3,6)*P(4,5)*Metric(1,2) + P(3,5)*P(4,6)*Metric(1,2) - P(2,6)*P(4,5)*Metric(1,3) - P(2,5)*P(4,6)*Metric(1,3) - P(1,6)*P(3,5)*Metric(2,4) - P(1,5)*P(3,6)*Metric(2,4) + P(1,6)*P(2,5)*Metric(3,4) + P(1,5)*P(2,6)*Metric(3,4)')

VVVVSS19 = Lorentz(name = 'VVVVSS19',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(3,6)*P(4,5)*Metric(1,2) + P(3,5)*P(4,6)*Metric(1,2) - P(2,6)*P(3,5)*Metric(1,4) - P(2,5)*P(3,6)*Metric(1,4) - P(1,6)*P(4,5)*Metric(2,3) - P(1,5)*P(4,6)*Metric(2,3) + P(1,6)*P(2,5)*Metric(3,4) + P(1,5)*P(2,6)*Metric(3,4)')

VVVVSS20 = Lorentz(name = 'VVVVSS20',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(2,6)*P(4,5)*Metric(1,3) + P(2,5)*P(4,6)*Metric(1,3) - P(2,6)*P(3,5)*Metric(1,4) - P(2,5)*P(3,6)*Metric(1,4) - P(1,6)*P(4,5)*Metric(2,3) - P(1,5)*P(4,6)*Metric(2,3) + P(1,6)*P(3,5)*Metric(2,4) + P(1,5)*P(3,6)*Metric(2,4)')

VVVVSS21 = Lorentz(name = 'VVVVSS21',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(-1,5)*P(-1,6)*Metric(1,4)*Metric(2,3) - P(-1,5)*P(-1,6)*Metric(1,2)*Metric(3,4)')

VVVVSS22 = Lorentz(name = 'VVVVSS22',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(-1,5)*P(-1,6)*Metric(1,4)*Metric(2,3) - P(-1,5)*P(-1,6)*Metric(1,3)*Metric(2,4)')

VVVVSS23 = Lorentz(name = 'VVVVSS23',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(-1,5)*P(-1,6)*Metric(1,3)*Metric(2,4) - P(-1,5)*P(-1,6)*Metric(1,2)*Metric(3,4)')

VVSSSS7 = Lorentz(name = 'VVSSSS7',
                  spins = [ 3, 3, 1, 1, 1, 1 ],
                  structure = '-4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,4) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,4) - 4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,5) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,5) - 4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,4)*P(-1,5) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,4)*P(-1,5) - 4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,6) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,6) - 4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,4)*P(-1,6) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,4)*P(-1,6) - 4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,5)*P(-1,6) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,5)*P(-1,6)')

VVSSS18 = Lorentz(name = 'VVSSS18',
                  spins = [ 3, 3, 1, 1, 1 ],
                  structure = '-4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,4) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,4) - 4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,5) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,5) - 4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,4)*P(-1,5) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,4)*P(-1,5)')

VVSS18 = Lorentz(name = 'VVSS18',
                 spins = [ 3, 3, 1, 1 ],
                 structure = '-4*Epsilon(1,2,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*P(-1,4) + 4*Epsilon(1,2,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*P(-1,4)')

VVVSSS24 = Lorentz(name = 'VVVSSS24',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = '-4*Epsilon(1,2,3,-2)*P(-2,1)*P(-1,4)*P(-1,5) - 4*Epsilon(1,2,3,-2)*P(-2,2)*P(-1,4)*P(-1,5) - 4*Epsilon(1,2,3,-2)*P(-2,3)*P(-1,4)*P(-1,5) - 4*Epsilon(1,2,3,-2)*P(-2,1)*P(-1,4)*P(-1,6) - 4*Epsilon(1,2,3,-2)*P(-2,2)*P(-1,4)*P(-1,6) - 4*Epsilon(1,2,3,-2)*P(-2,3)*P(-1,4)*P(-1,6) - 4*Epsilon(1,2,3,-2)*P(-2,1)*P(-1,5)*P(-1,6) - 4*Epsilon(1,2,3,-2)*P(-2,2)*P(-1,5)*P(-1,6) - 4*Epsilon(1,2,3,-2)*P(-2,3)*P(-1,5)*P(-1,6)')

VVVSS24 = Lorentz(name = 'VVVSS24',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = '-4*Epsilon(1,2,3,-2)*P(-2,1)*P(-1,4)*P(-1,5) - 4*Epsilon(1,2,3,-2)*P(-2,2)*P(-1,4)*P(-1,5) - 4*Epsilon(1,2,3,-2)*P(-2,3)*P(-1,4)*P(-1,5)')

VVV13 = Lorentz(name = 'VVV13',
                spins = [ 3, 3, 3 ],
                structure = '-(P(1,2)*P(2,3)*P(3,1)) + P(1,3)*P(2,1)*P(3,2) + P(-1,2)*P(-1,3)*P(3,1)*Metric(1,2) - P(-1,1)*P(-1,3)*P(3,2)*Metric(1,2) - P(-1,2)*P(-1,3)*P(2,1)*Metric(1,3) + P(-1,1)*P(-1,2)*P(2,3)*Metric(1,3) + P(-1,1)*P(-1,3)*P(1,2)*Metric(2,3) - P(-1,1)*P(-1,2)*P(1,3)*Metric(2,3)')

VVVSSS25 = Lorentz(name = 'VVVSSS25',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = '-(P(1,2)*P(2,3)*P(3,1)) + P(1,3)*P(2,1)*P(3,2) + P(-1,2)*P(-1,3)*P(3,1)*Metric(1,2) - P(-1,1)*P(-1,3)*P(3,2)*Metric(1,2) - P(-1,2)*P(-1,3)*P(2,1)*Metric(1,3) + P(-1,1)*P(-1,2)*P(2,3)*Metric(1,3) + P(-1,1)*P(-1,3)*P(1,2)*Metric(2,3) - P(-1,1)*P(-1,2)*P(1,3)*Metric(2,3)')

VVVSS25 = Lorentz(name = 'VVVSS25',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = '-(P(1,2)*P(2,3)*P(3,1)) + P(1,3)*P(2,1)*P(3,2) + P(-1,2)*P(-1,3)*P(3,1)*Metric(1,2) - P(-1,1)*P(-1,3)*P(3,2)*Metric(1,2) - P(-1,2)*P(-1,3)*P(2,1)*Metric(1,3) + P(-1,1)*P(-1,2)*P(2,3)*Metric(1,3) + P(-1,1)*P(-1,3)*P(1,2)*Metric(2,3) - P(-1,1)*P(-1,2)*P(1,3)*Metric(2,3)')

VVVS19 = Lorentz(name = 'VVVS19',
                 spins = [ 3, 3, 3, 1 ],
                 structure = '-(P(1,2)*P(2,3)*P(3,1)) + P(1,3)*P(2,1)*P(3,2) + P(-1,2)*P(-1,3)*P(3,1)*Metric(1,2) - P(-1,1)*P(-1,3)*P(3,2)*Metric(1,2) - P(-1,2)*P(-1,3)*P(2,1)*Metric(1,3) + P(-1,1)*P(-1,2)*P(2,3)*Metric(1,3) + P(-1,1)*P(-1,3)*P(1,2)*Metric(2,3) - P(-1,1)*P(-1,2)*P(1,3)*Metric(2,3)')

VVVV11 = Lorentz(name = 'VVVV11',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,1)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(3,2)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) - P(2,4)*P(4,1)*Metric(1,3) - P(2,3)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) + P(2,4)*P(3,1)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,1)*P(3,4)*Metric(1,4) - P(1,3)*P(4,1)*Metric(2,3) + P(1,3)*P(4,2)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,2)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) - P(1,4)*P(3,1)*Metric(2,4) - P(1,3)*P(3,2)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(-1,2)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(-1,1)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,1)*Metric(3,4) + P(1,2)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,1)*P(-1,4)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVSS24 = Lorentz(name = 'VVVVSS24',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(3,4)*P(4,1)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(3,2)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) - P(2,4)*P(4,1)*Metric(1,3) - P(2,3)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) + P(2,4)*P(3,1)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,1)*P(3,4)*Metric(1,4) - P(1,3)*P(4,1)*Metric(2,3) + P(1,3)*P(4,2)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,2)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) - P(1,4)*P(3,1)*Metric(2,4) - P(1,3)*P(3,2)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(-1,2)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(-1,1)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,1)*Metric(3,4) + P(1,2)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,1)*P(-1,4)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVS11 = Lorentz(name = 'VVVVS11',
                  spins = [ 3, 3, 3, 3, 1 ],
                  structure = 'P(3,4)*P(4,1)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(3,2)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) - P(2,4)*P(4,1)*Metric(1,3) - P(2,3)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) + P(2,4)*P(3,1)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,1)*P(3,4)*Metric(1,4) - P(1,3)*P(4,1)*Metric(2,3) + P(1,3)*P(4,2)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,2)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) - P(1,4)*P(3,1)*Metric(2,4) - P(1,3)*P(3,2)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(-1,2)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(-1,1)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,1)*Metric(3,4) + P(1,2)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,1)*P(-1,4)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVV12 = Lorentz(name = 'VVVV12',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,2)*P(4,1)*Metric(1,2) - P(3,1)*P(4,2)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) + P(2,1)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) + P(2,4)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) - P(2,1)*P(3,2)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,3)*P(3,4)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) - P(1,3)*P(4,1)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,4)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(-1,3)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,2)*P(3,1)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(1,3)*P(3,4)*Metric(2,4) - P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4) - P(-1,3)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(1,3)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVSS25 = Lorentz(name = 'VVVVSS25',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'P(3,2)*P(4,1)*Metric(1,2) - P(3,1)*P(4,2)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) + P(2,1)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) + P(2,4)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) - P(2,1)*P(3,2)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,3)*P(3,4)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) - P(1,3)*P(4,1)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,4)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(-1,3)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,2)*P(3,1)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(1,3)*P(3,4)*Metric(2,4) - P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4) - P(-1,3)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(1,3)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVS12 = Lorentz(name = 'VVVVS12',
                  spins = [ 3, 3, 3, 3, 1 ],
                  structure = 'P(3,2)*P(4,1)*Metric(1,2) - P(3,1)*P(4,2)*Metric(1,2) + P(3,4)*P(4,2)*Metric(1,2) + P(3,1)*P(4,3)*Metric(1,2) + P(2,3)*P(4,1)*Metric(1,3) + P(2,1)*P(4,2)*Metric(1,3) - P(2,1)*P(4,3)*Metric(1,3) + P(2,4)*P(4,3)*Metric(1,3) - P(2,3)*P(3,1)*Metric(1,4) - P(2,1)*P(3,2)*Metric(1,4) - P(2,4)*P(3,2)*Metric(1,4) - P(2,3)*P(3,4)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) - P(1,3)*P(4,1)*Metric(2,3) - P(1,4)*P(4,2)*Metric(2,3) - P(1,4)*P(4,3)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) + P(-1,1)*P(-1,3)*Metric(1,4)*Metric(2,3) + P(-1,2)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(-1,3)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,2)*P(3,1)*Metric(2,4) + P(1,4)*P(3,2)*Metric(2,4) - P(1,2)*P(3,4)*Metric(2,4) + P(1,3)*P(3,4)*Metric(2,4) - P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4) - P(-1,3)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,3)*P(2,1)*Metric(3,4) + P(1,4)*P(2,3)*Metric(3,4) + P(1,2)*P(2,4)*Metric(3,4) - P(1,3)*P(2,4)*Metric(3,4) - P(-1,1)*P(-1,3)*Metric(1,2)*Metric(3,4) - P(-1,2)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVVV1 = Lorentz(name = 'VVVVV1',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,1)*Metric(1,4)*Metric(2,3) - (P(5,2)*Metric(1,4)*Metric(2,3))/2. - (P(5,3)*Metric(1,4)*Metric(2,3))/2. - P(4,1)*Metric(1,5)*Metric(2,3) + (P(4,2)*Metric(1,5)*Metric(2,3))/2. + (P(4,3)*Metric(1,5)*Metric(2,3))/2. - (P(5,1)*Metric(1,3)*Metric(2,4))/2. + P(5,2)*Metric(1,3)*Metric(2,4) - (P(5,3)*Metric(1,3)*Metric(2,4))/2. + (P(3,1)*Metric(1,5)*Metric(2,4))/2. - (P(3,2)*Metric(1,5)*Metric(2,4))/2. + (P(4,1)*Metric(1,3)*Metric(2,5))/2. - P(4,2)*Metric(1,3)*Metric(2,5) + (P(4,3)*Metric(1,3)*Metric(2,5))/2. - (P(3,1)*Metric(1,4)*Metric(2,5))/2. + (P(3,2)*Metric(1,4)*Metric(2,5))/2. - (P(5,1)*Metric(1,2)*Metric(3,4))/2. - (P(5,2)*Metric(1,2)*Metric(3,4))/2. + P(5,3)*Metric(1,2)*Metric(3,4) + (P(2,1)*Metric(1,5)*Metric(3,4))/2. - (P(2,3)*Metric(1,5)*Metric(3,4))/2. + (P(1,2)*Metric(2,5)*Metric(3,4))/2. - (P(1,3)*Metric(2,5)*Metric(3,4))/2. + (P(4,1)*Metric(1,2)*Metric(3,5))/2. + (P(4,2)*Metric(1,2)*Metric(3,5))/2. - P(4,3)*Metric(1,2)*Metric(3,5) - (P(2,1)*Metric(1,4)*Metric(3,5))/2. + (P(2,3)*Metric(1,4)*Metric(3,5))/2. - (P(1,2)*Metric(2,4)*Metric(3,5))/2. + (P(1,3)*Metric(2,4)*Metric(3,5))/2.')

VVVVVS1 = Lorentz(name = 'VVVVVS1',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'P(5,1)*Metric(1,4)*Metric(2,3) - (P(5,2)*Metric(1,4)*Metric(2,3))/2. - (P(5,3)*Metric(1,4)*Metric(2,3))/2. - P(4,1)*Metric(1,5)*Metric(2,3) + (P(4,2)*Metric(1,5)*Metric(2,3))/2. + (P(4,3)*Metric(1,5)*Metric(2,3))/2. - (P(5,1)*Metric(1,3)*Metric(2,4))/2. + P(5,2)*Metric(1,3)*Metric(2,4) - (P(5,3)*Metric(1,3)*Metric(2,4))/2. + (P(3,1)*Metric(1,5)*Metric(2,4))/2. - (P(3,2)*Metric(1,5)*Metric(2,4))/2. + (P(4,1)*Metric(1,3)*Metric(2,5))/2. - P(4,2)*Metric(1,3)*Metric(2,5) + (P(4,3)*Metric(1,3)*Metric(2,5))/2. - (P(3,1)*Metric(1,4)*Metric(2,5))/2. + (P(3,2)*Metric(1,4)*Metric(2,5))/2. - (P(5,1)*Metric(1,2)*Metric(3,4))/2. - (P(5,2)*Metric(1,2)*Metric(3,4))/2. + P(5,3)*Metric(1,2)*Metric(3,4) + (P(2,1)*Metric(1,5)*Metric(3,4))/2. - (P(2,3)*Metric(1,5)*Metric(3,4))/2. + (P(1,2)*Metric(2,5)*Metric(3,4))/2. - (P(1,3)*Metric(2,5)*Metric(3,4))/2. + (P(4,1)*Metric(1,2)*Metric(3,5))/2. + (P(4,2)*Metric(1,2)*Metric(3,5))/2. - P(4,3)*Metric(1,2)*Metric(3,5) - (P(2,1)*Metric(1,4)*Metric(3,5))/2. + (P(2,3)*Metric(1,4)*Metric(3,5))/2. - (P(1,2)*Metric(2,4)*Metric(3,5))/2. + (P(1,3)*Metric(2,4)*Metric(3,5))/2.')

VVVVV2 = Lorentz(name = 'VVVVV2',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,1)*Metric(1,4)*Metric(2,3) - P(5,2)*Metric(1,4)*Metric(2,3) - P(4,1)*Metric(1,5)*Metric(2,3) + 2*P(4,2)*Metric(1,5)*Metric(2,3) - P(4,5)*Metric(1,5)*Metric(2,3) - P(5,1)*Metric(1,3)*Metric(2,4) + P(5,2)*Metric(1,3)*Metric(2,4) + P(3,1)*Metric(1,5)*Metric(2,4) - 2*P(3,2)*Metric(1,5)*Metric(2,4) + P(3,5)*Metric(1,5)*Metric(2,4) + 2*P(4,1)*Metric(1,3)*Metric(2,5) - P(4,2)*Metric(1,3)*Metric(2,5) - P(4,5)*Metric(1,3)*Metric(2,5) - 2*P(3,1)*Metric(1,4)*Metric(2,5) + P(3,2)*Metric(1,4)*Metric(2,5) + P(3,5)*Metric(1,4)*Metric(2,5) - P(4,1)*Metric(1,2)*Metric(3,5) - P(4,2)*Metric(1,2)*Metric(3,5) + 2*P(4,5)*Metric(1,2)*Metric(3,5) + P(2,1)*Metric(1,4)*Metric(3,5) - P(2,5)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) - P(1,5)*Metric(2,4)*Metric(3,5) + P(3,1)*Metric(1,2)*Metric(4,5) + P(3,2)*Metric(1,2)*Metric(4,5) - 2*P(3,5)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,5)*Metric(1,3)*Metric(4,5) - P(1,2)*Metric(2,3)*Metric(4,5) + P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVVS2 = Lorentz(name = 'VVVVVS2',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'P(5,1)*Metric(1,4)*Metric(2,3) - P(5,2)*Metric(1,4)*Metric(2,3) - P(4,1)*Metric(1,5)*Metric(2,3) + 2*P(4,2)*Metric(1,5)*Metric(2,3) - P(4,5)*Metric(1,5)*Metric(2,3) - P(5,1)*Metric(1,3)*Metric(2,4) + P(5,2)*Metric(1,3)*Metric(2,4) + P(3,1)*Metric(1,5)*Metric(2,4) - 2*P(3,2)*Metric(1,5)*Metric(2,4) + P(3,5)*Metric(1,5)*Metric(2,4) + 2*P(4,1)*Metric(1,3)*Metric(2,5) - P(4,2)*Metric(1,3)*Metric(2,5) - P(4,5)*Metric(1,3)*Metric(2,5) - 2*P(3,1)*Metric(1,4)*Metric(2,5) + P(3,2)*Metric(1,4)*Metric(2,5) + P(3,5)*Metric(1,4)*Metric(2,5) - P(4,1)*Metric(1,2)*Metric(3,5) - P(4,2)*Metric(1,2)*Metric(3,5) + 2*P(4,5)*Metric(1,2)*Metric(3,5) + P(2,1)*Metric(1,4)*Metric(3,5) - P(2,5)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) - P(1,5)*Metric(2,4)*Metric(3,5) + P(3,1)*Metric(1,2)*Metric(4,5) + P(3,2)*Metric(1,2)*Metric(4,5) - 2*P(3,5)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,5)*Metric(1,3)*Metric(4,5) - P(1,2)*Metric(2,3)*Metric(4,5) + P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVV3 = Lorentz(name = 'VVVVV3',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,2)*Metric(1,4)*Metric(2,3) + P(5,3)*Metric(1,4)*Metric(2,3) - 2*P(5,4)*Metric(1,4)*Metric(2,3) + P(4,2)*Metric(1,5)*Metric(2,3) + P(4,3)*Metric(1,5)*Metric(2,3) - 2*P(4,5)*Metric(1,5)*Metric(2,3) - P(5,3)*Metric(1,3)*Metric(2,4) + P(5,4)*Metric(1,3)*Metric(2,4) - P(3,2)*Metric(1,5)*Metric(2,4) + P(3,5)*Metric(1,5)*Metric(2,4) - P(4,3)*Metric(1,3)*Metric(2,5) + P(4,5)*Metric(1,3)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(3,4)*Metric(1,4)*Metric(2,5) - P(5,2)*Metric(1,2)*Metric(3,4) + P(5,4)*Metric(1,2)*Metric(3,4) - P(2,3)*Metric(1,5)*Metric(3,4) + P(2,5)*Metric(1,5)*Metric(3,4) + P(1,2)*Metric(2,5)*Metric(3,4) + P(1,3)*Metric(2,5)*Metric(3,4) - P(1,4)*Metric(2,5)*Metric(3,4) - P(1,5)*Metric(2,5)*Metric(3,4) - P(4,2)*Metric(1,2)*Metric(3,5) + P(4,5)*Metric(1,2)*Metric(3,5) - P(2,3)*Metric(1,4)*Metric(3,5) + P(2,4)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) - P(1,4)*Metric(2,4)*Metric(3,5) - P(1,5)*Metric(2,4)*Metric(3,5) + 2*P(3,2)*Metric(1,2)*Metric(4,5) - P(3,4)*Metric(1,2)*Metric(4,5) - P(3,5)*Metric(1,2)*Metric(4,5) + 2*P(2,3)*Metric(1,3)*Metric(4,5) - P(2,4)*Metric(1,3)*Metric(4,5) - P(2,5)*Metric(1,3)*Metric(4,5) - 2*P(1,2)*Metric(2,3)*Metric(4,5) - 2*P(1,3)*Metric(2,3)*Metric(4,5) + 2*P(1,4)*Metric(2,3)*Metric(4,5) + 2*P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVVS3 = Lorentz(name = 'VVVVVS3',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'P(5,2)*Metric(1,4)*Metric(2,3) + P(5,3)*Metric(1,4)*Metric(2,3) - 2*P(5,4)*Metric(1,4)*Metric(2,3) + P(4,2)*Metric(1,5)*Metric(2,3) + P(4,3)*Metric(1,5)*Metric(2,3) - 2*P(4,5)*Metric(1,5)*Metric(2,3) - P(5,3)*Metric(1,3)*Metric(2,4) + P(5,4)*Metric(1,3)*Metric(2,4) - P(3,2)*Metric(1,5)*Metric(2,4) + P(3,5)*Metric(1,5)*Metric(2,4) - P(4,3)*Metric(1,3)*Metric(2,5) + P(4,5)*Metric(1,3)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(3,4)*Metric(1,4)*Metric(2,5) - P(5,2)*Metric(1,2)*Metric(3,4) + P(5,4)*Metric(1,2)*Metric(3,4) - P(2,3)*Metric(1,5)*Metric(3,4) + P(2,5)*Metric(1,5)*Metric(3,4) + P(1,2)*Metric(2,5)*Metric(3,4) + P(1,3)*Metric(2,5)*Metric(3,4) - P(1,4)*Metric(2,5)*Metric(3,4) - P(1,5)*Metric(2,5)*Metric(3,4) - P(4,2)*Metric(1,2)*Metric(3,5) + P(4,5)*Metric(1,2)*Metric(3,5) - P(2,3)*Metric(1,4)*Metric(3,5) + P(2,4)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) - P(1,4)*Metric(2,4)*Metric(3,5) - P(1,5)*Metric(2,4)*Metric(3,5) + 2*P(3,2)*Metric(1,2)*Metric(4,5) - P(3,4)*Metric(1,2)*Metric(4,5) - P(3,5)*Metric(1,2)*Metric(4,5) + 2*P(2,3)*Metric(1,3)*Metric(4,5) - P(2,4)*Metric(1,3)*Metric(4,5) - P(2,5)*Metric(1,3)*Metric(4,5) - 2*P(1,2)*Metric(2,3)*Metric(4,5) - 2*P(1,3)*Metric(2,3)*Metric(4,5) + 2*P(1,4)*Metric(2,3)*Metric(4,5) + 2*P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVVV1 = Lorentz(name = 'VVVVVV1',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) + Metric(1,5)*Metric(2,6)*Metric(3,4) - (Metric(1,6)*Metric(2,4)*Metric(3,5))/2. - (Metric(1,4)*Metric(2,6)*Metric(3,5))/2. - (Metric(1,5)*Metric(2,4)*Metric(3,6))/2. - (Metric(1,4)*Metric(2,5)*Metric(3,6))/2. - (Metric(1,6)*Metric(2,3)*Metric(4,5))/2. - (Metric(1,3)*Metric(2,6)*Metric(4,5))/2. + Metric(1,2)*Metric(3,6)*Metric(4,5) - (Metric(1,5)*Metric(2,3)*Metric(4,6))/2. - (Metric(1,3)*Metric(2,5)*Metric(4,6))/2. + Metric(1,2)*Metric(3,5)*Metric(4,6) + Metric(1,4)*Metric(2,3)*Metric(5,6) + Metric(1,3)*Metric(2,4)*Metric(5,6) - 2*Metric(1,2)*Metric(3,4)*Metric(5,6)')

VVVVV4 = Lorentz(name = 'VVVVV4',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,1)*Metric(1,3)*Metric(2,4) - P(5,4)*Metric(1,3)*Metric(2,4) - P(3,1)*Metric(1,5)*Metric(2,4) + 2*P(3,4)*Metric(1,5)*Metric(2,4) - P(3,5)*Metric(1,5)*Metric(2,4) + P(4,1)*Metric(1,3)*Metric(2,5) - P(4,5)*Metric(1,3)*Metric(2,5) - P(3,1)*Metric(1,4)*Metric(2,5) - P(3,4)*Metric(1,4)*Metric(2,5) + 2*P(3,5)*Metric(1,4)*Metric(2,5) - P(5,1)*Metric(1,2)*Metric(3,4) + P(5,4)*Metric(1,2)*Metric(3,4) + P(2,1)*Metric(1,5)*Metric(3,4) - 2*P(2,4)*Metric(1,5)*Metric(3,4) + P(2,5)*Metric(1,5)*Metric(3,4) + P(1,4)*Metric(2,5)*Metric(3,4) - P(1,5)*Metric(2,5)*Metric(3,4) - P(4,1)*Metric(1,2)*Metric(3,5) + P(4,5)*Metric(1,2)*Metric(3,5) + P(2,1)*Metric(1,4)*Metric(3,5) + P(2,4)*Metric(1,4)*Metric(3,5) - 2*P(2,5)*Metric(1,4)*Metric(3,5) - P(1,4)*Metric(2,4)*Metric(3,5) + P(1,5)*Metric(2,4)*Metric(3,5) + 2*P(3,1)*Metric(1,2)*Metric(4,5) - P(3,4)*Metric(1,2)*Metric(4,5) - P(3,5)*Metric(1,2)*Metric(4,5) - 2*P(2,1)*Metric(1,3)*Metric(4,5) + P(2,4)*Metric(1,3)*Metric(4,5) + P(2,5)*Metric(1,3)*Metric(4,5)')

VVVVVS4 = Lorentz(name = 'VVVVVS4',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'P(5,1)*Metric(1,3)*Metric(2,4) - P(5,4)*Metric(1,3)*Metric(2,4) - P(3,1)*Metric(1,5)*Metric(2,4) + 2*P(3,4)*Metric(1,5)*Metric(2,4) - P(3,5)*Metric(1,5)*Metric(2,4) + P(4,1)*Metric(1,3)*Metric(2,5) - P(4,5)*Metric(1,3)*Metric(2,5) - P(3,1)*Metric(1,4)*Metric(2,5) - P(3,4)*Metric(1,4)*Metric(2,5) + 2*P(3,5)*Metric(1,4)*Metric(2,5) - P(5,1)*Metric(1,2)*Metric(3,4) + P(5,4)*Metric(1,2)*Metric(3,4) + P(2,1)*Metric(1,5)*Metric(3,4) - 2*P(2,4)*Metric(1,5)*Metric(3,4) + P(2,5)*Metric(1,5)*Metric(3,4) + P(1,4)*Metric(2,5)*Metric(3,4) - P(1,5)*Metric(2,5)*Metric(3,4) - P(4,1)*Metric(1,2)*Metric(3,5) + P(4,5)*Metric(1,2)*Metric(3,5) + P(2,1)*Metric(1,4)*Metric(3,5) + P(2,4)*Metric(1,4)*Metric(3,5) - 2*P(2,5)*Metric(1,4)*Metric(3,5) - P(1,4)*Metric(2,4)*Metric(3,5) + P(1,5)*Metric(2,4)*Metric(3,5) + 2*P(3,1)*Metric(1,2)*Metric(4,5) - P(3,4)*Metric(1,2)*Metric(4,5) - P(3,5)*Metric(1,2)*Metric(4,5) - 2*P(2,1)*Metric(1,3)*Metric(4,5) + P(2,4)*Metric(1,3)*Metric(4,5) + P(2,5)*Metric(1,3)*Metric(4,5)')

VVVVV5 = Lorentz(name = 'VVVVV5',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,1)*Metric(1,4)*Metric(2,3) + P(5,2)*Metric(1,4)*Metric(2,3) - P(5,3)*Metric(1,4)*Metric(2,3) - P(5,4)*Metric(1,4)*Metric(2,3) - P(4,1)*Metric(1,5)*Metric(2,3) + P(4,3)*Metric(1,5)*Metric(2,3) + P(5,1)*Metric(1,3)*Metric(2,4) + P(5,2)*Metric(1,3)*Metric(2,4) - P(5,3)*Metric(1,3)*Metric(2,4) - P(5,4)*Metric(1,3)*Metric(2,4) - P(3,1)*Metric(1,5)*Metric(2,4) + P(3,4)*Metric(1,5)*Metric(2,4) - P(4,2)*Metric(1,3)*Metric(2,5) + P(4,3)*Metric(1,3)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(3,4)*Metric(1,4)*Metric(2,5) - 2*P(5,1)*Metric(1,2)*Metric(3,4) - 2*P(5,2)*Metric(1,2)*Metric(3,4) + 2*P(5,3)*Metric(1,2)*Metric(3,4) + 2*P(5,4)*Metric(1,2)*Metric(3,4) + 2*P(2,1)*Metric(1,5)*Metric(3,4) - P(2,3)*Metric(1,5)*Metric(3,4) - P(2,4)*Metric(1,5)*Metric(3,4) + 2*P(1,2)*Metric(2,5)*Metric(3,4) - P(1,3)*Metric(2,5)*Metric(3,4) - P(1,4)*Metric(2,5)*Metric(3,4) + P(4,1)*Metric(1,2)*Metric(3,5) + P(4,2)*Metric(1,2)*Metric(3,5) - 2*P(4,3)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5) + P(2,3)*Metric(1,4)*Metric(3,5) - P(1,2)*Metric(2,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) + P(3,1)*Metric(1,2)*Metric(4,5) + P(3,2)*Metric(1,2)*Metric(4,5) - 2*P(3,4)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,4)*Metric(1,3)*Metric(4,5) - P(1,2)*Metric(2,3)*Metric(4,5) + P(1,4)*Metric(2,3)*Metric(4,5)')

VVVVVS5 = Lorentz(name = 'VVVVVS5',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'P(5,1)*Metric(1,4)*Metric(2,3) + P(5,2)*Metric(1,4)*Metric(2,3) - P(5,3)*Metric(1,4)*Metric(2,3) - P(5,4)*Metric(1,4)*Metric(2,3) - P(4,1)*Metric(1,5)*Metric(2,3) + P(4,3)*Metric(1,5)*Metric(2,3) + P(5,1)*Metric(1,3)*Metric(2,4) + P(5,2)*Metric(1,3)*Metric(2,4) - P(5,3)*Metric(1,3)*Metric(2,4) - P(5,4)*Metric(1,3)*Metric(2,4) - P(3,1)*Metric(1,5)*Metric(2,4) + P(3,4)*Metric(1,5)*Metric(2,4) - P(4,2)*Metric(1,3)*Metric(2,5) + P(4,3)*Metric(1,3)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(3,4)*Metric(1,4)*Metric(2,5) - 2*P(5,1)*Metric(1,2)*Metric(3,4) - 2*P(5,2)*Metric(1,2)*Metric(3,4) + 2*P(5,3)*Metric(1,2)*Metric(3,4) + 2*P(5,4)*Metric(1,2)*Metric(3,4) + 2*P(2,1)*Metric(1,5)*Metric(3,4) - P(2,3)*Metric(1,5)*Metric(3,4) - P(2,4)*Metric(1,5)*Metric(3,4) + 2*P(1,2)*Metric(2,5)*Metric(3,4) - P(1,3)*Metric(2,5)*Metric(3,4) - P(1,4)*Metric(2,5)*Metric(3,4) + P(4,1)*Metric(1,2)*Metric(3,5) + P(4,2)*Metric(1,2)*Metric(3,5) - 2*P(4,3)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5) + P(2,3)*Metric(1,4)*Metric(3,5) - P(1,2)*Metric(2,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) + P(3,1)*Metric(1,2)*Metric(4,5) + P(3,2)*Metric(1,2)*Metric(4,5) - 2*P(3,4)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,4)*Metric(1,3)*Metric(4,5) - P(1,2)*Metric(2,3)*Metric(4,5) + P(1,4)*Metric(2,3)*Metric(4,5)')

VVVVVV2 = Lorentz(name = 'VVVVVV2',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - (Metric(1,5)*Metric(2,6)*Metric(3,4))/2. + Metric(1,6)*Metric(2,4)*Metric(3,5) - (Metric(1,4)*Metric(2,6)*Metric(3,5))/2. - (Metric(1,5)*Metric(2,4)*Metric(3,6))/2. - (Metric(1,4)*Metric(2,5)*Metric(3,6))/2. - 2*Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,3)*Metric(2,6)*Metric(4,5) + Metric(1,2)*Metric(3,6)*Metric(4,5) + Metric(1,5)*Metric(2,3)*Metric(4,6) - (Metric(1,3)*Metric(2,5)*Metric(4,6))/2. - (Metric(1,2)*Metric(3,5)*Metric(4,6))/2. + Metric(1,4)*Metric(2,3)*Metric(5,6) - (Metric(1,3)*Metric(2,4)*Metric(5,6))/2. - (Metric(1,2)*Metric(3,4)*Metric(5,6))/2.')

VVVVV6 = Lorentz(name = 'VVVVV6',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,3)*Metric(1,4)*Metric(2,3) - P(5,4)*Metric(1,4)*Metric(2,3) + P(4,3)*Metric(1,5)*Metric(2,3) - P(4,5)*Metric(1,5)*Metric(2,3) - P(5,3)*Metric(1,3)*Metric(2,4) + P(5,4)*Metric(1,3)*Metric(2,4) + P(3,4)*Metric(1,5)*Metric(2,4) - P(3,5)*Metric(1,5)*Metric(2,4) - P(4,3)*Metric(1,3)*Metric(2,5) + P(4,5)*Metric(1,3)*Metric(2,5) - P(3,4)*Metric(1,4)*Metric(2,5) + P(3,5)*Metric(1,4)*Metric(2,5) - P(2,3)*Metric(1,5)*Metric(3,4) - P(2,4)*Metric(1,5)*Metric(3,4) + 2*P(2,5)*Metric(1,5)*Metric(3,4) + P(1,3)*Metric(2,5)*Metric(3,4) + P(1,4)*Metric(2,5)*Metric(3,4) - 2*P(1,5)*Metric(2,5)*Metric(3,4) - P(2,3)*Metric(1,4)*Metric(3,5) + 2*P(2,4)*Metric(1,4)*Metric(3,5) - P(2,5)*Metric(1,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) - 2*P(1,4)*Metric(2,4)*Metric(3,5) + P(1,5)*Metric(2,4)*Metric(3,5) + 2*P(2,3)*Metric(1,3)*Metric(4,5) - P(2,4)*Metric(1,3)*Metric(4,5) - P(2,5)*Metric(1,3)*Metric(4,5) - 2*P(1,3)*Metric(2,3)*Metric(4,5) + P(1,4)*Metric(2,3)*Metric(4,5) + P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVVS6 = Lorentz(name = 'VVVVVS6',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'P(5,3)*Metric(1,4)*Metric(2,3) - P(5,4)*Metric(1,4)*Metric(2,3) + P(4,3)*Metric(1,5)*Metric(2,3) - P(4,5)*Metric(1,5)*Metric(2,3) - P(5,3)*Metric(1,3)*Metric(2,4) + P(5,4)*Metric(1,3)*Metric(2,4) + P(3,4)*Metric(1,5)*Metric(2,4) - P(3,5)*Metric(1,5)*Metric(2,4) - P(4,3)*Metric(1,3)*Metric(2,5) + P(4,5)*Metric(1,3)*Metric(2,5) - P(3,4)*Metric(1,4)*Metric(2,5) + P(3,5)*Metric(1,4)*Metric(2,5) - P(2,3)*Metric(1,5)*Metric(3,4) - P(2,4)*Metric(1,5)*Metric(3,4) + 2*P(2,5)*Metric(1,5)*Metric(3,4) + P(1,3)*Metric(2,5)*Metric(3,4) + P(1,4)*Metric(2,5)*Metric(3,4) - 2*P(1,5)*Metric(2,5)*Metric(3,4) - P(2,3)*Metric(1,4)*Metric(3,5) + 2*P(2,4)*Metric(1,4)*Metric(3,5) - P(2,5)*Metric(1,4)*Metric(3,5) + P(1,3)*Metric(2,4)*Metric(3,5) - 2*P(1,4)*Metric(2,4)*Metric(3,5) + P(1,5)*Metric(2,4)*Metric(3,5) + 2*P(2,3)*Metric(1,3)*Metric(4,5) - P(2,4)*Metric(1,3)*Metric(4,5) - P(2,5)*Metric(1,3)*Metric(4,5) - 2*P(1,3)*Metric(2,3)*Metric(4,5) + P(1,4)*Metric(2,3)*Metric(4,5) + P(1,5)*Metric(2,3)*Metric(4,5)')

VVV14 = Lorentz(name = 'VVV14',
                spins = [ 3, 3, 3 ],
                structure = '-(Epsilon(1,2,3,-2)*P(-2,3)*P(-1,1)*P(-1,2)) - Epsilon(1,2,3,-2)*P(-2,2)*P(-1,1)*P(-1,3) - Epsilon(1,2,3,-2)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*P(1,2) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*P(1,3) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*P(2,1) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*P(2,3) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*P(3,1) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*P(3,2) - (Epsilon(3,-1,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*Metric(1,2))/2. + (Epsilon(3,-1,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*Metric(1,2))/2. + (Epsilon(2,-1,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*Metric(1,3))/2. - (Epsilon(1,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(2,3))/2. + (Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*Metric(2,3))/2.')

VVVSSS26 = Lorentz(name = 'VVVSSS26',
                   spins = [ 3, 3, 3, 1, 1, 1 ],
                   structure = '-(Epsilon(1,2,3,-2)*P(-2,3)*P(-1,1)*P(-1,2)) - Epsilon(1,2,3,-2)*P(-2,2)*P(-1,1)*P(-1,3) - Epsilon(1,2,3,-2)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*P(1,2) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*P(1,3) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*P(2,1) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*P(2,3) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*P(3,1) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*P(3,2) - (Epsilon(3,-1,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*Metric(1,2))/2. + (Epsilon(3,-1,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*Metric(1,2))/2. + (Epsilon(2,-1,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*Metric(1,3))/2. - (Epsilon(1,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(2,3))/2. + (Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*Metric(2,3))/2.')

VVVSS26 = Lorentz(name = 'VVVSS26',
                  spins = [ 3, 3, 3, 1, 1 ],
                  structure = '-(Epsilon(1,2,3,-2)*P(-2,3)*P(-1,1)*P(-1,2)) - Epsilon(1,2,3,-2)*P(-2,2)*P(-1,1)*P(-1,3) - Epsilon(1,2,3,-2)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*P(1,2) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*P(1,3) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*P(2,1) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*P(2,3) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*P(3,1) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*P(3,2) - (Epsilon(3,-1,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*Metric(1,2))/2. + (Epsilon(3,-1,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*Metric(1,2))/2. + (Epsilon(2,-1,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*Metric(1,3))/2. - (Epsilon(1,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(2,3))/2. + (Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*Metric(2,3))/2.')

VVVS20 = Lorentz(name = 'VVVS20',
                 spins = [ 3, 3, 3, 1 ],
                 structure = '-(Epsilon(1,2,3,-2)*P(-2,3)*P(-1,1)*P(-1,2)) - Epsilon(1,2,3,-2)*P(-2,2)*P(-1,1)*P(-1,3) - Epsilon(1,2,3,-2)*P(-2,1)*P(-1,2)*P(-1,3) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*P(1,2) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*P(1,3) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*P(2,1) + Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*P(2,3) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*P(3,1) - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*P(3,2) - (Epsilon(3,-1,-2,-3)*P(-3,2)*P(-2,1)*P(-1,3)*Metric(1,2))/2. + (Epsilon(3,-1,-2,-3)*P(-3,1)*P(-2,2)*P(-1,3)*Metric(1,2))/2. + (Epsilon(2,-1,-2,-3)*P(-3,3)*P(-2,1)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,-1,-2,-3)*P(-3,1)*P(-2,3)*P(-1,2)*Metric(1,3))/2. - (Epsilon(1,-1,-2,-3)*P(-3,3)*P(-2,2)*P(-1,1)*Metric(2,3))/2. + (Epsilon(1,-1,-2,-3)*P(-3,2)*P(-2,3)*P(-1,1)*Metric(2,3))/2.')

VVVV13 = Lorentz(name = 'VVVV13',
                 spins = [ 3, 3, 3, 3 ],
                 structure = '-(Epsilon(1,2,3,4)*P(-1,1)*P(-1,3)) + Epsilon(1,2,3,4)*P(-1,2)*P(-1,3) + Epsilon(1,2,3,4)*P(-1,1)*P(-1,4) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,2)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,4) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,1)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,4)*P(3,1) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,3)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,3) - Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,2) + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3))/2. + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(1,3) - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,3))/2. - Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,3) + (Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,4))/2. + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,4) - (Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,4))/2. + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3) + (Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,3))/2. - Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,3) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(2,4) + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4))/2. - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,4) - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,4))/2. - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4)')

VVVVSS26 = Lorentz(name = 'VVVVSS26',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = '-(Epsilon(1,2,3,4)*P(-1,1)*P(-1,3)) + Epsilon(1,2,3,4)*P(-1,2)*P(-1,3) + Epsilon(1,2,3,4)*P(-1,1)*P(-1,4) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,2)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,4) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,1)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,4)*P(3,1) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,3)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,3) - Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,2) + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3))/2. + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(1,3) - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,3))/2. - Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,3) + (Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,4))/2. + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,4) - (Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,4))/2. + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3) + (Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,3))/2. - Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,3) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(2,4) + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4))/2. - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,4) - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,4))/2. - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4)')

VVVVS13 = Lorentz(name = 'VVVVS13',
                  spins = [ 3, 3, 3, 3, 1 ],
                  structure = '-(Epsilon(1,2,3,4)*P(-1,1)*P(-1,3)) + Epsilon(1,2,3,4)*P(-1,2)*P(-1,3) + Epsilon(1,2,3,4)*P(-1,1)*P(-1,4) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,2)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,4) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,1)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,4)*P(3,1) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,3)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,3) - Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,2) - Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,2) + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3))/2. + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(1,3) - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,3))/2. - Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,3) + (Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(1,4))/2. + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,4) - (Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,4)*Metric(1,4))/2. + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3) + (Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,2)*Metric(2,3))/2. - (Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,3))/2. - Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,3) + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,1)*Metric(2,4) + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4))/2. - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,3)*Metric(2,4) - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,4))/2. - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4) - Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,2)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4)')

VVVV14 = Lorentz(name = 'VVVV14',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'Epsilon(1,2,3,4)*P(-1,1)*P(-1,2) - Epsilon(1,2,3,4)*P(-1,1)*P(-1,3) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) + Epsilon(1,2,3,4)*P(-1,3)*P(-1,4) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,4)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,3)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,2)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,4) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,1)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,3) + (Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,2))/2. - Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,2) + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3))/2. - Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,3) - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,3))/2. + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(1,3) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(1,4) + Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(2,3) - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,4) + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4))/2. + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(2,4) - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,4))/2. - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4) + (Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,3)*Metric(3,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,4)*Metric(3,4))/2.')

VVVVSS27 = Lorentz(name = 'VVVVSS27',
                   spins = [ 3, 3, 3, 3, 1, 1 ],
                   structure = 'Epsilon(1,2,3,4)*P(-1,1)*P(-1,2) - Epsilon(1,2,3,4)*P(-1,1)*P(-1,3) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) + Epsilon(1,2,3,4)*P(-1,3)*P(-1,4) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,4)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,3)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,2)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,4) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,1)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,3) + (Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,2))/2. - Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,2) + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3))/2. - Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,3) - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,3))/2. + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(1,3) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(1,4) + Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(2,3) - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,4) + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4))/2. + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(2,4) - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,4))/2. - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4) + (Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,3)*Metric(3,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,4)*Metric(3,4))/2.')

VVVVS14 = Lorentz(name = 'VVVVS14',
                  spins = [ 3, 3, 3, 3, 1 ],
                  structure = 'Epsilon(1,2,3,4)*P(-1,1)*P(-1,2) - Epsilon(1,2,3,4)*P(-1,1)*P(-1,3) - Epsilon(1,2,3,4)*P(-1,2)*P(-1,4) + Epsilon(1,2,3,4)*P(-1,3)*P(-1,4) + Epsilon(2,3,4,-1)*P(-1,1)*P(1,2) + Epsilon(2,3,4,-1)*P(-1,4)*P(1,2) - Epsilon(2,3,4,-1)*P(-1,1)*P(1,3) - Epsilon(2,3,4,-1)*P(-1,4)*P(1,3) + Epsilon(2,3,4,-1)*P(-1,2)*P(1,4) - Epsilon(2,3,4,-1)*P(-1,3)*P(1,4) - Epsilon(1,3,4,-1)*P(-1,2)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,3)*P(2,1) - Epsilon(1,3,4,-1)*P(-1,1)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,4)*P(2,3) + Epsilon(1,3,4,-1)*P(-1,2)*P(2,4) + Epsilon(1,3,4,-1)*P(-1,3)*P(2,4) - Epsilon(1,2,4,-1)*P(-1,2)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,3)*P(3,1) - Epsilon(1,2,4,-1)*P(-1,1)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,4)*P(3,2) + Epsilon(1,2,4,-1)*P(-1,2)*P(3,4) + Epsilon(1,2,4,-1)*P(-1,3)*P(3,4) + Epsilon(1,2,3,-1)*P(-1,2)*P(4,1) - Epsilon(1,2,3,-1)*P(-1,3)*P(4,1) + Epsilon(1,2,3,-1)*P(-1,1)*P(4,2) + Epsilon(1,2,3,-1)*P(-1,4)*P(4,2) - Epsilon(1,2,3,-1)*P(-1,1)*P(4,3) - Epsilon(1,2,3,-1)*P(-1,4)*P(4,3) + (Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(1,2))/2. - (Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,2))/2. - Epsilon(3,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,2) + Epsilon(3,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(1,2) + (Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(1,3))/2. - Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,3) - (Epsilon(2,4,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,3))/2. + Epsilon(2,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(1,3) + Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,2)*Metric(1,4) + Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,1)*P(-1,3)*Metric(1,4) - Epsilon(2,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(1,4) + Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,3) + Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,1)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,3) - Epsilon(1,4,-1,-2)*P(-2,3)*P(-1,4)*Metric(2,3) - Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,1)*Metric(2,4) + (Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,2)*Metric(2,4))/2. + Epsilon(1,3,-1,-2)*P(-2,4)*P(-1,3)*Metric(2,4) - (Epsilon(1,3,-1,-2)*P(-2,2)*P(-1,4)*Metric(2,4))/2. - Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,1)*Metric(3,4) + Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,2)*Metric(3,4) + (Epsilon(1,2,-1,-2)*P(-2,4)*P(-1,3)*Metric(3,4))/2. - (Epsilon(1,2,-1,-2)*P(-2,3)*P(-1,4)*Metric(3,4))/2.')

VVVVV7 = Lorentz(name = 'VVVVV7',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'Epsilon(2,3,4,5)*P(1,2) - Epsilon(2,3,4,5)*P(1,3) + Epsilon(1,3,4,5)*P(2,1) - Epsilon(1,3,4,5)*P(2,3) + Epsilon(1,2,4,5)*P(3,1) - Epsilon(1,2,4,5)*P(3,2) + Epsilon(3,4,5,-1)*P(-1,1)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,2)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,3)*Metric(1,2) + Epsilon(2,4,5,-1)*P(-1,1)*Metric(1,3) + Epsilon(2,4,5,-1)*P(-1,2)*Metric(1,3) + Epsilon(2,4,5,-1)*P(-1,3)*Metric(1,3) - (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. + (Epsilon(2,3,4,-1)*P(-1,2)*Metric(1,5))/2. - (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. + Epsilon(1,4,5,-1)*P(-1,1)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,2)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,3)*Metric(2,3) - (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. + (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. + (Epsilon(1,3,4,-1)*P(-1,1)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. - (Epsilon(1,2,5,-1)*P(-1,1)*Metric(3,4))/2. + (Epsilon(1,2,5,-1)*P(-1,2)*Metric(3,4))/2. + (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. - (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2.')

VVVVVS7 = Lorentz(name = 'VVVVVS7',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'Epsilon(2,3,4,5)*P(1,2) - Epsilon(2,3,4,5)*P(1,3) + Epsilon(1,3,4,5)*P(2,1) - Epsilon(1,3,4,5)*P(2,3) + Epsilon(1,2,4,5)*P(3,1) - Epsilon(1,2,4,5)*P(3,2) + Epsilon(3,4,5,-1)*P(-1,1)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,2)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,3)*Metric(1,2) + Epsilon(2,4,5,-1)*P(-1,1)*Metric(1,3) + Epsilon(2,4,5,-1)*P(-1,2)*Metric(1,3) + Epsilon(2,4,5,-1)*P(-1,3)*Metric(1,3) - (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. + (Epsilon(2,3,4,-1)*P(-1,2)*Metric(1,5))/2. - (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. + Epsilon(1,4,5,-1)*P(-1,1)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,2)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,3)*Metric(2,3) - (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. + (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. + (Epsilon(1,3,4,-1)*P(-1,1)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. - (Epsilon(1,2,5,-1)*P(-1,1)*Metric(3,4))/2. + (Epsilon(1,2,5,-1)*P(-1,2)*Metric(3,4))/2. + (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. - (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2.')

VVVVV8 = Lorentz(name = 'VVVVV8',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'Epsilon(2,3,4,5)*P(1,2) - Epsilon(2,3,4,5)*P(1,5) + Epsilon(1,3,4,5)*P(2,1) - Epsilon(1,3,4,5)*P(2,5) + Epsilon(1,2,3,4)*P(5,1) - Epsilon(1,2,3,4)*P(5,2) + Epsilon(3,4,5,-1)*P(-1,1)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,2)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,5)*Metric(1,2) + (Epsilon(2,4,5,-1)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. - (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,5)*Metric(1,4))/2. + Epsilon(2,3,4,-1)*P(-1,1)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,2)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,5)*Metric(1,5) + (Epsilon(1,4,5,-1)*P(-1,1)*Metric(2,3))/2. - (Epsilon(1,4,5,-1)*P(-1,5)*Metric(2,3))/2. - (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. + (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. + Epsilon(1,3,4,-1)*P(-1,1)*Metric(2,5) + Epsilon(1,3,4,-1)*P(-1,2)*Metric(2,5) + Epsilon(1,3,4,-1)*P(-1,5)*Metric(2,5) - (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. + (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2. + (Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5))/2. - (Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5))/2.')

VVVVVS8 = Lorentz(name = 'VVVVVS8',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = 'Epsilon(2,3,4,5)*P(1,2) - Epsilon(2,3,4,5)*P(1,5) + Epsilon(1,3,4,5)*P(2,1) - Epsilon(1,3,4,5)*P(2,5) + Epsilon(1,2,3,4)*P(5,1) - Epsilon(1,2,3,4)*P(5,2) + Epsilon(3,4,5,-1)*P(-1,1)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,2)*Metric(1,2) + Epsilon(3,4,5,-1)*P(-1,5)*Metric(1,2) + (Epsilon(2,4,5,-1)*P(-1,2)*Metric(1,3))/2. - (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. - (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,5)*Metric(1,4))/2. + Epsilon(2,3,4,-1)*P(-1,1)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,2)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,5)*Metric(1,5) + (Epsilon(1,4,5,-1)*P(-1,1)*Metric(2,3))/2. - (Epsilon(1,4,5,-1)*P(-1,5)*Metric(2,3))/2. - (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. + (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. + Epsilon(1,3,4,-1)*P(-1,1)*Metric(2,5) + Epsilon(1,3,4,-1)*P(-1,2)*Metric(2,5) + Epsilon(1,3,4,-1)*P(-1,5)*Metric(2,5) - (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. + (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2. + (Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5))/2. - (Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5))/2.')

VVVVV9 = Lorentz(name = 'VVVVV9',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = '-(Epsilon(1,3,4,5)*P(2,4)) + Epsilon(1,3,4,5)*P(2,5) - Epsilon(1,2,4,5)*P(3,4) + Epsilon(1,2,4,5)*P(3,5) + Epsilon(1,2,3,5)*P(4,2) - Epsilon(1,2,3,5)*P(4,3) + Epsilon(1,2,3,4)*P(5,2) - Epsilon(1,2,3,4)*P(5,3) + (Epsilon(3,4,5,-1)*P(-1,4)*Metric(1,2))/2. - (Epsilon(3,4,5,-1)*P(-1,5)*Metric(1,2))/2. + (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. - (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. - (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. - (Epsilon(2,3,4,-1)*P(-1,2)*Metric(1,5))/2. + (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. - Epsilon(1,4,5,-1)*P(-1,4)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,5)*Metric(2,3) - Epsilon(1,3,5,-1)*P(-1,2)*Metric(2,4) - (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. - Epsilon(1,3,5,-1)*P(-1,4)*Metric(2,4) - (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. - Epsilon(1,3,4,-1)*P(-1,2)*Metric(2,5) - (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. - Epsilon(1,3,4,-1)*P(-1,5)*Metric(2,5) - (Epsilon(1,2,5,-1)*P(-1,2)*Metric(3,4))/2. - Epsilon(1,2,5,-1)*P(-1,3)*Metric(3,4) - Epsilon(1,2,5,-1)*P(-1,4)*Metric(3,4) - (Epsilon(1,2,5,-1)*P(-1,5)*Metric(3,4))/2. - (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2. - Epsilon(1,2,4,-1)*P(-1,3)*Metric(3,5) - (Epsilon(1,2,4,-1)*P(-1,4)*Metric(3,5))/2. - Epsilon(1,2,4,-1)*P(-1,5)*Metric(3,5) + Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5) - Epsilon(1,2,3,-1)*P(-1,3)*Metric(4,5)')

VVVVVS9 = Lorentz(name = 'VVVVVS9',
                  spins = [ 3, 3, 3, 3, 3, 1 ],
                  structure = '-(Epsilon(1,3,4,5)*P(2,4)) + Epsilon(1,3,4,5)*P(2,5) - Epsilon(1,2,4,5)*P(3,4) + Epsilon(1,2,4,5)*P(3,5) + Epsilon(1,2,3,5)*P(4,2) - Epsilon(1,2,3,5)*P(4,3) + Epsilon(1,2,3,4)*P(5,2) - Epsilon(1,2,3,4)*P(5,3) + (Epsilon(3,4,5,-1)*P(-1,4)*Metric(1,2))/2. - (Epsilon(3,4,5,-1)*P(-1,5)*Metric(1,2))/2. + (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. - (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. - (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. - (Epsilon(2,3,4,-1)*P(-1,2)*Metric(1,5))/2. + (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. - Epsilon(1,4,5,-1)*P(-1,4)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,5)*Metric(2,3) - Epsilon(1,3,5,-1)*P(-1,2)*Metric(2,4) - (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. - Epsilon(1,3,5,-1)*P(-1,4)*Metric(2,4) - (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. - Epsilon(1,3,4,-1)*P(-1,2)*Metric(2,5) - (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. - Epsilon(1,3,4,-1)*P(-1,5)*Metric(2,5) - (Epsilon(1,2,5,-1)*P(-1,2)*Metric(3,4))/2. - Epsilon(1,2,5,-1)*P(-1,3)*Metric(3,4) - Epsilon(1,2,5,-1)*P(-1,4)*Metric(3,4) - (Epsilon(1,2,5,-1)*P(-1,5)*Metric(3,4))/2. - (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2. - Epsilon(1,2,4,-1)*P(-1,3)*Metric(3,5) - (Epsilon(1,2,4,-1)*P(-1,4)*Metric(3,5))/2. - Epsilon(1,2,4,-1)*P(-1,5)*Metric(3,5) + Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5) - Epsilon(1,2,3,-1)*P(-1,3)*Metric(4,5)')

VVVVV10 = Lorentz(name = 'VVVVV10',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'Epsilon(2,3,4,5)*P(1,4) - Epsilon(2,3,4,5)*P(1,5) + Epsilon(1,2,3,5)*P(4,1) - Epsilon(1,2,3,5)*P(4,5) + Epsilon(1,2,3,4)*P(5,1) - Epsilon(1,2,3,4)*P(5,4) - (Epsilon(3,4,5,-1)*P(-1,4)*Metric(1,2))/2. + (Epsilon(3,4,5,-1)*P(-1,5)*Metric(1,2))/2. + (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. - (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. + Epsilon(2,3,5,-1)*P(-1,1)*Metric(1,4) + Epsilon(2,3,5,-1)*P(-1,4)*Metric(1,4) + Epsilon(2,3,5,-1)*P(-1,5)*Metric(1,4) + Epsilon(2,3,4,-1)*P(-1,1)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,4)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,5)*Metric(1,5) + (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. - (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. + (Epsilon(1,3,4,-1)*P(-1,1)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. - (Epsilon(1,2,5,-1)*P(-1,1)*Metric(3,4))/2. + (Epsilon(1,2,5,-1)*P(-1,5)*Metric(3,4))/2. - (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. + (Epsilon(1,2,4,-1)*P(-1,4)*Metric(3,5))/2. + Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,4)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,5)*Metric(4,5)')

VVVVVS10 = Lorentz(name = 'VVVVVS10',
                   spins = [ 3, 3, 3, 3, 3, 1 ],
                   structure = 'Epsilon(2,3,4,5)*P(1,4) - Epsilon(2,3,4,5)*P(1,5) + Epsilon(1,2,3,5)*P(4,1) - Epsilon(1,2,3,5)*P(4,5) + Epsilon(1,2,3,4)*P(5,1) - Epsilon(1,2,3,4)*P(5,4) - (Epsilon(3,4,5,-1)*P(-1,4)*Metric(1,2))/2. + (Epsilon(3,4,5,-1)*P(-1,5)*Metric(1,2))/2. + (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. - (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. + Epsilon(2,3,5,-1)*P(-1,1)*Metric(1,4) + Epsilon(2,3,5,-1)*P(-1,4)*Metric(1,4) + Epsilon(2,3,5,-1)*P(-1,5)*Metric(1,4) + Epsilon(2,3,4,-1)*P(-1,1)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,4)*Metric(1,5) + Epsilon(2,3,4,-1)*P(-1,5)*Metric(1,5) + (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. - (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. + (Epsilon(1,3,4,-1)*P(-1,1)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. - (Epsilon(1,2,5,-1)*P(-1,1)*Metric(3,4))/2. + (Epsilon(1,2,5,-1)*P(-1,5)*Metric(3,4))/2. - (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. + (Epsilon(1,2,4,-1)*P(-1,4)*Metric(3,5))/2. + Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,4)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,5)*Metric(4,5)')

VVVVV11 = Lorentz(name = 'VVVVV11',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = '-(Epsilon(2,3,4,5)*P(1,3)) + Epsilon(2,3,4,5)*P(1,4) - Epsilon(1,3,4,5)*P(2,3) + Epsilon(1,3,4,5)*P(2,4) + Epsilon(1,2,4,5)*P(3,1) - Epsilon(1,2,4,5)*P(3,2) + Epsilon(1,2,3,5)*P(4,1) - Epsilon(1,2,3,5)*P(4,2) + Epsilon(3,4,5,-1)*P(-1,3)*Metric(1,2) - Epsilon(3,4,5,-1)*P(-1,4)*Metric(1,2) + Epsilon(2,4,5,-1)*P(-1,1)*Metric(1,3) + (Epsilon(2,4,5,-1)*P(-1,2)*Metric(1,3))/2. + Epsilon(2,4,5,-1)*P(-1,3)*Metric(1,3) + (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. + Epsilon(2,3,5,-1)*P(-1,1)*Metric(1,4) + (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. + Epsilon(2,3,5,-1)*P(-1,4)*Metric(1,4) - (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. + (Epsilon(2,3,4,-1)*P(-1,4)*Metric(1,5))/2. + (Epsilon(1,4,5,-1)*P(-1,1)*Metric(2,3))/2. + Epsilon(1,4,5,-1)*P(-1,2)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,3)*Metric(2,3) + (Epsilon(1,4,5,-1)*P(-1,4)*Metric(2,3))/2. + (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. + Epsilon(1,3,5,-1)*P(-1,2)*Metric(2,4) + (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. + Epsilon(1,3,5,-1)*P(-1,4)*Metric(2,4) - (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. + (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. - Epsilon(1,2,5,-1)*P(-1,1)*Metric(3,4) + Epsilon(1,2,5,-1)*P(-1,2)*Metric(3,4) + (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. - (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2. + (Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5))/2. - (Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5))/2.')

VVVVVS11 = Lorentz(name = 'VVVVVS11',
                   spins = [ 3, 3, 3, 3, 3, 1 ],
                   structure = '-(Epsilon(2,3,4,5)*P(1,3)) + Epsilon(2,3,4,5)*P(1,4) - Epsilon(1,3,4,5)*P(2,3) + Epsilon(1,3,4,5)*P(2,4) + Epsilon(1,2,4,5)*P(3,1) - Epsilon(1,2,4,5)*P(3,2) + Epsilon(1,2,3,5)*P(4,1) - Epsilon(1,2,3,5)*P(4,2) + Epsilon(3,4,5,-1)*P(-1,3)*Metric(1,2) - Epsilon(3,4,5,-1)*P(-1,4)*Metric(1,2) + Epsilon(2,4,5,-1)*P(-1,1)*Metric(1,3) + (Epsilon(2,4,5,-1)*P(-1,2)*Metric(1,3))/2. + Epsilon(2,4,5,-1)*P(-1,3)*Metric(1,3) + (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. + Epsilon(2,3,5,-1)*P(-1,1)*Metric(1,4) + (Epsilon(2,3,5,-1)*P(-1,2)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. + Epsilon(2,3,5,-1)*P(-1,4)*Metric(1,4) - (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. + (Epsilon(2,3,4,-1)*P(-1,4)*Metric(1,5))/2. + (Epsilon(1,4,5,-1)*P(-1,1)*Metric(2,3))/2. + Epsilon(1,4,5,-1)*P(-1,2)*Metric(2,3) + Epsilon(1,4,5,-1)*P(-1,3)*Metric(2,3) + (Epsilon(1,4,5,-1)*P(-1,4)*Metric(2,3))/2. + (Epsilon(1,3,5,-1)*P(-1,1)*Metric(2,4))/2. + Epsilon(1,3,5,-1)*P(-1,2)*Metric(2,4) + (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. + Epsilon(1,3,5,-1)*P(-1,4)*Metric(2,4) - (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. + (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. - Epsilon(1,2,5,-1)*P(-1,1)*Metric(3,4) + Epsilon(1,2,5,-1)*P(-1,2)*Metric(3,4) + (Epsilon(1,2,4,-1)*P(-1,1)*Metric(3,5))/2. - (Epsilon(1,2,4,-1)*P(-1,2)*Metric(3,5))/2. + (Epsilon(1,2,3,-1)*P(-1,1)*Metric(4,5))/2. - (Epsilon(1,2,3,-1)*P(-1,2)*Metric(4,5))/2.')

VVVVV12 = Lorentz(name = 'VVVVV12',
                  spins = [ 3, 3, 3, 3, 3 ],
                  structure = 'Epsilon(1,2,4,5)*P(3,4) - Epsilon(1,2,4,5)*P(3,5) + Epsilon(1,2,3,5)*P(4,3) - Epsilon(1,2,3,5)*P(4,5) + Epsilon(1,2,3,4)*P(5,3) - Epsilon(1,2,3,4)*P(5,4) - (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. + (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. - (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,5)*Metric(1,4))/2. - (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. + (Epsilon(2,3,4,-1)*P(-1,4)*Metric(1,5))/2. + (Epsilon(1,4,5,-1)*P(-1,4)*Metric(2,3))/2. - (Epsilon(1,4,5,-1)*P(-1,5)*Metric(2,3))/2. + (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. - (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. + (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. + Epsilon(1,2,5,-1)*P(-1,3)*Metric(3,4) + Epsilon(1,2,5,-1)*P(-1,4)*Metric(3,4) + Epsilon(1,2,5,-1)*P(-1,5)*Metric(3,4) + Epsilon(1,2,4,-1)*P(-1,3)*Metric(3,5) + Epsilon(1,2,4,-1)*P(-1,4)*Metric(3,5) + Epsilon(1,2,4,-1)*P(-1,5)*Metric(3,5) + Epsilon(1,2,3,-1)*P(-1,3)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,4)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,5)*Metric(4,5)')

VVVVVS12 = Lorentz(name = 'VVVVVS12',
                   spins = [ 3, 3, 3, 3, 3, 1 ],
                   structure = 'Epsilon(1,2,4,5)*P(3,4) - Epsilon(1,2,4,5)*P(3,5) + Epsilon(1,2,3,5)*P(4,3) - Epsilon(1,2,3,5)*P(4,5) + Epsilon(1,2,3,4)*P(5,3) - Epsilon(1,2,3,4)*P(5,4) - (Epsilon(2,4,5,-1)*P(-1,4)*Metric(1,3))/2. + (Epsilon(2,4,5,-1)*P(-1,5)*Metric(1,3))/2. - (Epsilon(2,3,5,-1)*P(-1,3)*Metric(1,4))/2. + (Epsilon(2,3,5,-1)*P(-1,5)*Metric(1,4))/2. - (Epsilon(2,3,4,-1)*P(-1,3)*Metric(1,5))/2. + (Epsilon(2,3,4,-1)*P(-1,4)*Metric(1,5))/2. + (Epsilon(1,4,5,-1)*P(-1,4)*Metric(2,3))/2. - (Epsilon(1,4,5,-1)*P(-1,5)*Metric(2,3))/2. + (Epsilon(1,3,5,-1)*P(-1,3)*Metric(2,4))/2. - (Epsilon(1,3,5,-1)*P(-1,5)*Metric(2,4))/2. + (Epsilon(1,3,4,-1)*P(-1,3)*Metric(2,5))/2. - (Epsilon(1,3,4,-1)*P(-1,4)*Metric(2,5))/2. + Epsilon(1,2,5,-1)*P(-1,3)*Metric(3,4) + Epsilon(1,2,5,-1)*P(-1,4)*Metric(3,4) + Epsilon(1,2,5,-1)*P(-1,5)*Metric(3,4) + Epsilon(1,2,4,-1)*P(-1,3)*Metric(3,5) + Epsilon(1,2,4,-1)*P(-1,4)*Metric(3,5) + Epsilon(1,2,4,-1)*P(-1,5)*Metric(3,5) + Epsilon(1,2,3,-1)*P(-1,3)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,4)*Metric(4,5) + Epsilon(1,2,3,-1)*P(-1,5)*Metric(4,5)')
