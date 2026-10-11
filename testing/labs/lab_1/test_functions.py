import unittest
from unittest.mock import patch

from functions import check_number, count_symbols, divide, count_vowels, ask_number


class TestFunctions(unittest.TestCase):
    def test_check_number(self):
        self.assertEqual(5, check_number("5"))
        with self.assertRaises(ValueError):
            check_number("abc")
        with self.assertRaises(AssertionError):
            check_number("-3")

    def test_count_symbols(self):
        self.assertEqual(3, count_symbols("abc"))
        self.assertEqual(0, count_symbols(""))

    def test_divide(self):
        self.assertEqual(2, divide(10, 5))
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)


class TestVowels(unittest.TestCase):
    def test_english(self):
        self.assertEqual(2, count_vowels("hello"))

    def test_upper(self):
        self.assertEqual(3, count_vowels("AbEcI"))

    def test_no_vowels(self):
        self.assertEqual(0, count_vowels("xyz"))

    def test_empty(self):
        self.assertEqual(0, count_vowels(""))

    def test_digits(self):
        self.assertEqual(0, count_vowels("12345"))

    def test_ukrainian(self):
        self.assertEqual(4, count_vowels("Привіт, Юра"))


class TestInput(unittest.TestCase):
    @patch("builtins.input", return_value="5")
    def test_ask_number(self, mock_input):
        self.assertEqual(5, ask_number())
        mock_input.assert_called_once()

    @patch("builtins.input", return_value="abc")
    def test_ask_number_wrong(self, mock_input):
        with self.assertRaises(ValueError):
            ask_number()


if __name__ == "__main__":
    unittest.main(verbosity=2)
