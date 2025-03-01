from tkinter import *
from tkinter import ttk
from tkinter import font
from funciones import *


class T3(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Amortizacion
        self.it1 = ttk.Label(self, text='Amortizacion', font=font.Font(size=12))
        self.it1.place(x=0, y=20)
        self.it2 = ttk.Label(self, text='Saldo inicial')
        self.it2.place(x=0, y=80)
        self.it3 = ttk.Label(self, text='Saldo final')
        self.it3.place(x=0, y=100)
        self.it3 = ttk.Label(self, text='Saldo final')
        self.it3.place(x=0, y=120)
        self.it3 = ttk.Label(self, text='Saldo final')
        self.it3.place(x=0, y=140)
        self.it4 = ttk.Entry(self, textvariable=0, width=13)
        self.it4.place(x=90, y=80)
        self.it5 = ttk.Entry(self, textvariable=5, width=13)
        self.it5.place(x=90, y=100)
        self.it5 = ttk.Entry(self, textvariable=5, width=13)
        self.it5.place(x=90, y=120)
        self.it5 = ttk.Entry(self, textvariable=5, width=13)
        self.it5.place(x=90, y=140)
        self.it6 = ttk.Button(self, text='Calcular')
        self.it6.place(x=0, y=170)
        self.it7 = ttk.Label(self, text='Resultado')
        self.it7.place(x=90, y=173)

        # Cuota Interes Fijo
        self.tdi1 = ttk.Label(self, text='Cuota Interes Fijo', font=font.Font(size=12))
        self.tdi1.place(x=200, y=20)
        self.tdi2 = ttk.Label(self, text='Valor Presente:')
        self.tdi2.place(x=200, y=80)
        self.tdi3 = ttk.Label(self, text='Interes')
        self.tdi3.place(x=200, y=100)
        self.tdi3 = ttk.Label(self, text='Periodos')
        self.tdi3.place(x=200, y=120)
        self.tdi4 = ttk.Entry(self, textvariable=0, width=13)
        self.tdi4.place(x=290, y=80)
        self.tdi5 = ttk.Entry(self, textvariable=5, width=13)
        self.tdi5.place(x=290, y=100)
        self.tdi5 = ttk.Entry(self, textvariable=5, width=13)
        self.tdi5.place(x=290, y=120)
        self.tdi6 = ttk.Button(self, text='Calcular')
        self.tdi6.place(x=200, y=150)
        self.tdi7 = ttk.Label(self, text='Resultado')
        self.tdi7.place(x=290, y=153)

        # Bonos
        self.ctis1 = ttk.Label(self, text='Bonos', font=font.Font(size=12))
        self.ctis1.place(x=0, y=220)
        self.ctis3 = ttk.Label(self, text='Interes Periodo1')
        self.ctis3.place(x=0, y=280)
        self.ctis4 = ttk.Label(self, text='Perdiodo 1')
        self.ctis4.place(x=0, y=300)
        self.ctis5 = ttk.Label(self, text='Periodo 2')
        self.ctis5.place(x=0, y=320)
        self.ctis5 = ttk.Label(self, text='Periodo 2')
        self.ctis5.place(x=0, y=340)
        self.ctis6 = ttk.Entry(self, textvariable=0, width=13)
        self.ctis6.place(x=90, y=280)
        self.ctis7 = ttk.Entry(self, textvariable=5, width=13)
        self.ctis7.place(x=90, y=300)
        self.ctis8 = ttk.Entry(self, textvariable=5, width=13)
        self.ctis8.place(x=90, y=320)
        self.ctis8 = ttk.Entry(self, textvariable=5, width=13)
        self.ctis8.place(x=90, y=340)
        self.ctis9 = ttk.Button(self, text='Calcular')
        self.ctis9.place(x=0, y=370)
        self.ctis10 = ttk.Label(self, text='Resultado')
        self.ctis10.place(x=90, y=373)

# End Document
