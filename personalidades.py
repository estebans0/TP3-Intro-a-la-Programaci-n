# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 27/05/2022 03:00pm
# Fecha de última Modificación: 04/06/2022 07:36am
# Versión: 3.10.2

# Importación de librerías
from funciones import *
from tkinter import *
from tkinter import messagebox

# FALTA GUARDAR UN ARCHIVO CON LA BASE DE DATOS PARA LEER AL INCIAR EL PROGRAMA
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

def cerrarMenuP(ppantalla): # Función de "Salir" del menú principal
    guardaBd()
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

    def ingresarDatos():
        cedula = entradaCedula.get()
        if validaCedula(cedula) == False:
            messagebox.showerror("Sistema de Personalidades", "Debe ingresar una cédula con el formato: #-####-####")
            return ""
        else:
            nombre = entradaNombre.get()
            if validaNombre(nombre) == False:
                messagebox.showerror("Sistema de Personalidades", "Debe ingresar su nombre con el formato: Nombre Ap1-Ap2")
                return ""
            else:
                if radioVar.get() == 1:
                    genero = True
                else:
                    genero = False
                personalidad = seleccion1.get().split(",")[0]
                personalidad = definirPersonalidad(personalidad)
                pais = seleccion2.get()
                pais = definirPais(pais)
                estado = [True,"",""]
                entradaEstado.config(text = "Activo")
                crearClasePersona(cedula, nombre, genero, personalidad, pais, estado)
                messagebox.showinfo("Sistema de Personalidades", "Se ha registrado correctamente a la persona.")
                cerrarPantalla(pRegistrarP)
                return ""
    
    def limpiar():
        entradaCedula.delete(0, END)
        entradaNombre.delete(0, END)
        radioVar.set(0)
        seleccion1.set("Seleccione")
        seleccion2.set("Seleccione")
        entradaEstado.config(text = "")

    Label(pRegistrarP, text = "Registrar los datos de una persona", font = ("Lucida Calligraphy", 21), fg = "Black").place(x = 30, y = 30)

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
    seleccion1 = StringVar()
    seleccion1.set("Seleccione")
    Label(pRegistrarP, text = "Personalidad", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 274)
    cajaSPersonalidad = OptionMenu(pRegistrarP, seleccion1, *subtipos)
    cajaSPersonalidad.place(x = 300, y = 275)

    paises = obtenerPaises()
    seleccion2 = StringVar()
    seleccion2.set("Seleccione")
    Label(pRegistrarP, text = "País", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 319)
    cajaSPersonalidad = OptionMenu(pRegistrarP, seleccion2, *paises)
    cajaSPersonalidad.place(x = 300, y = 320)

    Label(pRegistrarP, text = "Estado", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 364)
    entradaEstado = Label(pRegistrarP, width = 21, text = "", font = ("Sylfaen", 16), relief = "raised", bg = "#77b300")
    entradaEstado.place(x = 300, y = 365)

    botonIngresar = Button(pRegistrarP, text = "Ingresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#e6b800", command = ingresarDatos)
    botonIngresar.place(x = 63, y = 440)

    botonLimpiar = Button(pRegistrarP, text = "Limpiar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#24adc2", command = limpiar)
    botonLimpiar.place(x = 233, y = 440)

    botonRegresar = Button(pRegistrarP, text = "Regresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarPantalla(pRegistrarP))
    botonRegresar.place(x = 400, y = 440)
    return ""

# Interfaz de registro dinámico
def guiRegistroD():
    raiz.deiconify()
    pRegistroD = Toplevel()
    pRegistroD.geometry("600x290")
    pRegistroD.config(cursor = "star")

    def ingresarDatos():
        try:
            num = int(entradaCantidad.get())
            if num < 25:
                messagebox.showerror("Sistema de Personalidades", "Debe ingresar al menos 25 personas.")
                return ""
            registroDinamico(num)
            messagebox.showinfo("Sistema de Personalidades", f"Se ha registrado correctamente a {num} personas.")
            cerrarPantalla(pRegistroD)
            return ""
        except:
            messagebox.showerror("Sistema de Personalidades", f"Debe ingresar un valor numérico.")
    
    def limpiar():
        entradaCantidad.delete(0, END)

    Label(pRegistroD, text = "Registro dinámico", font = ("Lucida Calligraphy", 21), fg = "Black").place(x = 30, y = 30)

    Label(pRegistroD, text = "Cantidad", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 110)
    entradaCantidad = Entry(pRegistroD, width = 23, font = ("Sylfaen", 16), relief = "raised", bg = "#77b300")
    entradaCantidad.place(x = 300, y = 115)
    entradaCantidad.config(justify = "center")

    botonIngresar = Button(pRegistroD, text = "Ingresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#e6b800", command = ingresarDatos)
    botonIngresar.place(x = 63, y = 190)

    botonLimpiar = Button(pRegistroD, text = "Limpiar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#24adc2", command = limpiar)
    botonLimpiar.place(x = 233, y = 190)

    botonRegresar = Button(pRegistroD, text = "Regresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarPantalla(pRegistroD))
    botonRegresar.place(x = 400, y = 190)
    return ""

# Interfaz de modificar los datos de una persona
def guiModificarP():
    raiz.deiconify()
    pModificarP = Toplevel()
    pModificarP.geometry("600x290")
    pModificarP.config(cursor = "star")

    def guiModificarP2(cedula, nombre, personalidad):
        pModificarP.deiconify()
        pModificarP2 = Toplevel()
        pModificarP2.geometry("600x350")
        pModificarP2.config(cursor = "star")

        def modificarDP(cedula):
            personalidad = seleccion.get().split(",")[0]
            personalidad = definirPersonalidad(personalidad)
            modificarDatosP(cedula, personalidad)
            messagebox.showinfo("Sistema de Personalidades", f"Se han modificado correctamente los datos de {cedula}.")
            cerrarPantalla(pModificarP2)
            cerrarPantalla(pModificarP)
            return ""
        
        def limpiar():
            seleccion.set(personalidad)

        Label(pModificarP2, text = "Modificar los datos de una persona", font = ("Lucida Calligraphy", 21), fg = "Black").place(x = 30, y = 30)

        Label(pModificarP2, text = "Cédula", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 110)
        entradaCedula = Label(pModificarP2, width = 21, text = cedula, font = ("Sylfaen", 16), relief = "raised", bg = "#b82e8a")
        entradaCedula.place(x = 300, y = 115)
        entradaCedula.config(justify = "center")

        Label(pModificarP2, text = "Nombre completo", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 155)
        entradaNombre = Label(pModificarP2, width = 21, text = nombre, font = ("Sylfaen", 16), relief = "raised", bg = "#77b300")
        entradaNombre.place(x = 300, y = 160)
        entradaNombre.config(justify = "center")

        subtipos = obtenerSubtiposP()
        seleccion = StringVar()
        seleccion.set(personalidad)
        Label(pModificarP2, text = "Personalidad", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 204)
        cajaSPersonalidad = OptionMenu(pModificarP2, seleccion, *subtipos)
        cajaSPersonalidad.place(x = 300, y = 205)

        botonIngresar = Button(pModificarP2, text = "Ingresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#e6b800", command = lambda: modificarDP(cedula))
        botonIngresar.place(x = 63, y = 265)

        botonLimpiar = Button(pModificarP2, text = "Limpiar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#24adc2", command = limpiar)
        botonLimpiar.place(x = 233, y = 265)

        botonRegresar = Button(pModificarP2, text = "Regresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarPantalla(pModificarP2))
        botonRegresar.place(x = 400, y = 265)
        return ""

    def ingresarDatos():
        cedula = entradaCedula.get()
        if validaCedula(cedula) == False:
            messagebox.showerror("Sistema de Personalidades", "Debe ingresar una cédula con el formato: #-####-####.")
            return ""
        if identificarPersona(cedula) == False:
            messagebox.showerror("Sistema de Personalidades", "La cédula ingresada no existe en la base de datos.")
            return ""
        nombre = identificarPersona(cedula)[0]
        personalidad = identificarPersona(cedula)[-1]
        guiModificarP2(cedula, nombre, personalidad)
    
    def limpiar():
        entradaCedula.delete(0, END)

    Label(pModificarP, text = "Modificar los datos de una persona", font = ("Lucida Calligraphy", 21), fg = "Black").place(x = 30, y = 30)

    Label(pModificarP, text = "Cedula", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 110)
    entradaCedula = Entry(pModificarP, width = 23, font = ("Sylfaen", 16), relief = "raised", bg = "#77b300")
    entradaCedula.place(x = 300, y = 115)
    entradaCedula.config(justify = "center")

    botonIngresar = Button(pModificarP, text = "Ingresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#e6b800", command = ingresarDatos)
    botonIngresar.place(x = 63, y = 190)

    botonLimpiar = Button(pModificarP, text = "Limpiar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#24adc2", command = limpiar)
    botonLimpiar.place(x = 233, y = 190)

    botonRegresar = Button(pModificarP, text = "Regresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarPantalla(pModificarP))
    botonRegresar.place(x = 400, y = 190)
    return ""

# Interfaz de eliminar los datos de una persona
def guiEliminarP():
    raiz.deiconify()
    pEliminarP = Toplevel()
    pEliminarP.geometry("600x290")
    pEliminarP.config(cursor = "star")

    def guiEliminarP2(cedula):
        pEliminarP.deiconify()
        pEliminarP2 = Toplevel()
        pEliminarP2.geometry("600x290")
        pEliminarP2.config(cursor = "star")

        def eliminarDP(cedula):
            justificacion = entradaJustificacion.get()
            eliminarDatosP(cedula, justificacion)
            messagebox.showinfo("Sistema de Personalidades", f"Se han eliminado correctamente los datos de {cedula}.")
            cerrarPantalla(pEliminarP2)
            cerrarPantalla(pEliminarP)
            return ""
        
        def limpiar():
            entradaJustificacion.delete(0, END)

        Label(pEliminarP2, text = "Eliminar los datos de una persona", font = ("Lucida Calligraphy", 21), fg = "Black").place(x = 30, y = 30)

        Label(pEliminarP2, text = "Justificacion", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 110)
        entradaJustificacion = Entry(pEliminarP2, width = 23, font = ("Sylfaen", 16), relief = "raised", bg = "#77b300")
        entradaJustificacion.place(x = 300, y = 115)
        entradaJustificacion.config(justify = "center")

        botonIngresar = Button(pEliminarP2, text = "Ingresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#e6b800", command = lambda: eliminarDP(cedula))
        botonIngresar.place(x = 63, y = 190)

        botonLimpiar = Button(pEliminarP2, text = "Limpiar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#24adc2", command = limpiar)
        botonLimpiar.place(x = 233, y = 190)

        botonRegresar = Button(pEliminarP2, text = "Regresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarPantalla(pEliminarP2))
        botonRegresar.place(x = 400, y = 190)
        return ""

    def ingresarDatos():
        cedula = entradaCedula.get()
        if validaCedula(cedula) == False:
            messagebox.showerror("Sistema de Personalidades", "Debe ingresar una cédula con el formato: #-####-####.")
            return ""
        if identificarPersona(cedula) == False:
            messagebox.showerror("Sistema de Personalidades", "La cédula ingresada no existe en la base de datos.")
            return ""
        guiEliminarP2(cedula)
    
    def limpiar():
        entradaCedula.delete(0, END)

    Label(pEliminarP, text = "Eliminar los datos de una persona", font = ("Lucida Calligraphy", 21), fg = "Black").place(x = 30, y = 30)

    Label(pEliminarP, text = "Cedula", font = ("Sylfaen", 16), fg = "Black").place(x = 30, y = 110)
    entradaCedula = Entry(pEliminarP, width = 23, font = ("Sylfaen", 16), relief = "raised", bg = "#77b300")
    entradaCedula.place(x = 300, y = 115)
    entradaCedula.config(justify = "center")

    botonIngresar = Button(pEliminarP, text = "Ingresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#e6b800", command = ingresarDatos)
    botonIngresar.place(x = 63, y = 190)

    botonLimpiar = Button(pEliminarP, text = "Limpiar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#24adc2", command = limpiar)
    botonLimpiar.place(x = 233, y = 190)

    botonRegresar = Button(pEliminarP, text = "Regresar", padx = 30, pady = 5, font = ("Sylfaen", 14), relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarPantalla(pEliminarP))
    botonRegresar.place(x = 400, y = 190)
    return ""

# Interfaz del menú principal
botonRegistrarP = Button(raiz, text = "Registrar los datos de una persona", padx = 80, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#b82e8a", command = guiRegistrarP)
botonRegistrarP.place(x = 65, y = 170)

botonRegistroD = Button(raiz, text = "Registro dinámico", padx = 147, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#e6b800", command = guiRegistroD)
botonRegistroD.place(x = 65, y = 250)

botonModificarP = Button(raiz, text = "Modificar los datos de una persona", padx = 77, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#24adc2", command = guiModificarP)
botonModificarP.place(x = 65, y = 330)

botonEliminarP = Button(raiz, text = "Eliminar los datos de una persona", padx = 80, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#77b300", command = guiEliminarP)
botonEliminarP.place(x = 65, y = 410)

botonCrearXml = Button(raiz, text = "Crear XML", padx = 179, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#24adc2")
botonCrearXml.place(x = 65, y = 490)

botonReportes = Button(raiz, text = "Reportes", padx = 189, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#e6b800")
botonReportes.place(x = 65, y = 570)

botonSalir = Button(raiz, text = "Salir", padx = 206, pady = 5, font = "Sylfaen", relief = "raised", fg = "Black", bg = "#b82e8a", command = lambda: cerrarMenuP(raiz))
botonSalir.place(x = 65, y = 650)

raiz.mainloop()