import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def ham_yen_ngua(x,y):
    a = (x/3)**2 - (y/2)**2
    return a
# x = np.linspace(start=-15.0, stop=15.0,num=200)
# y = np.linspace(start=-15.0, stop=15.0,num=200)
# x,y = np.meshgrid(x,y)
# z1 = ham_yen_ngua(x,y)
# fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
# yenngua_surf = ax.plot_surface(x,y,z1,cmap='plasma',linewidth=0, antialiased=False)
# ax.set_zlim(-60,20)
# fig.colorbar(yenngua_surf, shrink=0.5,aspect=5)
# plt.show()
