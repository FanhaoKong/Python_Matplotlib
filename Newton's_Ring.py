import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource

def main():
    #Test data
    x, y = np.mgrid[-10:10:0.02, -10:10:0.02]
    #z=np.sin(x**2+y**2)
    z=0.5+0.5*np.cos(np.pi+(2*np.pi/(600e-4))*2*(200-np.sqrt(200*200-x**2-y**2)))
    fig = compare(z, plt.cm.copper)
    fig.suptitle("Newton\'s Rings",fontsize=12,y=0.94)
    fig.savefig("F:/Matplotlib/Newtown's Ring.jpg",dpi=500)
    plt.show()

def compare(z, cmap, ve=2):
    #Create subplots and hid ticks
    fig, ax=plt.subplots()
    ax.set(xticks=[],yticks=[])
    #Illuminate the scene from the northwest
    ls=LightSource(azdeg=315,altdeg=45)
    rgb = ls.shade(z, cmap=cmap, vert_exag=ve,blend_mode='hsv')
    ax.imshow(rgb)
    return fig

main()
