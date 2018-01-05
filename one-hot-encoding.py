# import dependencies
from numpy import argmax

# define input
data = 'hello world'
print(data)

# define universe of possible input values
alphabet = 'abcdefghijklmnopqrstuvwxyz '

# define a mapping of chars of integers
char_to_int = dict((c, i) for i, c in enumerate(alphabet))
int_to_char = dict((i, c) for i, c in enumerate(alphabet))

# integer encode input data
integer_encode = [char_to_int[char] for char in data]
print(integer_encode)

# one hot encode
onehot_encode = list()
for value in integer_encode:
    letter = [0 for _ in range(len(alphabet))]
    letter[value] = 1
    onehot_encode.append(letter)
print(onehot_encode)

# invert encoding
