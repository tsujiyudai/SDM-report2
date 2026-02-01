#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_


class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (21, calc(3,7))

        def test_sample2 (self):
                self.assertEqual (-1, calc(0,150))

        def test_sample3 (self):
                self.assertEqual (-1, calc('a','b'))

        def test_sample4 (self):
                self.assertEqual (-1, calc(0.1,999))
        
        def test1 (self):
                self.assertEqual (200, calc(20 ,10))

        def test2 (self):
                self.assertEqual (1, calc(1 ,1))

        def test3 (self):
                self.assertEqual (998001, calc(999 ,999))

        def test4 (self):
                self.assertEqual (-1, calc(0 ,1000))

        def test5 (self):
                self.assertEqual (-1, calc(10 ,"abc"))
        

