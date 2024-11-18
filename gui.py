#importamos la librería tkinter para GUIs
#ttk nos da acceso a los objetos o widgets que podemos utilizar en la GUI
#https://guia-tkinter.readthedocs.io/es/develop/chapters/6-widgets/6.1-Intro.html
import tkinter as tk

def saludaUser():
    labelSaludo.config(text="Hola " + entrySaluda.get())

#instanciamos la clase Tk, que crea una ventana raíz del proyecto:
rootWindow = tk.Tk()
#y le damos un título
rootWindow.title("Mi concesionario")
#y un tamaño
rootWindow.geometry("400x300")
#y le añadimos un frame o marco a la ventana raíz
frm = tk.Frame(rootWindow)
#le añadimos una etiqueta
label = tk.Label(rootWindow, text="Allá vamos")
#y la empaquetamos en un bloque para que se posicione, el posicionamiento SIEMPRE EN UNA LÍNEA DIFERENTE.
label.pack() #el valor por defecto es anchor=center, es decir, que lo ancla al centro
#y añadimos botones con funciones
butSaluda = tk.Button(text="Saluda", command=saludaUser)
butSaluda.pack(anchor="w") #el valor de anchor se da con puntos cardinales
#y cuadros de texto para introducir texto nosotros como usuarios
entrySaluda = tk.Entry( background="cyan") #al crearlo podemos darle estilos
entrySaluda.pack(anchor="center", pady="10")
#y una label para visualizar el saludo que se genera
labelSaludo = tk.Label(rootWindow, text="lala", background="#C9E1AE")
labelSaludo.pack()
#definimos el bucle que se ejecuta y mantiene la ventana abierta y el programa activo
rootWindow.mainloop()

