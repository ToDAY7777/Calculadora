#Importacion del modulo unittest para poder realizar pruebas unitarias
import unittest
#importanción de la clase calculadora desde el archivo 
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    # Pruebas del método suma
    def test_suma(self):
        self.assertEqual(self.calc.sumar(5, 2), 7)
        self.assertEqual(self.calc.sumar(0, 0), 0)

    # Pruebas del método resta
    def test_resta(self):
        self.assertEqual(self.calc.restar(10, 5), 5)  # Resta de positivos
        self.assertEqual(self.calc.restar(7, 7), 0)   # Resta de números iguales

    # Pruebas del método multiplicación
    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicar(3, 4), 12)  # Multiplicación de positivos
        self.assertEqual(self.calc.multiplicar(5, 0), 0)   # Multiplicación por cero
        self.assertEqual(self.calc.multiplicar(-2, 3), -6) # Multiplicación de negativo por positivo

    # Pruebas del método división
    def test_division(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)  # División exacta
        self.assertAlmostEqual(self.calc.dividir(7, 3), 2.3333, places=4)  # División con decimal
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(5, 0)  # División entre cero debe lanzar error

if __name__ == '__main__':
    unittest.main()
