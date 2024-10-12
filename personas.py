def crearPersona(personas):
    """Crea una nueva persona y la agrega al diccionario."""
    nombre = input("Ingrese el nombre: ")
    area = input("Ingrese el área: ")
    id_persona = len(personas) + 1  # Generar un ID único
    personas[id_persona] = {"nombre": nombre, "area": area}
    print("Persona creada exitosamente!")

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
    id_persona = int(input("Ingrese el número de la persona a actualizar: "))
    if id_persona in personas:
        nuevo_nombre = input("Ingrese el nuevo nombre (dejar en blanco para mantener el actual): ")
        nueva_area = input("Ingrese la nueva área (dejar en blanco para mantener la actual): ")
        if nuevo_nombre:
            personas[id_persona]["nombre"] = nuevo_nombre
        if nueva_area:
            personas[id_persona]["area"] = nueva_area
        print("Persona actualizada exitosamente!")
    else:
        print("ID inválido.")

def eliminarPersona(personas):
    """Elimina una persona del diccionario."""
    listarPersonas(personas)
    id_persona = int(input("Ingrese el número de la persona a eliminar: "))
    if id_persona in personas:
        del personas[id_persona]
        print("Persona eliminada exitosamente!")
    else:
        print("ID inválido.")

def main():
    
    # Diccionario para almacenar las personas
    personas = {}

    while True:
        print("\n--- CRUD de Personas ---")
        print("1. Crear persona")
        print("2. Listar personas")
        print("3. Actualizar persona")
        print("4. Eliminar persona")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            crearPersona()
        elif opcion == '2':
            listarPersonas()
        elif opcion == '3':
            actualizarPersona()
        elif opcion == '4':
            eliminarPersona()
        elif opcion == '5':
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
