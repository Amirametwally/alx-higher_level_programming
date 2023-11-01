#!/usr/bin/python3
"""unittest for max integer"""
import unittest
max_intger = __import__('6-max_intger').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests for max_integer"""
    def test_positive(self):
        """tests normal input"""
        self.assertEqual(max_intger([1, 2, 3, 4]), 4)

    def test_none(self):
        """tests empty"""
        self.assertEqual(max_intger(), None)

    def test_negative(self):
        """test negative"""
        self.assertEqual(max_intger([-1, -2, -3]), -1)

    def test_composed(self):
        """test composed(negative, posetive)"""
        self.assertEqual(max_intger([1, -3, -5, 6, 2]), 6)

    def test_not_intger(self):
        """tests not integer """
        with self.assertRaises(TypeError):
            max_intger([8, '2', 3])

    def test_float(self):
        """test float"""
        self.assertEqual(max_intger([1, 5, 6.5]), 6.5)


if __name__ == "__main__":
    unittest.main()
