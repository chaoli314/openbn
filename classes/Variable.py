# This Python file uses the following encoding: utf-8

""" Subject line.

Main text.
"""
from functools import total_ordering

__author__ = 'Chao Li'


@total_ordering
class Variable(object):
    def __init__(self, variable_index: int, variable_name, values: list):
        self._variable_index = variable_index
        self._variable_name = variable_name
        self._values = values
        self._cardinality = len(values)

    @property
    def index(self):
        return self._variable_index

    @property
    def name(self):
        return self._variable_name

    @property
    def card(self):
        return self._cardinality

    @property
    def values(self):
        return self._values

    def get_value(self, index):
        return self.values[index]

    def get_value_index(self, value):
        return self.values.index(value)

    def __hash__(self) -> int:
        return hash(self.index)

    def __lt__(self, other):
        return self.index < other.index

    def __eq__(self, other):
        return self.index == other.index

    def __repr__(self) -> str:
        return self.name

