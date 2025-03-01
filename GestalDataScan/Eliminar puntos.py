import openpyxl


def solve_dot(name):

    if '.' in name:
        newname = list(name)

        while '.' in newname:
            newname.remove('.')

        brandname = ''.join(newname)
        return brandname

    else:
        return name


wb2 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')

core = wb2['Datos']

len_core = len(core['A']) + 1


for y in range(2, len_core):

    val = str(core['F' + str(y)].value)

    if '.' in val:
        print(val)
        corr = solve_dot(val)
        core['F' + str(y)] = corr
        print(corr)

wb2.save("BBDD Empresas Arreglada.xlsx")