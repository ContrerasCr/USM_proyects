from math import sqrt
from scipy.stats import norm


def calc_z(x, miu, tetwo):
    tet = sqrt(tetwo)
    z = (x-miu)/tet
    return z


def fun_densidad(x, miu, tetwo):
    fx = (1 / (sqrt(2 * 3.1415926) * sqrt(tetwo))) * pow(2.718281, -pow((0.5 * ((x-miu)/sqrt(tetwo))), 2))
    return fx


def esperanza(x, miu, tetwo):
    ex = miu
    return


def varianza(x, miu, tetwo):
    v = tetwo
    return v


def fun_prob_acum(x, miu, tetwo):
    z = calc_z((x, miu, tetwo))
    Fx = norm(z)
    return Fx
# End document
