from tkinter import *
import matplotlib.pyplot as plt


class CrecimientoPop(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom


        # Variables

        self.pob_ini = IntVar(self, value=53591)
        self.pob_cre = DoubleVar(self, value=2.2)
        self.h_1_e = DoubleVar(self, value=9.75)
        self.h_2_e = DoubleVar(self, value=33.22)
        self.h_3_e = DoubleVar(self, value=5.53)
        self.m_1_e = DoubleVar(self, value=10.35)
        self.m_2_e = DoubleVar(self, value=35.22)
        self.m_3_e = DoubleVar(self, value=5.87)
        self.h_1_n = DoubleVar(self, value=0.815)
        self.h_2_n = DoubleVar(self, value=0.882)
        self.h_3_n = DoubleVar(self, value=0.885)
        self.m_1_n = DoubleVar(self, value=0.902)
        self.m_2_n = DoubleVar(self, value=0.778)
        self.m_3_n = DoubleVar(self, value=0.900)

        Label(self, text='Crecimiento de la poblacion', font=18).place(x=20, y=30)

        Label(self, text='Poblacion inicial').place(x=20, y=60)
        Entry(self, width=12, textvariable=self.pob_ini).place(x=150, y=60)
        Label(self, text='Tasa de Crecimiento (%)').place(x=20, y=90)
        Entry(self, width=12, textvariable=self.pob_cre).place(x=150, y=90)

        Label(self, text='Edad').place(x=100, y=130)
        Label(self, text='% de la poblacion').place(x=150, y=130)
        Label(self, text='total').place(x=150, y=145)
        Label(self, text='(M/M*)^(1/10)').place(x=290, y=130)
        Label(self, text='Hombre').place(x=20, y=160)
        Label(self, text='0-14').place(x=100, y=190)
        Label(self, text='15-64').place(x=100, y=220)
        Label(self, text='65+').place(x=100, y=250)

        Label(self, text='Mujer').place(x=20, y=290)
        Label(self, text='0-14').place(x=100, y=320)
        Label(self, text='15-64').place(x=100, y=350)
        Label(self, text='65+').place(x=100, y=380)

        Entry(self, width=12, textvariable=self.h_1_e).place(x=150, y=190)
        Entry(self, width=12, textvariable=self.h_2_e).place(x=150, y=220)
        Entry(self, width=12, textvariable=self.h_3_e).place(x=150, y=250)
        Entry(self, width=12, textvariable=self.m_1_e).place(x=150, y=320)
        Entry(self, width=12, textvariable=self.m_2_e).place(x=150, y=350)
        Entry(self, width=12, textvariable=self.m_3_e).place(x=150, y=380)

        Entry(self, width=12, textvariable=self.h_1_n).place(x=290, y=190)
        Entry(self, width=12, textvariable=self.h_2_n).place(x=290, y=220)
        Entry(self, width=12, textvariable=self.h_3_n).place(x=290, y=250)
        Entry(self, width=12, textvariable=self.m_1_n).place(x=290, y=320)
        Entry(self, width=12, textvariable=self.m_2_n).place(x=290, y=350)
        Entry(self, width=12, textvariable=self.m_3_n).place(x=290, y=380)

        Button(self, text='Calcular y Graficar', command=lambda: self.graficar()).place(x=450, y=190)

    def graficar(self):
        pob_ini_g = self.pob_ini.get()
        pob_cre_g = self.pob_cre.get()
        h_1_e_g = self.h_1_e.get()
        h_2_e_g = self.h_2_e.get()
        h_3_e_g = self.h_3_e.get()
        m_1_e_g = self.m_1_e.get()
        m_2_e_g = self.m_2_e.get()
        m_3_e_g = self.m_3_e.get()
        h_1_n_g = self.h_1_n.get()
        h_2_n_g = self.h_2_n.get()
        h_3_n_g = self.h_3_n.get()
        m_1_n_g = self.m_1_n.get()
        m_2_n_g = self.m_2_n.get()
        m_3_n_g = self.m_3_n.get()

        p0nh1 = pob_ini_g * 0.01 * h_1_e_g * h_1_n_g
        p0nh2 = pob_ini_g * 0.01 * h_2_e_g * h_2_n_g
        p0nh3 = pob_ini_g * 0.01 * h_3_e_g * h_3_n_g

        p0nm1 = pob_ini_g * 0.01 * m_1_e_g * m_1_n_g
        p0nm2 = pob_ini_g * 0.01 * m_2_e_g * m_2_n_g
        p0nm3 = pob_ini_g * 0.01 * m_3_e_g * m_3_n_g

        ptot = p0nh1 + p0nh2 + p0nh3 + p0nm1 + p0nm2 + p0nm3

        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        pob_anual = []
        for t in days:
            pop_act = ptot * pow(2.718, 10 * 0.01 * pob_cre_g * t)
            pob_anual.append(pop_act)

        plt.ion()
        plt.figure('Infectados Criticos')
        plt.scatter(days, pob_anual)
        plt.xlabel('Años')
        plt.ylabel('Poblacion')
        plt.show()


# End Document
