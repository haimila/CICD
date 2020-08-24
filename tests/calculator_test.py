import unittest
import src.calculator as calc

class TestCalculator(unittest.TestCase):
    def test_summa(self):
        num1 = 2
        num2 = 3
        result = calc.plus(num1, num2)
        self.assertEqual(result, 5)

    def test_onko_numero(self):
        with self.assertRaises(TypeError):
            calc.plus(1, "a")

if __name__ == '__main__':
    unittest.main()