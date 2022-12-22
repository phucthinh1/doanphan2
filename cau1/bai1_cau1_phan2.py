import numpy as np

def tinh_tich():
    A = np.random.randint(low=-10,high=10,size=15)
    A.reshape(3,5)
    n = int(input('n='))
    B = n*A
    print('ketquabai1:',B)
    return B


