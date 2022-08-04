
import tkinter
from tkinter import *
from tkinter import messagebox
from conection import *


def creacionPantalla(tamaño, title, icon, principal=False):
    if principal:
        pantalla = Tk()
    else:
        pantalla = Toplevel(pantallaMenu)
    pantalla.geometry(tamaño)
    pantalla.title(title)
    pantalla.iconbitmap(icon)
    pantalla.configure(bg='azure2')
    return pantalla


def menu_pantalla():
    global icon
    icon = './images/huellas-de-garras.ico'
    global pantallaMenu
    tamaño = "400x380"
    tittle = "Carnet de Vacunas para tus Mascotas"
    pantallaMenu = creacionPantalla(tamaño, tittle, icon, True)
    image = PhotoImage(
        file='./images/logo-removebg-preview.gif')
    image = image.subsample(2, 2)
    label = Label(image=image, bg='azure2')
    label.pack()
    Label(text="Carnets de vacunas de tus mascotas", bg="blueviolet",
          fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesión", height="3", border=0,
           width="30", fg='navy', command=inicioSesion).pack()
    Label(text="").pack()
    Button(text="Registrar", fg='navy',height="3", width="30",
           command=registrarUsuario).pack()
    pantallaMenu.mainloop()


def inicioSesion():
    global nombreUsuarioVerify
    global contrasenaUsuarioVerify
    nombreUsuarioVerify = StringVar()
    contrasenaUsuarioVerify = StringVar()
    global nombreUsuarioEntry
    global contrasenaUsuarioEntry
    global pantallaInicioSesion

    tamaño = "350x300"
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
        pantallaInicioSesion, show="*", textvariable=contrasenaUsuarioVerify)
    contrasenaUsuarioEntry.pack()
    Label(pantallaInicioSesion).pack()

    Button(pantallaInicioSesion, text="Ingresar",
           command=validacionlogin).pack()


def registrarUsuario():

    global pantallaRegistrarUsuario
    tamaño = "350x550"
    tittle = "Registrar usuario nuevo"
    pantallaRegistrarUsuario = creacionPantalla(tamaño, tittle, icon)

    global nombreUsuarioEntryRegister
    global contrasenaUsuarioEntryRegister
    global nombreReal
    global apellidoReal
    global cedulaNit
    global email

    nombreUsuarioEntryRegister = StringVar()
    contrasenaUsuarioEntryRegister = StringVar()
    nombreReal = StringVar()
    apellidoReal = StringVar()
    cedulaNit = int()
    email = StringVar()

    Label(pantallaRegistrarUsuario, text="Diligencie la siguiente información", bg="blueviolet",
          fg="white", width="300", height="3", font=("Calibri", 12)).pack()
    Label(pantallaRegistrarUsuario, text="").pack()
    # usuario
    Label(pantallaRegistrarUsuario, text="Usuario:").pack()
    nombreUsuarioEntryRegister = Entry(
        pantallaRegistrarUsuario)
    nombreUsuarioEntryRegister.pack()
    Label(pantallaRegistrarUsuario).pack()
    # contraseña
    Label(pantallaRegistrarUsuario, text="Contraseña:").pack()
    contrasenaUsuarioEntryRegister = Entry(pantallaRegistrarUsuario, show="*")
    contrasenaUsuarioEntryRegister.pack()
    Label(pantallaRegistrarUsuario).pack()
    # Nombre real del usuario
    Label(pantallaRegistrarUsuario, text="Nombres:").pack()
    nombreReal = Entry(pantallaRegistrarUsuario)
    nombreReal.pack()
    Label(pantallaRegistrarUsuario).pack()
    # Apellido real del usuario
    Label(pantallaRegistrarUsuario, text="Apellidos:").pack()
    apellidoReal = Entry(pantallaRegistrarUsuario)
    apellidoReal.pack()
    Label(pantallaRegistrarUsuario).pack()
    # Cedula o nit
    Label(pantallaRegistrarUsuario,
          text="Número de identificación (Cedula o Nit):").pack()
    cedulaNit = Entry(pantallaRegistrarUsuario)
    cedulaNit.pack()
    Label(pantallaRegistrarUsuario).pack()
    # Email
    Label(pantallaRegistrarUsuario, text="Email:").pack()
    email = Entry(pantallaRegistrarUsuario)
    email.pack()
    Label(pantallaRegistrarUsuario).pack()

    Button(pantallaRegistrarUsuario, text="Registrar Usuario",
           command=InsertRegistroNuevo).pack()


def InsertRegistroNuevo():
    bd = conexionBD()
    fcursor = bd.cursor()
    sql = "INSERT INTO TBL_SYSUSUARIOS (nom_usuario, password, nombre, apellido, cedula_nit, email) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')".format(
        nombreUsuarioEntryRegister.get(), contrasenaUsuarioEntryRegister.get(), nombreReal.get(), apellidoReal.get(), cedulaNit.get(), email.get())
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Exitoso", title="Aviso")
    except:
        bd.rollback
        messagebox.showinfo(message="No registrado", title="Aviso")
    bd.close()


def validacionlogin():
    bd = conexionBD()
    fcursor = bd.cursor()
    sql = "SELECT password from TBL_SYSUSUARIOS where nom_usuario = :ussername and password = :contrasena"
    fcursor.execute(sql, ussername=nombreUsuarioVerify.get(),
                    contrasena=contrasenaUsuarioVerify.get())
    if fcursor.fetchall():
        messagebox.showinfo(title='Inicio de sesión correcto',
                            message='Usuario y contraseña correctos')
    else:
        messagebox.showinfo(title='Inicio de sesión incorrecto',
                            message='Usuario y contraseña incorrectos')

    bd.close()
