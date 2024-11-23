def crearPersona(personas, nombre=None, area=None):
    """Crea una nueva persona y la agrega al diccionario."""
    try:
        if nombre is None:
            nombre = input("Ingrese el nombre: ")
        if area is None:
            area = input("Ingrese el área: ")
        id_persona = len(personas) + 1  # Generar un ID único
        personas[id_persona] = {"nombre": nombre, "area": area}
        print(f"¡Persona con ID {id_persona} creada exitosamente!")
    except Exception as e:
        print(f"Error al crear la persona: {e}")

def listarPersonas(personas):
    """Lista todas las personas almacenadas."""
    try:
        if not personas:
            print("No hay personas registradas.")
        else:
            for id_persona, persona in personas.items():
                print(f"{id_persona}. Nombre: {persona['nombre']}, Área: {persona['area']}")
    except Exception as e:
        print(f"Error al listar personas: {e}")

def actualizarPersona(personas):
    """Actualiza los datos de una persona existente."""
    try:
        listarPersonas(personas)
        id_persona = int(input("Ingrese el número de la persona a actualizar: "))
        if id_persona in personas:
            nuevo_nombre = input("Ingrese el nuevo nombre (dejar en blanco para mantener el actual): ")
            nueva_area = input("Ingrese la nueva área (dejar en blanco para mantener la actual): ")
            if nuevo_nombre:
                personas[id_persona]["nombre"] = nuevo_nombre
            if nueva_area:
                personas[id_persona]["area"] = nueva_area
            print("¡Persona actualizada exitosamente!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Error: Debe ingresar un número válido para el ID.")
    except Exception as e:
        print(f"Error al actualizar la persona: {e}")

def eliminarPersona(personas):
    """Elimina una persona del diccionario."""
    try:
        listarPersonas(personas)
        id_persona = int(input("Ingrese el número de la persona a eliminar: "))
        if id_persona in personas:
            del personas[id_persona]
            print("¡Persona eliminada exitosamente!")
        else:
            print("ID inválido.")
    except ValueError:
        print("Error: Debe ingresar un número válido para el ID.")
    except Exception as e:
        print(f"Error al eliminar la persona: {e}")
