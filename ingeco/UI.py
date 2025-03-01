from tkinter import *
from tkinter import ttk
from tab1 import T1
from tab2 import T2
from tab3 import T3
from tab4 import T4


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.notebook = ttk.Notebook()
        self.hig = 800
        self.wid = 460
        self.geom = (self.hig, self.wid)
        self.geo = '{0}x{1}'.format(self.hig, self.wid)
        self.geometry(self.geo)
        self.title('Herramientas Financieras')
        self.add_tab()
        self.notebook.place(x=0, y=0, width=self.hig, height=self.wid)

    def add_tab(self):
        tab1 = T1(self.geom)
        tab2 = T2(self.geom)
        tab3 = T3(self.geom)
        tab4 = T4(self.geom)

        self.notebook.add(tab1, text='Intereses')
        self.notebook.add(tab2, text='Payment')
        self.notebook.add(tab3, text='Creditos')
        self.notebook.add(tab4, text='Tasas')


maine = App()
maine.mainloop()

# End Document
