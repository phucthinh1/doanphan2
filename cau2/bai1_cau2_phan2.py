from sympy import symbols, Eq, solve

def ham_giai_he_phuong_trinh():
    x,y,z = symbols('x y z')
    eq1 = Eq(2*x-5*y+z,-5)
    eq2 = Eq(4*x+2*y-2*z,2)
    eq3 = Eq(x+y-z,0)
    answer = solve((eq1,eq2),(x,y,z))
    print('he phuong trinh:',answer)
    return(answer)