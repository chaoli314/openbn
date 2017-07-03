# This Python file uses the following encoding: utf-8

""" Subject line.

Main text.
"""
from unittest import TestCase
import numpy as np

from classes.Factor import Factor
from classes.Variable import Variable

__author__ = 'Chao Li'


class TestFactor(TestCase):
    def setUp(self):
        self.A = Variable(1, "A", ['a1', 'a2', 'a3'])
        self.B = Variable(5, "B", ['b1', 'b2'])
        self.C = Variable(3, "C", ['c1', 'b2'])

    def test___mul__(self):
        """
        References
        ----------
        D. Koller and N. Friedman (2009). Probabilistic Graphical Models: Principles and Techniques. edited by . MIT Press.
        page 107, Figure 4.3 An example of factor product
        """
        # Expected
        phi1_scope = [self.B, self.A]
        phi2_scope = [self.C, self.B]
        psi_scope = [self.C, self.B, self.A]
        phi1_parameters = np.array([0.5, 0.8, 0.1, 0, 0.3, 0.9])
        phi2_parameters = np.array([0.5, 0.7, 0.1, 0.2])
        psi_parameters = np.array([0.25, 0.35, 0.08, 0.16, 0.05, 0.07, 0., 0., 0.15, 0.21, 0.09, 0.18])
        phi1 = Factor(phi1_scope, phi1_parameters)
        phi2 = Factor(phi2_scope, phi2_parameters)
        psi = Factor(psi_scope, psi_parameters)
        # Actual
        results = phi1 * phi2
        results = results.reordered_variables(psi_scope)
        assert psi == results
