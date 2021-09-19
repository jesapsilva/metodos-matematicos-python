import numpy as np
import matplotlib.pyplot as plt


# parametros do simulador
Lx = 1.0
Ly = 1.0
nx = 4
ny = 4
npoints = nx*ny
ne = 18

#---------------------------------------------------------------------------------

# # condicao de contorno
# ui = 1.0 # condicao de contorno em x=0
# uf = 3.0 # condicao de contorno em x=L
#---------------------------------------------------------------------------------


# criacao da malha
X,Y = np.meshgrid([0.0,1.0/3.0,2.0/3.0,1.0],
                  [0.0,1.0/3.0,2.0/3.0,1.0])
X = X.reshape(npoints)
Y = Y.reshape(npoints)

# matriz com os nós pertencentes a cada elemento
IEN = np.zeros( (ne,3), dtype='int')

IEN[0,0] = 0; IEN[0,1] = 5; IEN[0,2] = 4
IEN[1,0] = 0; IEN[1,1] = 1; IEN[1,2] = 5
IEN[2,0] = 1; IEN[2,1] = 6; IEN[2,2] = 5
IEN[3,0] = 2; IEN[3,1] = 6; IEN[3,2] = 1
IEN[4,0] = 2; IEN[4,1] = 7; IEN[4,2] = 6
IEN[5,0] = 2; IEN[5,1] = 3; IEN[5,2] = 7
IEN[6,0] = 4; IEN[6,1] = 9; IEN[6,2] = 8
IEN[7,0] = 4; IEN[7,1] = 5; IEN[7,2] = 9
IEN[8,0] = 5; IEN[8,1] = 10; IEN[8,2] = 9
IEN[9,0] = 5; IEN[9,1] = 6; IEN[9,2] = 10
IEN[10,0] = 6; IEN[10,1] = 11; IEN[10,2] = 10
IEN[11,0] = 6; IEN[11,1] = 7; IEN[11,2] = 11
IEN[12,0] = 8; IEN[12,1] = 13; IEN[12,2] = 12
IEN[13,0] = 8; IEN[13,1] = 9; IEN[13,2] = 13
IEN[14,0] = 9; IEN[14,1] = 14; IEN[14,2] = 13
IEN[15,0] = 9; IEN[15,1] = 10; IEN[15,2] = 14
IEN[16,0] = 10; IEN[16,1] = 15; IEN[16,2] = 14
IEN[17,0] = 10; IEN[17,1] = 11; IEN[17,2] = 15

# pontos de cc
cc = [0,1,2,3,4,7,8,11,12,13,14,15]

#---------------------------------------------------------------------------------

##mostrando a malha
#plt.triplot(X,Y,IEN)
#plt.show()
#---------------------------------------------------------------------------------


# inicializando as matrizes K e M e os vetores F e Q
K =  np.zeros( (npoints,npoints), dtype='float')
M =  np.zeros( (npoints,npoints), dtype='float')
Gx =  np.zeros( (npoints,npoints), dtype='float') #gradiente x
Gy =  np.zeros( (npoints,npoints), dtype='float') #gradiente y

# loop dos elementos da malha
for e in range(0,ne):
 v = IEN[e]
 # area do elemento
 det = X[v[2]]*( Y[v[0]]-Y[v[1]]) \
       + X[v[0]]*( Y[v[1]]-Y[v[2]]) \
       + X[v[1]]*(-Y[v[0]]+Y[v[2]])

 area = det/2.0
 
 # matrizes do elemento linear
 m = (area/6.0) * np.array([ [2.0, 1.0, 1.0],
                             [1.0, 2.0, 1.0],
                             [1.0, 1.0, 2.0] ])

 # formula do k do elementro triangular linear
 b1 = Y[v[1]]-Y[v[2]]
 b2 = Y[v[2]]-Y[v[0]]
 b3 = Y[v[0]]-Y[v[1]]

 c1 = X[v[2]]-X[v[1]]
 c2 = X[v[0]]-X[v[2]]
 c3 = X[v[1]]-X[v[0]]

 # matriz do gradiente
 B = (1.0/(2.0*area)) * np.array([ [b1, b2, b3],
                                   [c1, c2, c3] ])
 # matriz do divergente
 BT = B.transpose()

 kele = 2*area*np.dot(BT,B)

 gxele = (1.0/6.0)*np.array([ [b1, b2, b3],
                              [b1, b2, b3],
                              [b1, b2, b3] ])
 gyele = (1.0/6.0)*np.array([ [c1, c2, c3],
                              [c1, c2, c3],
                              [c1, c2, c3] ])

 for i in range(0,3):
  ii = IEN[e,i]
  for j in range(0,3):
   jj = IEN[e,j]
   
   # montagem (assembling) das matrizes K e M
   K[ii,jj] = K[ii,jj] + kele[i,j]
   M[ii,jj] = M[ii,jj] + m[i,j]
   Gx[ii,jj] = Gx[ii,jj] + gxele[i,j]
   Gy[ii,jj] = Gy[ii,jj] + gyele[i,j]
   
# copiando a matriz K para mat
mat =  np.zeros( (npoints,npoints), dtype='float')
mat = mat + K

# imposicao das condicoes de contorno
for i in cc:
 mat[i,:] = 0.0
 mat[i,i] = 1.0


Z =  np.zeros( (npoints,1), dtype='float')
Z[0] = 0.0 
Z[1] = 0.0
Z[2] = 0.0
Z[3] = 0.0
Z[4] = Y[4]
Z[7] = Y[7]
Z[8] = Y[8]
Z[11] = Y[11]
Z[12] = Y[12]
Z[13] = Y[13]
Z[14] = Y[14]
Z[15] = Y[15]
#---------------------------------------------------------------------------------
# resolução do sistema linear

u = np.linalg.solve(mat,Z)
#---------------------------------------------------------------------------------

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(X, Y, u.reshape(npoints),cmap='jet')
plt.title(' Função corrente ψ escoamento irrotacional 2D com EF\n')
plt.savefig('./figs6/função corrente 2D.png')      
plt.xlabel('x [mm]')
plt.ylabel('y [mm]') 
plt.show()
#---------------------------------------------------------------------------------







