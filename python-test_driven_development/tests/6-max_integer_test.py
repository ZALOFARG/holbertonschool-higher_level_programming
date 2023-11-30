#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_value(self):
        self.assertAlmostEqual(max_integer([2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-1, 3, 10]), 10)

    def eval_types(self):
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, "hola")
        self.assertRaises(TypeError, max_integer, 3 + 5j)

    def is_none(self):
        self.assertTrue(max_integer, "the expression is not true")

