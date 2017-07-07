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

    @property
    def scope(self):
        return self._scope

    def marginalization(self, new_scope):
        new_scope = sorted(new_scope)
        i = index_for(new_scope, self._scope)
        new_parameters = np.bincount(i, weights=self._parameters)
        return Factor(new_scope, new_parameters)

    def summing_out(self, y):
        new_scope = sorted(list(set(self.scope) - set([y])))
        return self.marginalization(new_scope)

    def __mul__(self, other):
        """ The implementation of a factor product operation.

        References
        ----------
        D. Koller and N. Friedman (2009). Probabilistic Graphical Models: Principles and Techniques. edited by . MIT Press.
        Algorithm 10.A.1 — Efficient implementation of a factor product operation.
        """
        phi1 = self
        phi2 = other
        psi_scope = sorted(list(set(phi1.scope) | set(phi2.scope)))
        k_number_of_assignments = np.prod([v.card for v in psi_scope])  # Table size
        psi_parameters = np.zeros(k_number_of_assignments)  # Pre-allocate memory
        # index
        j = index_for(phi1.scope, psi_scope)
        k = index_for(phi2.scope, psi_scope)
        # multiply
        np.multiply(phi1._parameters[j], phi2._parameters[k], out=psi_parameters)
        return Factor(psi_scope, psi_parameters)

    def reordered_variables(self, new_order: list):
        index_scope4new_order = index_for(self._scope, new_order)
        new_parameters = np.array(self._parameters[index_scope4new_order])
        return Factor(new_order, new_parameters)

    def __eq__(self, other) -> bool:
        reordered_self = self.reordered_variables(sorted(self.scope))
        reordered_other = other.reordered_variables(sorted(other.scope))
        return reordered_self.scope == reordered_other.scope and np.allclose(reordered_self._parameters,
                                                                             reordered_other._parameters)

    def __truediv__(self, other):
        phi1 = self
        phi2 = other
        psi_scope = sorted(phi1.scope)
        psi_parameters = np.zeros_like(phi1._parameters)  # Pre-allocate memory
        # index
        j = index_for(phi1.scope, psi_scope)
        k = index_for(phi2.scope, psi_scope)
        # true divide
        np.true_divide(phi1._parameters[j], phi2._parameters[k], out=psi_parameters, where=phi2._parameters[k] != 0)
        return Factor(psi_scope, psi_parameters)
