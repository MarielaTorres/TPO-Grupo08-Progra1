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
def crearCamara(camaras, camara=None, lugar=None):
    """Crea una nueva cámara y la agrega al diccionario 'camaras' con un ID generado automáticamente.

    Args:
        camaras: El diccionario donde se almacenarán las cámaras.
    """
    try:
        contador_id = len(camaras) + 1
        if camara is None:
            camara = input("Ingrese el nombre de la cámara: ").strip()
            if not camara:
                raise ValueError("El nombre de la cámara no puede estar vacío.")
        if lugar is None:
            lugar = input("Ingrese el lugar de la cámara: ").strip()
            if not lugar:
                raise ValueError("El lugar de la cámara no puede estar vacío.")

        camaras[contador_id] = {'camara': camara, 'lugar': lugar}
        print(f"¡Cámara creada exitosamente con el ID {contador_id}!")
    except ValueError as e:
        print(f"Error al crear la cámara: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def listarCamaras(camaras):
    """Lista todas las cámaras almacenadas en el diccionario 'camaras'."""
    try:
        if not camaras:
            print("No hay cámaras registradas.")
        else:
            for id, datos in camaras.items():
                print(f"ID: {id}, Cámara: {datos['camara']}, Lugar: {datos['lugar']}")
    except Exception as e:
        print(f"Ocurrió un error al listar las cámaras: {e}")

def actualizarCamara(camaras, id):
    """Actualiza los datos de una cámara existente en el diccionario 'camaras'.

    Args:
        camaras: El diccionario donde se almacenan las cámaras.
        id: El ID de la cámara a actualizar.
    """
    try:
        listarCamaras(camaras)
        id = int(id)  # Asegurarse de que el ID sea un entero
        if id not in camaras:
            raise KeyError(f"El ID {id} no corresponde a ninguna cámara registrada.")

        nueva_camara = input("Ingrese el nuevo nombre de la cámara (dejar en blanco para mantener el actual): ").strip()
        nuevo_lugar = input("Ingrese el nuevo lugar (dejar en blanco para mantener el actual): ").strip()

        if nueva_camara:
            camaras[id]['camara'] = nueva_camara
        if nuevo_lugar:
            camaras[id]['lugar'] = nuevo_lugar

        print("¡Cámara actualizada exitosamente!")
    except ValueError:
        print("Error: El ID debe ser un número entero.")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

def eliminarCamara(camaras, id):
    """Elimina una cámara del diccionario 'camaras'.

    Args:
        camaras: El diccionario donde se almacenan las cámaras.
        id: El ID de la cámara a eliminar.
    """
    try:
        listarCamaras(camaras)
        id = int(id)  # Asegurarse de que el ID sea un entero
        if id not in camaras:
            raise KeyError(f"El ID {id} no corresponde a ninguna cámara registrada.")

        camaras.pop(id)
        print("¡Cámara eliminada exitosamente!")
    except ValueError:
        print("Error: El ID debe ser un número entero.")
    except KeyError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
