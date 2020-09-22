#!/usr/bin/env python3

import unittest
import math

class TestMathMethods(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_sin(self):
        self.assertEqual(1.0, math.sin(math.pi/2.0))
    
    def test_cos(self):
        self.assertEqual(0.0, math.cos(math.pi/2.0))

    def test_sqrt(self):
        self.assertEqual(3, math.sqrt(9.0))

if __name__ == '__main__':
    unittest.main()