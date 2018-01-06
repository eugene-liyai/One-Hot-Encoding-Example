from unittest import TestCase
from .scikit_one_hot_encoding import *


class Scikit_One_Hot_Encoding(TestCase):
    '''Scikit One hot encoding tests'''

    def test_input_string(self):
        self.assertEqual(True, isinstance(data, str))