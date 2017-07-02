# This Python file uses the following encoding: utf-8

""" Subject line.

Main text.
"""
from unittest import TestCase

from classes.Variable import Variable

__author__ = 'Chao Li'


class TestVariable(TestCase):
    def setUp(self):
        self.A = Variable(1, "A", ['a1', 'a2', 'a3'])
        self.B = Variable(2, "B", ['b1', 'b2'])
        self.C = Variable(3, "C", ['c1', 'b2'])
        # D.index = 1
        self.D = Variable(1, "D", ['d1', 'd2'])

    def test_index(self):
        assert self.A.index == 1
        assert self.B.index == 2
        assert self.C.index == 3
        assert self.D.index == 1

    def test_name(self):
        assert "A" == self.A.name
        assert "B" == self.B.name
        assert "C" == self.C.name
        assert "D" == self.D.name

    def test_values(self):
        assert ['a1', 'a2', 'a3'] == self.A.values
        assert ['b1', 'b2'] == self.B.values

    def test_card(self):
        assert 3 == self.A.card
        assert 2 == self.B.card

    def test___eq__(self):
        assert self.A == self.A
        assert self.A != self.B
        assert self.A != self.C
        assert self.A == self.D

        assert self.B != self.A
        assert self.B == self.B
        assert self.B != self.C
        assert self.B != self.D

    def test___lt__(self):
        assert self.A >= self.A
        assert self.A < self.B
        assert self.A < self.C
        assert self.A >= self.D

        assert self.B > self.A
        assert self.B >= self.B
        assert self.B < self.C
        assert self.B > self.D

    def test___hash__(self):
        assert hash(self.A) == hash(self.A)
        assert hash(self.A) != hash(self.B)
        assert hash(self.A) != hash(self.C)
        assert hash(self.A) == hash(self.D)

    def test_get_value(self):
        assert "a1" == self.A.get_value(0)
        assert "a2" == self.A.get_value(1)
        assert "a3" == self.A.get_value(2)

        assert "b1" == self.B.get_value(0)
        assert "b2" == self.B.get_value(1)

    def test_get_value_index(self):
        assert 0 == self.B.get_value_index("b1")
        assert 1 == self.B.get_value_index("b2")
