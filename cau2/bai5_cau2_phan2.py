from sympy import *

def ham_tinh_tich_phan():
    x = symbols('x')
    f = ((1-x*tan(x))/(x**2*cos(x)+x))
    answer = integrate(f, (x,pi,(2*pi/3)))
    print('ham tinh tich phan:',answer)
    return (answer)