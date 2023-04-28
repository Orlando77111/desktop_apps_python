from tkinter import *

ventana_principal = Tk()

ventana_principal.title("Bandera_Noruega - Guanenta")

ventana_principal.geometry("900x600")

ventana_principal.resizable(False, False)

ventana_principal.config(bg="midnight blue")

#-----------------------------------
# lineas blancas
#-----------------------------------
frame_blanca = Frame(ventana_principal)
frame_blanca.config(bg="azure", width=350, height=700)
frame_blanca.place(x=0, y=300)

#-----------------------------------
# lineas blancas1
#-----------------------------------
frame_blanca1 = Frame(ventana_principal)
frame_blanca1.config(bg="azure", width=500, height=700)
frame_blanca1.place(x=410, y=300)

#-----------------------------------
# lineas blancas2
#-----------------------------------
frame_blanca2 = Frame(ventana_principal)
frame_blanca2.config(bg="azure", width=500, height=250)
frame_blanca2.place(x=410, y=0)


#-----------------------------------
# lineas blancas3
#-----------------------------------
frame_blanca3 = Frame(ventana_principal)
frame_blanca3.config(bg="azure", width=350, height=250)
frame_blanca3.place(x=0, y=0)

#-----------------------------------
# lineas roja1
#-----------------------------------
frame_rojo1 = Frame(ventana_principal)
frame_rojo1.config(bg="red", width=310, height=250)
frame_rojo1.place(x=0, y=350)

#-----------------------------------
# lineas roja2
#-----------------------------------
frame_rojo2 = Frame(ventana_principal)
frame_rojo2.config(bg="red", width=310, height=200)
frame_rojo2.place(x=0, y=0)

#-----------------------------------
# lineas roja3
#-----------------------------------
frame_rojo3 = Frame(ventana_principal)
frame_rojo3.config(bg="red", width=500, height=200)
frame_rojo3.place(x=450, y=0)

#-----------------------------------
# lineas roja4
#-----------------------------------
frame_rojo4 = Frame(ventana_principal)
frame_rojo4.config(bg="red", width=450, height=500)
frame_rojo4.place(x=450, y=350)

ventana_principal.mainloop()