import openpyxl

def corrector_minusculas(palabra):
    ramo = palabra
    ramo = ramo.lower()
    return ramo


wb2 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')

shop = wb2['Datos']
hoja1 = ['B']
len_core = len(shop['A']) + 1

for x in hoja1:
    for y in range(2, len_core):
        val = str(shop[str(x)+str(y)].value)
        corr = corrector_minusculas(val)
        print(corr)
        shop[str(x) + str(y)] = corr

wb2.save('BBDD Empresas Arreglada.xlsx')