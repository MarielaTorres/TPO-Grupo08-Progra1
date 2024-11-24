import os

#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------

def personasCaptadasPorCamaras(registros, outputPath):
    """Genera un archivo .txt con la lista de camaras y la cantidad de personas captadas de cada camara."""
    fecha_dia = input("Ingrese la fecha para generar el informe de personas captadas por cámara (YYYY-MM-DD): ")
    asistencias_por_camara = {}

    # Filtrar eventos por la fecha dada
    for evento in registros.values():
        if evento["fecha"] == fecha_dia:
            id_camara = evento["camara"]
            asistencias_por_camara[id_camara] = asistencias_por_camara.get(id_camara, 0) + 1

    if asistencias_por_camara:
        # Generar el archivo
        archivo_nombre = f"personas_por_camara_{fecha_dia.replace('-', '')}.txt"
        os.makedirs(outputPath, exist_ok=True)
        archivo_path = os.path.join(outputPath, archivo_nombre)

        with open(archivo_path, "w") as archivo:
            archivo.write(f"--- Informe de personas captadas por camara (Fecha: {fecha_dia}) ---\n")
            for camara, cantidad in asistencias_por_camara.items():
                archivo.write(f"Cámara ID {camara}: {cantidad} personas captadas\n")

        print(f"Informe generado exitosamente: {archivo_path}")
    else:
        print(f"No se dectetaron personas en la fecha {fecha_dia}.")







def informePersonasPorArea(personas, outputPath):
    """Genera un informe general de la cantidad de personas en cada área de trabajo y lo guarda en un archivo .txt especificado por outputPath."""
    personas_por_area = {}
    for persona in personas.values():
        area = persona["area"]
        if area in personas_por_area:
            personas_por_area[area] += 1
        else:
            personas_por_area[area] = 1
    
    if personas_por_area:
        #Generar archivo .txt
        archivo_nombre= f"personas_por_area_ {fecha_dia.replace('-', '')}.txt"
        os.makedirs(outputPath, exist_ok=True)
        archivo_path = os.path.join(outputPath, archivo_nombre)

        with open(archivo_path, "w") as archivo:
            archivo.write(f"--- Informe de personas por area de trabajo (Fecha: {fecha_dia}) ---\n")
            for area, cantidad in personas_por_area.items:
                archivo.write(f"Area: {area}, Cantidad de personas: {cantidad}")
        print(f"\nEl informe ha sido guardado en '{outputPath}'.")

    return personas_por_area







def asistenciasPorPersona(registros, personas, outputPath):
    """Cuenta la cantidad de asistencias para cada persona en una fecha específica y guarda un archivo."""
    fecha_dia = input("Ingrese la fecha para generar el informe de asistencias por persona (YYYY-MM-DD): ")
    asistencias = {}

    # Filtrar eventos por la fecha dada
    for evento in registros.values():
        if evento["fecha"] == fecha_dia:
            persona_id = evento["persona_detectada"]
            asistencias[persona_id] = asistencias.get(persona_id, 0) + 1

    if asistencias:
        # Generar el archivo
        archivo_nombre = f"Asistencias_Por_Persona_{fecha_dia.replace('-', '')}.txt"
        os.makedirs(outputPath, exist_ok=True)
        archivo_path = os.path.join(outputPath, archivo_nombre)

        with open(archivo_path, "w") as archivo:
            archivo.write(f"--- Informe de Asistencias por Persona (Fecha: {fecha_dia}) ---\n")
            for persona_id, cantidad in asistencias.items():
                if persona_id in personas:
                    archivo.write(f"ID Persona: {persona_id}, Nombre: {personas[persona_id]['nombre']}, Asistencias: {cantidad}\n")

        print(f"Informe generado exitosamente: {archivo_path}")
    else:
        print(f"No se registraron asistencias en la fecha {fecha_dia}.")






