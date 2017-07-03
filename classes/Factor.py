# This Python file uses the following encoding: utf-8

""" Subject line.

Main text.
"""
import numpy as np

from classes.Index import index_for

__author__ = 'Chao Li'


class Factor(object):
    """ factor

    A factor is defined over a set of variables, which is called the scope of the factor.
    """

    def __init__(self, scope, parameters):
        self._scope = scope
        self._parameters = parameters

    def __mul__(self, other):
        """ The implementation of a factor product operation.

        :param other:
        :return: psi

        References
        ----------
        D. Koller and N. Friedman (2009). Probabilistic Graphical Models: Principles and Techniques. edited by . MIT Press.
        Algorithm 10.A.1 — Efficient implementation of a factor product operation.
        """
        phi1 = self
        phi2 = other
        psi_scope = sorted(list(set(phi1._scope) | set(phi2._scope)))
        k_number_of_assignments = np.prod([v.card for v in psi_scope])  # Table size
        psi_parameters = np.zeros(k_number_of_assignments)  # allocating memory
        # index
        j = index_for(phi1._scope, psi_scope)
        k = index_for(phi2._scope, psi_scope)
        # multiply
        np.multiply(phi1._parameters[j], phi2._parameters[k], psi_parameters)
        return Factor(psi_scope, psi_parameters)

    def reordered_variables(self, new_order: list):
        new_parameters = np.zeros(len(self._parameters))  # allocating memory
        index_scope4new_order = index_for(self._scope, new_order)
        for i in range(len(self._parameters)):
            new_parameters[i] = self._parameters[index_scope4new_order[i]]
        return Factor(new_order, new_parameters)

    def __eq__(self, other) -> bool:
        reordered_self = self.reordered_variables(sorted(self._scope))
        reordered_other = other.reordered_variables(sorted(other._scope))
        return reordered_self._scope == reordered_other._scope and np.allclose(reordered_self._parameters,
                                                                               reordered_other._parameters)
