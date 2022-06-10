# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 27/05/2022 03:00pm
# Fecha de última Modificación: 04/06/2022 07:36am
# Versión: 3.10.2

# Importación de librerías
from clases import *
import re
import random
import names

# Variables globales
diccPersonalidades = {}
personas = []

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
    diccPersonalidades
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
                diccPersonalidades[llave] = valores
            contador += 1
    return diccPersonalidades

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

def generarCedula():
    cedula = ""
    cedula += str(random.randint(1,9))+"-"
    for i in range(2):
        for j in range(4):
            cedula += str(random.randint(1,9))
        if i == 0:
            cedula += "-"
    return cedula

def generarNombre():
    nombre = ""
    nombre += str(names.get_first_name())+" "
    for i in range(2):
        nombre += names.get_last_name()
        if i == 0:
            nombre += "-"
    return nombre

def generarGenero():
    num = random.randint(0,1)
    if num == 0:
        return True
    else:
        return False

def generarPersonalidad():
    contador = 0
    diccPersonalidades = crearDiccPersonalidades()
    cTipo = len(diccPersonalidades) - 1
    tipo = random.randint(0, cTipo)
    for i in diccPersonalidades:
        if contador == tipo:
            subcategoria = random.randint(0, len(diccPersonalidades[i]) - 1)
        contador += 1
    return tipo, subcategoria

def generarPais():
    pais = random.randint(0, len(obtenerPaises()) - 1)
    return pais

def crearClasePersona(cedula, nombre, genero, personalidad, pais, estado):
    personas
    persona = Persona(cedula)
    persona.asignarNombre(nombre)
    persona.asignarGenero(genero)
    persona.asignarPersonalidad(personalidad)
    persona.asignarPais(pais)
    persona.asignarEstado(estado)
    print(persona.mostrarTodo())
    personas.append(persona)
    #print(personas[0].mostrarTodo())

def registroDinamico(num):
    for i in range(num):
        cedula = generarCedula()
        nombre = generarNombre()
        genero = generarGenero()
        personalidad = generarPersonalidad()
        pais = generarPais()
        estado = True
        crearClasePersona(cedula, nombre, genero, personalidad, pais, estado)
    return ""