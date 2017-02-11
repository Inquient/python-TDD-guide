# -*- coding: utf-8 -*-
import pytest
from ProductionCode import *

@pytest.fixture
def setVertices():
    rectangle = Rectangle()
    return rectangle

@pytest.fixture
def ShortFileString():
    stringformatter = StringFormatter()
    return stringformatter


# Проверка списка поэлементно, с учётом порядка
@pytest.mark.parametrize("arr, expected", [
    ([2, 1, 6, 9, 111, 12, 22, 98, 105, 222], [12, 22, 98]),
    ([5, 55, 234, 234234, 45, 88, 0, 0], [45, 55, 88]),
    ([2, 4, 5, 6, 21, 122, 1223, 567, 8], [21])
])
def test_SortAndFilter(arr, expected):
    assert ArrayProcessor.SortAndFilter(arr) == expected

# Проверка вычисления длинны диагонали
@pytest.mark.parametrize("arr_x, arr_y, expected", [
    ([0, 0, 5, 5], [0, 5, 5, 0], 7.0710678118654755),
    ([0, 0, 12, 12], [0, 9, 9, 0], 15.0),
    ([2, 2, 5, 5], [2, 3, 3, 2], 3.1622776601683795)])
def test_diagonal(arr_x, arr_y, expected, setVertices):
    assert setVertices.setVertices(arr_x, arr_y) == expected

# Проверяет, бросается ли исключение, если объект не является прямоугольником
@pytest.mark.parametrize("arr_x, arr_y", [
    ([0, 0, 7, 5], [0, 5, 7, 0]),
    ([1, 2, 3, 4], [7, 8, 9, 0]),
    ([9, 7, 7, 5], [7, 5, 3, 12])])
def test_checkRect(arr_x, arr_y, setVertices):
    with pytest.raises(ValueError):
        assert setVertices.setVertices(arr_x, arr_y)

@pytest.mark.parametrize("path, expected", [
    ("C:\\asd\\asdfsger\\weuyrt46s\\nEw22.bat", "NEW22.TMP"),
    ("C:\\lfkhnjfl\\123hq34\\hero.jpg", "HERO.TMP"),
    ("G:\\00000\\w3efwf\\wdajsdh888\\5675.docx", "5675.TMP")])
def test_ShortFileString(path, expected, ShortFileString):
    assert ShortFileString.ShortFileString(path) == expected
