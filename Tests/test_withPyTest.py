# -*- coding: utf-8 -*-
import pytest
from ProductionCode import *


class TestCode:

    def setup_class(self):
        self.rectangle = Rectangle()
        self.strfrm = StringFormatter()

    # def test_Dvuznachnosti(self):
    #     # Проверка двух списков на совпадение элементов и их количества, независимо от их порядка
    #     assert ArrayProcessor.SortAndFilter([2, 1, 6, 9, 111, 12, 22, 98, 105, 222]) == [98, 22, 12]

    def test_Order(self):
        # Проверка списка поэлементно, с учётом порядка
        assert ArrayProcessor.SortAndFilter([2, 1, 6, 9, 111, 98, 12, 22, 105, 222]) == [12, 22, 98]

    def test_Diagonal(self, setVertices):
        # Проверка вычисления длинны диагонали
        assert setVertices([0, 0, 5, 5], [0, 5, 5, 0]) == 7.0710678118654755

    def test_Exception(self):
        # Проверяет, бросается ли исключение, если объект не является прямоугольником
        with pytest.raises(ValueError) as ex:
            assert self.rectangle.setVertices([0, 0, 7, 5], [0, 5, 7, 0]) == 9.899494936611665
            print(ex)

    def test_StringSearch(self):
        assert self.strfrm.ShortFileString("C:\\asd\\asdfsger\\weuyrt46s\\nEw22.bat") == "NEW22.TMP"
