from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera_Francia - Guanenta")

ventana_principal.geometry("900x600")

ventana_principal.resizable(False, False)

ventana_principal.config(bg="black")

#-----------------------------------
# frama azul
#-----------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="navy", width=300, height=600)
frame_azul.place(x=0, y=0)

#-----------------------------------
# frama blanco
#-----------------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config(bg="white", width=300, height=600)
frame_blanco.place(x=300, y=0)


#-----------------------------------
# frama rojo
#-----------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red3", width=300, height=600)
frame_rojo.place(x=600, y=0)

ventana_principal.mainloop()