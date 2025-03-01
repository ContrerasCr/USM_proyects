from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import funciones
# from Distribuciones import Test1


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.notebook = ttk.Notebook()
        self.hig = 800
        self.wid = 420
        self.geom = (self.hig, self.wid)
        self.geo = '{0}x{1}'.format(self.hig, self.wid)
        self.geometry(self.geo)
        self.title('Modelos de probabilidad')
        self.add_tab()
        self.notebook.place(x=0, y=0, width=self.hig, height=self.wid)

    def add_tab(self):
        tab1 = Bernulli(self.geom)
        tab2 = Binomial(self.geom)
        tab3 = Hipergeometrica(self.geom)
        tab4 = Geometrica(self.geom)
        tab5 = BinomialNegativa(self.geom)
        tab6 = Poisson(self.geom)
        tab7 = Exponencial(self.geom)
        tab8 = Gamma(self.geom)
        tab9 = Uniforme(self.geom)
        tab10 = Weibull(self.geom)
        tab11 = Normal(self.geom)

        self.notebook.add(tab1, text='Ber')
        self.notebook.add(tab2, text='Bin')
        self.notebook.add(tab3, text='Hip')
        self.notebook.add(tab4, text='Geo')
        self.notebook.add(tab5, text='BN')
        self.notebook.add(tab6, text='Poisson')
        self.notebook.add(tab7, text='Exp')
        self.notebook.add(tab8, text='Gamma')
        self.notebook.add(tab9, text='Unif')
        self.notebook.add(tab10, text='Weibull')
        self.notebook.add(tab11, text='Normal')


class Bernulli(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Bernulli')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Ber(p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de p')
        self.x0y5.place(x=0, y=100)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_x)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y5.place(x=80, y=100)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=130)

        # Column 2
        direct = r'Imagenes\Formulas\Bernulli.png'
        self.x2y0 = ttk.Button(self, text='Formulas', command=lambda: funciones.formulas(self, direct))
        self.x2y0.place(x=400, y=300, anchor=CENTER)

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class Binomial(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Binomial')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Bin(n,p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de n')
        self.x0y5.place(x=0, y=100)
        self.x0y52 = ttk.Label(self, text='Valor de p')
        self.x0y52.place(x=0, y=120)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='n: Intentos totales')
        self.x0y12.place(x=0, y=320)
        self.x0y13 = ttk.Label(self, text='p: Probabilidad')
        self.x0y13.place(x=0, y=340)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_n = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_x)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_n)
        self.x1y5.place(x=80, y=100)
        self.x1y52 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y52.place(x=80, y=120)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=150)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\Binomial.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class Hipergeometrica(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Hipergeometrica')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Hip(N,M,n)')
        self.x0y2.place(x=0, y=40)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de N')
        self.x0y5.place(x=0, y=100)
        self.x0y52 = ttk.Label(self, text='Valor de M')
        self.x0y52.place(x=0, y=120)
        self.x0y53 = ttk.Label(self, text='Valor de N')
        self.x0y53.place(x=0, y=140)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_N = IntVar(self, value=0)
        self.var_M = IntVar(self, value=0)
        self.var_n = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_x)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_N)
        self.x1y5.place(x=80, y=100)
        self.x1y52 = ttk.Entry(self, textvariable=self.var_M)
        self.x1y52.place(x=80, y=120)
        self.x1y53 = ttk.Entry(self, textvariable=self.var_n)
        self.x1y53.place(x=80, y=140)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=170)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\Hipergeometrica.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class Geometrica(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Geometrica')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Ber(p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de p')
        self.x0y5.place(x=0, y=100)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y5.place(x=80, y=100)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=130)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\Geometrica.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class BinomialNegativa(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion BinomialNegativa')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Ber(p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de p')
        self.x0y5.place(x=0, y=100)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y5.place(x=80, y=100)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=130)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\BinomialNegativa.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class Poisson(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Poisson')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Ber(p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de p')
        self.x0y5.place(x=0, y=100)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y5.place(x=80, y=100)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=130)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\Poisson.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class Exponencial(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Exponencial')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Ber(p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de p')
        self.x0y5.place(x=0, y=100)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y5.place(x=80, y=100)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=130)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\Exponencial.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class Gamma(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Gamma')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Ber(p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de p')
        self.x0y5.place(x=0, y=100)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y5.place(x=80, y=100)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=130)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\Gamma.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class Uniforme(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Uniforme')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Ber(p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de p')
        self.x0y5.place(x=0, y=100)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y5.place(x=80, y=100)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=130)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\Uniforme.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class Weibull(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Weibull')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Ber(p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de p')
        self.x0y5.place(x=0, y=100)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y5.place(x=80, y=100)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=130)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\Weibull.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


