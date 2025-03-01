from tkinter import *



class VentanaPrincipal(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        Label(self, text='Cantidad de alimentos escogidos por grupo etario Diario', font=18).place(x=20, y=30)
        Label(self, text='Edad', font=12).place(x=100, y=60)
        Label(self, text='Hombre', font=12).place(x=20, y=80)
        Label(self, text='0-14').place(x=100, y=100)
        Label(self, text='15-64').place(x=100, y=130)
        Label(self, text='65+').place(x=100, y=160)

        Label(self, text='Mujer', font=12).place(x=20, y=190)
        Label(self, text='0-14').place(x=100, y=220)
        Label(self, text='15-64').place(x=100, y=250)
        Label(self, text='65+').place(x=100, y=280)

        Label(self, text='Nuez[gr]').place(x=190, y=60)
        Label(self, text='Papa Cocida[gr]').place(x=240, y=60)
        Label(self, text='Espinaca[gr]').place(x=330, y=60)
        Label(self, text='Pimiento Rojo[gr]').place(x=410, y=60)
        Label(self, text='Almendras[gr]').place(x=500, y=60)

        Label(self, text='230[gr]').place(x=190, y=100)
        Label(self, text='210[gr]').place(x=240, y=100)
        Label(self, text='60[gr]').place(x=330, y=100)
        Label(self, text='10[gr]').place(x=410, y=100)
        Label(self, text='10[gr]').place(x=500, y=100)

        Label(self, text='270[gr]').place(x=190, y=130)
        Label(self, text='250[gr]').place(x=240, y=130)
        Label(self, text='50[gr]').place(x=330, y=130)
        Label(self, text='120[gr]').place(x=410, y=130)
        Label(self, text='10[gr]').place(x=500, y=130)

        Label(self, text='80[gr]').place(x=190, y=160)
        Label(self, text='130[gr]').place(x=240, y=160)
        Label(self, text='290[gr]').place(x=330, y=160)
        Label(self, text='170[gr]').place(x=410, y=160)
        Label(self, text='60[gr]').place(x=500, y=160)

        Label(self, text='140[gr]').place(x=190, y=220)
        Label(self, text='180[gr]').place(x=240, y=220)
        Label(self, text='0[gr]').place(x=330, y=220)
        Label(self, text='100[gr]').place(x=410, y=220)
        Label(self, text='60[gr]').place(x=500, y=220)

        Label(self, text='20[gr]').place(x=190, y=250)
        Label(self, text='200[gr]').place(x=240, y=250)
        Label(self, text='60[gr]').place(x=330, y=250)
        Label(self, text='20[gr]').place(x=410, y=250)
        Label(self, text='180[gr]').place(x=500, y=250)

        Label(self, text='0[gr]').place(x=190, y=280)
        Label(self, text='190[gr]').place(x=240, y=280)
        Label(self, text='220[gr]').place(x=330, y=280)
        Label(self, text='140[gr]').place(x=410, y=280)
        Label(self, text='50[gr]').place(x=500, y=280)
