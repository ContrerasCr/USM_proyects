from math import comb


def fun_densidad(x, p):

    fx = p * pow(1-p, 1-x)
    return fx


def esperanza(x, p):
    ex = 1/p
    return ex


def varianza(x, p):
    v = (1-p)/pow(p, 2)
    return v


def fun_prob_acum(x, p):
    Fx = 1 - pow((1-p), x)
    return Fx


# End document
