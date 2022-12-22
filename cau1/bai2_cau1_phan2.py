import numpy as np

def tinh_tich_hadamad():
    A = np.random.randint(low=-10,high=10,size=15).reshape((3,5))
    B = np.random.randint(low=-10,high=10,size=15).reshape((3,5))
    C = np.multiply(A,B)
    print('AnhanB :',C)
    return C

def tinh_tich_chuyen_vi():
    A1 = np.random.randint(low=-10,high=10,size=15).reshape((3,5))
    B = np.random.randint(low=-10, high=10, size=15).reshape((3,5))
    print('chuyen vi vecto A')
    A2 = np.transpose(A1)
    C1 = np.dot(A2,B)
    print('nhanA1voiB :',C1)
    return C1

