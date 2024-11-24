import unittest
from unittest.mock import patch
from camaras import crearCamara, listarCamaras, actualizarCamara, eliminarCamara
from personas import crearPersona, listarPersonas, actualizarPersona, eliminarPersona
from logEvents import registrarEvento, listarEventos

class TestSistemaCamaras(unittest.TestCase):

    def setUp(self):
        """Inicializa datos de prueba para cada test"""
        self.camaras = {
            1: {"camara": "CAM01", "lugar": "Hall de entrada"},
            2: {"camara": "CAM02", "lugar": "Comedor"}
        }
        self.personas = {
            1: {"nombre": "Juan Pérez", "area": "Recursos Humanos"},
            2: {"nombre": "María García", "area": "Finanzas"}
        }
        self.registros = {}

    def test_crearCamara_valida(self):
        """Prueba la creación de una cámara válida"""
        crearCamara(self.camaras, "CAM03", "Biblioteca")
        self.assertIn(3, self.camaras)
        self.assertEqual(self.camaras[3]["camara"], "CAM03")
        self.assertEqual(self.camaras[3]["lugar"], "Biblioteca")

    def test_crearCamara_invalida(self):
        """Prueba la creación de una cámara inválida"""
        with self.assertRaises(ValueError):
            crearCamara(self.camaras, "CAM02", "Comedor")

    def test_listarCamaras(self):
        """Prueba el listado de cámaras"""
        with patch('builtins.print') as mocked_print:
            listarCamaras(self.camaras)
            mocked_print.assert_any_call("ID: 1, Cámara: CAM01, Lugar: Hall de entrada")
            mocked_print.assert_any_call("ID: 2, Cámara: CAM02, Lugar: Comedor")

    def test_actualizarCamara_valida(self):
        """Prueba la actualización de una cámara existente"""
        with patch('builtins.input', side_effect=["1", "Nueva CAM01", "Nuevo lugar"]):
            actualizarCamara(self.camaras, 1)
            self.assertEqual(self.camaras[1]["camara"], "Nueva CAM01")
            self.assertEqual(self.camaras[1]["lugar"], "Nuevo lugar")

    def test_eliminarCamara(self):
        """Prueba la eliminación de una cámara"""
        with patch('builtins.input', side_effect=["1"]):
            eliminarCamara(self.camaras, 1)
            self.assertNotIn(1, self.camaras)

    def test_registrarEvento(self):
        """Prueba el registro de un evento válido"""
        with patch('builtins.input', side_effect=["1", "1"]):
            registrarEvento(self.registros, self.camaras, self.personas)
            self.assertIn("E001", self.registros)
            self.assertEqual(self.registros["E001"]["camara"], 1)
            self.assertEqual(self.registros["E001"]["persona_detectada"], 1)

    def test_listarEventos(self):
        """Prueba el listado de eventos"""
        self.registros = {
            "E001": {"camara": 1, "persona_detectada": 1, "fecha": "2024-11-24", "hora": "10:00"}
        }
        with patch('builtins.print') as mocked_print:
            listarEventos(self.registros)
            mocked_print.assert_any_call(
                "ID: E001 - Cámara: 1, Persona: 1, Fecha: 2024-11-24, Hora: 10:00"
            )

if __name__ == '__main__':
    unittest.main()
