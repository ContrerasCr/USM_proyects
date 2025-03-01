import openpyxl

def corrector(palabra):
    #if ('S.A' or 'LTDA' or 'S.A.' or 'SPA' or 'SpA' or 'S A') in palabra:

    ramo = palabra
    ramo = ramo.lower()
    lis = ramo.split()
    fr = []
    for i in lis:
        la = list(i)
        n = la[0].upper()
        la[0] = n
        tt = ''.join(la)
        fr.append(tt)

    frase = ' '.join(fr)
    return frase


wb2 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')

core = wb2['Datos']

abecedario =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
             'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
             'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
             'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó',
             'ú', 'ñ', 'Ñ', 'Á', 'É', 'Í', 'Ó', 'Ú',
             '@', '.', '&', ' ', '-', '@', '0', '1',
             '2', '3', '4', '5', '6', '7', '8', '9',
             '+', '_']

hoja1 = ['B', 'D', 'E', 'F', 'G']



len_core = len(core['A']) + 1


for x in hoja1:
    for y in range(2, len_core):
        val = str(core[str(x)+str(y)].value)
        corr = corrector(val)
        print(corr)
        core[str(x) + str(y)] = corr
        print(core['B' + str(y)].value)

wb2.save("BBDD Empresas Arreglada.xlsx")