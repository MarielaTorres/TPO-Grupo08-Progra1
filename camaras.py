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
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def crearCamara(camaras,camara=None, lugar=None):
    """Crea una nueva cámara y la agrega al diccionario 'camaras' con un ID generado automáticamente.

    Args:
        camaras: El diccionario donde se almacenarán las cámaras.
    """
    contador_id = len(camaras)+1
    if camara is None:
        camara = input("Ingrese el nombre de la cámara: ")
    if lugar is None:
        lugar = input("Ingrese el lugar de la cámara: ")
    if esNombreCamaraValido(camara, camaras):
        if esLugarCamaraValido(lugar):
            camaras[contador_id] = {'camara': camara, 'lugar': lugar}
            print("¡Cámara creada exitosamente con el ID", contador_id,"!")

def listarCamaras(camaras):
    """Lista todas las cámaras almacenadas en el diccionario 'camaras'."""
    if not camaras:
        print("No hay cámaras registradas.")
    else:
        for id, datos in camaras.items():
            print(f"ID: {id}, Cámara: {datos['camara']}, Lugar: {datos['lugar']}")

def actualizarCamara(camaras, id):
    """Actualiza los datos de una cámara existente en el diccionario 'camaras'.

    Args:
        camaras: El diccionario donde se almacenan las cámaras.
        id: El ID de la cámara a actualizar.
    """
    listarCamaras(camaras)
    id = input("Ingrese el ID de la cámara a actualizar: ")
    if esIdValido(id, camaras):
        nueva_camara = input("Ingrese el nuevo nombre de la cámara (dejar en blanco para mantener el actual): ")
        nuevo_lugar = input("Ingrese el nuevo lugar (dejar en blanco para mantener el actual): ")

        if nueva_camara:
            if esNombreCamaraValido(nueva_camara, camaras):
                camaras[id]['camara'] = nueva_camara
        if nuevo_lugar:
            if esLugarCamaraValido(nuevo_lugar):
                camaras[id]['lugar'] = nuevo_lugar

        print("¡Cámara actualizada exitosamente!")
    else:
        print("ID de cámara inválido.")

def eliminarCamara(camaras, id):
    """Elimina una cámara del diccionario 'camaras'.

    Args:
        camaras: El diccionario donde se almacenan las cámaras.
        id: El ID de la cámara a eliminar.
    """
    listarCamaras(camaras)
    id = input("Ingrese el ID de la cámara a eliminar: ")
    if esIdValido(id, camaras):
        camaras.pop(id) 
        print("¡Cámara eliminada exitosamente!")
    else:
            print("ID de cámara inválido.")

