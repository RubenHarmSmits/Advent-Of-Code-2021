import numpy as np


fR = 0.02
fSD = 0.3
fK = 100
fC = 0.75
iT = 1
iN = 1
bOVT = True
fS0 = getfS0 (fC,fK)
mValue = np.zeros(iN)

#EV UP and DOWN#
def getfNU(fSD,iT,iN,fR):
    fNU = iN * getPUp (fSD,iT,iN,fR)
    return fNU

def getfND(fSD,iT,iN,fR):
    fND = iN - calcNu(fSD,iT,iN,fR)
    return fND

#INITIAL VALUE#
def getfS0 (fC,fK):
    fS0 = fC*fK
    mValue[0]=
    return fS0

#CHANGE OF TIME#
def getfDeltaT (iT,iN):
    fDeltaT = iT/iN
    return fDeltaT

#SIZE#
def getfU (fSD,iT,iN):
    fU = np.exp(fSD*np.sqrt(getfDeltaT(iT,iN)))
    return fU

def getfD(fSD,iT,iN):
    fD = 1/getfU(fSD,iT,iN)
    return fD

def getS (fC,fK,fSD,iT,iN, fR):
    fS = getS0(fC,fK)*pow(getfU (fSD,iT,iN),getfNU(fSD,iT,iN,fR)-getfND(fSD,iT,iN,fR))
    return fS

#Probability#
def getPUp (fSD,iT,iN,fR):
    fPU = (1/(getfU(fSD,iT,iN)-getfD(fSD,iT,iN)))*(np.exp(fR*getfDeltaT(iT,iN))-getfD(fSD,iT,iN))
    return fPU

def getPDown (fSD,iT,iN,fR):
    fPD = 1 - getPUp (fSD,iT,iN,fR)
    return fPD

#VALUE AT EXPIRATION#
def valueCall (fC,fK,fSD,iT,iN,r):
    fCCall = max(getS(fC,fK,fSD,iT,iN,r)-fK,0)
    return fCCall

def valuePut (fC,fK,fSD,iT,iN,r):
    fCPut = max(fK - getS(fC,fK,fSD,iT,iN,r),0)
    return fCPut

#Pricing#
def getC (fSD,iT,iN,fR,fS,fK, bOVT):

    if bOVT:

    else:


#Trials#

print(valueCall(fC,fK,fSD,iT,iN,fR))
print(valuePut(fC,fK,fSD,iT,iN,fR))







