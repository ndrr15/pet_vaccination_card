import tkinter
from tkinter import *
from tkinter import messagebox

def menu_pantalla():
    global pantallaMenu
    pantallaMenu = Tk()
    pantallaMenu.geometry("400x380")
    pantallaMenu.title("Carnet de Vacunas para tus Mascotas")
    pantallaMenu.iconbitmap(
        './images/logo-removebg-preview.ico')

    image = PhotoImage(
        file='./images/logo-removebg-preview.gif')
    image = image.subsample(2, 2)
    label = Label(image=image)
    label.pack()

    Label(text="Ingresa al carnet de vacunas de tus mascotas", bg="navy",
          fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", height="3", width="30", command = inicio_sesion).pack()
    Label(text="").pack()
    Button(text="Rgistrar", height="3", width="30").pack()
    pantallaMenu.mainloop()


def inicio_sesion():
    global nombreUsuarioVerify
    global contrasenaUsuarioVerify
    nombreUsuarioVerify = StringVar()
    contrasenaUsuarioVerify = StringVar()
    global nombreUsuarioEntry
    global contrasenaUsuarioEntry
    global pantallaInicioSesion

    pantallaInicioSesion = Toplevel(pantallaMenu)
    pantallaInicioSesion.geometry("400x380")
    pantallaInicioSesion.title("Inicio de sesión")
    pantallaInicioSesion.iconbitmap(
        '/Users/nestorrodriguez/Desktop/Aplicacion/python-app/logo-removebg-preview.ico')

    Label(pantallaInicioSesion, text="Por favor ingresar su usuario y contraseña").pack()
    Label(pantallaInicioSesion, text="").pack()

    Label(pantallaInicioSesion, text="Usuario").pack()
    nombreUsuarioEntry = Entry(
        pantallaInicioSesion, textvariable=nombreUsuarioVerify)
    nombreUsuarioEntry.pack()
    Label(pantallaInicioSesion).pack()

    Label(pantallaInicioSesion, text="Contraseña").pack()
    contrasenaUsuarioEntry = Entry(
        pantallaInicioSesion, textvariable=contrasenaUsuarioVerify)
    contrasenaUsuarioEntry.pack()
    Label(pantallaInicioSesion).pack()
    Button(pantallaInicioSesion, text="Iniciar Sesion").pack()