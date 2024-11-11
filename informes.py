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