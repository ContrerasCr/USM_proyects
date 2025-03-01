from math import comb

def fun_densidad(x, p, n):
    fx = comb(n, x) * pow(p, x) * pow(1-p, 1-x)
    return fx


def esperanza(x, p, n):
    return n * p


def varianza(x, p, n):
    v = n * p * (1 - p)
    return v


def fun_prob_acum(x, p, n):
    Fx = 0
    for i in range(n):
        Fx += fun_densidad(x, p, n)
    return Fx
# End document
