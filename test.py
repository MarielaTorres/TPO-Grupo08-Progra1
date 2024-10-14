from camaras import crearCamara
from personas import crearPersona
from log_events import registrar_evento

def precarga_datos(camaras, personas, registros, contador_id):
    """
    Args:
        camaras: Diccionario donde se almacenan las cámaras.
        personas: Diccionario donde se almacenan las personas.
        registros: Diccionario donde se registran los eventos de las cámaras.
        contador_id: Contador actual para los IDs de las cámaras.
    Return:
        contador_id: Contador actualizado después de la precarga
    """

    """Precarga 30 cámaras, 30 personas y registra 30 eventos simulados."""

    # Precarga de cámaras
    print("\n--- Precargando Cámaras ---")
    for i in range(1, 31):
        nombre_camara = f"Camara_{i}"
        lugar = f"Lugar_{i}"
        contador_id = crearCamara(camaras, nombre_camara, lugar, contador_id)

    # Precarga de personas
    print("\n--- Precargando Personas ---")
    for i in range(1, 31):
        nombre_persona = f"Persona_{i}"
        area = f"Area_{i}"
        crearPersona(personas,nombre_persona,area)

    # Registro de 30 eventos simulados
    print("\n--- Registrando Eventos ---")
    for i in range(1, 31):
        id_camara = f"CAM{str(i).zfill(2)}"
        id_persona = str(i)
        registrar_evento(id_camara, id_persona, registros)

    # Retornar el contador actualizado
    return contador_id
