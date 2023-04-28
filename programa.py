# Desktop app No. 1

#Se importa toda la libreria tkinter
from tkinter import *

#Funciones de la app

#Ventana principal de la app


#Se declara una ventana llamada ventana_principal, que adquiere las caracteristicas de un objeto TK()
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Especialidad de sistemas - Guanenta")

#Tamaño de la ventana
ventana_principal.geometry("500x500")

#Desabilitar el boton de maximizar
ventana_principal.resizable(False, False)

#Color de fondo de la ventana
ventana_principal.config(bg="black")

#-----------------------------------
# frama amarillo
#-----------------------------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=500, height=250)
frame_amarillo.place(x=0, y=0)

#-----------------------------------
# frama Azul
#-----------------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=500, height=125)
frame_azul.place(x=0, y=250)


#-----------------------------------
# frama rojo
#-----------------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=500, height=125)
frame_rojo.place(x=0, y=375)


#run
# Se ejecuta el metodo mainloop() de la clase Tk() a través de la ventana_prinsipal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que elusuario haga (click en un boton,escribir, etc). cada accion del usuario se conose como un evento. el método mainloop() es un bucle infinito.

ventana_principal.mainloop()
