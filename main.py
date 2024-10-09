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

'''TBD'''
#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
'''TBD'''

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#---------------------------------------------------------------------------------
# 
# -------------
def main():
    #-------------------------------------------------
    # Inicialización de variables
    #----------------------------------------------------------------------------------------------
    ...

    #-------------------------------------------------
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
            exit() 

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

            if opcion_camara == "0":  # Volver al menú principal
                continue

            # Aquí puedes implementar la lógica para cada opción del CRUD de cámaras
            if opcion_camara == "1":
                print("Crear cámara")
                # Lógica para crear cámara
            elif opcion_camara == "2":
                print("Listar cámaras")
                # Lógica para listar cámaras
            elif opcion_camara == "3":
                print("Actualizar cámara")
                # Lógica para actualizar cámara
            elif opcion_camara == "4":
                print("Eliminar cámara")
                # Lógica para eliminar cámara

        elif opcion == "2":  # Opción 2 - Gestión de personas
            opciones = 6
            while True:
                print("\n--- Menú de gestión de Personas ---")
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

            # Aquí puedes implementar la lógica para cada opción del CRUD de personas
            if opcion_persona == "1":
                print("Crear persona")
                # Lógica para crear persona
            elif opcion_persona == "2":
                print("Listar personas")
                # Lógica para listar personas
            elif opcion_persona == "3":
                print("Actualizar persona")
                # Lógica para actualizar persona
            elif opcion_persona == "4":
                print("Eliminar persona")
                # Lógica para eliminar persona

        elif opcion == "3":  # Opción 3 - Log de Movimientos
            pass  # Implementar menú de log de movimientos

        elif opcion == "4":  # Opción 4 - Informes generales
            pass  # Implementar menú de informes

        input("\nPresione ENTER para volver al menú.")
        print("\n\n")


# Punto de entrada al programa
main()

#----------------------------------------------------------------------------------------------
# Test
#----------------------------------------------------------------------------------------------
"""
personas = {
    "12345678": {
        "nombre_completo": "Juan Pérez",
        "DNI": "12345678",
        "fecha_nacimiento": "20-01-1990",
        "email": "juanperez@uade.edu.ar",
        "area": "Seguridad",
        "rol": "Guardia"
    },
    "87654321": {
        "nombre_completo": "Ana López",
        "DNI": "87654321",
        "fecha_nacimiento": "22-10-1996",
        "email": "analopez@uade.edu.ar",
        "area": "Administración",
        "rol": "Administradora"
    }
}

camaras = {
    "CAM01": {
        "ubicacion": "Hall Central",
        "tipo_sensor": "Facial",
        "estado": "Activa"
    },
    "CAM02": {
        "ubicacion": "Pasillo 2",
        "tipo_sensor": "Movimiento",
        "estado": "Activa"
    },
    "CAM03": {
        "ubicacion": "Comedor",
        "tipo_sensor": "Movimiento",
        "estado": "Inactiva"
    }
}

registros = {
    "E001": {
        "camara": "CAM01",
        "persona_detectada": "12345678",
        "fecha": "2024-09-30",
        "hora": "08:30"
    },
    "E002": {
        "camara": "CAM02",
        "persona_detectada": "87654321",
        "fecha": "2024-09-30",
        "hora": "09:15"
    }
}
"""
