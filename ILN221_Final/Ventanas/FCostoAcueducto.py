from tkinter import *
import matplotlib.pyplot as plt
from funciones import poner_punto_de_miles


def calculo_van(costos, descuento):
    van = 0
    descuento = descuento * 0.01
    for i in range(0, len(costos)):
        value = costos[i] / pow(1 + descuento, i)
        van += value
    van = int(van)
    val = str(van)
    val = poner_punto_de_miles(val)
    return val


class CostoAcueducto(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Variables

        self.met_inst = IntVar(self, value=221)
        self.pre_bomb = IntVar(self, value=7580656)
        self.cant_bomb = IntVar(self, value=1)
        self.cost_elec = DoubleVar(self, value=176800)
        self.mas_error = DoubleVar(self, value=10)
        self.descuento = DoubleVar(self, value=5)

        Label(self, text='Costos instalacion Tuberias', font=18).place(x=20, y=30)

        Label(self, text='Metros de tubería').place(x=20, y=60)
        Entry(self, width=12, textvariable=self.met_inst).place(x=150, y=60)
        Label(self, text='Precio de la Bomba').place(x=20, y=90)
        Entry(self, width=12, textvariable=self.pre_bomb).place(x=150, y=90)

        Label(self, text='Cantidad de Bombas').place(x=20, y=120)
        Label(self, text='Costo electricidad MWh').place(x=20, y=150)
        Entry(self, width=12, textvariable=self.cant_bomb).place(x=150, y=120)
        Entry(self, width=12, textvariable=self.cost_elec).place(x=150, y=150)

        Button(self, text='Calcular y Graficar', command=lambda: self.graficar()).place(x=150, y=190)

        Label(self, text='Margen de error (%)').place(x=20, y=250)
        Entry(self, width=12, textvariable=self.mas_error).place(x=150, y=250)
        Label(self, text='Tasa de descuento (%)').place(x=20, y=280)
        Entry(self, width=12, textvariable=self.descuento).place(x=150, y=280)
        Button(self, text='Analisis de sensibilidad', command=lambda: self.sensibilidad()).place(x=150, y=310)

    def graficar(self):

        met_in_g = self.met_inst.get()
        pre_bomb_g = self.pre_bomb.get()
        can_bomb_g = self.cant_bomb.get()
        cost_ele_g = self.cost_elec.get()

        costo_inversion = met_in_g * 48696 + pre_bomb_g * can_bomb_g
        costo_uso = cost_ele_g * 262.8 * can_bomb_g

        years = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        gasto_ele = []
        gasto_acu = costo_inversion
        for t in years:
            gasto_acu += costo_uso
            gasto_ele.append(gasto_acu)

        plt.ion()
        plt.figure('Costos totales acumulados')
        plt.scatter(years, gasto_ele)
        plt.xlabel('Años')
        plt.ylabel('Poblacion')
        plt.show()

        Label(self, text='Costo Total: ').place(x=300, y=150)
        Label(self, text=poner_punto_de_miles(int(gasto_ele[-1]))).place(x=400, y=150)

    def sensibilidad(self):

        met_in_g = self.met_inst.get()
        pre_bomb_g = self.pre_bomb.get()
        can_bomb_g = self.cant_bomb.get()
        cost_ele_g = self.cost_elec.get()
        error = self.mas_error.get()
        descuento = self.descuento.get()

        costo_inversion = met_in_g * 48696 + pre_bomb_g * can_bomb_g
        costo_uso_id = cost_ele_g * 262.8 * can_bomb_g
        costo_uso_menos = cost_ele_g * 262.8 * can_bomb_g * (1 - (0.01 * error))
        costo_uso_mas = cost_ele_g * 262.8 * can_bomb_g * (1 + (0.01 * error))

        years = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        gasto_tot_id = []
        gasto_tot_low = []
        gasto_tot_up = []

        gasto_cre_id = []
        gasto_cre_low = []
        gasto_cre_up = []
        gasto_acu_id = costo_inversion
        gasto_acu_low = costo_inversion
        gasto_acu_up = costo_inversion
        for t in years:
            if t == 0:
                gast_ti = costo_inversion
                gast_tl = costo_inversion
                gast_tu = costo_inversion
            else:
                gast_ti = costo_uso_id
                gast_tl = costo_uso_menos
                gast_tu = costo_uso_mas

                gasto_acu_id += costo_uso_id
                gasto_acu_low += costo_uso_menos
                gasto_acu_up += costo_uso_mas

            gasto_tot_id.append(gast_ti)
            gasto_tot_low.append(gast_tl)
            gasto_tot_up.append(gast_tu)
            gasto_cre_id.append(gasto_acu_id)
            gasto_cre_low.append(gasto_acu_low)
            gasto_cre_up.append(gasto_acu_up)

        plt.ion()
        plt.figure('Costos totales acumulados')
        plt.scatter(years, gasto_cre_id)
        plt.scatter(years, gasto_cre_low)
        plt.scatter(years, gasto_cre_up)
        plt.xlabel('Años')
        plt.ylabel('Costos ($)')
        plt.show()

        van0 = calculo_van(gasto_tot_id, descuento)
        van_low = calculo_van(gasto_tot_low, descuento)
        van_up = calculo_van(gasto_tot_up, descuento)

        Label(self, text='VAN Ideal: ').place(x=20, y=350)
        Label(self, text='VAN Maximo: ').place(x=20, y=380)
        Label(self, text='VAN Minimo: ').place(x=20, y=410)

        Label(self, text=van0).place(x=150, y=350)
        Label(self, text=van_low).place(x=150, y=410)
        Label(self, text=van_up).place(x=150, y=380)

# End Document
