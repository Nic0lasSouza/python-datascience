from tkinter import Tk, Frame, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ventana = Tk()
ventana.geometry('655x505')
ventana.wm_title('Gráfico Circular')
ventana.minsize(width=655, height=505)
frame=Frame(ventana, bg='gray')
frame.grid(column=0, row=0, sticky='nsew')

idades = ['25 a 34','35 a 44','45 a 54', '18 a 24']
ccolor = ['green', 'yellow', 'red', 'blue']
tamanho = [5.6, 11.1, 16.7, 66.7]
explotar = [0.5, 0.5, 0.5, 0.5]

fig, ax1 = plt.subplot()