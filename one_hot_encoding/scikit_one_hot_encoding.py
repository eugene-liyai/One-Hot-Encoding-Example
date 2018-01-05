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