import unittest
from calculator import is_number
from calculator import casting 

class TestCalculator(unittest.TestCase):
    def test_is_number(self):
        self.assertTrue(is_number("456"))
        self.assertTrue(is_number("0.230"))
        self.assertTrue(is_number(".123"))
        self.assertTrue(is_number("-0.347"))
        self.assertTrue(is_number("144.489"))
        self.assertFalse(is_number("abcdef"))
        self.assertFalse(is_number("23a3"))
        self.assertFalse(is_number(""))

    def test_casting(self):
        self.assertEqual(casting("123"), 123)
        self.assertEqual(casting("0.123"), 0.123)
        self.assertEqual(casting(".123"), 0.123)
        self.assertEqual(casting("-0.123"), -0.123)
        self.assertEqual(casting("123.456"), 123.456)
if __name__ == "__main__":
    unittest.main()