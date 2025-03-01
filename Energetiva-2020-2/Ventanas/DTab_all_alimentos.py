from tkinter import *
import numpy as np


class TodosLosAlimentos(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        self.var_platano = DoubleVar(self, value=0)
        self.var_zanahoria = DoubleVar(self, value=0)
        self.var_berenjena = DoubleVar(self, value=0)
        self.var_espinaca = DoubleVar(self, value=0)
        self.var_repollo = DoubleVar(self, value=0)
        self.var_lechuga = DoubleVar(self, value=0)
        self.var_cebolla = DoubleVar(self, value=0)
        self.var_pimiento_verde = DoubleVar(self, value=0)
        self.var_pimiento_rojo = DoubleVar(self, value=0)
        self.var_zapallo_cocido = DoubleVar(self, value=0)
        self.var_tomate = DoubleVar(self, value=0)
        self.var_palta = DoubleVar(self, value=0)
        self.var_naranja = DoubleVar(self, value=0)
        self.var_lima = DoubleVar(self, value=0)
        self.var_limon = DoubleVar(self, value=0)
        self.var_guayaba = DoubleVar(self, value=0)
        self.var_mango = DoubleVar(self, value=0)
        self.var_pina = DoubleVar(self, value=0)
        self.var_sandia = DoubleVar(self, value=0)
        self.var_papa = DoubleVar(self, value=0)
        self.var_apio = DoubleVar(self, value=0)
        self.var_coliflor_cocida = DoubleVar(self, value=0)
        self.var_haba_cocida = DoubleVar(self, value=0)
        self.var_cereza = DoubleVar(self, value=0)
        self.var_damasco = DoubleVar(self, value=0)
        self.var_manzana = DoubleVar(self, value=0)
        self.var_nuez = DoubleVar(self, value=0)
        self.var_almendra = DoubleVar(self, value=0)
        self.var_kiwi = DoubleVar(self, value=0)

        Label(self, text='Arma tu dieta [1=100gr del producto]').place(x=10, y=20)
        Button(self, text='Calcular', command=lambda: self.place_dieta()).place(x=20, y=250)
        Label(self, text='Nutrientes Obtenidos').place(x=20, y=330)

        # Column 0
        Entry(self, width=4, textvariable=self.var_platano).place(x=10, y=90)
        Entry(self, width=4, textvariable=self.var_zanahoria).place(x=10, y=120)
        Entry(self, width=4, textvariable=self.var_berenjena).place(x=10, y=150)
        Entry(self, width=4, textvariable=self.var_espinaca).place(x=10, y=180)
        Entry(self, width=4, textvariable=self.var_repollo).place(x=10, y=210)
        Label(self, text='Platano').place(x=40, y=90)
        Label(self, text='Zanahoria').place(x=40, y=120)
        Label(self, text='Berengena').place(x=40, y=150)
        Label(self, text='Espinaca').place(x=40, y=180)
        Label(self, text='Repollo').place(x=40, y=210)

        # Column 1
        Entry(self, width=4, textvariable=self.var_lechuga).place(x=140, y=90)
        Entry(self, width=4, textvariable=self.var_cebolla).place(x=140, y=120)
        Entry(self, width=4, textvariable=self.var_pimiento_verde).place(x=140, y=150)
        Entry(self, width=4, textvariable=self.var_pimiento_rojo).place(x=140, y=180)
        Entry(self, width=4, textvariable=self.var_zapallo_cocido).place(x=140, y=210)
        Label(self, text='Lechuga').place(x=170, y=90)
        Label(self, text='Cebolla').place(x=170, y=120)
        Label(self, text='Pimiento Verde').place(x=170, y=150)
        Label(self, text='Pimiento Rojo').place(x=170, y=180)
        Label(self, text='Zapallo Cocido').place(x=170, y=210)

        # Column 2
        Entry(self, width=4, textvariable=self.var_tomate).place(x=270, y=90)
        Entry(self, width=4, textvariable=self.var_palta).place(x=270, y=120)
        Entry(self, width=4, textvariable=self.var_naranja).place(x=270, y=150)
        Entry(self, width=4, textvariable=self.var_lima).place(x=270, y=180)
        Entry(self, width=4, textvariable=self.var_limon).place(x=270, y=210)
        Label(self, text='Tomate').place(x=300, y=90)
        Label(self, text='Palta').place(x=300, y=120)
        Label(self, text='Naranja').place(x=300, y=150)
        Label(self, text='Lima').place(x=300, y=180)
        Label(self, text='Limon').place(x=300, y=210)

        # Column 3
        Entry(self, width=4, textvariable=self.var_guayaba).place(x=400, y=90)
        Entry(self, width=4, textvariable=self.var_mango).place(x=400, y=120)
        Entry(self, width=4, textvariable=self.var_pina).place(x=400, y=150)
        Entry(self, width=4, textvariable=self.var_sandia).place(x=400, y=180)
        Entry(self, width=4, textvariable=self.var_papa).place(x=400, y=210)
        Label(self, text='Guayaba').place(x=430, y=90)
        Label(self, text='Mango').place(x=430, y=120)
        Label(self, text='Piña').place(x=430, y=150)
        Label(self, text='Sandia').place(x=430, y=180)
        Label(self, text='Papa').place(x=430, y=210)

        # Column 4
        Entry(self, width=4, textvariable=self.var_apio).place(x=530, y=90)
        Entry(self, width=4, textvariable=self.var_coliflor_cocida).place(x=530, y=120)
        Entry(self, width=4, textvariable=self.var_haba_cocida).place(x=530, y=150)
        Entry(self, width=4, textvariable=self.var_cereza).place(x=530, y=180)
        Entry(self, width=4, textvariable=self.var_damasco).place(x=530, y=210)
        Label(self, text='Apio').place(x=560, y=90)
        Label(self, text='Coliflor Cocida').place(x=560, y=120)
        Label(self, text='Haba Cocida').place(x=560, y=150)
        Label(self, text='Cereza').place(x=560, y=180)
        Label(self, text='Damazco').place(x=560, y=210)

        # Column 5
        Entry(self, width=4, textvariable=self.var_manzana).place(x=660, y=90)
        Entry(self, width=4, textvariable=self.var_nuez).place(x=660, y=120)
        Entry(self, width=4, textvariable=self.var_almendra).place(x=660, y=150)
        Entry(self, width=4, textvariable=self.var_kiwi).place(x=660, y=180)
        Label(self, text='Manzana').place(x=690, y=90)
        Label(self, text='Nuez').place(x=690, y=120)
        Label(self, text='Almendra').place(x=690, y=150)
        Label(self, text='Kiwi').place(x=690, y=180)

    def place_dieta(self):

        self.v_pla = self.var_platano.get()
        self.v_zan = self.var_zanahoria.get()
        self.v_ber = self.var_berenjena.get()
        self.v_esp = self.var_espinaca.get()
        self.v_rep = self.var_repollo.get()
        self.v_lec = self.var_lechuga.get()
        self.v_ceb = self.var_cebolla.get()
        self.v_pve = self.var_pimiento_verde.get()
        self.v_pro = self.var_pimiento_rojo.get()
        self.v_zco = self.var_zapallo_cocido.get()
        self.v_tom = self.var_tomate.get()
        self.v_pal = self.var_palta.get()
        self.v_nar = self.var_naranja.get()
        self.v_lima = self.var_lima.get()
        self.v_lim = self.var_limon.get()
        self.v_gua = self.var_guayaba.get()
        self.v_man = self.var_mango.get()
        self.v_pin = self.var_pina.get()
        self.v_san = self.var_sandia.get()
        self.v_pap = self.var_papa.get()
        self.v_api = self.var_apio.get()
        self.v_cco = self.var_coliflor_cocida.get()
        self.v_hab = self.var_haba_cocida.get()
        self.v_cer = self.var_cereza.get()
        self.v_dam = self.var_damasco.get()
        self.v_man = self.var_manzana.get()
        self.v_nue = self.var_nuez.get()
        self.v_alm = self.var_almendra.get()
        self.v_kiw = self.var_kiwi.get()

        self.pla = np.array([95.03, 1.06, 20.80, 7.30, 0.59, 0.04, 11.50])
        self.zan = np.array([23.91, 0.63, 4.75, 27.00, 0.50, 0.44, 3.80])
        self.ber = np.array([21.02, 1.25, 2.39, 16.39, 0.40, 0.01, 5.87])
        self.esp = np.array([20.74, 2.63, 0.61, 117.00, 2.70, 0.59, 40.00])
        self.rep = np.array([30.20, 1.38, 4.18, 45.00, 0.41, 0.01, 48.00])
        self.lec = np.array([19.60, 1.37, 1.40, 34.70, 1.00, 0.19, 13.00])
        self.ceb = np.array([31.85, 1.19, 5.30, 25.40, 0.27, 0.00, 6.90])
        self.pve = np.array([19.68, 0.63, 1.60, 11.31, 0.49, 0.03, 107.19])
        self.pro = np.array([32.90, 1.25, 4.20, 11.89, 0.37, 0.54, 138.73])
        self.zco = np.array([32.00, 1.10, 7.70, 18.30, 0.40, 0.74, 6.50])
        self.tom = np.array([22.17, 0.88, 3.50, 10.60, 0.70, 0.22, 26.60])
        self.pal = np.array([233.0, 1.88, 0.40, 12.00, 0.49, 0.01, 6.00])
        self.nar = np.array([45.48, 0.87, 8.90, 41.00, 0.49, 0.03, 50.60])
        self.lima = np.array([8.00, 0.60, 1.00, 24.00, 0.00, 0.00, 42.00])
        self.lim = np.array([27.66, 0.69, 3.16, 11.00, 0.45, 0.06, 0.04])
        self.gua = np.array([57.00, 0.82, 11.90, 17.00, 0.60, 0.07, 273.00])
        self.man = np.array([61.13, 0.63, 12.80, 12.00, 0.40, 0.21, 37.00])
        self.pin = np.array([50.76, 0.44, 10.40, 14.50, 0.41, 0.01, 14.99])
        self.san = np.array([28.40, 0.63, 5.60, 6.72, 0.29, 0.04, 6.34])
        self.pap = np.array([73.59, 2.34, 14.80, 6.40, 0.43, 0.09, 17.00])
        self.api = np.array([19.20, 1.19, 2.47, 41.00, 0.40, 0.01, 7.00])
        self.cco = np.array([27.52, 2.44, 0.00, 19.26, 0.84, 0.01, 58.77])
        self.hab = np.array([50.40, 5.40, 4.20, 23.00, 1.80, 0.01, 24.00])
        self.cer = np.array([72.50, 0.88, 13.30, 17.00, 0.35, 0.01, 15.00])
        self.dam = np.array([41.68, 0.88, 8.54, 16.00, 0.65, 0.28, 6.00])
        self.man = np.array([54.08, 0.31, 11.40, 5.50, 0.56, 0.00, 12.40])
        self.nue = np.array([649.00, 14.42, 4.40, 87.10, 2.80, 0.00, 2.60])
        self.alm = np.array([589.00, 19.13, 6.20, 248.25, 3.59, 0.00, 0.00])
        self.kiw = np.array([51.80, 1.00, 9.12, 34.11, 0.37, 0.01, 43.14])

        self.mul_pla = self.v_pla * self.pla
        self.mul_zan = self.v_zan * self.zan
        self.mul_ber = self.v_ber * self.ber
        self.mul_esp = self.v_esp * self.esp
        self.mul_rep = self.v_rep * self.rep
        self.mul_lec = self.v_lec * self.lec
        self.mul_ceb = self.v_ceb * self.ceb
        self.mul_pve = self.v_pve * self.pve
        self.mul_pro = self.v_pro * self.pro
        self.mul_zco = self.v_zco * self.zco
        self.mul_tom = self.v_tom * self.tom
        self.mul_pal = self.v_pal *self.pal
        self.mul_nar = self.v_nar * self.nar
        self.mul_lima = self.v_lima * self.lima
        self.mul_lim = self.v_lim * self.lim
        self.mul_gua = self.v_gua * self.gua
        self.mul_man = self.v_man * self.man
        self.mul_pin = self.v_pin * self.pin
        self.mul_san = self.v_san * self.san
        self.mul_pap = self.v_pap * self.pap
        self.mul_api = self.v_api * self.api
        self.mul_cco = self.v_cco * self.cco
        self.mul_hab = self.v_hab * self.hab
        self.mul_cer = self.v_cer * self.cer
        self.mul_dam = self.v_dam * self.dam
        self.mul_man = self.v_man * self.man
        self.mul_nue = self.v_nue * self.nue
        self.mul_alm = self.v_alm * self.alm
        self.mul_kiw = self.v_kiw * self.kiw

        recursos_totales_1 = self.mul_pla + self.mul_zan + self.mul_ber + self.mul_esp + self.mul_rep + self.mul_lec
        recursos_totales_2 = self.mul_ceb + self.mul_pve + self.mul_pro + self.mul_zco + self.mul_tom + self.mul_pal
        recursos_totales_3 = self.mul_nar + self.mul_lima + self.mul_lim + self.mul_gua + self.mul_man + self.mul_pin
        recursos_totales_4 = self.mul_san + self.mul_pap + self.mul_api +  self.mul_cco + self.mul_hab + self.mul_cer
        recursos_totales_5 =self.mul_dam + self.mul_man + self.mul_nue + self.mul_alm + self.mul_kiw
        recursos_totales = recursos_totales_1 + recursos_totales_2 + recursos_totales_3 + recursos_totales_4 + recursos_totales_5
        try:
            dieta_recomendada = list(recursos_totales)
            cadena = []
            for val in dieta_recomendada:
                val = round(val, 1)
                val = str(val)
                val2 = val.rjust(10)
                cadena.append(val2)
            string = ''.join(cadena)
            Label(self, text=string).place(x=150, y=330)
        except KeyError:
            pass


# End Document
