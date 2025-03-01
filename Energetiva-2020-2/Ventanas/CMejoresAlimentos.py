from tkinter import *
from tkinter import ttk
import funciones



class MejAlimentos(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        self.main_values_nut = StringVar(self)
        self.main_values_nut.set(None)

        Label(self, text='Nutrientes').place(x=20, y=300)
        Label(self, text='Energia').place(x=120, y=280)
        Label(self, text='Proteinas').place(x=170, y=280)
        Label(self, text='Carbohi.').place(x=230, y=280)
        Label(self, text='Calcio').place(x=290, y=280)
        Label(self, text='Hierro').place(x=350, y=280)
        Label(self, text='Vit. A').place(x=410, y=280)
        Label(self, text='Vit. C').place(x=470, y=280)

        # Column 0
        x1y1 = ttk.Label(self, text='Energia')
        x1y1.place(x=20, y=10)
        nutrientes0 = funciones.lista_alimentos_nutrientes(0)
        anchor0 = 50
        for nombre, nut in nutrientes0:
            b = Radiobutton(self, text=nombre, variable=self.main_values_nut, value=nut,
                            command=lambda: Label(self, text=funciones.join_list_nut(self.main_values_nut.get())).place(x=100, y=300))
            b.place(x=20, y=anchor0)
            anchor0 += 30

        # Column 1
        xy = ttk.Label(self, text='Proteina')
        xy.place(x=120, y=10)
        nutrientes1 = funciones.lista_alimentos_nutrientes(1)
        anchor1 = 50
        for nombre, nut in nutrientes1:
            b = Radiobutton(self, text=nombre, variable=self.main_values_nut, value=nut,
                            command=lambda: Label(self, text=funciones.join_list_nut(self.main_values_nut.get())).place(x=100, y=300))
            b.place(x=110, y=anchor1)
            anchor1 += 30

        # Column 2
        xy = ttk.Label(self, text='Carbohidratos')
        xy.place(x=220, y=10)
        nutrientes2 = funciones.lista_alimentos_nutrientes(2)
        anchor2 = 50
        for nombre, nut in nutrientes2:
            b = Radiobutton(self, text=nombre, variable=self.main_values_nut, value=nut,
                            command=lambda: Label(self, text=funciones.join_list_nut(self.main_values_nut.get())).place(x=100, y=300))
            b.place(x=220, y=anchor2)
            anchor2 += 30

        # Column 3
        xy = ttk.Label(self, text='Calcio')
        xy.place(x=320, y=10)
        nutrientes3 = funciones.lista_alimentos_nutrientes(3)
        anchor3 = 50
        for nombre, nut in nutrientes3:
            b = Radiobutton(self, text=nombre, variable=self.main_values_nut, value=nut,
                            command=lambda: Label(self,
                                                text=funciones.join_list_nut(self.main_values_nut.get())).place(x=100, y=300))
            b.place(x=320, y=anchor3)
            anchor3 += 30

        # Column 4
        xy = ttk.Label(self, text='Hierro')
        xy.place(x=420, y=10)
        nutrientes4 = funciones.lista_alimentos_nutrientes(4)
        anchor4 = 50
        for nombre, nut in nutrientes4:
            b = Radiobutton(self, text=nombre, variable=self.main_values_nut, value=nut,
                            command=lambda: Label(self, text=funciones.join_list_nut(self.main_values_nut.get())).place(x=100, y=300))
            b.place(x=420, y=anchor4)
            anchor4 += 30

        # Column 5
        xy = ttk.Label(self, text='Vitamina A')
        xy.place(x=520, y=10)
        nutrientes5 = funciones.lista_alimentos_nutrientes(5)
        anchor5 = 50
        for nombre, nut in nutrientes5:
            b = Radiobutton(self, text=nombre, variable=self.main_values_nut, value=nut,
                            command=lambda: Label(self, text=funciones.join_list_nut(self.main_values_nut.get())).place(x=100, y=300))
            b.place(x=520, y=anchor5)
            anchor5 += 30

        # Column 6
        xy = ttk.Label(self, text='Vitamina C')
        xy.place(x=620, y=10)
        nutrientes6 = funciones.lista_alimentos_nutrientes(6)
        anchor6 = 50
        for nombre, nut in nutrientes6:
            b = Radiobutton(self, text=nombre, variable=self.main_values_nut, value=nut,
                            command=lambda: Label(self, text=funciones.join_list_nut(self.main_values_nut.get())).place(x=100, y=300))
            b.place(x=620, y=anchor6)
            anchor6 += 30

