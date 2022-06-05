# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 27/05/2022 03:00pm
# Fecha de última Modificación: 04/06/2022 07:36am
# Versión: 3.10.2

# Importación de librerías
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
def guiRegDatos():
    return ""

botonBDPaises = Button(raiz, text = "Registrar los datos de una persona", padx = 80, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#b82e8a")
botonBDPaises.place(x = 65, y = 170)

botonIns1P = Button(raiz, text = "Registro dinámico", padx = 147, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#e6b800")
botonIns1P.place(x = 65, y = 250)

botonInsNP = Button(raiz, text = "Modificar los datos de una persona", padx = 77, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#24adc2")
botonInsNP.place(x = 65, y = 330)

botonEnlazarAbu = Button(raiz, text = "Eliminar los datos de una persona", padx = 80, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#77b300")
botonEnlazarAbu.place(x = 65, y = 410)

botonDarBaja = Button(raiz, text = "Crear XML", padx = 179, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#24adc2")
botonDarBaja.place(x = 65, y = 490)

botonCorreo = Button(raiz, text = "Reportes", padx = 189, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#e6b800")
botonCorreo.place(x = 65, y = 570)

botonSalir = Button(raiz, text = "Salir", padx = 206, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarPantalla(raiz))
botonSalir.place(x = 65, y = 650)

raiz.mainloop()