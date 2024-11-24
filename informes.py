import os
from datetime import datetime
from validaciones import validar_fecha
#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------

def personasCaptadasPorCamaras(registros, outputPath):
    """Genera un archivo .txt con la lista de cámaras y la cantidad de personas captadas por cada cámara."""
    fecha_dia = input("Ingrese la fecha para generar el informe de personas captadas por cámara (YYYY-MM-DD): ")
    while not validar_fecha(fecha_dia):
        print("La fecha ingresada es inválida. Intente nuevamente.")
        fecha_dia = input("Ingrese la fecha (YYYY-MM-DD): ")
    asistencias_por_camara = {}
    # Filtrar eventos por la fecha dada
    for evento in registros.values():
        if evento.get("fecha") == fecha_dia:
            id_camara = evento.get("camara")
            if id_camara:
                asistencias_por_camara[id_camara] = asistencias_por_camara.get(id_camara, 0) + 1

    if asistencias_por_camara:
        try:
            archivo_nombre = f"personas_por_camara_{fecha_dia.replace('-', '')}.txt"
            os.makedirs(outputPath, exist_ok=True)
            archivo_path = os.path.join(outputPath, archivo_nombre)

            with open(archivo_path, "w") as archivo:
                archivo.write(f"--- Informe de personas captadas por cámara (Fecha: {fecha_dia}) ---\n")
                for camara, cantidad in asistencias_por_camara.items():
                    archivo.write(f"Cámara ID {camara}: {cantidad} personas captadas\n")

            print(f"Informe generado exitosamente: {archivo_path}")
        except OSError as e:
            print(f"Error al crear el archivo: {e}")
    else:
        print(f"No se detectaron personas en la fecha {fecha_dia}.")

def informePersonasPorArea(personas, outputPath):
    """Genera un archivo .txt mostrando la cantidad de personas en cada area de trabajo.
    
    Args:
        personas: Diccionario de personas registradas.
        outputPath: Ruta donde se guardará el archivo.
    """
    fecha_dia = input("Ingrese la fecha para generar el informe de cantidad de personas en cada area de trabajo (YYYY-MM-DD): ")
    while not validar_fecha(fecha_dia):
        print("La fecha ingresada es inválida. Intente nuevamente.")
        fecha_dia = input("Ingrese la fecha (YYYY-MM-DD): ")

    personas_por_area = {}

    for persona in personas.values():
        area = persona["area"]
        if area in personas_por_area:
            personas_por_area[area] += 1
        else:
            personas_por_area[area] = 1
    
    if personas_por_area:
        #Generar archivo .txt
        archivo_nombre= f"personas_por_area_{fecha_dia.replace('-', '')}.txt"
        os.makedirs(outputPath, exist_ok=True)
        archivo_path = os.path.join(outputPath, archivo_nombre)

        with open(archivo_path, "w") as archivo:
            archivo.write(f"--- Informe de personas por area de trabajo (Fecha: {fecha_dia}) ---\n")
            for area, cantidad in personas_por_area.items():
                archivo.write(f"Area: {area}, Cantidad de personas: {cantidad}\n")
        print(f"\nEl informe ha sido guardado en '{outputPath}'.")
    else:
        print("No se encontraron personas registradas para generar el informe.")
    return personas_por_area

def porcentajeAsistenciaPorFechas(registros, personas, outputPath):
    """Genera un archivo .txt mostrando la fecha con mayor y menor porcentaje de asistencia."""
    total_personas = len(personas)
    if total_personas == 0:
        print("No hay personas registradas para calcular asistencia.")
        return

    asistencias_por_fecha = {}

    for evento in registros.values():
        fecha = evento.get("fecha")
        if fecha:
            if fecha not in asistencias_por_fecha:
                asistencias_por_fecha[fecha] = set()
            asistencias_por_fecha[fecha].add(evento.get("persona_detectada"))

    porcentaje_por_fecha = {}
    for fecha, asistentes in asistencias_por_fecha.items():
        porcentaje_por_fecha[fecha] = (len(asistentes) / total_personas) * 100

    if not porcentaje_por_fecha:
        print("No se registraron asistencias en los registros.")
        return

    try:
        archivo_nombre = "Informe_Asistencias_Porcentajes.txt"
        os.makedirs(outputPath, exist_ok=True)
        archivo_path = os.path.join(outputPath, archivo_nombre)

        fecha_mayor_asistencia = max(porcentaje_por_fecha, key=porcentaje_por_fecha.get)
        fecha_menor_asistencia = min(porcentaje_por_fecha, key=porcentaje_por_fecha.get)

        with open(archivo_path, "w") as archivo:
            archivo.write("Informe de Porcentaje de Asistencia\n\n")
            archivo.write(f"Fecha con mayor asistencia: {fecha_mayor_asistencia}\n")
            archivo.write(f"Porcentaje de asistencia: {porcentaje_por_fecha[fecha_mayor_asistencia]:.2f}%\n\n")
            archivo.write(f"Fecha con menor asistencia: {fecha_menor_asistencia}\n")
            archivo.write(f"Porcentaje de asistencia: {porcentaje_por_fecha[fecha_menor_asistencia]:.2f}%\n")

        print(f"Informe generado exitosamente: {archivo_path}")
    except OSError as e:
        print(f"Error al crear el archivo: {e}")

