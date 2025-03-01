
def fun_densidad(x, p):

    fx = pow(p, x) * pow(1-p, 1-x)
    return fx


def esperanza(x, p):
    return p


def varianza(x, p):
    v = p*(1-p)
    return v


# End document
