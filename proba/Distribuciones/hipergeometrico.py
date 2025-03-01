from math import comb


def fun_densidad(x, N, M, n):
    fx = (comb(M, n) * comb(N-M, n-x)) / comb(N, n)
    return fx


def esperanza(N, M, n):
    ex = n * (M / N)
    return ex


def varianza(N, M, n):
    v = n * (M / N) * ((N-M)/N) * ((N-n)/(N-1))
    return v


def fun_prob_acum(x, N, M, n):
    Fx = 0
    for i in range(n):
        Fx += fun_densidad(x, N, M, n)
    return Fx
# End document
