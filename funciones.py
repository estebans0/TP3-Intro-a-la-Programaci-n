# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 27/05/2022 03:00pm
# Fecha de última Modificación: 04/06/2022 07:36am
# Versión: 3.10.2

# Importación de librerías
import re
from clases import *

# Variables globales
diccPaises = {}

# Definción de funciones
def validaCedula(cedula):
    if re.match("^\d{1}-\d{4}-\d{4}$", cedula):
        return True
    return False

def validaNombre(nombre):
    if re.match("^[a-zA-Z]{2,}\s[a-zA-Z]{2,}-[a-zA-Z]{2,}$", nombre):
        return True
    return False

def crearDiccPersonalidades():
    diccPaises
    llave = ""
    valores = []
    contador = 0
    with open("personalidades.txt") as file:
        for i in file:
            if i[0] == "*":
                if contador == 23:
                    valor = (i[1:-5], i[-4:])
                else:
                    valor = (i[1:-6], i[-5:-1])
                valores.append(valor)
            if i[0] == "-":
                valores = []
                llave = i[1:-1]
            if llave != "":
                diccPaises[llave] = valores
            contador += 1
    return diccPaises

def obtenerSubtiposP():
    valores = list(crearDiccPersonalidades().values())
    subtipos = []
    for i in valores:
        for j in i:
            subtipo = str(j[0])+", "+str(j[1])
            subtipos.append(subtipo)
    return subtipos

def obtenerPaises():
    indice = 0
    paises = []
    with open("paises.txt") as file:
        for i in file:
            for j in i:
                if j == "(":
                    paises.append(i[:indice-1])
                indice += 1
            indice = 0
    return paises

def definirPersonalidad(subtipo):
    valores = list(crearDiccPersonalidades().values())
    tipo = 0
    subcategoria = 0
    for i in valores:
        for j in i:
            if subtipo == j[0]:
                return tipo, subcategoria
            subcategoria += 1
        subcategoria = 0
        tipo += 1
    return ""

def definirPais(pais):
    valor = 0
    for i in obtenerPaises():
        if pais == i:
            return valor
        valor += 1
    
def crearClasePersona(cedula, nombre, genero, personalidad, pais, estado):
    datos = []
    persona = Persona(cedula)
    persona.asignarNombre(nombre)
    persona.asignarGenero(genero)
    persona.asignarPersonalidad(personalidad)
    persona.asignarPais(pais)
    persona.asignarEstado(estado)
    datos = persona.mostrarTodo()
    print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(f"Se ha registrado correctamente a la persona: {persona.mostrarCedula()}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
    print(datos)