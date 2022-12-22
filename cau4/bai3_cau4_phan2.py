import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def ham_mat_cau(x,y):
    c = (4-(x+2)**2 - (y-1)**2)**(1/2) +4
    return c
def ham_mat_cau2(x,y):
    f = -((4-(x+2)**2 - (y-1)**2)**(1/2)) +4
    return f
# fig,ax = plt.subplots(subplot_kw={"projection":"3d"})
# x = np.linspace(-6,2,15000)
# y = np.linspace(-3,5,15000)
# x,y = np.meshgrid(x,y)
# a = ham_mat_cau(x,y)
# v = ham_mat_cau2(x,y)
# ax.plot_surface(x,y,a,cmap='winter_r',linewidth=0, antialiased=False)
# ax.plot_surface(x,y,v,cmap='winter',linewidth=0, antialiased=False)
# ax.set_zlim(0,7)
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
#
#
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
#
# # Make data
# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 100)
# x = 10 * np.outer(np.cos(u), np.sin(v))
# y = 10 * np.outer(np.sin(u), np.sin(v))
#
# # Plot the surface
# ax.plot_surface(x,y,z)
# ax.set_zlim(-8,8)
# # Set an equal aspect ratio
# ax.set_aspect('equal')
# ax.plot_surface(x,y,cmap='plasma',linewidth=0, antialiased=False)
#
# plt.show()