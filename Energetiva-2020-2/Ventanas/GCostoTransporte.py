from tkinter import *
from tkinter import ttk
import funciones
import numpy as np


class CostoTransporte(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        self.vehiculo_elegido = IntVar(self, value=0)

        self.km_litro = DoubleVar(self, value=20)
        self.pre_combustible = IntVar(self, value=500)
        self.litros_necesarios_totales = DoubleVar(self, value=100000000)
        self.camiones_por_dia = IntVar(self, value=1)
        self.km_ruta = DoubleVar(self, value=100)

        Label(self, text='Costo de Transporte por dia', font=15).place(x=20, y=20)

        Radiobutton(self, text='Freightliner FLD 120', variable=self.vehiculo_elegido, value=0).place(x=20, y=50)
        Radiobutton(self, text='Freightliner C-120', variable=self.vehiculo_elegido, value=1).place(x=20, y=70)

        Entry(self, width=13, textvariable=self.km_litro).place(x=10, y=100)
        Entry(self, width=13, textvariable=self.pre_combustible).place(x=10, y=130)
        Entry(self, width=13, textvariable=self.litros_necesarios_totales).place(x=10, y=160)
        Entry(self, width=13, textvariable=self.camiones_por_dia).place(x=10, y=190)
        Entry(self, width=13, textvariable=self.km_ruta).place(x=10, y=220)
        Label(self, text='km/litro Camion').place(x=100, y=100)
        Label(self, text='Precio Combustible').place(x=100, y=130)
        Label(self, text='Litros de Agua Necesarios por dia').place(x=100, y=160)
        Label(self, text='Cantidad de camiones por dia').place(x=100, y=190)
        Label(self, text='Km entre fuente de agua y lugar de almacenamiento').place(x=100, y=220)

        Button(self,text='Calcular', command=lambda: self.calcular_datos()).place(x=20, y=250)

        Label(self, text='Consumo Combustible: ').place(x=450, y=100)
        Label(self, text='Vehiculos Necesarios: ').place(x=450, y=130)
        Label(self, text='Vueltas Necesarias:').place(x=450, y=160)
        Label(self, text='Gasto en Combustible: ').place(x=450, y=190)
        Label(self, text='Gasto en Arriendo: ').place(x=450, y=220)


    def calcular_datos(self):

        var_camion = self.vehiculo_elegido.get()
        var_km_litro = self.km_litro.get()
        var_pre_combustible = self.pre_combustible.get()
        var_litros_totales = self.litros_necesarios_totales.get()
        var_cam_dia = self.camiones_por_dia.get()
        var_km_ruta = self.km_ruta.get()
        costo_arriendo = 60000
        capacidad_camion = 10000
        if var_camion == 0:
            costo_arriendo = 60000
            capacidad_camion = 10000
        if var_camion == 1:
            costo_arriendo = 90000
            capacidad_camion = 20000

        values = funciones.costo_transporte_x_dia(capacidad_camion, var_km_ruta, var_km_litro, var_cam_dia,
                                                  var_pre_combustible, var_litros_totales, costo_arriendo)

        Label(self, text=str(values[0]) + '             ').place(x=600, y=100)
        Label(self, text=str(values[1]) + '             ').place(x=600, y=130)
        Label(self, text=str(values[2]) + '             ').place(x=600, y=160)
        Label(self, text=str(values[3]) + '             ').place(x=600, y=190)
        Label(self, text=str(values[4]) + '             ').place(x=600, y=220)

# End Document
