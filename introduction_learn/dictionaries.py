example_dictionary = {'key': 'value', 'key2': 'value2'}
print(example_dictionary)
# {'key': 'value', 'key2': 'value2'}
print(example_dictionary['key'])
# value

# Dodanie kolejnego klucza
example_dictionary['added new key'] = 'value3'
print(example_dictionary)
# {'key': 'value', 'key2': 'value2', 'added new key': 'value3'}

# podmiana zawartości klucza
example_dictionary['added new key'] = 'value4'
print(example_dictionary)
#{'key': 'value', 'key2': 'value2', 'added new key': 'value4'}

# print(example_dictionary['NIEISTNIEJĄCY']) > KeyError: 'NIEISTNIEJĄCY'
print(example_dictionary.get('not existing key', 'Dictionary does not contain this key'))
# Dictionary does not contain this key

print(example_dictionary.get('added new key', 'Dictionary does not contain this key'))
# value3

if 'key2' in example_dictionary:
    print("This key exists in dictionary")
else:
    print("This key does not exist in dictionary")

example_dictionary['new key that is dictionary'] = {'key_a': 'value_a', 'key_b': 'value_b'}
print(example_dictionary)
# {'key': 'value', 'key2': 'value2', 'added new key': 'value4', 'new key that is dictionary': {'key_a': 'value_a', 'key_b': 'value_b'}}

print(example_dictionary['new key that is dictionary'])
# {'key_a': 'value_a', 'key_b': 'value_b'}
print(example_dictionary['new key that is dictionary']['key_a'])
# value_a

example_dictionary['new key that is list'] = [234, 'xeddss', 324.6, {'key_new': 'value new'}]
print(example_dictionary)
# {'key': 'value', 'key2': 'value2', 'added new key': 'value4', 'new key that is dictionary':
# {'key_a': 'value_a', 'key_b': 'value_b'}, 'new key that is list': [234, 'xeddss', 324.6, {'key_new': 'value new'}]}