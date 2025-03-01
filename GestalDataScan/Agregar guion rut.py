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
        lis = list(name)
        verificador = lis[-1]
        lis.pop(-1)
        lis.append('-')
        lis.append(verificador)
        casa = ''.join(lis)

        return casa

    except IndexError:
        print(name, num)




wb2 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')

core = wb2['Datos']

len_core = len(core['A']) + 1


for y in range(2, len_core):

    val = str(core['B' + str(y)].value)

    if '-' not in val and val != 'None':
        print(val, ' B',y)
        corr = solve_space(val)
        corr = solve_dot(corr)
        corr = fix_rut(corr, y)
        core['B' + str(y)] = corr


wb2.save("BBDD Empresas Arreglada.xlsx")