import tkinter as tk
from PIL import ImageTk, Image


def formulas(top, directory):

    toplevel = tk.Toplevel(top)
    img = ImageTk.PhotoImage(Image.open(directory))
    img.image = img
    canvas = tk.Canvas(toplevel, width=img.width(), height=img.height())
    canvas.grid(column=0, row=0)
    canvas.create_image(0, 0, image=img, anchor='nw')

# End Document
