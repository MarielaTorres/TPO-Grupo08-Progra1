import os

#----------------------------------------------------------------------------------------------
# FUNCIONES DE INFORMES
#----------------------------------------------------------------------------------------------

def informeAsistenciasPorCamara(registros):
    """Genera un informe de la cantidad de asistencias registradas por cada cámara."""
    asistencias_por_camara = {}
    for evento in registros.values():
        id_camara = evento["camara"]
        if id_camara in asistencias_por_camara:
            asistencias_por_camara[id_camara] += 1
        else:
            asistencias_por_camara[id_camara] = 1

    print("\n--- Informe de Asistencias por Cámara ---")
    for camara, cantidad in asistencias_por_camara.items():
        print(f"Cámara ID {camara}: {cantidad} asistencias registradas")
    return asistencias_por_camara



def informePersonasPorArea(personas):
    """Genera un informe de la cantidad de personas en cada área de trabajo."""
    personas_por_area = {}
    for persona in personas.values():
        area = persona["area"]
        if area in personas_por_area:
            personas_por_area[area] += 1
        else:
            personas_por_area[area] = 1

    print("\n--- Informe de Personas por Área de Trabajo ---")
    for area, cantidad in personas_por_area.items():
        print(f"Área: {area}, Cantidad de personas: {cantidad}")
    return personas_por_area

def asistenciasPorPersona(registros):
    """Cuenta la cantidad de asistencias para cada persona."""
    asistencias = {}
    for evento in registros.values():
        persona_id = evento["persona_detectada"]
        if persona_id in asistencias:
            asistencias[persona_id] += 1
        else:
            asistencias[persona_id] = 1

    for persona, cantidad in asistencias.items():
        print(f"ID Persona: {persona}, Asistencias: {cantidad}")
    return asistencias

def porcentajeAsistenciaPorFecha(registros):
    """Calcula el porcentaje de asistencia para la fecha de menor y mayor asistencia."""
    # Contar asistencias por fecha
    asistencias_por_fecha = {}
    for evento in registros.values():
        fecha = evento["fecha"]
        asistencias_por_fecha[fecha] = asistencias_por_fecha.get(fecha, 0) + 1
    
    if not asistencias_por_fecha:
        print("No hay asistencias registradas.")
        return None
    
    # Encontrar las fechas con menor y mayor asistencia
    fecha_menor = min(asistencias_por_fecha, key=asistencias_por_fecha.get)
    fecha_mayor = max(asistencias_por_fecha, key=asistencias_por_fecha.get)
    total_eventos = sum(asistencias_por_fecha.values())
    
    # Calcular porcentaje de asistencia para esas fechas
    porcentaje_menor = (asistencias_por_fecha[fecha_menor] / total_eventos) * 100
    porcentaje_mayor = (asistencias_por_fecha[fecha_mayor] / total_eventos) * 100

    print(f"Fecha con menor asistencia: {fecha_menor} ({porcentaje_menor:.2f}%)")
    print(f"Fecha con mayor asistencia: {fecha_mayor} ({porcentaje_mayor:.2f}%)")
    return {
        "fecha_menor": (fecha_menor, porcentaje_menor),
        "fecha_mayor": (fecha_mayor, porcentaje_mayor)
    }

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