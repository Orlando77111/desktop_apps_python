# Desktop app No. 1

#Se importa toda la libreria tkinter
from tkinter import *
from tkinter import messagebox
#Funciones de la app

#sumar
def sumar():
    pass

#borrar
def borrar():
    pass

#salir
def salir():
    messagebox.showinfo("Suma enteros 1.0", "La app se va a cerrar")
    ventana_principal.destroy()

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
ventana_principal.config(bg="blue")

#-----------------------------------
# Entrada datos
#-----------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

#logo de la app
logo = PhotoImage(file="ing/escudo_colegio.png")
lb_logo = Label(frame_entrada, image=logo)
lb_logo.place(x=70, y=40)

#titulo de la app
titulo = Label(frame_entrada, text="Suma Enteros 1.0")
titulo.config(bg="white", fg="blue", font=("Helvetica", 20))
titulo.place(x=240, y=10)

#Etiqueta para el valor de x
lb_x = Label(frame_entrada, text="X =")
lb_x.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_x.place(x=240, y=60)

#Caja de texto para el valor de x
entry_x = Entry(frame_entrada)
entry_x.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=290, y=60)

#etuqueta para el valorde y
lb_y = Label(frame_entrada, text="Y =")
lb_y.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_y.place(x=240, y=120)

#caja de texto para y
entry_y = Entry(frame_entrada)
entry_y.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_y.place(x=290, y=120)

#-----------------------------------
# variables globales
#-----------------------------------
x = StringVar()
y = StringVar()

#-----------------------------------
# frama operaciones
#-----------------------------------
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

#Boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
bt_sumar.place(x=45, y=35, width=100, height=30)

#Boton para borrar 
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

#Boton para salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)


#-----------------------------------
# frama resultados
#-----------------------------------
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="white", width=480, height=180)
frame_resultado.place(x=10, y=310)

#area de texto para los resultados
t_resultados = Text(frame_resultado)
t_resultados.config(bg="black", fg="green yellow", font=("Cuorie", 20))
t_resultados.place(x=10, y=10, width=460, height=160)


#run
# Se ejecuta el metodo mainloop() de la clase Tk() a través de la ventana_prinsipal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que elusuario haga (click en un boton,escribir, etc). cada accion del usuario se conose como un evento. el método mainloop() es un bucle infinito.

ventana_principal.mainloop()