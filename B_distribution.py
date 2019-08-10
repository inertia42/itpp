import numpy as np
from module import *

def q(rr):
    #rr=r(x,y,z)
    return 0.1+rr**2

def R(x,y,z):
    return np.sqrt(x**2+y**2)

def r(x,y,z):
    return np.sqrt(np.abs((np.sqrt(x**2+y**2)-R0)**2+z**2))

def Bt(RR):
    return B0*R0/RR

def Bp(rr,RR):
    return Bt(RR)*rr/(q(rr)*R0)

def tokamak(x,y,z):
    RR=R(x,y,z)
    rr=r(x,y,z)
    # print(rr)
    Btn=Bt(RR)
    Bpn=Bp(rr,RR)
    Bx=-Btn*(y/RR)-Bpn*(z/rr)*(x/RR)
    By=Btn*(x/RR)-Bpn*(z/rr)*(y/RR)
    Bz=Bpn*(RR-R0)/rr
    return Bx,By,Bz

def uniform(x,y,z):
    return 0,0,B0

def grad_B(x,y,z):
    return 0,0,B0*y*0.02+B0

def curvature_B(x,y,z):
    a=R(x,y,z)
    B0=10/a
    return B0*(y/a),B0*(-x/a),0 



if B_type==0:
    B_distribution=uniform
if B_type==1:
    B_distribution=grad_B
if B_type==2:
    B_distribution=curvature_B
else:
    B_distribution=tokamak

