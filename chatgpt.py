import tkinter as tk

def cambiar_texto():
    labelSaludo.config(text="¡Hola, mundo!")

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Saludo")

# Crear una etiqueta
labelSaludo = tk.Label(root, text="Texto original")
labelSaludo.pack(pady=10)

# Crear un botón que cambia el texto de la etiqueta
botonSaluda = tk.Button(root, text="Saluda", command=cambiar_texto)
botonSaluda.pack(pady=5)

# Iniciar el bucle principal de la aplicación
root.mainloop()