def listarAsistentesPorDia(registros, personas, outputPath):
    """
    Genera un archivo .txt con la lista de personas que asistieron en una fecha específica.
    
    Args:
        registros: Diccionario de eventos registrados.
        personas: Diccionario de personas registradas.
        outputPath: Ruta donde se guardará el archivo.
    """
    fecha_dia = input("Ingrese la fecha para generar el informe de los que asistieron (YYYY-MM-DD): ")
    while not validar_fecha(fecha_dia):
        print("La fecha ingresada es inválida. Intente nuevamente.")
        fecha_dia = input("Ingrese la fecha (YYYY-MM-DD): ")
        
    personas_vistas = set()

    # Filtrar eventos por la fecha dada
    for evento in registros.values():
        if evento.get("fecha") == fecha_dia:
            persona_id = evento.get("persona_detectada")
            if persona_id:
                personas_vistas.add(persona_id)

    if personas_vistas:
        try:
            # Nombre del archivo
            archivo_nombre = f"Asistentes_{fecha_dia.replace('-', '')}.txt"
            # Crear la ruta si no existe
            os.makedirs(outputPath, exist_ok=True)
            archivo_path = os.path.join(outputPath, archivo_nombre)

            with open(archivo_path, "w") as archivo:
                archivo.write(f"Personas que asistieron el {fecha_dia}\n")
                # Ordenar personas por ID
                for id_persona in sorted(personas_vistas, key=int):  # Asegura la comparación numérica
                    if id_persona in personas:
                        persona = personas[id_persona]
                        archivo.write(f"ID: {id_persona}, Nombre: {persona['nombre']}, Área: {persona['area']}\n")

            print(f"Informe generado exitosamente: {archivo_path}")
        except OSError as e:
            print(f"Error al crear el archivo: {e}")
    else:
        print(f"No hubo asistencias registradas en la fecha {fecha_dia}.")

def generarInformeAsistenciasGeneral(registros, outputPath):
    """
    Genera un informe en un archivo .txt que muestra la cantidad de personas que asistieron por fecha,
    ordenado de lo más reciente a lo menos reciente.

    Args:
        registros: Diccionario de eventos registrados.
        outputPath: Ruta donde se guardará el archivo.
    """
    # Crear un diccionario para almacenar asistentes únicos por fecha
    asistencias_por_fecha = {}

    for evento in registros.values():
        fecha = evento["fecha"]
        persona = evento["persona_detectada"]

        # Si la fecha no existe en el diccionario, inicializarla con un conjunto
        if fecha not in asistencias_por_fecha:
            asistencias_por_fecha[fecha] = set()

        # Agregar la persona al conjunto correspondiente a la fecha
        asistencias_por_fecha[fecha].add(persona)

    # Crear una lista de tuplas con la fecha y la cantidad de asistentes, ordenada de forma descendente
    asistencias_ordenadas = sorted(
        ((fecha, len(personas)) for fecha, personas in asistencias_por_fecha.items()),
        key=lambda x: x[0],
        reverse=True,
    )

    # Nombre del archivo
    archivo_nombre = "Informe_Asistencias.txt"
    archivo_path = os.path.join(outputPath, archivo_nombre)

    # Crear la carpeta si no existe
    os.makedirs(outputPath, exist_ok=True)

    # Generar el archivo
    with open(archivo_path, "w") as archivo:
        # Escribir encabezado
        archivo.write("Informe de Asistencias por Fecha\n")

        # Escribir cada fecha y cantidad de asistentes
        for fecha, cantidad in asistencias_ordenadas:
            archivo.write(f"Fecha: {fecha}, Cantidad de asistentes: {cantidad}\n")
    
    print(f"Informe generado exitosamente: {archivo_path}")