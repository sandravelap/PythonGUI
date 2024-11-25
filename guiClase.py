import tkinter as tk

#creamos una ventana principal con el método Tk()
window = tk.Tk()
#la ventana tiene métodos para añadirle características
window.title("Mi programita")
window.geometry("400x300")

#definimos la función para el botón saludar
def funcionSaludar():
    lblSaludo.config(text="Hola hola " + entNombre.get())

def funcionDespedirse():
    lblSaludo.config(text="Bye bye " + entNombre.get())

#añadimos un widget tipo Label
lblTitulo = tk.Label(window, text="Mi primer programa chispas")
#posionamos el widget en la ventana window con el método pack()
lblTitulo.pack(pady=20)
#label para introducir el nombre del usuario
lblNombre = tk.Label(window, text="Introduce tu nombre: ")
lblNombre.pack()
entNombre = tk.Entry(window)
entNombre.pack()
#añadimos un widget tipo botón
btnSaludar = tk.Button(window, text="Saludar", command=funcionSaludar)
btnSaludar.pack()
btnDespedirse = tk.Button(window, text="Despedirse", command=funcionDespedirse)
btnDespedirse.pack()
#creamos otro label para escribir en él el saludo al hacer click
lblSaludo = tk.Label(window, text="Aquí irá el saludo")
lblSaludo.pack()

#esta instrucción permite que el programa no se cierre y la ventana desaparezca
window.mainloop()