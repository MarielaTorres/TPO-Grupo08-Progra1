def crear_persona():
  """Crea una nueva persona y la agrega a la lista."""
  nombre = input("Ingrese el nombre: ")
  area = input("Ingrese el área: ")
  personas.append({"nombre": nombre, "area": area})
  print("Persona creada exitosamente!")

def listar_personas():
  """Lista todas las personas almacenadas."""
  if not personas:
    print("No hay personas registradas.")
  else:
    for i, persona in enumerate(personas):
      print(f"{i+1}. Nombre: {persona['nombre']}, Area: {persona['area']}")

def actualizar_persona():
  """Actualiza los datos de una persona existente."""
  listar_personas()
  indice = int(input("Ingrese el número de la persona a actualizar: ")) - 1
  if 0 <= indice < len(personas):
    nuevo_nombre = input("Ingrese el nuevo nombre (dejar en blanco para mantener el actual): ")
    nueva_area = input("Ingrese la nueva área (dejar en blanco para mantener la actual): ")
    if nuevo_nombre:
      personas[indice]["nombre"] = nuevo_nombre
    if nueva_area:
      personas[indice]["area"] = int(nueva_area)
    print("Persona actualizada exitosamente!")
  else:
    print("Índice inválido.")

def eliminar_persona():
  """Elimina una persona de la lista."""
  listar_personas()
  indice = int(input("Ingrese el número de la persona a eliminar: ")) - 1
  if 0 <= indice < len(personas):
    del personas[indice]
    print("Persona eliminada exitosamente!")
  else:
    print("Índice inválido.")

# Lista para almacenar las personas
personas = []

while True:
  print("\n--- CRUD de Personas ---")
  print("1. Crear persona")
  print("2. Listar personas")
  print("3. Actualizar persona")
  print("4. Eliminar persona")
  print("5. Salir")

  opcion = input("Ingrese una opción: ")

  if opcion == '1':
    crear_persona()
  elif opcion == '2':
    listar_personas()
  elif opcion == '3':
    actualizar_persona()
  elif opcion == '4':
    eliminar_persona()
  elif opcion == '5':
    break
  else:
    print("Opción inválida.")