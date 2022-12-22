from sympy import *

def ham_tinh_gioi_han():
    x = symbols('x')
    f = ((x**3-3*x**2)**1/3+(x**2-2*x)**1/2)
    answer = limit(f,x,oo)
    print('ket qua gioi han:', answer)
    return(answer)