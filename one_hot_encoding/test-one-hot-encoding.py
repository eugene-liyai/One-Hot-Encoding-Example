from unittest import TestCase
from one_hot_encoding import *


class One_Hot_Encoding(TestCase):
    '''One hot encoding tests'''

    def test_input_string(self):
        self.assertEqual(True, isinstance(data, str))

    def test_univeral_input_dataset(self):
        self.assertEqual(True, isinstance(alphabet, str))

    def test_integer_encode(self):
        self.assertEqual(True, isinstance(integer_encode, list))

    def test_input_mapping(self):
        self.assertEqual(True, isinstance(char_to_int, dict))
        self.assertEqual(True, isinstance(int_to_char, dict))

    def test_onehot_encoding(self):
        self.assertEqual(True, isinstance(onehot_encode, list))
        self.assertIsNotNone(onehot_encode)

    def test_inverted_data(self):
        self.assertEqual(True, isinstance(inverted, str))
