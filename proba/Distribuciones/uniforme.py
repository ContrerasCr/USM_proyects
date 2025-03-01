def fun_densidad(x, a, b):
    fx = 1 / (b-a)
    return fx


def esperanza(x, a, b):
    ex = (0.5) * (a+b)
    return ex


def varianza(x, a, b):
    v = (1/12) * pow(b-a, 2)
    return v


def fun_prob_acum(x, a, b):
    Fx = (x-a)/(b-a)
    return Fx


# End document
