from tkinter import *
from tkinter import ttk
from Ventanas.AVentanaMain import VentanaPrincipal
from Ventanas.BCrecimientoPob import CrecimientoPop
from Ventanas.CMejoresAlimentos import MejAlimentos
from Ventanas.DTab_all_alimentos import TodosLosAlimentos
from Ventanas.EElegirDieta import ElegirDieta
from Ventanas.FCostoAcueducto import CostoAcueducto
from Ventanas.GCostoTransporte import CostoTransporte


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.notebook = ttk.Notebook()
        self.hig = 920
        self.wid = 500
        self.geom = (self.hig, self.wid)
        self.geo = '{0}x{1}'.format(self.hig, self.wid)
        self.geometry(self.geo)
        self.title('Cultivo Urbano')
        self.add_tab()
        self.notebook.place(x=0, y=0, width=self.hig, height=self.wid)

    def add_tab(self):
        tab1 = VentanaPrincipal(self.geom)
        tab2 = CrecimientoPop(self.geom)
        tab3 = MejAlimentos(self.geom)
        tab4 = ElegirDieta(self.geom)
        tab5 = TodosLosAlimentos(self.geom)
        tab6 = CostoAcueducto(self.geom)
        tab7 = CostoTransporte(self.geom)

        self.notebook.add(tab1, text='Main')
        self.notebook.add(tab2, text='Poblacion')
        self.notebook.add(tab3, text='Datos Top Alimentos')
        self.notebook.add(tab4, text='Crear Dieta Recomendada')
        self.notebook.add(tab5, text='Crear Dieta')
        self.notebook.add(tab6, text='Costos Acueducto')
        self.notebook.add(tab7, text='Costos Transporte')


maine = App()
maine.mainloop()

# End Document
