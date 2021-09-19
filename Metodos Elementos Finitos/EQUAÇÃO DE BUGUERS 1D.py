#---------------------------------------------------------------------------------
#           EQUAÇÃO DO TRANSPORTE TRANSIENTE COM DIFERENÇAS FINITAS
#---------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# parametros do dominio numerico
npoints = 101
L = 1.0
dx = L / (npoints-1)

# parametros da simulacao
CFL = 0.1                    
v = 1.0
dt = CFL*dx/v
#---------------------------------------------------------------------------------
# malha
X = np.linspace(0,L,npoints)
#
#method = 'central'
method = 'upwind1'
#method = 'dvisc1'
#method = 'lagrangian'
#method = 'semi-lagrangian'

#---------------------------------------------------------------------------------
# matriz do perfil U 
# iniciar perfil u
u = np.zeros( (npoints),dtype = 'float')
unew = np.zeros( (npoints),dtype = 'float')
for i in range(0,npoints):
 if X[i] >= L/6.0 and X[i] <= 2*L/6.0:  #condição de contorno
  u[i] = 1.0

#Plot gráfico inicial
plt.plot(X,u,'b-')

#---------------------------------------------------------------------------------
#Função plot gráfico 
def funcplot(_L,_X,_u):
 plt.axis([0,_L,-0.5,1.5])
 plt.plot(_X,_u,'c-')
 plt.show()
 plt.clf()

#---------------------------------------------------------------------------------
if method == 'central':
 # tratando os pontos internos
 for t in range(0,100):
  for i in range(1,npoints-1):
   unew[i] = u[i] - dt*v/(2.0*dx) * (u[i+1] - u[i-1])

  for i in range(0,npoints):
   u[i] = unew[i]
   plt.axis([0,L,-0.5,1.5])
   plt.plot(X,u,'c-')
   plt.savefig('./figs_questão6_central/fig-central' + str(t) + '.png')
   plt.clf()
#---------------------------------------------------------------------------------
if method == 'upwind1':
 # tratando os pontos internos
 for t in range(0,100):
  for i in range(1,npoints-1):
   unew[i] = u[i] - dt*v/dx * (u[i] - u[i-1])
   
  unew[-1] = unew[-2]
  unew[0] = unew[-1]  

  for i in range(0,npoints):
   u[i] = unew[i]
   plt.axis([0,L,-0.5,1.5])
   plt.plot(X,u,'c-')
   plt.savefig('./figs_questão6_upwind/fig-upwind' + str(t) + '.png')
   plt.clf()
#---------------------------------------------------------------------------------
if method == 'dvisc1':
 alpha = (v*dx/2.0) * (1.0-CFL)
 alpha = 0.08*alpha
 # tratando os pontos internos
 for t in range(0,100):
  for i in range(1,npoints-1):
   unew[i] = u[i] - dt*v/dx * (u[i] - u[i-1]) \
             - dt*alpha/(dx*dx)*(u[i+1]-2*u[i]+u[i-1]) # difusao artificial
   
  # condicao de contorno periodica
  unew[-1] = unew[-2]
  unew[0] = unew[-1]  

  for i in range(0,npoints):
   u[i] = unew[i]

  funcplot(L,X,u)
#---------------------------------------------------------------------------------  
if method == 'lagrangian':
 # tratando os pontos internos
 for t in range(0,100):
  for i in range(0,npoints):
   unew[i] = u[i] 
   X[i] = X[i] + v*dt

  # condicao de contorno periodica
  for i in range(0,npoints):
   if X[i] > L:
    X[i] = X[i] - L
  
   
  for i in range(0,npoints):
   u[i] = unew[i]

  funcplot(L,X,u)
 
#---------------------------------------------------------------------------------
if method == 'semi-lagrangian':
 # tratando os pontos internos
 for t in range(0,100):
  Xd = np.zeros( (npoints),dtype='float')
  for i in range(0,npoints):
   Xd[i] = X[i] - v*dt

  # velocidade ud interpolada no tempo n-1
  unew = np.interp(Xd,X,u)

  # condicao de contorno periodica
   
  for i in range(0,npoints):
   u[i] = unew[i]

  funcplot(L,X,u)
