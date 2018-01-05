# import libraries
from numpy import array, argmax
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# define input data
data = ['cold', 'cold', 'warm', 'cold', 'hot', 'hot', 'warm', 'cold', 'warm', 'hot']
values = array(data)
print(values)

# integer encode
label_encoding = LabelEncoder()
integer_encoded = label_encoding.fit_transform(values)
print(integer_encoded)

# binary encode
onehot_encoding = OneHotEncoder(sparse=False)
integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
onehot_encoded = onehot_encoding.fit_transform(integer_encoded)
print(onehot_encoded)

# invert first example
inverted_first = label_encoding.inverse_transform([argmax(onehot_encoded[0, :])])
print(inverted_first)
