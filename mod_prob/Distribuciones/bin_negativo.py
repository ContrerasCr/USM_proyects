from math import comb


def fun_densidad(x, p, r, n):
    fx = comb(x-1, r-1) * pow(p, r) * pow(1-p, n-x)
    return fx


def esperanza(x, p, r):
    ex = r / p
    return ex


def varianza(x, p, r):
    v = (r * (1 - p)) / pow(p, 2)
    return v


def fun_prob_acum(x, p):
    Fx = 1 - pow((1 - p), x)
    return 'Arreglar'

# End document