import openpyxl


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


def fix_rut(name, num):

    try:
        value = name.split('-')
        rut = value[0]
        verificador = value[1]
        revert = rut[::-1]
        count = 0
        new_val = []
        for i in range(len(rut)):

            if count != 3:
                count += 1
                new_val.append(revert[i])
            if count == 3:
                new_val.append('.')
                count = 0

        new_val.reverse()
        new_val.append('-')
        new_val.append(verificador)
        alele = ''.join(new_val)

        return alele

    except IndexError:
        print(name, num)




wb2 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')

core = wb2['Datos']

len_core = len(core['A']) + 1


for y in range(2, len_core):
#editar columna 'D'
    val = str(core['D' + str(y)].value)

    if '-' in val:
        print(val)
        corr = solve_space(val)
        corr = solve_dot(corr)
        corr = fix_rut(corr, y)
        core['D' + str(y)] = corr


wb2.save("BBDD Empresas Arreglada.xlsx")