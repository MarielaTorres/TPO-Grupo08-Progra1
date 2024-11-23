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
from logEvents import registrarEvento, listarEventos, contarAsistenciasPorDia
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
    try:
        precargaDatos(camaras, personas, registros)
    except Exception as e:
        print(f"Error durante la precarga de datos: {e}")
        return  # Finaliza el programa si no se puede inicializar correctamente

    #----------------------------------------------------------------------------------------------
    # Bloque de menú
    #----------------------------------------------------------------------------------------------
    while True:
        try:
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

            opcion = input("Seleccione una opción: ").strip()
            if opcion not in ["0", "1", "2", "3", "4"]:
                raise ValueError("Opción inválida. Seleccione una opción del menú.")

            if opcion == "0":  # Salir del programa
                print("Saliendo del programa...")
                break

            elif opcion == "1":  # Gestión de cámaras
                while True:
                    try:
                        print("---------------------------")
                        print("--- Menú de Gestión de Cámaras ---")
                        print("1. Crear cámara")
                        print("2. Listar cámaras")
                        print("3. Actualizar cámara")
                        print("4. Eliminar cámara")
                        print("0. Volver al menú principal")
                        print("---------------------------")

                        opcion_camara = input("Seleccione una opción: ").strip()
                        if opcion_camara not in ["0", "1", "2", "3", "4"]:
                            raise ValueError("Opción inválida en gestión de cámaras.")

                        if opcion_camara == "0":
                            break
                        elif opcion_camara == "1":
                            crearCamara(camaras)
                        elif opcion_camara == "2":
                            listarCamaras(camaras)
                        elif opcion_camara == "3":
                            id = int(input("Ingrese el ID de la cámara a actualizar: "))
                            actualizarCamara(camaras, id)
                        elif opcion_camara == "4":
                            id = int(input("Ingrese el ID de la cámara a eliminar: "))
                            eliminarCamara(camaras, id)
                    except ValueError as ve:
                        print(f"Error: {ve}")
                    except Exception as e:
                        print(f"Error inesperado en gestión de cámaras: {e}")

            elif opcion == "2":  # Gestión de personas
                while True:
                    try:
                        print("---------------------------")
                        print("--- Menú de Gestión de Personas ---")
                        print("1. Crear persona")
                        print("2. Listar personas")
                        print("3. Actualizar persona")
                        print("4. Eliminar persona")
                        print("0. Volver al menú principal")
                        print("---------------------------")

                        opcion_persona = input("Seleccione una opción: ").strip()
                        if opcion_persona not in ["0", "1", "2", "3", "4"]:
                            raise ValueError("Opción inválida en gestión de personas.")

                        if opcion_persona == "0":
                            break
                        elif opcion_persona == "1":
                            crearPersona(personas)
                        elif opcion_persona == "2":
                            listarPersonas(personas)
                        elif opcion_persona == "3":
                            actualizarPersona(personas)
                        elif opcion_persona == "4":
                            eliminarPersona(personas)
                    except ValueError as ve:
                        print(f"Error: {ve}")
                    except Exception as e:
                        print(f"Error inesperado en gestión de personas: {e}")

            elif opcion == "3":  # Log de Movimientos
                while True:
                    try:
                        print("---------------------------")
                        print("--- Log de Movimientos ---")
                        print("1. Registrar evento")
                        print("2. Listar eventos")
                        print("3. Listar personas que asistieron en una fecha específica")
                        print("0. Volver al menú principal")
                        print("---------------------------")

                        opcion_log = input("Seleccione una opción: ").strip()
                        if opcion_log not in ["0", "1", "2", "3"]:
                            raise ValueError("Opción inválida en log de movimientos.")

                        if opcion_log == "0":
                            break
                        elif opcion_log == "1":
                            id_camara = input("Ingrese el ID de la cámara: ").strip()
                            id_persona = input("Ingrese el ID de la persona: ").strip()
                            registrarEvento(id_camara, id_persona, registros)
                        elif opcion_log == "2":
                            listarEventos(registros)
                        elif opcion_log == "3":
                            contarAsistenciasPorDia(registros)
                    except ValueError as ve:
                        print(f"Error: {ve}")
                    except Exception as e:
                        print(f"Error inesperado en log de movimientos: {e}")

            elif opcion == "4":  # Informes generales
                print("Funcionalidad de informes generales aún no implementada.")
        except ValueError as ve:
            print(f"Error en el menú principal: {ve}")
        except Exception as e:
            print(f"Error inesperado en el sistema: {e}")
        input("\nPresione ENTER para volver al menú.")

# Punto de entrada al programa
if __name__ == "__main__":
    main()
