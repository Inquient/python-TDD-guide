# -*- coding: utf-8 -*-
import math
import re


class ArrayProcessor:

    @staticmethod
    def SortAndFilter(array):
        new = []
        for el in array:
            if (int(el/10) > 0)and(int(el/10 < 10)):
                new.append(el)
        new.sort()
        return new


class Rectangle:

    def __init__(self):
        self.x = []
        self.y = []
        self.diagLen = 0

    def setVertices(self, x, y):
        self.x = x
        self.y = y
        self.diagonal()
        if self.checRect() == False:
            raise ValueError("Not a rectangle")
        return self.diagLen

    def diagonal(self):
        self.diagLen = math.sqrt(((self.x[2] - self.x[0])**2)+((self.y[2] - self.y[0])**2))

    def checRect(self):
        a = math.sqrt(((self.x[1] - self.x[0]) ** 2) + ((self.y[1] - self.y[0]) ** 2))
        b = math.sqrt(((self.x[2] - self.x[1]) ** 2) + ((self.y[2] - self.y[1]) ** 2))
        c = math.sqrt((a**2)+(b**2))
        if c == self.diagLen:
            return True
        else:
            return False


class StringFormatter:

    def ShortFileString(self, path):
        result = re.findall(r'\w+\.', path)
        name = (result[0] + "tmp").upper()
        return name


