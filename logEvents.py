from datetime import datetime
import os

def registrarEvento(id_camara, id_persona,registros, camaras, personas):
    """
    Args:
        id_camara: Identificador de la cámara que detecta el evento.
        id_persona: Id de la persona detectada.
        registros: Diccionario de logs
        camaras: Diccionario de cámaras disponibles.
        personas: Diccionario de personas registradas.
    """

    """ Verificamos si la cámara y la persona existen"""

    if int(id_camara) not in camaras:
        raise ValueError(f"ID de cámara inválido: {id_camara}. Verifique las cámaras disponibles.")
    if int(id_persona) not in personas:
        raise ValueError(f"ID de persona inválido: {id_persona}. Verifique las personas disponibles.")
    
    """ Se genera un ID único para el evento"""
    id_evento = f"E{str(len(registros) + 1).zfill(3)}"
    
    """ Obtenemos la fecha y hora del registro del evento"""
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    hora_actual = datetime.now().strftime("%H:%M")
    
    """ Registrar el evento en el diccionario"""
    registros[id_evento] = {
        "camara": id_camara,
        "persona_detectada": id_persona,
        "fecha": fecha_actual,
        "hora": hora_actual
    }
    
    print(f"Evento {id_evento} registrado exitosamente!")

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
