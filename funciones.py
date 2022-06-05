# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 27/05/2022 03:00pm
# Fecha de última Modificación: 04/06/2022 07:36am
# Versión: 3.10.2

# Importación de librerías
import re

# Variables globales
diccPaises = {}

# Definción de funciones
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

def validaCedula(cedula):
    if re.match("^\d{1}-\d{4}-\d{4}$", cedula):
        return True
    return False

def validaNombre(nombre):
    if re.match("^[a-zA-Z]{2,}\s[a-zA-Z]{2,}-[a-zA-Z]{2,}$", nombre):
        return True
    return False
