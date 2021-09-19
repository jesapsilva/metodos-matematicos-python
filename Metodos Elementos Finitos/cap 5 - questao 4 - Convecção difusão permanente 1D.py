# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:20:43 2019

@author: jesap
"""
#---------------------------------------------------------------------------------
#    SOLUÇÃO DE PROBLEMA CONVECÇÃO DIFUSÃO PERMANENTE COM ELEMENTOS FINITOS
#---------------------------------------------------------------------------------
#           Equação na forma fraca: (M/dt + K )Tn+1 = (M/dt)Tn

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# dados da malha
ne = 200
npoints = ne + 1 
L = 1.0
h = L/ne

#condições de contorno
Ti = 0.0
Tf = 1.0

# dados para as matrizes
alpha = 1.0  #acompanha matriz de rigidez/difusão
v = 100.0 #acompanha a matriz C

#---------------------------------------------------------------------------------

#criação da malha
X = np.linspace(0,L,npoints)   # vetor posição dos elementos5

IEN = np.zeros((ne,2),dtype='int') # criação da matriz de posição dos elementos

for e in range(0,ne):
    IEN[e,0] = e
    IEN[e,1] = e+1
    
#---------------------------------------------------------------------------------
# criação da matriz de rigidez e de massa
K = np.zeros((npoints,npoints),dtype='float')
C = np.zeros((npoints,npoints),dtype='float')
F = np.zeros((npoints,1),dtype='float')    #
Z = np.zeros((npoints,npoints),dtype='float')  #matriz da soma de C+K


# vetor direito + condição de contorno
b = np.zeros((npoints,1),dtype="float")

#---------------------------------------------------------------------------------
# preenchendo as matrizes
for e in range(0,ne):
    #comprimento do elemento
    h = X[IEN[e,1]] - X[IEN[e,0]] 
    
    # matrizes do elemento linear
    k = (alpha/h) * np.array([[1,-1],
                             [-1,1]],dtype='float')
    
    c = (v/2.0)* np.array([[-1,1],
                             [-1,1]],dtype='float')
    
    f = (c*h/6.0) * np.array([[2,1],
                             [1,2]],dtype='float')    
    
    for i in range(0,2):
        ii = IEN[e,i]
        
        # montagem ( assembly) do vetor do lado direito
        F[ii,0] = F[ii,0] + f[i,0]
        
        for j in range(0,2):
            jj = IEN[e,j]
            
            K[ii,jj] = K[ii,jj] + k[i,j]        
            C[ii,jj] = C[ii,jj] + c[i,j]  
            Z[ii,jj] = K[ii,jj] + C[ii,jj]

# imposição das condições de contorno nas matrizes  
            
#               vetor lado direito
b[0] = b[0] - (-v/2.0 - alpha/h)*Ti
b[npoints-1] = b[npoints-1] - (-v/2.0 - alpha/h)*Tf
#               na matriz principal Z
Z[0,0], Z[0,1] = 1.0, 0.0
Z[npoints-1,npoints-1], Z[npoints-1,npoints-2] = 1.0, 0.0
    
#---------------------------------------------------------------------------------
##   resolvendo o sistema ficar do tipo Tn+1 = inversa(Z)*b onde o vetor b 
##                       será o vetor b = M*Tn

#resolvendo sistema linear para encontrar o novo vetor T  

u = np.linalg.solve(Z,b)
    
#construção do grafico

plt.plot(X,u,'--')
plt.xlabel('x [mm]')
plt.ylabel('Temperatura [ºC]')
plt.title(' Convecção difusão 1D v= '+ str(v) + '\n')
plt.savefig('./figs4/resultado v= ' + str(v)+ '.png')                                                       
#plt.clf()
plt.show()

#---------------------------------------------------------------------------------
