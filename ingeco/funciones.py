# Pagina 1 -----------------------------------------------------------------------

def interes_total(s_final, s_inicial):
    interes = s_final - s_inicial
    return interes


def tasa_de_interes(interes, credito):
    t_interes = (interes/credito) * 100
    return t_interes


def valor_futuro_int_simple(vp, i, n):
    vf = vp * (1 + i*n)
    return vf


def valor_futuro_int_comp(vp, i, n):
    vf = vp * pow(1 + i, n)
    return vf


def conv_tasa_int_simple(i, n1, n2):
    i2 = (i*n1)/n2
    return i2


def conv_tasa_int_compuesto(i1, n1, n2):
    i2 = pow((pow(1+i1, n1)), (1/n2))
    return i2


def conv_tasa_int_nominal_a_efectiva(interes_nominal, capitalizaciones):
    i_efectivo = pow((1 + (interes_nominal/capitalizaciones)), capitalizaciones) - 1
    return i_efectivo

# Pagina 2 --------------------------------------------------------------


def payment_vp(vp, i, n):
    inter = pow(1+i, n)
    pmt = vp * ((inter*i)/(inter-1))
    return pmt


def payment_vf(vf, i, n):
    inter = pow(1 + i, n)
    pmt = vf * (i/inter - 1)
    return pmt


def gradiantes_pos(p, i, n, g):
    inter = pow(1 + i, n)
    vp = p * ((inter-1)/(inter*i)) + (g/i) * ((inter-1)/(inter*i)) * (n/inter)
    return vp


def gradiantes_neg(p, i, n, g):
    inter = pow(1 + i, n)
    vp = p * ((inter-1)/(inter*i)) - (g/i) * ((inter-1)/(inter*i)) * (n/inter)
    return vp


def gradiante_escala(p, e, i, n):
    vp = (p/(e-i)) * (pow((1+e/1+i), n) - 1)
    return vp

# Pagina 3 ---------------------------------------------------------------


def amortizacion(vp, i, n, n_actual):
    # buscar formula
    return None


def credito_cuota_fija(vp, i, n):
    inter = pow(1+i, n)
    cuota = vp * ((inter*i)/(inter-1))
    return cuota


def bonos_vp(interes, i, n, v_nominal):
    inter = pow(1 + i, n)
    vp = interes * ((inter-1)/(inter*i)) + (v_nominal/inter)
    return vp


# Pagina 4 -----------------------------------------------


def tasa_interes_real(i, f):
    ir = ((i-f) / (1+f))
    return ir


def tasa_inflada(ir, f):
    t_if = ir + (ir+f) + f
    return t_if


def valor_presente_inflacion(vp, i, f, n):
    ir = tasa_de_interes(i, f)
    v = vp * pow((1+ir), n)
    return v


def valor_futuro_inflacion(vp, f, n):
    vf = vp * pow(1+f, n)
    return vf


# End Document
