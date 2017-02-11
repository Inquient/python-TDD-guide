# -*- coding: utf-8 -*-
import unittest
from ProductionCode import *


class MyTest(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle()
        self.strfrm = StringFormatter()


    def testDvuznachnosti(self):
        # Проверка двух списков на совпадение элементов и их количества, независимо от их порядка
        self.assertCountEqual(ArrayProcessor.SortAndFilter([2, 1, 6, 9, 111, 12, 22, 98, 105, 222]), [98, 22, 12])

    def testOrder(self):
        # Проверка списка поэлементно, с учётом порядка
        self.assertEqual(ArrayProcessor.SortAndFilter([2, 1, 6, 9, 111, 98, 12, 22, 105, 222]), [12, 22, 98])

    def testDiagonal(self):
        # Проверка вычисления длинны диагонали
        self.assertAlmostEqual(self.rectangle.setVertices([0, 0, 5, 5], [0, 5, 5, 0]), 7.0710678118654755)

    def testException(self):
        # Проверяет, бросается ли исключение, если объект не является прямоугольником
        with self.assertRaises(ValueError) as ex:
            self.assertAlmostEqual(self.rectangle.setVertices([0, 0, 7, 5], [0, 5, 7, 0]), 9.899494936611665)
            print(ex)

    def testStringSearch(self):
        self.assertEqual(self.strfrm.ShortFileString("C:\\asd\\asdfsger\\weuyrt46s\\nEw22.bat"), "NEW22.TMP")
