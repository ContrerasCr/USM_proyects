import openpyxl

wb1 = openpyxl.load_workbook('BBDD Empresas Arreglada.xlsx')

core = wb1['Datos']

len_core = len(core['A']) + 1

row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

for i in row:
    for j in range(2, len_core):
        value = str(core[str(i)+str(j)].value)
        lis = list(value)

        if lis[-1] == '.':
            print(core[str(i) + str(j)].value)
            lis.pop(-1)
            new = ''.join(lis)
            core[str(i)+str(j)] = new
            print(core[str(i)+str(j)].value)

wb1.save('BBDD Empresas Arreglada.xlsx')
print('End')