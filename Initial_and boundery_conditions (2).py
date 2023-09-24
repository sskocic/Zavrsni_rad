import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from Initial_conditions import matrica


gitara=matrica()

c = 3960
L=1
N= 300
dr = L / (N-1)
dt = 0.0000001
t_max = 0.0005
Nt = int(t_max / dt)

print(c*dt/dr) #koeficijent stabilnosti rješenja

u = np.zeros((Nt, N, N))
u_new = np.zeros((N, N)) 
u_old = np.zeros((N, N))

#Pocetni uvjeti
for k in range(N):
    for l in range(N):
        if gitara[k,l]==2:
            u[0, k, l] = 0.001
    
for k in range(1,N-1):
    for l in range(1,N-1):
        u_old[k,l]=u[0,k,l]+dt/(2*dr**2)*(u[0,k+1,l]-4*u[0,k,l]+u[0,k-1,l]+u[0,k,l+1]+u[0,k,l-1])

        
#prikaz pocetnih uvjeta
#plt.imshow(u[0], cmap='viridis')
#plt.show()

for frame in range(Nt-2):
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            temp = (c*dt/dr)*(c*dt/dr)*(u[frame,i+1,j] + u[frame,i,j-1] + u[frame,i,j+1] + u[frame,i-1,j] - 4*u[frame,i,j]) + 2*u[frame,i,j] - u_old[i,j]
            u_new[i, j] = temp
    
    for m in range(1, N - 1):
        for n in range(1, N - 1):         

            if (gitara[m,n])==1:
                u_new[m,n]=0

    u[frame+1]=u_new    
    u_old = u[frame]
    u_new = u[frame+2]

#prikaz rješenja

flag=True
if flag==True:
    for i in range(Nt):
        plt.clf()
        plt.title("Sekunda: " + str(round(i*dt*1000,4))+str(" ms"))
        plt.xlabel("N[L/dr]")
        plt.ylabel("N[L/dr]")
        plt.imshow(u[i], cmap='plasma')  
        plt.colorbar()
        plt.pause(0.1) #ubrzavanje usporavnaje animacije
    plt.show()
