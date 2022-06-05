# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 27/05/2022 03:00pm
# Fecha de última Modificación: 04/06/2022 07:36am
# Versión: 3.10.2

# Importación de librerías
from personalidades import *

class Persona():
    # Definición de métodos
    def __init__(self, pcedula):
        self.cedula = pcedula
        self.nombre = ""
        self.genero = True
        self.personalidad = ()
        self.pais = 0
        self.estado = []

    def asignarCedula(self, pcedula):
        self.cedula = pcedula
        return
    
    def mostrarCedula(self):
        return self.cedula
    
    def asignarNombre(self, pnombre):
        self.nombre = pnombre
        return
    
    def mostrarNombre(self):
        return self.nombre
    
    def asignarGenero(self, pgenero):
        self.genero = pgenero
        return
    
    def mostrarGenero(self):
        return self.genero
    
    def asignarPersonalidad(self, ppersonalidad):
        self.personalidad = ppersonalidad
        return
    
    def mostrarPersonalidad(self):
        return self.personalidad
    
    def asignarPais(self, ppais):
        self.pais = ppais
        return
    
    def mostrarPais(self):
        return self.pais
    
    def asignarEstado(self, pestado):
        self.estado = pestado
        return
    
    def mostrarEstado(self):
        return self.estado

    def mostrarTodo(self):
        return [self.cedula, self.nombre, self.genero, self.personalidad, self.pais, self.estado]