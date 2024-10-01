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
            print("MENÚ DEL SISTEMA           ")
            print("---------------------------")
            print("[1] Gestion de personas")
            print("[2] Gestion de cámaras")
            print("[3] Log de Movimientos")
            print("[4] Informes generales")
            print("---------------------------")
            print("[0] Salir del programa")
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
            pass#menuUsuarios()
        elif opcion == "2":   # Opción 2
            pass#menuCamaras
        elif opcion == "3":   # Opción 3
            pass#logRegistro
        elif opcion == "4":   # Opción 4
            pass#Informes

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
    }
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
}"""
