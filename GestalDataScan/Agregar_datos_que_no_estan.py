#Agregar datos faltantes

import openpyxl
wb1 = openpyxl.load_workbook('BBDD Empresas.xlsx')
wb2 = openpyxl.load_workbook('BBDD Universal Arreglada.xlsx')

core = wb1['Empresas']
shop = wb2['Oferta']

len_core = len(core['A']) + 1
len_shop = len(shop['A']) + 1

for i in range(3, len_core):
    for j in range(2, len_shop):
        comp_core = [core['A'+str(i)].value, core['E'+str(i)].value]
        comp_shop = [shop['A'+str(j)].value, shop['E'+str(j)].value]
        if comp_core == comp_shop:
            print(comp_shop,comp_core, 'Value')


            control_core = [core['A'+str(i)].value, core['B'+str(i)].value,
                            core['C'+str(i)].value, core['D'+str(i)].value,
                            core['F'+str(i)].value, core['G'+str(i)].value]


            control_shop = [shop['A'+str(i)].value, shop['B'+str(i)].value,
                            shop['C'+str(i)].value, shop['D'+str(i)].value,
                            shop['F'+str(i)].value, shop['G'+str(i)].value]

#wb2.save("Base de Datos empresas nueva 2.xlsx")
print('End')