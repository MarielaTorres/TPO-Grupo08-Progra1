import json


# Función para exportar datos a un archivo JSON
def exportarDatos(archivo, datos):
    """Exporta datos a un archivo JSON.

    Args:
        archivo (str): Nombre del archivo donde se guardarán los datos.
        datos (dict): Datos a exportar.
    """
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
    print(f"-- Responsibilidad JSON: Datos exportados a {archivo} --")


# Función para importar datos desde un archivo JSON
def importarDatos(archivo):
    """Importa datos desde un archivo JSON.
    Args:
        archivo (str): Nombre del archivo desde el que se cargarán los datos.
    Returns:
        dict: Datos importados.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        result = {key: value for key, value in datos.items()}
        print(f"-- Responsibilidad JSON: Datos importados de {archivo} --")
        return result
    except FileNotFoundError:
        print(f"-- Responsibilidad JSON: El archivo {archivo} no se encontró. --")
        return {}
    except json.JSONDecodeError:
        print(
            f"-- Responsibilidad JSON: Error al decodificar el archivo {archivo}. Asegúrate de que sea un archivo JSON válido. -- "
        )
        return {}


def actualizarDatoJson(archivo, id, dic):
    """Actualiza un diccionario del archivo JSON según el id

    Args:
        archivo (str): Nombre del archivo desde el que se cargarán los datos.
        id (str): id del dato
        dic (dict): Diccionario con los datos actualizados
    Returns:
    """
    datos = importarDatos(archivo)
    idStr = str(id)

    if idStr in datos:
        datos[idStr] = dic  # Actualiza el diccionario con el nuevo contenido
        exportarDatos(archivo, datos)
        print(f"-- Responsibilidad JSON: El ID {id} ha sido actualizado. -- ")
    else:
        print(f"-- Responsibilidad JSON: No se encontró el ID {id} en el archivo. --")


def eliminarDatoJson(archivo, id):
    """Elimina un dato del archivo JSON según su id.
    Args:
        archivo (str): Nombre del archivo desde el que se eliminará el dato.
        id (str): id del dato a eliminar.
    """
    try:
        datos = importarDatos(archivo)

        # Convertir el ID a string (porque las claves en JSON son strings)
        id_str = str(id)

        if id_str in datos:
            del datos[id_str]

            exportarDatos(archivo, datos)
            print(
                f"-- Responsibilidad JSON: Registro con id {id} eliminado de {archivo} --"
            )
        else:
            print(
                f"-- Responsibilidad JSON: No se encontró el id {id} en el archivo. --"
            )
    except FileNotFoundError:
        print(f"-- Responsibilidad JSON: El archivo {archivo} no se encontró. --")
    except json.JSONDecodeError:
        print(
            f"-- Responsibilidad JSON: Error al decodificar el archivo {archivo}. Asegúrate de que sea un archivo JSON válido. --"
        )
