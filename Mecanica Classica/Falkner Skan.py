# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:51:57 2019

@author: jesap
"""
#------------------------------------------------------------------------
#                          FALKNER SKAN
#------------------------------------------------------------------------

import math
import matplotlib.pyplot as plt
import numpy as np

#------------------------------------------------------------------------
def inicializa(f,g,h,nIter,dni):
    f10 = f
    f1 = np.zeros((nIter,1),dtype='float')
    f1[0][0] = f10
    
    f20 = g
    f2 = np.zeros((nIter,1),dtype='float')
    f2[0][0] = f20
    
    f30 = h  
    f3 = np.zeros((nIter,1),dtype='float')
    f3[0][0] = f30
    
    return f1,f2,f3

def falker(f1,f2,f3,tam,dni):
    for i in range(0,nIter-1):
        f1[i] = f2[i-1]*dni + f1[i-1]
        f2[i] = f3[i-1]*dni + f2[i-1]
        f3[i] = (-f1[i-1]*f3[i-1] -beta*(1-(f2[i-1])**2))*dni + f3[i-1]
    return f1,f2,f3    

#------------------------------------------------------------------------    

# Gráfiso
X =np.linspace(0,Ni,nIter)

dni = 0.1
Ni = 6.2
nIter = 10
f1,f2,f3 = inicializa(0.0,0.0,0.005218,nIter,dni)
beta=-0.1988
x1,y1,z1=falker(f1,f2,f3,nIter,dni)
plt.plot(X,y1,'-')

#------------------------------------------------------------------------

dni = 0.0001
Ni = 5.0
f1,f2,f3 = inicializa(0,0,0.4696,60)
beta = -0.1988
x2,y2,z2=falker(f1,f2,f3,51,dni)
plt.plot(y2,'r-')

#------------------------------------------------------------------------

dni = 0.00001
Ni = 8.4
f1,f2,f3 = inicializa(0,0,0.005218,Ni,dni)
beta=1.0
x3,y3,z3=falker(f1,f2,f3,85,dni)
plt.plot(y3,'*')

#------------------------------------------------------------------------

dni = 0.000001
Ni = 4.73
f1,f2,f3 = inicializa(0,0,0.005218,Ni,dni)
beta=2.0
x4,y4,z4=falker(f1,f2,f3,48,dni)
plt.plot(y4,'--')

#------------------------------------------------------------------------
