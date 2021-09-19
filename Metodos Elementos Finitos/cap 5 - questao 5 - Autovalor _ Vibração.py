# -*- coding: utf-8 -*-
"""
Created on Wed May 15 19:20:43 2019

@author: jesap
"""
#---------------------------------------------------------------------------------
#    SOLUÇÃO DE PROBLEMA VIBRAÇÃO 1D COM ELEMENTOS FINITOS
#---------------------------------------------------------------------------------


#           Equação na forma fraca: (M/dt + K )Tn+1 = (M/dt)Tn

import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------- 

# dados da malha
ne = 10
npoints = ne + 1 
L = 1.0
Le = L/ne

#condições de contorno
ui = 0.0
uf = 1.0

# dados para as matrizes
ro = 7800 
A = 0.0001
E = 200

#condição transiente
dt = 1.0
nIter = 101
t = 0.0

#-------------------------------------------------------------------------------
 
#criação da malha
X = np.linspace(0,L,npoints)   # vetor posição dos elementos5

IEN = np.zeros((ne,2),dtype='int') # criação da matriz de posição dos elementos

for e in range(0,ne):
    IEN[e,0] = e
    IEN[e,1] = e+1
    
# criação da matriz de rigidez e de massa
K = np.zeros((npoints,npoints),dtype='float')
M = np.zeros((npoints,npoints),dtype='float')
Z = np.zeros((npoints,npoints),dtype='float')  #matriz M-Kdt²

# vetor direito + condição de contorno
U = np.zeros((npoints,1),dtype="float")

#-------------------------------------------------------------------------------

for e in range(0,ne):
    #comprimento do elemento
    h = X[IEN[e,1]] - X[IEN[e,0]] 
    
    # matrizes do elemento linear
    k = ((A*E)/Le) * np.array([[1,-1],
                               [-1,1]],dtype='float')

    m = ((ro*A*Le)/6.0)* np.array([[2,1],
                                   [1,2]],dtype='float')    

    for i in range(0,2):
        ii = IEN[e,i]
        
        for j in range(0,2):
            jj = IEN[e,j]
            
            K[ii,jj] = K[ii,jj] + k[i,j]        
            M[ii,jj] = M[ii,jj] + m[i,j]  
            Z[ii,jj] = -(dt*dt)*K[ii,jj] + M[ii,jj]
            
#-------------------------------------------------------------------------------
            
# imposição das condições de contorno na matriz F
U[1,0] = U[1,0] -Z[1,0]*ui
U[npoints-2,0] = U[npoints-2,0] -Z[npoints-2,npoints-1]*uf

# imposição das condições de contorno nas matrizes
Z[0,0], Z[0,1] = 1.0, 0.0
Z[npoints-1,npoints-1], Z[npoints-1,npoints-2] = 1.0, 0.0
Z[1,0]=0
Z[npoints-2,npoints-1]=0

#-------------------------------------------------------------------------------

# iteração para resolução do transiente
for j in range(1,nIter):
    # vamos iniciar j com 1 pois já criei a primeira imagem la em cima e nao quero sobrepor
    b = np.dot(M,U)
    #resolvendo sistema linear para encontrar o novo vetor T    
    U = np.linalg.solve(Z,b)
    #avança no tempo
    t = t + dt
    
#------------------------------------------------------------------------------- 

    
#construção do grafico
    if j%10==0: 
        plt.plot(X,U,'o--')
        plt.xlabel('x [mm]')
        plt.ylabel('deslocamento [mm]')
#        plt.axis((0, 1.0, 0, 10),1.5)
        plt.title(' Vibração em um corpo sólido\n')
        plt.savefig('./figs5/resultado' + str(j) + '.png')                                                       
        plt.clf()
#---------------------------------------------------------------------------------

