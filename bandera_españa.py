# se importa la libreria tkinter con todoas sus fnciones
from tkinter import *

#-----------------------
# funciones de la app
#-----------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_pricipal,que aquiere las carateristicas de un objeto TK[]
ventana_principal = Tk () 

# titulo de la ventana
ventana_principal.title ("especialidad en sistemas - guanentá")
# ventana tamaño
ventana_principal.geometry("900x500")
# desabilitar boton de maximizar
ventana_principal.resizable(False,False)
# color de fondo de la ventana
ventana_principal.config(bg="red")
#---------------
# frama amarilla
#---------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=900, height=250)
frame_amarillo.place(x=0, y=120 )

#---------------
# frama roja
#---------------
frame_roja = Frame(ventana_principal)
frame_roja.config(bg="red", width=900, height=200)
frame_roja.place(x=0, y=450 )

ventana_principal.mainloop()

