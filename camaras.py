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
def crear_camara(camaras, camara, lugar):
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

def listar_camaras(camaras):
    """Lista todas las cámaras almacenadas en el diccionario 'camaras'."""
    if not camaras:
      print("No hay cámaras registradas.")
    else:
      for id, datos in camaras.items():
        print(f"ID: {id}, Cámara: {datos['camara']}, Lugar: {datos['lugar']}")

def actualizar_camara(camaras, id):
    """Actualiza los datos de una cámara existente en el diccionario 'camaras'.

    Args:
        camaras: El diccionario donde se almacenan las cámaras.
        id: El ID de la cámara a actualizar.
    """
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

def eliminar_camara(camaras, id):
    """Elimina una cámara del diccionario 'camaras'.

    Args:
        camaras: El diccionario donde se almacenan las cámaras.
        id: El ID de la cámara a eliminar.
    """
    if id in camaras:
        camaras.pop(id) 
        print("¡Cámara eliminada exitosamente!")
    else:
        print("ID de cámara inválido.")


#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    # Diccionario para almacenar las cámaras y contador para los IDs
    camaras = {}
    contador_id = 1

    #-------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        opciones = 5
        while True:
            print()
            print("---------------------------")
            print("\n--- CRUD de Cámaras ---")
            print("---------------------------")
            print("1. Crear cámara")
            print("2. Listar cámaras")
            print("3. Actualizar cámara")
            print("4. Eliminar cámara")
            print("0. Salir del programa")
            print("---------------------------")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones)]: # Sólo continua si se elije una opcion de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0": # Opción salir del programa
            exit() 

        elif opcion == "1":   # Opción 1
            crear_camara()
        elif opcion == "2":   # Opción 2
            listar_camaras()
        elif opcion == "3":   # Opción 3
            actualizar_camara()
        elif opcion == "4":   # Opción 4
            eliminar_camara()

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()




while True:
  print("\n--- CRUD de Cámaras ---")
  print("1. Crear cámara")
  print("2. Listar cámaras")
  print("3. Actualizar cámara")
  print("4. Eliminar cámara")
  print("5. Salir")

  opcion = input("Ingrese una opción: ")

  if opcion == '1':
    camara = input("Ingrese el nombre de la cámara: ")
    lugar = input("Ingrese el lugar de la cámara: ")
    crear_camara(camaras, camara, lugar)
  elif opcion == '2':
    listar_camaras(camaras)
  elif opcion == '3':
    id = int(input("Ingrese el ID de la cámara a actualizar: ")) 
    actualizar_camara(camaras, id)
  elif opcion == '4':
    id = int(input("Ingrese el ID de la cámara a eliminar: ")) 
    eliminar_camara(camaras, id)
  elif opcion == '5':
    break
  else:
    print("Opción inválida.")
