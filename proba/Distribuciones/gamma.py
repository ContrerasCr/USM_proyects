from math import gamma


def fun_densidad(x, r, tet):
    fx = (pow(tet, r) / gamma(r)) * pow(x, r-1) * pow(2.718281,  - tet * x)
    return fx


def esperanza(x, r, tet):
    ex = r/tet
    return ex


def varianza(x, r, tet):
    v = r / pow(tet, 2)
    return v


def fun_prob_acum(x, r, tet):
    Fx = 'Arreglar'
    return Fx
# End document
