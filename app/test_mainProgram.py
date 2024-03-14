import unittest
from mainProgram import obtenerGenomaParaNombreDeGen

class TestObtenerGenomaParaNombreDeGen(unittest.TestCase):
    def test_obtener_genoma_correcto(self):
        genoma = obtenerGenomaParaNombreDeGen()
        self.assertIsNotNone(genoma)
        self.assertIsInstance(genoma, str)
        self.assertGreater(len(genoma), 0)

    def test_obtener_genoma_fallido(self):
        # Simular un error al abrir el archivo
        with self.assertRaises(Exception):
            obtenerGenomaParaNombreDeGen()

if __name__ == '__main__':
    unittest.main()