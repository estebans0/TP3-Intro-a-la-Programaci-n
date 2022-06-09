# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 27/05/2022 03:00pm
# Fecha de última Modificación: 04/06/2022 07:36am
# Versión: 3.10.2

# Importación de librerías
from turtle import bgcolor
from funciones import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pickle

# Creación de la raiz
raiz = Tk()
raiz.title("Sistema de Personalidades") 
raiz.iconbitmap("logo.ico")
raiz.geometry("600x750")
raiz.config(cursor = "star")
# Canvas para añadir fondo y demás widgets
canvas_raiz = Canvas(raiz, width = 600, height = 750, bg = "White")
canvas_raiz.pack()
bg_principal = PhotoImage(file = "bg.png")
canvas_raiz.create_image(0, 0, anchor = NW, image = bg_principal)

# Funciones de GUI
def cerrarPantalla(ppantalla): # Función de "Salir" de la pantalla
    ppantalla.destroy()
    return ""

#================================================================================================================================================#
#                                                        SECCIÓN DE INTERFAZ GRÁFICA
#================================================================================================================================================#
# Interfaz de registrar los datos de una persona
def guiRegistrarP():
    raiz.deiconify()
    pRegistrarP = Toplevel()
    pRegistrarP.geometry("600x530")
    pRegistrarP.config(cursor = "star")

    Label(pRegistrarP, text = "Registrar los datos de una persona", font = ("Lucida Calligraphy", 22), fg = "Black").place(x = 30, y = 30)

    Label(pRegistrarP, text = "Cédula", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 110)
    entradaCedula = Entry(pRegistrarP, width = 23, font = ("Sylfaen", 16), relief = "raised", bg = "#b82e8a")
    entradaCedula.place(x = 300, y = 115)
    entradaCedula.config(justify = "center")

    Label(pRegistrarP, text = "Nombre completo", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 155)
    entradaNombre = Entry(pRegistrarP, width = 23, font = ("Sylfaen", 16), relief = "raised", bg = "#e6b800")
    entradaNombre.place(x = 300, y = 160)
    entradaNombre.config(justify = "center")
    
    radioVar = IntVar()
    Label(pRegistrarP, text = "Género", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 200)
    radioBHombre = Radiobutton(pRegistrarP, text = "Hombre", font = ("Sylfaen", 14), variable = radioVar, value = 1)
    radioBMujer = Radiobutton(pRegistrarP, text = "Mujer", font = ("Sylfaen", 14), variable = radioVar, value = 2)
    radioBHombre.place(x = 300, y = 201)
    radioBMujer.place(x = 300, y = 230)

    subtipos = obtenerSubtiposP()
    seleccion = StringVar()
    seleccion.set("Seleccione")
    Label(pRegistrarP, text = "Personalidad", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 274)
    cajaSPersonalidad = OptionMenu(pRegistrarP, seleccion, *subtipos)
    cajaSPersonalidad.place(x = 300, y = 275)

    paises = obtenerPaises()
    seleccion = StringVar()
    seleccion.set("Seleccione")
    Label(pRegistrarP, text = "País", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 319)
    cajaSPersonalidad = OptionMenu(pRegistrarP, seleccion, *paises)
    cajaSPersonalidad.place(x = 300, y = 320)

    Label(pRegistrarP, text = "Estado", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 364)
    entradaEstado = Label(pRegistrarP, width = 21, font = ("Sylfaen", 16), relief = "raised", bg = "#77b300")
    entradaEstado.place(x = 300, y = 365)

    botonIngresar = Button(pRegistrarP, text = "Ingresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "Black", bg = "#e6b800")
    botonIngresar.place(x = 63, y = 440)

    botonLimpiar = Button(pRegistrarP, text = "Limpiar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "Black", bg = "#24adc2")
    botonLimpiar.place(x = 233, y = 440)

    botonRegresar = Button(pRegistrarP, text = "Regresar", padx = 30, pady = 5, font = ("Impact", 13), relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarPantalla(pRegistrarP))
    botonRegresar.place(x = 400, y = 440)
    return ""

botonRegistrarP = Button(raiz, text = "Registrar los datos de una persona", padx = 80, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#b82e8a", command = guiRegistrarP)
botonRegistrarP.place(x = 65, y = 170)

botonRegistroD = Button(raiz, text = "Registro dinámico", padx = 147, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#e6b800")
botonRegistroD.place(x = 65, y = 250)

botonModificarP = Button(raiz, text = "Modificar los datos de una persona", padx = 77, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#24adc2")
botonModificarP.place(x = 65, y = 330)

botonEliminarP = Button(raiz, text = "Eliminar los datos de una persona", padx = 80, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#77b300")
botonEliminarP.place(x = 65, y = 410)

botonCrearXml = Button(raiz, text = "Crear XML", padx = 179, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#24adc2")
botonCrearXml.place(x = 65, y = 490)

botonReportes = Button(raiz, text = "Reportes", padx = 189, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#e6b800")
botonReportes.place(x = 65, y = 570)

botonSalir = Button(raiz, text = "Salir", padx = 206, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarPantalla(raiz))
botonSalir.place(x = 65, y = 650)

raiz.mainloop()