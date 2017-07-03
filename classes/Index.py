# This Python file uses the following encoding: utf-8

""" Subject line.

Main text.
"""
import numpy as np

__author__ = 'Chao Li'


def index_for(X: list, Z: list):
    k_number_of_variables = len(Z)
    k_number_of_assignments = np.prod([v.card for v in Z])  # Table size

    # card
    card = np.array([v.card for v in Z])

    # stride
    stride = np.zeros(k_number_of_variables, dtype=int)
    step = 1
    for x in X:
        l = Z.index(x)
        stride[l] = step
        step *= card[l]

    # index
    assignment = np.zeros(k_number_of_variables, dtype=int)
    index_X4Z = np.zeros(k_number_of_assignments, dtype=int)
    j = 0
    for i in range(k_number_of_assignments):
        index_X4Z[i] = j
        for l in range(k_number_of_variables):
            assignment[l] += 1
            if assignment[l] == card[l]:
                assignment[l] = 0
                j -= (card[l] - 1) * stride[l]
            else:
                j += stride[l]
                break

    return index_X4Z
