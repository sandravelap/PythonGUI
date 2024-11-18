import tkinter as tk 

def defSaludar():
    lbSaludoText.config(text = "¡Hola!")

window = tk.Tk()
window.title("Mi programa")
window.geometry("400x300")
frmTitulo = tk.Frame(window)
frmTitulo.pack(padx=20, pady=20)
lbTitulo = tk.Label(frmTitulo, text="Mi programa mola")
lbTitulo.pack()
frmMain = tk.Frame(window)
frmMain.pack()
lbSaluda = tk.Label(frmMain, 
    text="Para ser saludado haz click en saludar.",
    padx=10, pady=10)
lbSaluda.grid(column=1, row="2")
#entrySaluda = tk.Entry(window, width="25")
#entrySaluda.grid(column=2, row=3)
btnSaluda = tk.Button(frmMain, text="Saludar", command=defSaludar)
btnSaluda.grid(column=1, row=3)
lbSaludoText = tk.Label(frmMain, width="25", text=" Aquí irá el saludo", bg="#C9E1AE")
lbSaludoText.grid(column=2, row=3)
window.mainloop()