# This Python file uses the following encoding: utf-8

""" Subject line.

Main text.
"""
from unittest import TestCase

from classes.Index import index_for
from classes.Variable import Variable

__author__ = 'Chao Li'


class TestIndexFor(TestCase):
    def setUp(self):
        self.A = Variable(1, "A", ['a1', 'a2', 'a3'])
        self.B = Variable(2, "B", ['b1', 'b2'])
        self.C = Variable(3, "C", ['c1', 'b2'])
        # D.index = 1
        self.D = Variable(1, "D", ['d1', 'd2'])

        self.X = [ self.B, self.A]
        self.Y = [ self.C, self.B]
        self.Z = [ self.C, self.B, self.A]

    def test_IndexFor(self):
        """
        References
        ----------
        D. Koller and N. Friedman (2009). Probabilistic Graphical Models: Principles and Techniques. edited by . MIT Press.
        page 107, Figure 4.3 An example of factor product
        """
        index_X4Z = index_for(self.X, self.Z)
        assert 0 == index_X4Z[0]
        assert 0 == index_X4Z[1]
        assert 1 == index_X4Z[2]
        assert 1 == index_X4Z[3]
        assert 5 == index_X4Z[10]
        assert 5 == index_X4Z[11]

        index_Y4Z = index_for(self.Y, self.Z)
        assert 0 == index_Y4Z[8]
        assert 1 == index_Y4Z[9]
        assert 2 == index_Y4Z[10]
        assert 3 == index_Y4Z[11]
