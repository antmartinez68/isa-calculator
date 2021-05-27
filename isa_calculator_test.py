"""Tests para el módulo calculadora"""
import unittest
import isa_calculator


class PyCalculatorTest(unittest.TestCase):
    #
    # Bloque de tests función suma
    #

    def test_suma_dos_positivos(self):
        # Arrange
        value_1 = 2
        value_2 = 3
        expected = 5
        # Act
        result = isa_calculator.add(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_suma_dos_negativos(self):
        # Arrange
        value_1 = -2
        value_2 = -3
        expected = -5
        # Act
        result = isa_calculator.add(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_suma_positivo_negativo(self):
        # Arrange
        value_1 = 2
        value_2 = -3
        expected = -1
        # Act
        result = isa_calculator.add(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_suma_negativo_positivo(self):
        # Arrange
        value_1 = -2
        value_2 = 3
        expected = 1
        # Act
        result = isa_calculator.add(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    #
    # Bloque de tests función resta
    #

    def test_resta_positivos(self):
        # Arrange
        value_1 = 2
        value_2 = 3
        expected = -1
        # Act
        result = isa_calculator.sub(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_resta_negativos(self):
        # Arrange
        value_1 = -2
        value_2 = -3
        expected = 1
        # Act
        result = isa_calculator.sub(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_resta_positivo_negativo(self):
        # Arrange
        value_1 = 2
        value_2 = -3
        expected = 5
        # Act
        result = isa_calculator.sub(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_resta_negativo_positivo(self):
        # Arrange
        value_1 = -2
        value_2 = 3
        expected = -5
        # Act
        result = isa_calculator.sub(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    #
    # Bloque de tests función producto
    #

    def test_multiplicacion_positivos(self):
        # Arrange
        value_1 = 2
        value_2 = 3
        expected = 6
        # Act
        result = isa_calculator.mul(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_multiplicacion_negativos(self):
        # Arrange
        value_1 = -2
        value_2 = -3
        expected = 6
        # Act
        result = isa_calculator.mul(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_multiplicacion_positivo_negativo(self):
        # Arrange
        value_1 = 2
        value_2 = -3
        expected = -6
        # Act
        result = isa_calculator.mul(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_multiplicacion_negativo_positivo(self):
        # Arrange
        value_1 = -2
        value_2 = 3
        expected = -6
        # Act
        result = isa_calculator.mul(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    #
    # Bloque de tests función división
    #

    def test_division_positivos(self):
        # Arrange
        value_1 = 3
        value_2 = 2
        expected = 1.5
        # Act
        result = isa_calculator.div(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_division_negativos(self):
        # Arrange
        value_1 = -6
        value_2 = -3
        expected = 2
        # Act
        result = isa_calculator.div(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_division_positivo_negativo(self):
        # Arrange
        value_1 = 3
        value_2 = -2
        expected = -1.5
        # Act
        result = isa_calculator.div(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_division_negativo_positivo(self):
        # Arrange
        value_1 = -6
        value_2 = 3
        expected = -2
        # Act
        result = isa_calculator.div(value_1, value_2)
        # Assert
        self.assertEqual(expected, result)

    def test_division_por_cero_lanza_excepción(self):
        # Arrange
        value_1 = 2
        value_2 = 0
        expected = ZeroDivisionError
        # Act & assert (juntos por peculiaridades de unittest)
        with self.assertRaises(expected):
            isa_calculator.div(value_1, value_2)

    #
    # Bloque de tests función raíz cuadrada
    #

    def test_raiz_de_negativo_lanza_excepción(self):
        # Arrange
        value = -2
        expected = ArithmeticError
        # Act & assert (juntos por peculiaridades de unittest)
        with self.assertRaises(expected):
            isa_calculator.sqrt(value)

    def test_raiz_cuadrado_perfecto(self):
        # Arrange
        value = 4
        expected = 2
        # Act
        result = isa_calculator.sqrt(value)
        # Assert
        self.assertEqual(expected, result)

    def test_raiz_con_suficiente_precision(self):
        # Arrange
        value = 2
        expected = 1.414213562
        tolerance = 1e-5
        # Act
        result = isa_calculator.sqrt(value)
        # Assert
        self.assertLess(abs(result - expected), tolerance)


if __name__ == "__main__":
    unittest.main()
