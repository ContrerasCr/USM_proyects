import openpyxl

def corrector(palabra,coor):
    #if ('S.A' or 'LTDA' or 'S.A.' or 'SPA' or 'SpA' or 'S A') in palabra:
    for i in palabra:
        if i not in abecedario:

            return coor


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
             '+', ',', "'", '(', ')', '&', '"', '/', '_']

hoja1 = ['A', 'C', 'D', 'E']

#print(list(shop['A'+'5897'].value))

len_core = len(core['A']) + 1


for i in range(2, len_core):
    coor = 'G' + str(i)
    try:
        if corrector(core['G' + str(i)].value, 'G' + str(i)):
            print('G' + str(i), core['G' + str(i)].value)
    except TypeError:
        print('G' + str(i))


#wb2.save("BBDD Empresas Arreglada.xlsx")