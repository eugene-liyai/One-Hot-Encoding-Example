from unittest import TestCase
import numpy
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from .scikit_one_hot_encoding import *


class Scikit_One_Hot_Encoding(TestCase):
    '''Scikit One hot encoding tests'''

    def test_input_data(self):
        self.assertEqual(True, isinstance(data, list))

    def test_value_input(self):
        self.assertEqual(numpy.ndarray, type(values))

    def test_label_encoding(self):
        self.assertEqual(LabelEncoder, type(label_encoding))

    def test_integer_encoded(self):
        self.assertEqual(numpy.ndarray, type(integer_encoded))

    def test_onehot_encoding(self):
        self.assertEqual(OneHotEncoder, type(onehot_encoding))

    def test_onehot_encoded(self):
        self.assertEqual(numpy.ndarray, type(onehot_encoded))
