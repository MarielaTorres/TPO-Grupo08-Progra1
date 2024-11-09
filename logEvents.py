from datetime import datetime

def registrarEvento(id_camara, id_persona, registros):
    """
    Argumentos:
        id_camara: Identificador de la cámara que detecta el evento.
        id_persona: Id de la persona detectada.
        registros: Diccionario de logs
    """
    # Genera un ID único para el evento
    id_evento = f"E{str(len(registros) + 1).zfill(3)}"
    
    # Obtenemos la fecha y hora del registro del evento
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    hora_actual = datetime.now().strftime("%H:%M")
    
    # Registrar el evento en el diccionario
    registros[id_evento] = {
        "camara": id_camara,
        "persona_detectada": id_persona,
        "fecha": fecha_actual,
        "hora": hora_actual
    }
    
    print(f"!Evento {id_evento} registrado exitosamente!")

def listarEventos(registros):
    """Lista todos los eventos registrados."""
    if not registros:
        print("No hay eventos registrados.")
    else:
        for id_evento, evento in registros.items():
            print(f"ID: {id_evento} - Cámara: {evento['camara']}, "
                  f"Persona: {evento['persona_detectada']}, "
                  f"Fecha: {evento['fecha']}, Hora: {evento['hora']}")

def contarAsistenciasPorDia(registros):
    """Devuelve una lista de personas que asistieron en una fecha dada ingresada por el usuario."""
    fecha_dia = input("Ingrese la fecha para verificar asistencias (YYYY-MM-DD): ")
    personas_vistas = set()

    for evento in registros.values():
        # Filtrar eventos por la fecha dada
        if evento["fecha"] == fecha_dia:
            personas_vistas.add(evento["persona_detectada"])
    
    if personas_vistas:
        print(f"Personas que asistieron el {fecha_dia}: {list(personas_vistas)}")
    else:
        print(f"No hubo asistencias registradas en la fecha {fecha_dia}.")
    
    return list(personas_vistas)