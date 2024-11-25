"""
-----------------------------------------------------------------------------------------------
Título: Modulo de camaras del sistema de gestion de camaras
Fecha: 07/10/2024
Autor: Equipo 8

Descripción: Modulo donde se gestionará todas las funcionalidades relacionadas con las cámaras del sistema

Pendientes:
-----------------------------------------------------------------------------------------------
"""
from validaciones import esIdValido, esNombreCamaraValido, esLugarCamaraValido
import crudJson
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def crearCamara(camaras, camara=None, lugar=None):
    """Crea una nueva cámara y la agrega al diccionario 'camaras' con un ID generado automáticamente.

    Args:
        camaras: El diccionario donde se almacenarán las cámaras.
    """
    contador_id = len(camaras) + 1
    if not camara:
        camara = input("Ingrese el nombre de la cámara: ").strip()
    if not lugar :
        lugar = input("Ingrese el lugar de la cámara: ").strip()
    if esNombreCamaraValido(camara, camaras) and esLugarCamaraValido(lugar):
        camaras[str(contador_id)] = {'camara': camara, 'lugar': lugar}
        crudJson.exportarDatos("camaras.json", camaras)
        print(f"¡Cámara creada exitosamente con el ID {contador_id}!")
    

def listarCamaras(camaras):
    """Lista todas las cámaras almacenadas en el diccionario 'camaras'."""
    if not camaras:
        print("No hay cámaras registradas.")
    else:
        for id, datos in camaras.items():
            print(f"ID: {id}, Cámara: {datos['camara']}, Lugar: {datos['lugar']}")

def actualizarCamara(camaras, id = None):
    """Actualiza los datos de una cámara existente en el diccionario 'camaras'.

    Args:
        camaras: El diccionario donde se almacenan las cámaras.
        id: El ID de la cámara a actualizar.
    """
    listarCamaras(camaras)
    id = int(input("Ingrese el ID de la cámara a actualizar: ").strip())   # Asegurarse de que el ID sea un entero
    id = str(id)
    if esIdValido(id, camaras):
        nueva_camara = input("Ingrese el nuevo nombre de la cámara (dejar en blanco para mantener el actual): ").strip()
        nuevo_lugar = input("Ingrese el nuevo lugar (dejar en blanco para mantener el actual): ").strip()
        if nueva_camara:
            camaras[id]['camara'] = nueva_camara
        if nuevo_lugar:
            camaras[id]['lugar'] = nuevo_lugar
        crudJson.actualizarDatoJson("camaras.json", id, camaras)
        print("¡Cámara actualizada exitosamente!")


def eliminarCamara(camaras, id = None):
    """Elimina una cámara del diccionario 'camaras'.

    Args:
        camaras: El diccionario donde se almacenan las cámaras.
        id: El ID de la cámara a eliminar.
    """
    listarCamaras(camaras)
    id = int(input("Ingrese el ID de la cámara a eliminar: ").strip()) # Asegurarse de que el ID sea un entero
    id = str(id)
    if esIdValido(id, camaras):
        camaras.pop(id)
        crudJson.eliminarDatoJson("camaras.json", id)
        print("¡Cámara eliminada exitosamente!")