class Normal(Frame):
    def __init__(self, geom):
        Frame.__init__(self, )
        self.hig, self.wid = geom

        # Column 0
        self.valor_fx = 0
        self.valor_e = 0
        self.valor_v = 0
        self.x0y1 = ttk.Label(self, text='Distribucion Normal')
        self.x0y1.place(x=0, y=20)
        self.x0y2 = ttk.Label(self, text='X~Ber(p)')
        self.x0y2.place(x=0, y=40)
        self.x0y3 = ttk.Label(self, text='      ')
        self.x0y3.place(x=0, y=60)
        self.x0y4 = ttk.Label(self, text='Valor de X')
        self.x0y4.place(x=0, y=80)
        self.x0y5 = ttk.Label(self, text='Valor de p')
        self.x0y5.place(x=0, y=100)
        self.x0y6 = ttk.Label(self, text='Resultados')
        self.x0y6.place(x=0, y=180)
        self.x0y7 = ttk.Label(self, text='fx(x)= {}'.format(self.valor_fx))
        self.x0y7.place(x=0, y=200)
        self.x0y8 = ttk.Label(self, text='E[x] = {}'.format(self.valor_e))
        self.x0y8.place(x=0, y=220)
        self.x0y9 = ttk.Label(self, text='V[x] = {}'.format(self.valor_v))
        self.x0y9.place(x=0, y=240)
        self.x0y10 = ttk.Label(self, text='Glosario')
        self.x0y10.place(x=0, y=280)
        self.x0y11 = ttk.Label(self, text='X: Variable Aleatoria')
        self.x0y11.place(x=0, y=300)
        self.x0y12 = ttk.Label(self, text='p: Probabilidad')
        self.x0y12.place(x=0, y=320)

        self.x0y13 = ttk.Label(self, text='fx(x): Funcion de densidad')
        self.x0y13.place(x=150, y=300)
        self.x0y14 = ttk.Label(self, text='E[x]: Esperanza')
        self.x0y14.place(x=150, y=320)
        self.x0y15 = ttk.Label(self, text='V[x]: Varianza')
        self.x0y15.place(x=150, y=340)

        # Column 1
        self.var_x = IntVar(self, value=0)
        self.var_p = IntVar(self, value=0)
        self.x1y4 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y4.place(x=80, y=80)
        self.x1y5 = ttk.Entry(self, textvariable=self.var_p)
        self.x1y5.place(x=80, y=100)
        self.x1y6 = ttk.Button(self, text='Calcular', command=lambda: print('holamundo'))
        self.x1y6.place(x=105, y=130)

        # Column 2
        self.img = ImageTk.PhotoImage(Image.open(r'Imagenes\Formulas\Normal.png'))
        self.img.image = self.img
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height())
        self.canvas.place(x=410, y=100, anchor=CENTER)
        self.canvas.create_image(0, 0, image=self.img, anchor='nw')

        # Column 3 'Comentarios'
        self.col3 = 600
        self.x3y0 = ttk.Label(self, text='Comentarios')
        self.x3y0.place(x=self.col3, y=20)


maine = App()
maine.mainloop()

# End Document
