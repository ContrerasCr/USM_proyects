from tkinter import *
from tkinter import ttk
import funciones
import numpy as np


class VentanaPrincipal(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        Label(self, text='Consumo total de agua', font=("Courier", 13)).place(x=20, y=40)
        Button(self, text='Calcular', command=lambda: self.consumo_total_agua()).place(y=70, x=20)
        Label(self, text='Cantidad de Camiones de agua necesarios', font=("Courier", 13)).place(x=20, y=110)
        Button(self, text='Calcular', command=lambda: self.camiones_necesarios()).place(y=140, x=20)
        Label(self, text='Consumo de combustible', font=("Courier", 13)).place(x=20, y=180)
        Button(self, text='Calcular', command=lambda: self.consumo_combustible()).place(y=210, x=20)
        Label(self, text='Emisiones de CO2', font=("Courier", 13)).place(x=20, y=250)
        Button(self, text='Calcular', command=lambda: self.emisiones_co2()).place(y=280, x=20)
        Label(self, text='Costo del Proyecto', font=("Courier", 13)).place(x=20, y=320)
        Button(self, text='Calcular', command=lambda: self.costo_proyecto()).place(y=350, x=20)
        Label(self, text='Analisis de Sensibilidad', font=("Courier", 13)).place(x=20, y=390)
        Button(self, text='Calcular', command=lambda: self.analisis_sensibilidad()).place(y=420, x=20)

        Label(self, text='Valores Elegidos', font=18).place(x=480, y=30)
        Label(self, text='Dieta', font=12).place(x=480, y=60)

        Label(self, text='Almendras: 200gr').place(x=480, y=90)
        Label(self, text='Papa Cocida: 250gr').place(x=480, y=120)
        Label(self, text='Espinaca: 40gr').place(x=480, y=150)
        Label(self, text='Pimiento Rojo: 40gr').place(x=480, y=180)



        Label(self, text='Transporte', font=12).place(x=480, y=200)


    def consumo_total_agua(self):

        Label(self, text='Consumo total de agua: ').place(x=100, y=70)
        return None

    def camiones_necesarios(self):
        Label(self, text='Cantidad de Camiones de agua necesarios: ').place(x=100, y=140)
        return None

    def consumo_combustible(self):
        Label(self, text='Consumo de combustible: ').place(x=100, y=210)
        return None

    def emisiones_co2(self):
        Label(self, text='Emisiones de CO2: ').place(x=100, y=280)
        return None

    def costo_proyecto(self):
        Label(self, text='Costo del Proyecto: ').place(x=100, y=350)
        return None

    def analisis_sensibilidad(self):
        Label(self, text='Analisis de Sensibilidad: ').place(x=100, y=420)
        return None

