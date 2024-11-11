"""
-----------------------------------------------------------------------------------------------
Título: Modulo de validaciones
Fecha: 07/10/2024
Autor: Equipo 8

Descripción: Modulo donde se gestionará todas las validaciones de los datos ingresados por el usuario

Pendientes:
-----------------------------------------------------------------------------------------------
"""
import re

def esIdValido(id, camaras):
    try:
        int(id) # Intentar convertir el ID a un entero
        print("ID válido.")
        if id in camaras:
            return True
        else:
            return False
    except ValueError:
        print("El ID debe ser un número entero.")
        return False
    
def esNombreCamaraValido(camara, camaras):
    if camara in (cam['camara'] for cam in camara.values()):
        print("El nombre de la cámara ya existe.")
        return False
    return True

def esLugarCamaraValido(lugar):
    if re.search(r'\d', lugar):  # Verifica si hay un número en el lugar
        print("Error: El lugar no debe contener números.")
        return False
    return True

    
