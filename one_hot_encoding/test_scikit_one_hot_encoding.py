from unittest import TestCase
import numpy
from .scikit_one_hot_encoding import *


class Scikit_One_Hot_Encoding(TestCase):
    '''Scikit One hot encoding tests'''

    def test_input_data(self):
        self.assertEqual(True, isinstance(data, list))

    def test_value_input(self):
        self.assertEqual(numpy.ndarray, type(values))