def porcentajeAsistenciaPorFechas(registros, personas, outputPath):
    """
    Genera un informe con la fecha de mayor y menor porcentaje de asistencia basado en los registros.

    Args:
        registros: Diccionario de eventos registrados.
        personas: Diccionario de personas registradas.
        outputPath: Ruta donde se guardará el archivo.
    """
    total_personas = len(personas)
    if total_personas == 0:
        print("No hay personas registradas para calcular asistencia.")
        return

    asistencias_por_fecha = {}
    porcentaje_por_fecha = {}

    # Contar asistentes únicos por fecha
    for evento in registros.values():
        fecha = evento["fecha"]
        if fecha not in asistencias_por_fecha:
            asistencias_por_fecha[fecha] = set()
        asistencias_por_fecha[fecha].add(evento["persona_detectada"])

    # Calcular porcentaje de asistencia por fecha
    for fecha, asistentes in asistencias_por_fecha.items():
        cantidad_asistentes = len(asistentes)
        porcentaje_asistencia = (cantidad_asistentes / total_personas) * 100
        porcentaje_por_fecha[fecha] = porcentaje_asistencia

    if not porcentaje_por_fecha:
        print("No se registraron asistencias en los registros.")
        return

    # Encontrar la fecha con mayor y menor porcentaje de asistencia
    fecha_mayor_asistencia = max(porcentaje_por_fecha, key=porcentaje_por_fecha.get)
    fecha_menor_asistencia = min(porcentaje_por_fecha, key=porcentaje_por_fecha.get)

    # Crear el archivo con los resultados
    archivo_nombre = "Informe_Asistencias_Porcentajes.txt"
    os.makedirs(outputPath, exist_ok=True)
    archivo_path = os.path.join(outputPath, archivo_nombre)

    with open(archivo_path, "w") as archivo:
        archivo.write("Informe de Porcentaje de Asistencia\n\n")
        archivo.write(f"Fecha con mayor asistencia: {fecha_mayor_asistencia}\n")
        archivo.write(f"Porcentaje de asistencia: {porcentaje_por_fecha[fecha_mayor_asistencia]:.2f}%\n\n")
        archivo.write(f"Fecha con menor asistencia: {fecha_menor_asistencia}\n")
        archivo.write(f"Porcentaje de asistencia: {porcentaje_por_fecha[fecha_menor_asistencia]:.2f}%\n")

    print(f"Informe generado exitosamente: {archivo_path}")






def listarAsistentesPorDia(registros, personas, outputPath):
    """
    Genera un archivo .txt con la lista de personas que asistieron en una fecha específica.
    
    Args:
        registros: Diccionario de eventos registrados.
        personas: Diccionario de personas registradas.
        outputPath: Ruta donde se guardará el archivo.
    """
    fecha_dia = input("Ingrese la fecha para generar el informe de los que asistieron (YYYY-MM-DD): ")
    personas_vistas = set()

    # Filtrar eventos por la fecha dada
    for evento in registros.values():
        if evento["fecha"] == fecha_dia:
            personas_vistas.add(int(evento["persona_detectada"]))

    if personas_vistas:
        # Nombre del archivo
        archivo_nombre = f"Asistentes_{fecha_dia.replace('-', '')}.txt"
        
        # Crear la ruta si no existe
        os.makedirs(outputPath, exist_ok=True)
        archivo_path = os.path.join(outputPath, archivo_nombre)
        
        # Crear el archivo
        with open(archivo_path, "w") as archivo:
            # Escribir header
            archivo.write(f"Personas que asistieron el {fecha_dia}\n")

            # Escribir los datos de las personas
            for id_persona in personas_vistas:
                if id_persona in personas:
                    persona = personas[id_persona]
                    archivo.write(f"ID: {id_persona}, Nombre: {persona['nombre']}, Área: {persona['area']}\n")
        
        print(f"Informe generado exitosamente: {archivo_path}")
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