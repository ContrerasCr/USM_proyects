from math import gamma


def fun_densidad(x, alpha, lamda):
    fx = alpha * pow(lamda, alpha) * pow(x, alpha-1) * pow(2.718281, -pow(lamda*x, alpha))
    return fx


def esperanza(x, alpha, lamda):
    ex = (1/lamda) * gamma(1+(1/alpha))
    return ex


def varianza(x, alpha, lamda):
    v = (1/pow(lamda, 2)) * (gamma(1+(2/alpha)) - pow(gamma(1+(1/alpha)), 2 ))
    return v


def fun_prob_acum(x, alpha, lamda):
    Fx = 1 - pow(2.718281, -pow(lamda*x, alpha))
    return Fx


# End document
