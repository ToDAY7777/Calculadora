#Importacion del modulo unittest para poder realizar pruebas unitarias
import unittest
#importanción de la clase calculadora desde el archivo 
from calculadora import Calculadora
#
class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_resta(self):
        self.assertEqual(self.calc.restar(5, 2), 3)

        self.assertEqual(self.calc.restar(0, 0), 0)

        

if __name__ == '__main__':
    unittest.main()
    