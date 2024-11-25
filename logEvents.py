from datetime import datetime
from camaras import listarCamaras
import crudJson
from personas import listarPersonas
from validaciones import esIdValido, esIdPersonaValido

def registrarEvento(registros, camaras, personas,id_camara=None, id_persona=None):
    """
    Args:
        registros: Diccionario de logs
        camaras: Diccionario de cámaras disponibles.
        personas: Diccionario de personas registradas.
        id_camara: Identificador de la cámara que detecta el evento.
        id_persona: Id de la persona detectada.
    """
    """Solicitamos el id_camara por teclado en caso de que no se haya pasado por parámetro"""
 # Solicitar ID de cámara si no se pasa como parámetro
    while id_camara is None:
        try:
            print("Listado de cámaras disponibles:\n")
            listarCamaras(camaras)
            id_camara = int(input("Ingrese el ID de la cámara: ").strip())
            if not esIdValido(str(id_camara) , camaras):
                print()
                print("===========================ERROR===========================\n")
                raise ValueError(f"ID de cámara inválido: {id_camara}. Verifique las cámaras disponibles a continuación e ingrese nuevamente el id:\n")
        except (ValueError, KeyError) as e:
            print(e)
            id_camara = None  # Reiniciar para volver a solicitar el ID

    # Solicitar ID de persona si no se pasa como parámetro
    while id_persona is None:
        try:
            print("Listado de personas dadas de alta:\n")
            listarPersonas(personas)
            id_persona = int(input("Ingrese el ID de la persona: ").strip())
            if not esIdPersonaValido(str(id_persona), personas):
                print()
                print("===========================ERROR===========================\n")
                raise ValueError(f"ID de persona inválido: {id_persona}. Verifique las personas disponibles a continuación e ingrese nuevamente el id:\n")
        except (ValueError, KeyError) as e:
            print(e)
            id_persona = None  # Reiniciar para volver a solicitar el ID
  
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

    crudJson.exportarDatos("registros.json", registros)
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
            

