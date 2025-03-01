import openpyxl


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
             '+', '_', ',', "'", '(', ')', '&','"', '/']


def corrector(palabra, vall):
    #if ('S.A' or 'LTDA' or 'S.A.' or 'SPA' or 'SpA' or 'S A') in palabra:

    ramo = palabra
    ramo = ramo.lower()
    fr = palabra
    for i in palabra:

        if i not in abecedario:
            lis = ramo.split()
            print(i)
            for j in lis:
                base = lis

                if i in j:
                    posicion = lis.index(j)
                    print('pass')
                    try:

                        new_pal = list(j)
                        new_pal.remove(i)
                        frase = ''.join(new_pal)
                        print(frase)
                        base[posicion] = frase
                    except ValueError:
                        continue


            fr = ' '.join(base)

            print(fr, vall)
    return (fr)
wb2 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')

core = wb2['Datos']

hoja1 = ['A', 'C', 'D', 'E']

len_core = len(core['A']) + 1

flag = False

for y in range(2, len_core):
    val = core[('A'+str(y))].value
    corr = corrector(val, 'A' + str(y))
    core['A' + str(y)] = corr

wb2.save("BBDD Empresas Arreglada.xlsx")