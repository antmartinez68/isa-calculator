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


if __name__ == "__main__":
    unittest.main()
