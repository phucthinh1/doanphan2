import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def ham_hyperbolic_1_tang(x,y):
    b = (x/3)**2 + (y/5)**2-1
    return 2*np.sqrt(b)
def ham_hyperbolic_1_tang2(x,y):
    d = (x/3)**2 + (y/5)**2-1
    return -2*np.sqrt(d)


# x = np.linspace(start=-15.0, stop=15.0,num=10000)
# y = np.linspace(start=-15.0, stop=15.0,num=10000)
# x,y = np.meshgrid(x,y)
# z1 = ham_hyperbolic_1_tang(x,y)
# z2 = ham_hyperbolic_1_tang2(x,y)
# fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
# hyperbolic_surf = ax.plot_surface(x,y,z1,cmap='nipy_spectral',linewidth=0, antialiased=False)
# hyperbolic_surf = ax.plot_surface(x,y,z2,cmap='nipy_spectral',linewidth=0, antialiased=False)
# ax.set_zlim(-8,8)
# fig.colorbar(hyperbolic_surf, shrink=0.7,aspect=5)
# plt.show()

