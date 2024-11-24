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
from informes import personasCaptadasPorCamaras, informePersonasPorArea, asistenciasPorPersona, porcentajeAsistenciaPorFechas,listarAsistentesPorDia,generarInformeAsistenciasGeneral
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
    outputPath = "C:\\Users\\iann\\Documents\\Reportes"
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
            opciones = 4
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
                print("Listado de cámaras disponibles:\n")
                listarCamaras(camaras)
                id_camara = int(input("Ingrese el ID de la cámara: "))
                print("Listado de personas:\n")
                listarPersonas(personas)
                id_persona = int(input("Ingrese el ID de la persona: "))
                try:
                    registrarEvento(id_camara, id_persona, registros, camaras, personas)
                except ValueError as e:
                    print(e)

            elif opcion_log == '2':
                listarEventos(registros)
            elif opcion_log == '0':
                break
            else:
                print("Opción inválida.")

        elif opcion == "4":  # Opción 4 - Informes generales
            opciones = 7
            while True:
                print("1. Cantidad de personas captadas por cámara")
                print("2. Cantidad de asistencias por persona")
                print("3. Porcentaje de asistencia (fecha con menor y mayor asistencia)")
                print("4. Informe de personas por área de trabajo")
                print("5. Informe de personas que asistieron en un día")
                print("6. Informe de cantidad de asistentes de todos los días")
                print("0. Volver al menú principal")
                print("---------------------------")
                opcion_informe = input("Seleccione una opción: ")
                if opcion_informe in [str(i) for i in range(0, opciones)]:  # Solo continua si se elige una opción de menú válida
                    break
                else:
                    input("Opción inválida. Presione ENTER para volver a seleccionar.")
                print()

            if opcion_informe == "0":  # Volver al menú principal
                continue
            
            if opcion_informe == "1":
                personasCaptadasPorCamaras(registros, outputPath)
            elif opcion_informe == "2":
                asistenciasPorPersona(registros, personas, outputPath)
            elif opcion_informe == "3":
                porcentajeAsistenciaPorFechas (registros, personas, outputPath)
            elif opcion_informe == "4":
                informePersonasPorArea(personas, outputPath)
            elif opcion_informe == "5":
                listarAsistentesPorDia(registros, personas, outputPath)
            elif opcion_informe == "6":
                generarInformeAsistenciasGeneral(registros, outputPath)
              # Implementar menú de informes

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")

# Punto de entrada al programa
if __name__ == "__main__":
    main()
