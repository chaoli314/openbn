# This Python file uses the following encoding: utf-8

""" Subject line.

Main text.
"""

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

        phi1.parameters








