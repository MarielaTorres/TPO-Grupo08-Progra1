"""
-----------------------------------------------------------------------------------------------
Título: Modulo de validaciones
Fecha: 07/10/2024
Autor: Equipo 8

Descripción: Modulo donde se gestionará todas las validaciones de los datos ingresados por el usuario

Pendientes:
-----------------------------------------------------------------------------------------------
"""
from datetime import datetime
import re

def esNombreCamaraValido(camara, camaras):
    if not camara or camara == "":
        raise ValueError("El nombre de la cámara no puede estar vacío.")
    elif camara in (cam['camara'] for cam in camaras.values()):
        raise ValueError("El nombre de la cámara ya existe.")       
    return True

def esLugarCamaraValido(lugar):
    if not lugar or lugar == "":
        raise ValueError("El nombre de la cámara no puede estar vacío.")
    elif re.search(r'\d', lugar):  # Verifica si hay un número en el lugar
        raise ValueError("Error: El lugar no debe contener números.")
    return True

def esIdValido(id, camaras):
    if id not in camaras.keys():
        raise KeyError(f"El ID {id} no corresponde a ninguna cámara registrada.")
    return True

def esIdPersonaValido(id, personas):
    if id not in personas.keys():
        raise KeyError(f"El ID {id} no corresponde a ninguna persona registrada.")
    return True

def validar_fecha(fecha):
    """Valida que una fecha ingresada tenga el formato correcto (YYYY-MM-DD)."""
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def esNombrePersonaValido(nombre):
    if not nombre:
        raise Exception("El nombre de la persona no puede estar vacio.")
    elif re.search(r'\d', nombre):  # Verifica si hay un número en el lugar
        raise ValueError("Error: El nombre no debe contener números.")
    return True

def esAreaValida(area):
    if not area:
        raise Exception("El nombre del área no puede estar vacio.")
    return True

def manejar_intentos(funcion, *args, intentos=3, mensaje_error="Dato inválido. Inténtalo de nuevo."):
    """
    Maneja intentos para ejecutar una función y capturar errores.
    :param funcion: La función que queremos ejecutar.
    :param args: Argumentos para la función.
    :param intentos: Número de intentos permitidos.0
    :param mensaje_error: Mensaje de error a mostrar.
    :return: None si falla o el resultado de la función si tiene éxito.
    """
    for intento in range(intentos):
        try:
            return funcion(*args)
        except (ValueError, KeyError, Exception) as e:
            print(f"{mensaje_error}: {str(e)} ({intento + 1}/{intentos})")
            if intento == intentos - 1:
                print("Se superó el número de intentos. Regresando al menú principal.")
                return None






    
