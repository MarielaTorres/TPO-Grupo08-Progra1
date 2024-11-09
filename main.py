"""
-----------------------------------------------------------------------------------------------
Título: Menu principal trabajo práctica: Gestor de cámaras
Fecha: 30/09/2024
Autor: Equipo 8

Descripción:
Menu principal que manejará las funcionalidades del gestor de cámaras, creado por el equipo 8

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# MÓDULOS
#----------------------------------------------------------------------------------------------

from personas import crearPersona, listarPersonas, actualizarPersona, eliminarPersona
from camaras import crearCamara, listarCamaras, actualizarCamara, eliminarCamara
from logEvents import registrarEvento, listarEventos
from test import precargaDatos

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
'''TBD'''

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------

def main():

    #----------------------------------------------------------------------------------------------
    # Inicialización de variables y diccionarios
    #----------------------------------------------------------------------------------------------
    camaras = {}
    personas = {}
    registros = {}

    #----------------------------------------------------------------------------------------------
    # Precarga de datos para pruebas
    #----------------------------------------------------------------------------------------------
    precargaDatos(camaras, personas, registros)
    
    #----------------------------------------------------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        opciones = 5
        while True:
            print()
            print("---------------------------")
            print("MENÚ DEL SISTEMA PRINCIPAL           ")
            print("---------------------------")
            print("[1] Gestión de cámaras")
            print("[2] Gestión de personas")
            print("[3] Log de Movimientos")
            print("[4] Informes generales")
            print("---------------------------")
            print("[0] Salir del programa")
            print()
            
            opcion = input("Seleccione una opción: ")
            if opcion in [str(i) for i in range(0, opciones)]:  # Solo continua si se elige una opción de menú válida
                break
            else:
                input("Opción inválida. Presione ENTER para volver a seleccionar.")
        print()

        if opcion == "0":  # Opción salir del programa
            break

        elif opcion == "1":  # Opción 1 - Gestión de cámaras
            opciones = 5
            while True:
                print()
                print("---------------------------")
                print("\n--- Menú de Gestión de Cámaras ---")
                print("---------------------------")
                print("1. Crear cámara")
                print("2. Listar cámaras")
                print("3. Actualizar cámara")
                print("4. Eliminar cámara")
                print("0. Volver al menú principal")
                print("---------------------------")
                print()
                
                opcion_camara = input("Seleccione una opción: ")
                if opcion_camara in [str(i) for i in range(0, opciones)]:  # Solo continua si se elige una opción de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

            if opcion_camara == "0":  # Si la condición evalúa y es verdad, sigue con el siguiente bloque de código
                continue

            # Aquí puedes implementar la lógica para cada opción del CRUD de cámaras
            if opcion_camara == "1":
                crearCamara(camaras)
                # Lógica para crear cámara
            elif opcion_camara == "2":
                listarCamaras(camaras)
                # Lógica para listar cámaras
            elif opcion_camara == "3":
                id = int(input("Ingrese el ID de la cámara a actualizar: ")) 
                actualizarCamara(camaras, id)
                # Lógica para actualizar cámara
            elif opcion_camara == "4":
                id = int(input("Ingrese el ID de la cámara a actualizar: ")) 
                eliminarCamara(camaras, id)
                # Lógica para eliminar cámara

        elif opcion == "2":  # Opción 2 - Gestión de personas
            opciones = 6
            while True:
                print("---------------------------")
                print("\n--- Menú de gestión de Personas ---")
                print("---------------------------")
                print("1. Crear persona")
                print("2. Listar personas")
                print("3. Actualizar persona")
                print("4. Eliminar persona")
                print("0. Volver al menú principal")
                print("---------------------------")
                
                opcion_persona = input("Ingrese una opción: ")
                if opcion_persona in [str(i) for i in range(0, opciones)]:  # Solo continua si se elige una opción de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

            if opcion_persona == "0":  # Volver al menú principal
                continue

            if opcion_persona == "1":
                crearPersona(personas)
            elif opcion_persona == "2":
                listarPersonas(personas)
            elif opcion_persona == "3":
                actualizarPersona(personas)
            elif opcion_persona == "4":
                eliminarPersona(personas)

        elif opcion == "3":  # Opción 3 - Log de Movimientos
            opciones = 3
            while True:
                print("---------------------------")
                print("\n--- Log de Movimientos ---")
                print("---------------------------")
                print("1. Registrar evento")
                print("2. Listar eventos")
                print("0. Volver al menú principal")
                print("---------------------------")
                opcion_log = input("Seleccione una opción: ")
                if opcion_log in [str(i) for i in range(0, opciones)]:  # Solo continua si se elige una opción de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

            if opcion_log == "0":  # Volver al menú principal
                continue
            if opcion_log == '1':
                id_camara = input("Ingrese el ID de la cámara: ")
                id_persona = input("Ingrese el ID de la persona: ")
                registrarEvento(id_camara, id_persona, registros)
            elif opcion_log == '2':
                listarEventos(registros)
            elif opcion_log == '0':
                break
            else:
                print("Opción inválida.")

        elif opcion == "4":  # Opción 4 - Informes generales
            pass  # Implementar menú de informes

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")

# Punto de entrada al programa
if __name__ == "__main__":
    main()
