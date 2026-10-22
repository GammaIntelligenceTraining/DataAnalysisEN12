
# String Methods - Boolean Checks

print('hello world'.endswith('world'))  # True if ends with substring
print('hello world'.startswith('hello'))  # True if starts with substring
print('123test'.isalnum())  # True if (A-Z, a-z, 0-9) only
print('asdasda'.isalpha())  # True if (A-Z, a-z) only
print('123asd asdas 😂'.isascii()) # True if all characters are ASCII
print('123123'.isdecimal())  # True if (0-9) only (no arabic, roman, fractions, etc)
print('1231212312'.isdigit())  # True if (0-9) also superscripts, subscripts, arabic, etc
print("Ⅴ".isnumeric())  # True if (0-9) also roman, fractions, etc
print('⅕'.isnumeric())  # True if (0-9) also roman, fractions, etc
print('Hello World'.istitle())  # True if first letter of each word is uppercase
print('hello world'.islower())  # True if all letters are lowercase
print('HELLO'.isupper())  # True if all letters are uppercase
print('   '.isspace())  # True if all characters are whitespace
print('world' in 'hello world')  # True if substring found in string


# List/Set/Tuple methods - Boolean Checks
print(1 in [1, 2, 3])  # Count occurrences of value
print(4 not in [1, 2, 3])  # True if value not found in list
print(all([1, 2, 3]))  # True if all elements are truth
print(any([0, 1, 2, 3]))  # True if any element is truthy

