import json
import random
from datetime import datetime, timedelta
from camaras import crearCamara
from personas import crearPersona
from logEvents import registrarEvento
import os

def cargar_datos_json(outputPathJSON):
    """
    Carga un archivo JSON desde la ruta especificada y devuelve el contenido como un diccionario.

    Args:
        outputPathJSON: Ruta del archivo JSON.
    
    Returns:
        dict: Contenido del archivo como diccionario.
    """
    if os.path.exists(outputPathJSON):
        with open(outputPathJSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    # Retorna un diccionario vacío si el archivo no existe
    return {}  

def precargaDatos(outputPathJSON):
    """
    Crea y/o carga datos desde archivos JSON: uno para cámaras, otro para personas, y otro para registros.
    Si un archivo ya existe, lo carga; si no existe, lo genera.

    Args:
        outputPathJSON: Ruta donde se guardarán o cargarán los archivos JSON.

    Returns:
        tuple: Diccionarios de cámaras, personas y registros.
    """
    # Asegurar que la ruta exista
    os.makedirs(outputPathJSON, exist_ok=True)

    # Generar nombres de archivos
    camaras_file = os.path.join(outputPathJSON, "camaras.json")
    personas_file = os.path.join(outputPathJSON, "personas.json")
    registros_file = os.path.join(outputPathJSON, "registros.json")

    # Inicializar diccionarios
    camaras = cargar_datos_json(camaras_file)
    personas = cargar_datos_json(personas_file)
    registros = cargar_datos_json(registros_file)

    # Verificar y generar datos faltantes
    if not camaras:
        print("Generando datos de cámaras...")
        for i in range(1, 31):
            nombre_camara = f"CAM{str(i).zfill(2)}"
            lugar = random.choice([
                "Hall de entrada", "Recepción", "Comedor", "Pasillo principal",
                "Aula magna", "Biblioteca", "Laboratorio de computación",
                "Sala de profesores", "Auditorio", "Oficina administrativa"
            ])
            crearCamara(camaras, nombre_camara, lugar)
        # Guardar cámaras
        with open(camaras_file, 'w', encoding='utf-8') as f:
            json.dump(camaras, f, ensure_ascii=False, indent=4)

    if not personas:
        print("Generando datos de personas...")
        nombres_personas = [
            "Juan Pérez", "María García", "Carlos López", "Ana Martínez",
            "Pedro González", "Lucía Fernández", "Jorge Ramírez", "Elena Torres",
            "Luis Sánchez", "Sofía Jiménez", "Andrés Herrera", "Valentina Ruiz",
            "Daniel Romero", "Marta Navarro", "Sergio Díaz", "Patricia Castro",
            "Fernando Molina", "Camila Ortiz", "Pablo Silva", "Gabriela Ríos",
            "Raúl Vargas", "Isabel Peña", "Miguel Morales", "Laura Flores",
            "Ricardo Reyes", "Paula Rivera", "Gonzalo Cabrera", "Estefanía Soto",
            "Ignacio Ramos", "Alejandra Vega"
        ]
        for i, nombre in enumerate(nombres_personas, start=1):
            area = random.choice([
                "Recursos Humanos", "Finanzas", "Marketing", "Ventas",
                "Tecnología de la Información", "Investigación y Desarrollo",
                "Logística", "Atención al Cliente", "Compras"
            ])
            crearPersona(personas, nombre, area)
        # Guardar personas
        with open(personas_file, 'w', encoding='utf-8') as f:
            json.dump(personas, f, ensure_ascii=False, indent=4)

    if not registros:
        print("Generando datos de registros...")
        for i in range(1, 31):
            id_camara = str(i)
            id_persona = str(i)
            dias_a_restar = random.randint(1, 5)
            fecha_evento = (datetime.now() - timedelta(days=dias_a_restar)).strftime("%Y-%m-%d")
            registrarEvento(registros, camaras, personas, id_camara, id_persona)
            registros[f"E{i:03}"]["fecha"] = fecha_evento
        # Guardar registros
        with open(registros_file, 'w', encoding='utf-8') as f:
            json.dump(registros, f, ensure_ascii=False, indent=4)

    print(f"Archivos generados o cargados en: {outputPathJSON}")
    return camaras, personas, registros

