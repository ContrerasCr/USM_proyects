

def fun_densidad(x, tet, t):
    fx = tet * (pow(2.718281,  - tet * x))
    return fx


def esperanza(x, tet, t):
    ex = 1/tet
    return ex


def varianza(x, tet, t):
    v = 1 / pow(tet, 2)
    return v


def fun_prob_acum(x, tet, t):
    Fx = 1 - (pow(2.718281,  - tet * x))
    return Fx
# End document
