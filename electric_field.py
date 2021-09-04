import numpy as np
import matplotlib.pyplot as plt

Y,X = np.mgrid[-10:10:100j, -10:10:100j]

def fieldx(charge,a,b,x,y):
    dist=np.sqrt((x-a)**2+(y-b)**2)
    power=charge/(dist**2)
    strengthx=power*(x-a)/dist
    return strengthx
def fieldy(charge,a,b,x,y):
    dist=np.sqrt((x-a)**2+(y-b)**2)
    power=charge/(dist**2)
    strengthy=power*(y-b)/dist
    return strengthy
number=eval(input("Please input the number of charges:\n(The number \
must be an integer)\n"))
data=np.zeros((number,3))
for i in range(number):
    en=np.array(list(map(eval,(input("charge, x, y\n").split(" ")))))
    data[i]=en
U,V=0,0
for i in range(number):
    U=U+fieldx(data[i,0],data[i,1],data[i,2],X,Y)
    V=V+fieldy(data[i,0],data[i,1],data[i,2],X,Y)
#U=fieldx(2,-2,0,X,Y)+fieldx(2,2,0,X,Y)
#V=fieldy(2,-2,0,X,Y)+fieldy(2,2,0,X,Y)
speed = np.sqrt(U*U + V*V)
fig, ax = plt.subplots(figsize=(10,10))
ax.axis('equal')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
strm = ax.streamplot(X, Y, U, V, color='k', linewidth=0.5, \
        density=[3, 3],minlength=0.1,maxlength=10.0,arrowstyle='simple')
fig.suptitle("Electric Field",fontsize='20',y=0.92)
fig.savefig("F:/Matplotlib/Electric Field experiment5.jpg",dpi=800)

plt.show()
