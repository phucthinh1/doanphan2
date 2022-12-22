from sympy import *
def ham_tinh_dao_ham():
    x = symbols('x')
    f = ((2*x-1)/(x+2))
    answer = diff(f,x)
    print('ham tinh dao ham:',answer)
    return (answer)

