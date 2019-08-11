import numpy as np
from module import *

def uniformE(x,y,z):
    return Ex0,Ey0,Ez0

def SinE(x,y,z):
    return Ex0*np.cos(0.01*y),0,0

if E_type==0:
    E_distribution=uniformE
elif E_type==1:
    E_distribution=SinE
