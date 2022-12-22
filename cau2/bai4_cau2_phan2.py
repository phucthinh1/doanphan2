from sympy import *

def ham_tinh_nguyen_ham():
    x= symbols('x')
    f = ((x)/(x**2+1))
    answer = integrate(f,x)
    print('ham tinh nguyen ham:',answer)
    return (answer)