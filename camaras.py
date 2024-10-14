"""
-----------------------------------------------------------------------------------------------
Título: Modulo de camaras del sistema de gestion de camaras
Fecha: 07/10/2024
Autor: Equipo 8

Descripción: Modulo donde se gestionará todas las funcionalidades relacionadas con las cámaras del sistema

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def crearCamara(camaras, camara, lugar, contador_id):
    """Crea una nueva cámara y la agrega al diccionario 'camaras' con un ID generado automáticamente.

    Args:
        camaras: El diccionario donde se almacenarán las cámaras.
        camara: El nombre o modelo de la cámara.
        lugar: La ubicación de la cámara.
        contador_id: El contador actual para generar el ID.
    """
    
    camaras[contador_id] = {'camara': camara, 'lugar': lugar}
    print("¡Cámara creada exitosamente con el ID", contador_id, "!")
    return contador_id + 1  # Retorna el nuevo contador

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
    if id in camaras:
        nueva_camara = input("Ingrese el nuevo nombre de la cámara (dejar en blanco para mantener el actual): ")
        nuevo_lugar = input("Ingrese el nuevo lugar (dejar en blanco para mantener el actual): ")

        if nueva_camara:
            camaras[id]['camara'] = nueva_camara
        if nuevo_lugar:
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
    if id in camaras:
        camaras.pop(id) 
        print("¡Cámara eliminada exitosamente!")
    else:
        print("ID de cámara inválido.")
