# Funciones del programa principal
import variables
import numpy as np


def poner_punto_de_miles(value):

    value = str(value)
    lis = list(value)

    lis.reverse()
    grups = list()
    for i in range(0, len(lis), 3):
        try:
            grups.append(str(lis[i])+str(lis[i+1])+str(lis[i+2]))
        except IndexError:
            try:
                grups.append(str(lis[i]) + str(lis[i + 1]))
            except IndexError:
                grups.append(str(lis[i]))

    grups = '.'.join(grups)
    val = list(grups)
    val.reverse()
    ret = ''.join(val)
    ret = '$' + ret

    return ret


def fun_de_poblacion(po, mi, mni, r, t):

    mi_matriz = np.array(mi)
    mni_matriz = np.array(mni)
    razon = mi_matriz * (1/mni_matriz)
    productoria = 0
    pj_t = po * pow(2.718, 10*r*t) * pow(mi * mni, (1/10))


# Mejores 5 alimientos por recurso
# 0: Energia, 1:Proteina, 2:Carbohidratos, 3:Calcio, 4:Hierro, 5:Vit.A, 6:Vit.C
# recurso es un int entre 0 y 6


def mejor_por_recurso(recurso):
    alimentos = variables.dat_dic_nut().keys()
    nutrientes = variables.dat_dic_nut()
    consumo_agua = variables.consumo_dict_agua()
    recurso_s_agua = {}
    for value in alimentos:
        disponibilidad = nutrientes[value][recurso]
        agua = consumo_agua[value]
        relacion = round(disponibilidad / agua, 7)
        recurso_s_agua[value] = relacion
    valores = list(recurso_s_agua.values())
    valores.sort(reverse=True)
    top_five = valores[:5]
    top_five_values = []
    for i in recurso_s_agua.items():
        for k in top_five:
            if k in i:
                alimento, nutri = i
                tup = (nutri, alimento)
                top_five_values.append(tup)
    top_five_values.sort(reverse=True)
    # Devuelve los 5 alimentos mas eficientes de ese recurso
    return top_five_values


# Retorna mejores 5 aliemntos, solo nombre en una lista
# 0: Energia, 1:Proteina, 2:Carbohidratos, 3:Calcio, 4:Hierro, 5:Vit.A, 6:Vit.C
# recurso es un int entre 0 y 6
def top_five_alimentos(recurso):
    nutr = mejor_por_recurso(recurso)
    lista_top_five = []
    for alim in nutr:
        val, al = alim
        lista_top_five.append(al)
    return lista_top_five


# Devuelve en una lista una tupla con el nombre del recurso y los valores nutricionales
# 0: Energia, 1:Proteina, 2:Carbohidratos, 3:Calcio, 4:Hierro, 5:Vit.A, 6:Vit.C
# recurso es un int entre 0 y 6
def lista_alimentos_nutrientes(recursos):
    alimentos = top_five_alimentos(recursos)
    alimentos_y_recursos = []
    for values in alimentos:
        diccionario_nutrientes = variables.dat_dic_nut()
        nutrientes = diccionario_nutrientes[values]
        tup = (values, nutrientes)
        alimentos_y_recursos.append(tup)
    return alimentos_y_recursos


# Recibe una lista de strings y devuelve los valores en un string concatenado
def join_list_nut(lista):
    lista = list(lista)
    lis = lista[:]
    lis.remove('(')
    lis.remove(')')
    lis2 = ''.join(lis)
    lis2 = lis2.split(',')
    liss = []
    for val in lis2:
        val2 = val.rjust(13)
        liss.append(val2)
    liss2 = '   '.join(liss)
    liss2 = liss2 + '               '
    return liss2


# Consumo de combustible, recibe cantidad de combustible consumido
def produccion_co2(comb_consumido):
    co2_producido = comb_consumido*2.65
    return co2_producido


def costo_transporte_x_dia(aguatransportada, kmruta, consumoxlitrocamion, cantidadcamiones,
                           preciocombustible, litrosnecesarios, costocamion):

    camionesunitariosneces = litrosnecesarios / aguatransportada  # Camiones totales necesarios.
    distancia_total = camionesunitariosneces * kmruta  # Km totales que tiene que recorrer indiferente de la cant de cam
    consumo_combustible_tot = distancia_total / consumoxlitrocamion  # Lt de combustible total
    gasto_arriendo_tot = cantidadcamiones * costocamion
    vueltas_necesarias_tot = camionesunitariosneces / cantidadcamiones

    consumo_combustible = round(consumo_combustible_tot, 2)
    vehiculos_necesarios = round(cantidadcamiones, 2)
    vueltas_necesarias = round(vueltas_necesarias_tot, 2)
    gasto_combustible = round(consumo_combustible_tot * preciocombustible, 2)
    gasto_arriendo = round(gasto_arriendo_tot, 2)
    prod_co2 = produccion_co2(consumo_combustible)
    valores_retorno = [int(consumo_combustible), int(vehiculos_necesarios),
                       int(vueltas_necesarias), poner_punto_de_miles(int(gasto_combustible)),
                       poner_punto_de_miles(int(gasto_arriendo)), int(prod_co2)]
    return valores_retorno


# End Document
