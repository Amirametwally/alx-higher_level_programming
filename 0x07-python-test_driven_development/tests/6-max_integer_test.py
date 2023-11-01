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
        """test repeated"""
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_string(self):
        """test string """
        with self.assertRaises(TypeError):
            max_integer([8, '2', 3])

    def test_float(self):
        """test float"""
        self.assertEqual(max_integer([1, 5, 6.5]), 6.5)

    def test_zero_number(self):
        """test zero"""
        self.assertEqual(max_integer([0, 0]), 0)

    def test_dictionary(self):
        """test dictionary in list"""
        with self.assertRaises(KeyError):
            max_integer({'key1': 20, 'key2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_list(self):
        """test list"""
        self.assertEqual(max_integer([
            801, 802, 803, 804, 805, 806, 807, 808, 808, 810,
            811, 812, 813, 814, 815, 816, 817, 818, 818, 820,
            818, 818, 817, 1000, 815, 814, 813, 812, 811, 810,
            808, 808, 807, 806, 805, 804, 803, 802, 801]), 1000)

    def test_one_number(self):
        """test ome number"""
        self.assertEqual(max_integer([5]), 5)

    def test_tuple(self):
        """tuple in list"""
        with self.assertRaises(TypeError):
            max_integer([10, (1, 20)])
