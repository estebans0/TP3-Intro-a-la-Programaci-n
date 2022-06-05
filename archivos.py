# Elaborado por: Juan Ceballos y Esteban Solano
# Fecha de Creación: 27/05/2022 03:00pm
# Fecha de última Modificación: 04/06/2022 07:36am
# Versión: 3.10.2

# Importación de librerías
from personalidades import *

# Definción de funciones
def graba(nomArchGrabar,lista):
    #Función que graba un archivo con una lista de estudiantes
    try:
        f=open(nomArchGrabar,"wb")
        print("1.Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee (nomArchLeer):
    #Función que lee un archivo con una lista de estudiantes
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        print("2. Voy a leer el archivo: ", nomArchLeer)
        lista = pickle.load(f)
        print("2. Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return lista
