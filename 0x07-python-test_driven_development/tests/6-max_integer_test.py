#!/usr/bin/python3
"""unittest for max integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """tests for max_integer"""
    def test_positive(self):
        """tests normal input"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_none(self):
        """tests empty"""
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        """test negative"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_operated_integer(self):
        self.assertEqual(max_integer([-3, -5 * -5, 12, -1]), 25)

    def test_composed(self):
        """test composed(negative, posetive)"""
        self.assertEqual(max_integer([1, -3, -5, 6, 2]), 6)

    def test_repeated_number(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_not_intger(self):
        """tests not integer """
        with self.assertRaises(TypeError):
            max_integer([8, '2', 3])

    def test_float(self):
        """test float"""
        self.assertEqual(max_integer([1, 5, 6.5]), 6.5)

    def test_zero_number(self):
        """test zero"""
        self.assertEqual(max_integer([0, 0]), 0)
