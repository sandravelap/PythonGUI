import tkinter as tk

#definimos la clase Coche
class Coche:
    def __init__(self, modelo, cvs, precio, parMotor, traccion, cilindrada):
        self.modelo = modelo
        self.cvs = cvs
        self.precio = precio
        self.parMotor = parMotor
        self.traccion = traccion
        self.cilindrada = cilindrada
        self.kilometros = 0

    def actualizarkms(self, kms):
        self.kilometros = self.kilometros + kms
    global cont

def siguienteCoche():
    
    if Coche.cont < len(listaCoches) - 1:
        Coche.cont = Coche.cont + 1
    else:
        Coche.cont = 0
    lblModeloData.config(text=listaCoches[Coche.cont].modelo)
    lblCvsData.config(text=listaCoches[Coche.cont].cvs)
    lblKmsData.config(text=listaCoches[Coche.cont].kilometros)
    entSumarKms.delete(0)
    entSumarKms.insert(0, "0")
    
def actualizarKms():
    listaCoches[Coche.cont].actualizarkms(int(entSumarKms.get()))
    lblKmsData.config(text=listaCoches[Coche.cont].kilometros)
    

#instanciamos los coches
coche1 = Coche("Dacia Duster", 135, 19000, 240, "delantera", "i3")
coche2 = Coche("Range Rover SV", 635, 237000, 800, "4 ruedas", "V8")
coche3=Coche("Mercedes AMGGt63S", 639, 228443, 900, "4 ruedas", "V8")
coche4=Coche("Renault Clio", 101, 17300, 170, "delantera", "I3")
coche5=Coche("Cupra Formentor", 333, 56090, 420, "4 ruedas", "I4")
Coche.cont=0

#creamos una lista con los coches para poder recorrerla con código
listaCoches = [coche1, coche2, coche3, coche4, coche5]

window = tk.Tk()
window.title("Mi concesionario")
window.geometry("400x300")

lblTitulo = tk.Label(window,text="Concesionario San Alberto Magno")
lblTitulo.pack()

frmInfoCoches = tk.Frame(window, padx=20, pady=20)
frmInfoCoches.pack()

lblModelo = tk.Label(frmInfoCoches,text="Modelo: ")
lblModelo.grid(column="1", row="1")

lblModeloData = tk.Label(frmInfoCoches, text=listaCoches[0].modelo)
lblModeloData.grid(column="2", row="1")

lblCvs = tk.Label(frmInfoCoches, text="Cavallos: ")
lblCvs.grid(column="1", row="2")

lblCvsData = tk.Label(frmInfoCoches, text=listaCoches[0].cvs)
lblCvsData.grid(column="2", row="2")

lblPrecio = tk.Label(frmInfoCoches, text="Precio: ")
lblPrecio.grid(column="1", row="3")

lblPrecioData = tk.Label(frmInfoCoches, text=listaCoches[0].precio)
lblPrecioData.grid(column="2", row="3")

lblKms = tk.Label(frmInfoCoches, text="Kilómetros: ")
lblKms.grid(column="1", row="4")

lblKmsData = tk.Label(frmInfoCoches, text=listaCoches[0].kilometros)
lblKmsData.grid(column="2", row="4")


frmBotones=tk.Frame(window, padx=20, pady=20)
frmBotones.pack()

#botón para cambiar de coche visualizado
btnSiguienteCoche = tk.Button(frmBotones, text="Siguiente", command=siguienteCoche)
btnSiguienteCoche.grid(column="1", row="1")

#botón para modificar los kms de un coche
btnSumarKms = tk.Button(frmBotones, text="Añadir kms", command=actualizarKms)
entSumarKms = tk.Entry(frmBotones, width=10)
entSumarKms.insert(0, "0")
btnSumarKms.grid(column="1", row="2")
entSumarKms.grid(column="2", row="2")

window.mainloop()
