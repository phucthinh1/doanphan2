from phan2.cau4 import bai1_cau4_phan2,bai2_cau_4_phan2,bai3_cau4_phan2
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(start=-15.0, stop=15.0, num=200)
    y = np.linspace(start=-15.0, stop=15.0, num=200)
    x1 = np.linspace(start=-15.0, stop=15.0, num=10000)
    y1 = np.linspace(start=-15.0, stop=15.0, num=10000)
    x22 = np.linspace(-6, 2, 15000)
    y22 = np.linspace(-3, 5, 15000)
    x, y = np.meshgrid(x, y)
    x1, y1 = np.meshgrid(x1, y1)
    x22, y22 = np.meshgrid(x22, y22)
    a=bai1_cau4_phan2.ham_yen_ngua(x,y)
    b1=bai2_cau_4_phan2.ham_hyperbolic_1_tang2(x1,y1)
    b2=bai2_cau_4_phan2.ham_hyperbolic_1_tang(x1,y1)
    c1=bai3_cau4_phan2.ham_mat_cau(x22,y22)
    c2=bai3_cau4_phan2.ham_mat_cau2(x22,y22)
    fig,(ax1,ax2,ax3)=plt.subplots(1,3,subplot_kw={"projection":"3d"})
    ax1.plot_surface(x, y,a, cmap='plasma', linewidth=0, antialiased=False)
    ax2.plot_surface(x1, y1, b2, cmap='plasma', linewidth=0, antialiased=False)
    ax2.plot_surface(x1, y1, b1, cmap='plasma', linewidth=0, antialiased=False)
    ax3.plot_surface(x22, y22, c1, cmap='plasma', linewidth=0, antialiased=False)
    ax3.plot_surface(x22, y22, c2, cmap='plasma', linewidth=0, antialiased=False)
    ax1.set_zlim(-60,20)
    ax2.set_zlim(-8,8)
    ax3.set_zlim(0,7)
    plt.show()


if __name__=='__main__':
    main()