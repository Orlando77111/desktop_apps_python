from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera_Noruega - Guanenta")

ventana_principal.geometry("500x500")

ventana_principal.resizable(False, False)

ventana_principal.config(bg="red")

#Frange blanco1
frame_blanca = Frame(ventana_principal)
frame_blanca.config(bg="white", width=100, height=300)
frame_blanca.place(x=200, y=100)

#Frange blanco2
frame_blanca2 = Frame(ventana_principal)
frame_blanca2.config(bg="white", width=300, height=100)
frame_blanca2.place(x=100, y=200)

ventana_principal.mainloop()