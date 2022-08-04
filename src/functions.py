from array import array
import tkinter
from tkinter import *
from tkinter import messagebox

def creacionPantalla(tamaño, title, icon, principal = False):
    if principal:
        pantalla = Tk()
    else:
        pantalla = Toplevel(pantallaMenu)
    pantalla.geometry(tamaño)
    pantalla.title(title)
    pantalla.iconbitmap(icon)
    return pantalla

def menu_pantalla():
    global icon
    icon = '/Users/nestorrodriguez/Desktop/Aplicacion/python-app/logo-removebg-preview.ico'
    global pantallaMenu
    tamaño= "400x380"
    tittle = "Carnet de Vacunas para tus Mascotas"
    pantallaMenu = creacionPantalla(tamaño, tittle, icon, True)
    image = PhotoImage(
        file='./images/logo-removebg-preview.gif')
    image = image.subsample(2, 2)
    label = Label(image=image)
    label.pack()
    Label(text="Bienvenidos a tus carnet de vacunas de tus mascotas", bg="blueviolet",
          fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", height="3", width="30", command = inicioSesion).pack()
    Label(text="").pack()
    Button(text="Rgistrar", height="3", width="30", command = registrarUsuario).pack()
    pantallaMenu.mainloop()


def inicioSesion():
    global nombreUsuarioVerify
    global contrasenaUsuarioVerify
    nombreUsuarioVerify = StringVar()
    contrasenaUsuarioVerify = StringVar()
    global nombreUsuarioEntry
    global contrasenaUsuarioEntry
    global pantallaInicioSesion

    tamaño= "350x300"
    tittle = "Inicio de sesión"
    pantallaInicioSesion = creacionPantalla(tamaño, tittle, icon)

    Label(pantallaInicioSesion, text="Por favor ingresar su usuario y contraseña", bg="blueviolet",
          fg="white", width="300", height="3", font=("Calibri", 12)).pack()
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

def registrarUsuario():
    global pantallaRegistrarUsuario
    tamaño= "350x550"
    tittle = "Registrar usuario nuevo"
    pantallaRegistrarUsuario = creacionPantalla(tamaño, tittle, icon)
    global nombreUsuarioEntryRegister
    global contrasenaUsuarioEntryRegister
    global cedulaNitverify
    global emailVerify
    cedulaNitverify = int()
    emailVerify = StringVar()
    nombreUsuarioEntryRegister = StringVar()
    contrasenaUsuarioEntryRegister = StringVar()
    nombreReal  = StringVar()
    apellidoReal  = StringVar()
    cedulaNit  = int()
    email  = StringVar()
    
    Label(pantallaRegistrarUsuario, text="Diligencie la siguiente información", bg="blueviolet",
          fg="white", width="300", height="3", font=("Calibri", 12)).pack()
    Label(pantallaRegistrarUsuario, text="").pack()
    #usuario
    Label(pantallaRegistrarUsuario, text="Usuario:").pack()
    nombreUsuarioEntryRegister = Entry(
        pantallaRegistrarUsuario)
    nombreUsuarioEntryRegister.pack()
    Label(pantallaRegistrarUsuario).pack()
    #contraseña
    Label(pantallaRegistrarUsuario, text="Contraseña:").pack()
    contrasenaUsuarioEntryRegister = Entry(pantallaRegistrarUsuario)
    contrasenaUsuarioEntryRegister.pack()
    Label(pantallaRegistrarUsuario).pack()
    #Nombre real del usuario
    Label(pantallaRegistrarUsuario, text="Nombres:").pack()
    nombreReal = Entry(pantallaRegistrarUsuario)
    nombreReal.pack()
    Label(pantallaRegistrarUsuario).pack()
    #Apellido real del usuario
    Label(pantallaRegistrarUsuario, text="Apellidos:").pack()
    apellidoReal = Entry(pantallaRegistrarUsuario)
    apellidoReal.pack()
    Label(pantallaRegistrarUsuario).pack()
    #Cedula o nit
    Label(pantallaRegistrarUsuario, text="número de identificación (Cedula o Nit):").pack()
    cedulaNit = Entry(pantallaRegistrarUsuario)
    cedulaNit.pack()
    Label(pantallaRegistrarUsuario).pack()
    #Email
    Label(pantallaRegistrarUsuario, text="Email:").pack()
    email = Entry(pantallaRegistrarUsuario)
    email.pack()
    Label(pantallaRegistrarUsuario).pack()
    