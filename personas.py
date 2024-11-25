import crudJson
from validaciones import esNombrePersonaValido, esAreaValida, esIdPersonaValido

def crearPersona(personas, nombre=None, area=None):
    """Crea una nueva persona y la agrega al diccionario."""
    if nombre is None:
        nombre = input("Ingrese el nombre: ").strip()
    if area is None:
        area = input("Ingrese el área: ").strip()
    if esNombrePersonaValido(nombre) and esAreaValida(area):
        id_persona = len(personas) + 1  # Generar un ID único
        personas[str(id_persona)] = {"nombre": nombre, "area": area}
        crudJson.exportarDatos("personas.json", personas)
        print(f"¡Persona con ID {id_persona} creada exitosamente!")
    

def listarPersonas(personas):
    """Lista todas las personas almacenadas."""
    if not personas:
        print("No hay personas registradas.")
    else:
        for id_persona, persona in personas.items():
            print(f"{id_persona}. Nombre: {persona['nombre']}, Área: {persona['area']}")

def actualizarPersona(personas):
    """Actualiza los datos de una persona existente."""
    listarPersonas(personas)
    id_persona = int(input("Ingrese el número de la persona a actualizar: ").strip())
    id_persona = str(id_persona) 
    if esIdPersonaValido(id_persona, personas):
        nuevo_nombre = input("Ingrese el nuevo nombre (dejar en blanco para mantener el actual): ").strip()
        nueva_area = input("Ingrese la nueva área (dejar en blanco para mantener la actual): ").strip()
        if nuevo_nombre:
            personas[id_persona]["nombre"] = nuevo_nombre
        if nueva_area:
            personas[id_persona]["area"] = nueva_area
        crudJson.actualizarDatoJson("personas.json", id_persona, personas)
        print("¡Persona actualizada exitosamente!")


def eliminarPersona(personas):
    """Elimina una persona del diccionario."""
    listarPersonas(personas)
    id_persona = int(input("Ingrese el número de la persona a eliminar: ").strip())
    id_persona = str(id_persona) 
    if esIdPersonaValido(id_persona, personas):
        del personas[id_persona]
        crudJson.eliminarDatoJson("personas.json", id_persona)
        print("¡Persona eliminada exitosamente!")
    