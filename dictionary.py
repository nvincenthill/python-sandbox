# dict() constructor builds dictionaries directly from sequences of key-value pairs
example = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(example)
print('sape' in example)
print(list(example))

# creating a dictionary with a list comprehension
second_example = {x: x**2 for x in (2, 4, 6)}
print(second_example)

# basic dictionary
basic_dictionary = {'jack': 4098, 'sape': 4139}
print(basic_dictionary)
