"""
-----------------------------------------------------------------------------------------------
Título: Precarga de datos.
Fecha: 07/10/2024
Autor: Equipo 8

Descripción: Modulo donde se realizara la precarga de datos para la inicializacion del sistema

Pendientes:
-----------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
from camaras import crearCamara
from personas import crearPersona
from logEvents import registrarEvento
import random


def precargaDatos(camaras, personas, registros):
    """
    Args:
        camaras: Diccionario donde se almacenan las cámaras.
        personas: Diccionario donde se almacenan las personas.
        registros: Diccionario donde se registran los eventos de las cámaras.
    """
    """Precarga 30 cámaras, 30 personas y registra 30 eventos simulados."""

    #Variable de 30 nombres y apellidos aleatorios
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

    areas_comunes = [
        "Hall de entrada", "Recepción", "Comedor", "Pasillo principal",
        "Aula magna", "Biblioteca", "Laboratorio de computación",
        "Sala de profesores", "Auditorio", "Oficina administrativa"
    ]
    areas_trabajo = [
        "Recursos Humanos", "Finanzas", "Marketing", "Ventas",
        "Tecnología de la Información", "Investigación y Desarrollo",
        "Logística", "Atención al Cliente", "Compras"
    ]
    cant_personas_carga = len(nombres_personas)
    # Precarga de cámaras
    print("\n--- Precargando Cámaras ---")
    for i in range(1, 31):
        nombre_camara = f"CAM{str(i).zfill(2)}"
        lugar = random.choice(areas_comunes)
        crearCamara(camaras,nombre_camara,lugar)

    # Precarga de personas
    print("\n--- Precargando Personas ---")
    for i in range(1, cant_personas_carga):
        nombre_persona = nombres_personas[i]
        area = random.choice(areas_trabajo)
        crearPersona(personas, nombre_persona, area)

    # Registro de 30 eventos simulados
    print("\n--- Registrando Eventos ---")
    for i in range(1, 31):
        id_camara = str(i)
        id_persona = str(i)
        registrarEvento(id_camara, id_persona, registros)

