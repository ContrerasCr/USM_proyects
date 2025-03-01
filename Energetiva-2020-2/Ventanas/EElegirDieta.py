from tkinter import *
from tkinter import ttk
import funciones
import numpy as np


class ElegirDieta(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        self.dieta_value = StringVar(self, 'HombreAdulto')

        self.var_zanahoria = IntVar(self, value=0)
        self.var_espinaca = IntVar(self, value=0)
        self.var_repollo = IntVar(self, value=0)
        self.var_lechuga = IntVar(self, value=0)
        self.var_pimiento_verde = IntVar(self, value=0)
        self.var_pimiento_rojo = IntVar(self, value=0)
        self.var_zapallo_cocido = IntVar(self, value=0)
        self.var_palta = IntVar(self, value=0)
        self.var_guayaba = IntVar(self, value=0)
        self.var_papa = IntVar(self, value=0)
        self.var_coliflor_cocida = IntVar(self, value=0)
        self.var_damasco = IntVar(self, value=0)
        self.var_nuez = IntVar(self, value=0)
        self.var_almendra = IntVar(self, 0)

        Label(self, text='Mejores alimentos por relacion nutriente / consumo de agua').place(x=20, y=20)
        Label(self, text='Cada 100grx   ').place(x=20, y=40)
        Label(self, text='Dietas   ', font=14).place(x=580, y=240)
        Radiobutton(self, text='Grupo 1', variable=self.dieta_value, value='Grupo1').place(x=600, y=280)
        Radiobutton(self, text='Grupo 2', variable=self.dieta_value, value='Grupo2').place(x=600, y=310)
        Radiobutton(self, text='Grupo 3', variable=self.dieta_value, value='Grupo3').place(x=600, y=340)

        Button(self, text='Calcular', command=lambda: self.activador()).place(x=510, y=250)
        Label(self, text='Dieta Recomendada').place(x=20, y=300)
        Label(self, text='Dieta Obtenida').place(x=20, y=330)

        # Column 0
        Entry(self, width=4, textvariable=self.var_nuez).place(x=10, y=90)
        Entry(self, width=4, textvariable=self.var_almendra).place(x=10, y=120)
        Entry(self, width=4, textvariable=self.var_palta).place(x=10, y=150)
        Entry(self, width=4, textvariable=self.var_papa).place(x=10, y=180)
        Entry(self, width=4, textvariable=self.var_pimiento_rojo).place(x=10, y=210)
        Label(self, text='Energia').place(x=20, y=60)
        Label(self, text='Nuez').place(x=40, y=90)
        Label(self, text='Almendra').place(x=40, y=120)
        Label(self, text='Palta').place(x=40, y=150)
        Label(self, text='Papa Cocida').place(x=40, y=180)
        Label(self, text='Pimiento Rojo').place(x=40, y=210)

        # Column 1
        Entry(self, width=4, textvariable=self.var_almendra).place(x=140, y=90)
        Entry(self, width=4, textvariable=self.var_nuez).place(x=140, y=120)
        Entry(self, width=4, textvariable=self.var_lechuga).place(x=140, y=150)
        Entry(self, width=4, textvariable=self.var_pimiento_rojo).place(x=140, y=180)
        Entry(self, width=4, textvariable=self.var_espinaca).place(x=140, y=210)
        Label(self, text='Proteinas').place(x=150, y=60)
        Label(self, text='Almendra').place(x=170, y=90)
        Label(self, text='Nuez').place(x=170, y=120)
        Label(self, text='Lechuga').place(x=170, y=150)
        Label(self, text='Pimiento Rojo').place(x=170, y=180)
        Label(self, text='Espinaca').place(x=170, y=210)

        # Column 2
        Entry(self, width=4, textvariable=self.var_papa).place(x=270, y=90)
        Entry(self, width=4, textvariable=self.var_pimiento_rojo).place(x=270, y=120)
        Entry(self, width=4, textvariable=self.var_damasco).place(x=270, y=150)
        Entry(self, width=4, textvariable=self.var_zapallo_cocido).place(x=270, y=180)
        Entry(self, width=4, textvariable=self.var_guayaba).place(x=270, y=210)
        Label(self, text='Carbohidratos').place(x=280, y=60)
        Label(self, text='Papa cocida').place(x=300, y=90)
        Label(self, text='Pimiento Rojo').place(x=300, y=120)
        Label(self, text='Damasco').place(x=300, y=150)
        Label(self, text='Zapallo Cocido').place(x=300, y=180)
        Label(self, text='Guayaba').place(x=300, y=210)

        # Column 3
        Entry(self, width=4, textvariable=self.var_almendra).place(x=400, y=90)
        Entry(self, width=4, textvariable=self.var_espinaca).place(x=400, y=120)
        Entry(self, width=4, textvariable=self.var_lechuga).place(x=400, y=150)
        Entry(self, width=4, textvariable=self.var_repollo).place(x=400, y=180)
        Entry(self, width=4, textvariable=self.var_nuez).place(x=400, y=210)
        Label(self, text='Calcio').place(x=410, y=60)
        Label(self, text='Almendra').place(x=430, y=90)
        Label(self, text='Espinaca').place(x=430, y=120)
        Label(self, text='Lechuga').place(x=430, y=150)
        Label(self, text='Repollo').place(x=430, y=180)
        Label(self, text='Nuez').place(x=430, y=210)

        # Column 4
        Entry(self, width=4, textvariable=self.var_espinaca).place(x=530, y=90)
        Entry(self, width=4, textvariable=self.var_lechuga).place(x=530, y=120)
        Entry(self, width=4, textvariable=self.var_almendra).place(x=530, y=150)
        Entry(self, width=4, textvariable=self.var_nuez).place(x=530, y=180)
        Entry(self, width=4, textvariable=self.var_pimiento_verde).place(x=530, y=210)
        Label(self, text='Hierro').place(x=540, y=60)
        Label(self, text='Espinaca').place(x=560, y=90)
        Label(self, text='Lechuga').place(x=560, y=120)
        Label(self, text='Almendra').place(x=560, y=150)
        Label(self, text='Nuez').place(x=560, y=180)
        Label(self, text='Pimiento Verde').place(x=560, y=210)

        # Column 5
        Entry(self, width=4, textvariable=self.var_pimiento_rojo).place(x=660, y=90)
        Entry(self, width=4, textvariable=self.var_zapallo_cocido).place(x=660, y=120)
        Entry(self, width=4, textvariable=self.var_espinaca).place(x=660, y=150)
        Entry(self, width=4, textvariable=self.var_zanahoria).place(x=660, y=180)
        Entry(self, width=4, textvariable=self.var_lechuga).place(x=660, y=210)
        Label(self, text='Vitamina A').place(x=670, y=60)
        Label(self, text='Pimiento Rojo').place(x=690, y=90)
        Label(self, text='Zapallo cocido').place(x=690, y=120)
        Label(self, text='Espinaca').place(x=690, y=150)
        Label(self, text='Zanahoria').place(x=690, y=180)
        Label(self, text='Lechuga').place(x=690, y=210)

        # Column 6
        Entry(self, width=4, textvariable=self.var_pimiento_rojo).place(x=790, y=90)
        Entry(self, width=4, textvariable=self.var_pimiento_verde).place(x=790, y=120)
        Entry(self, width=4, textvariable=self.var_guayaba).place(x=790, y=150)
        Entry(self, width=4, textvariable=self.var_repollo).place(x=790, y=180)
        Entry(self, width=4, textvariable=self.var_coliflor_cocida).place(x=790, y=210)
        Label(self, text='Vitamina C').place(x=800, y=60)
        Label(self, text='Pimiento Rojo').place(x=820, y=90)
        Label(self, text='Pimineto Verde').place(x=820, y=120)
        Label(self, text='Guayaba').place(x=820, y=150)
        Label(self, text='Repollo').place(x=820, y=180)
        Label(self, text='Coliflor Cocida').place(x=820, y=210)

        Label(self, text='Energia').place(x=120, y=280)
        Label(self, text='Proteinas').place(x=170, y=280)
        Label(self, text='Carbohi.').place(x=230, y=280)
        Label(self, text='Calcio').place(x=290, y=280)
        Label(self, text='Hierro').place(x=350, y=280)
        Label(self, text='Vit. A').place(x=410, y=280)
        Label(self, text='Vit. C').place(x=470, y=280)

    def activador(self):
        self.place_values()
        self.place_dieta()

    def place_values(self):
        # Dieta por clasificacion demografica
        dieta = {'Grupo1': [1100, 43.6, 159, 335, 7.7, 0, 14.6], 'Grupo2': [1900, 69, 250, 664, 12, 0.4, 55],
                 'Grupo3': [2550, 93.6, 325, 993, 15.5, 0.863, 91.4]}
        eleccion_dieta = self.dieta_value.get()

        try:
            dieta_recomendada = list(dieta[eleccion_dieta])
            cadena = []
            for val in dieta_recomendada:
                val = str(val)
                val2 = val.rjust(13)
                cadena.append(val2)
            string = ''.join(cadena)
            Label(self, text=string).place(x=150, y=300)
        except KeyError:
            pass

    def place_dieta(self):
        self.v_za = self.var_zanahoria.get()
        self.v_es = self.var_espinaca.get()
        self.v_re = self.var_repollo.get()
        self.v_le = self.var_lechuga.get()
        self.v_pv = self.var_pimiento_verde.get()
        self.v_pr = self.var_pimiento_rojo.get()
        self.v_zc = self.var_zapallo_cocido.get()
        self.v_pal = self.var_palta.get()
        self.v_gu = self.var_guayaba.get()
        self.v_pap = self.var_papa.get()
        self.v_cc = self.var_coliflor_cocida.get()
        self.v_da = self.var_damasco.get()
        self.v_nu = self.var_nuez.get()
        self.v_al = self.var_almendra.get()

        self.za = np.array([23.91, 0.63, 4.75, 27.00, 0.50, 0.44, 3.80])
        self.es = np.array([20.74, 2.63, 0.61, 117.00, 2.70, 0.59, 40.00])
        self.re = np.array([30.20, 1.38, 4.18, 45.00, 0.41, 0.01, 48.00])
        self.le = np.array([19.60, 1.37, 1.40, 34.70, 1.00, 0.19, 13.00])
        self.pv = np.array([19.68, 0.63, 1.60, 11.31, 0.49, 0.03, 107.19])
        self.pr = np.array([32.90, 1.25, 4.20, 11.89, 0.37, 0.54, 138.73])
        self.zc = np.array([32.00, 1.10, 7.70, 18.30, 0.40, 0.74, 6.50])
        self.pal = np.array([233.0, 1.88, 0.40, 12.00, 0.49, 0.01, 6.00])
        self.gu = np.array([57.00, 0.82, 11.90, 17.00, 0.60, 0.07, 273.00])
        self.pap = np.array([73.59, 2.34, 14.80, 6.40, 0.43, 0.09, 17.00])
        self.cc = np.array([27.52, 2.44, 0.00, 19.26, 0.84, 0.01, 58.77])
        self.da = np.array([41.68, 0.88, 8.54, 16.00, 0.65, 0.28, 6.00])
        self.nu = np.array([649.00, 14.42, 4.40, 87.10, 2.80, 0.00, 2.60])
        self.al = np.array([589.00, 19.13, 6.20, 248.25, 3.59, 0.00, 0.00])

        mult_za = self.za * self.v_za
        mult_es = self.es * self.v_es
        mult_re = self.re * self.v_re
        mult_le = self.le * self.v_le
        mult_pv = self.pv * self.v_pv
        mult_pr = self.pr * self.v_pr
        mult_zc = self.zc * self.v_zc
        mult_pal = self.pal * self.v_pal
        mult_gu = self.gu * self.v_gu
        mult_pap = self.pap * self.v_pap
        mult_cc = self.cc * self.v_cc
        mult_da = self.da * self.v_da
        mult_nu = self.nu * self.v_nu
        mult_al = self.al * self.v_al

        recursos_totales_1 = mult_za+mult_es + mult_re + mult_le + mult_pv + mult_pr
        recursos_totales_2 = mult_zc + mult_pal + mult_gu + mult_pap + mult_cc + mult_da + mult_nu + mult_al
        recursos_totales = recursos_totales_1 + recursos_totales_2
        try:
            dieta_recomendada = list(recursos_totales)
            cadena = []
            for val in dieta_recomendada:
                val = round(val, 1)
                val = str(val)
                val2 = val.rjust(13)
                cadena.append(val2)
            string = ''.join(cadena)
            Label(self, text=string).place(x=150, y=330)
        except KeyError:
            pass

        self.agua_za = np.array([23.91, 0.63, 4.75, 27.00, 0.50, 0.44, 3.80])
        self.agua_es = np.array([20.74, 2.63, 0.61, 117.00, 2.70, 0.59, 40.00])
        self.agua_re = np.array([30.20, 1.38, 4.18, 45.00, 0.41, 0.01, 48.00])
        self.agua_le = np.array([19.60, 1.37, 1.40, 34.70, 1.00, 0.19, 13.00])
        self.agua_pv = np.array([19.68, 0.63, 1.60, 11.31, 0.49, 0.03, 107.19])
        self.agua_pr = np.array([32.90, 1.25, 4.20, 11.89, 0.37, 0.54, 138.73])
        self.agua_zc = np.array([32.00, 1.10, 7.70, 18.30, 0.40, 0.74, 6.50])
        self.agua_pal = np.array([233.0, 1.88, 0.40, 12.00, 0.49, 0.01, 6.00])
        self.agua_gu = np.array([57.00, 0.82, 11.90, 17.00, 0.60, 0.07, 273.00])
        self.agua_pap = np.array([73.59, 2.34, 14.80, 6.40, 0.43, 0.09, 17.00])
        self.agua_cc = np.array([27.52, 2.44, 0.00, 19.26, 0.84, 0.01, 58.77])
        self.agua_da = np.array([41.68, 0.88, 8.54, 16.00, 0.65, 0.28, 6.00])
        self.agua_nu = np.array([649.00, 14.42, 4.40, 87.10, 2.80, 0.00, 2.60])
        self.agua_al = np.array([589.00, 19.13, 6.20, 248.25, 3.59, 0.00, 0.00])

        mult_za = self.agua_za * self.v_za
        mult_es = self.agua_es * self.v_es
        mult_re = self.agua_re * self.v_re
        mult_le = self.agua_le * self.v_le
        mult_pv = self.agua_pv * self.v_pv
        mult_pr = self.agua_pr * self.v_pr
        mult_zc = self.agua_zc * self.v_zc
        mult_pal = self.agua_pal * self.v_pal
        mult_gu = self.agua_gu * self.v_gu
        mult_pap = self.agua_pap * self.v_pap
        mult_cc = self.agua_cc * self.v_cc
        mult_da = self.agua_da * self.v_da
        mult_nu = self.agua_nu * self.v_nu
        mult_al = self.agua_al * self.v_al

