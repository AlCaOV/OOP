import unittest

from app import Figure


class TestFigure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nпочаток тестів Figure")

    @classmethod
    def tearDownClass(cls):
        print("\nкінець тестів Figure")

    def setUp(self):
        self.obj = Figure("квадрат", 5)

    def tearDown(self):
        self.obj = None

    def test_figure_type(self):
        self.assertEqual("квадрат", self.obj.get_figure_type)

    def test_figure_length(self):
        self.assertEqual(5, self.obj.get_figure_length)

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            Figure("коло", 1)

    def test_invalid_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", 0)

    def test_negative_length(self):
        with self.assertRaises(AssertionError):
            Figure("квадрат", -5)

    def test_angles(self):
        self.assertEqual(4, Figure("квадрат", 2).get_angles)
        self.assertEqual(4, Figure("прямокутник", 2).get_angles)
        self.assertEqual(3, Figure("трикутник", 2).get_angles)

    def test_figure_lengths(self):
        for length in [1, 5, 10]:
            with self.subTest(length=length):
                self.assertEqual(length, Figure("квадрат", length).get_figure_length)

    def test_all_figures(self):
        for figure_type in Figure.FIGURES:
            with self.subTest(figure_type=figure_type):
                f = Figure(figure_type, 3)
                self.assertEqual(figure_type, f.get_figure_type)
                self.assertEqual(3, f.get_figure_length)


if __name__ == "__main__":
    unittest.main(verbosity=2)
