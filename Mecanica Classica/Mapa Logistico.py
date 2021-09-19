# -*- coding: utf-8 -*-
"""
Created on Wed May  8 13:39:50 2019

@author: viana
"""
#------------------------------------------------------------------------
#           MAPA LOGISTICO DA POPULAÇÃO
#------------------------------------------------------------------------

import matplotlib.pyplot as plt 

#parametos da simulação
nIter = 65
dt = 20

#------------------------------------------------------------------------
def calcula(xn,mi,dt,nIter):
    time = 0.0
    tempo = []
    espaco = []
    for i in range(0,nIter):
        x = mi*xn - mi*xn*xn
        xn = x
        time += dt
        espaco.append(x)
        tempo.append(time)
    return tempo, espaco

def imprime(mi,xn,dt,nIter):
    x,y = calcula(xn,mi,dt,nIter)
    plt.plot(x,y,'',label='mi ='+ str(mi))
    plt.xlabel('tempo [meses]')
    plt.ylabel('x')
    plt.title(' Razão de população\n')
    plt.savefig('./figs/Grafico com mi ' + str(mi) + '.png')
    plt.show() 
    return 
#------------------------------------------------------------------------
#parametros do problema
xn = 0.45
m1 = 0.8
x = imprime(m1,xn,dt,nIter)
#------------------------------------------------------------------------
 
m2 = 1.7 
x =imprime(m2,xn,dt,nIter)
#------------------------------------------------------------------------
m3 =2.8
x =imprime(m3,xn,dt,nIter)
#------------------------------------------------------------------------
m4 = 3.2
x =imprime(m4,xn,dt,nIter)
#------------------------------------------------------------------------
m5 = 3.5 
x =imprime(m5,xn,dt,nIter)
#------------------------------------------------------------------------
m6 = 2.5
x =imprime(m6,xn,dt,nIter)
#------------------------------------------------------------------------