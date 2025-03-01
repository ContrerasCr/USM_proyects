from math import factorial


def fun_densidad(x, tet, t):
    fx = (pow(2.718281,  - tet * t) * pow(tet * t, x)) / factorial(x)
    return fx


def esperanza(x, tet, t):
    ex = tet * t
    return ex


def varianza(x, tet, t):
    v = tet * t
    return v


def fun_prob_acum(x, tet, t):
    Fx = 0
    for i in range(x):
        Fx += fun_densidad(i, tet, t)
    return Fx
# End document
