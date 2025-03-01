import openpyxl
import numpy as np
# encoding=utf-8

# Obtener el dígito verificador del RUT en Python.
#
# La función recibe el RUT como un entero,
# y entrega el dígito verificador como un entero.
# Si el resultado es 10, el RUT es "raya k".

from itertools import cycle
def solve_space(name):

    if ' ' in name:
        newname = list(name)

        while ' ' in newname:
            newname.remove(' ')

        brandname = ''.join(newname)
        return brandname

    else:
        return name


def solve_dot(name):

    if '.' in name:
        newname = list(name)

        while '.' in newname:
            newname.remove('.')

        brandname = ''.join(newname)
        return brandname

    else:
        return name

def validarRut(rut, coor):

    if rut != 'None':
        rut = rut.lower()
        rut = solve_space(rut)
        rut = solve_dot(rut)
        valores = rut.split('-')
        numeros = valores[0]
        ver = valores[1]
        multiplicadores = np.array([2, 3, 4, 5, 6, 7, 2, 3], dtype=float)
        if len(numeros) == 8:
            multiplicadores = np.array([2, 3, 4, 5, 6, 7, 2, 3], dtype=float)
        elif len(numeros) == 7:
            multiplicadores = np.array([2, 3, 4, 5, 6, 7, 2], dtype=float)
        else:
            print(rut, coor, 'len != 8,7', coor)
            return

        numeros = list(numeros)
        numeros.reverse()
        numeradores = np.array(numeros, dtype=float)

        suma = float(np.dot(multiplicadores, numeradores))
        resto = int(suma) % 11

        pre_ver = 11-resto
        verificador = ''
        if pre_ver == 11:
            verificador = '0'
        elif pre_ver == 10:
            verificador = 'k'
        else:
            verificador= str(pre_ver)

        if verificador == ver:
            return True
        else:
            return False



wb2 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')

core = wb2['Datos']

len_core = len(core['A']) + 1


for y in range(2, len_core):

    val = str(core['C' + str(y)].value)

    value = validarRut(val, y)
    coor = 'C' + str(y)
    if value == False:
        print(coor, val)

#wb2.save("BBDD Empresas Arreglada.xlsx")