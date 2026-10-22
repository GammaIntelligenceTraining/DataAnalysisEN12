string_example1 = 'Hello world world'
                #  0123456789...
                        #  -5-4-3-2-1
string_example2 = 'fiRst lEttEr is LowErCase'
string_example3 = '  **   extra whitespaces  **  '
string_example4 = 'der fluß'

escape_string = "My favourite book is \n\"Metro 2033\""
# print(escape_string)
# print(len(escape_string))

# print(len(str(1231.2312)))

# print(string_example1[len(string_example1) - 1])
# print(string_example1[-1])

# # [START:STOP:STEP]
# print(string_example1[0:5] + string_example1[6:12])
# print(string_example1[:5])
# print(string_example1[6:])
# print(string_example1[-6:-1])
# print(string_example1[0:10:2])
# print(string_example1[15:4:-1])

print(string_example1.upper())
print(string_example4.lower())
print(string_example4.casefold())

print(string_example2.capitalize())
print(string_example2.title())


# string_example1 = string_example1.upper()
# print(string_example1)

# print(string_example3)
# print(string_example3.strip(' *'))
# print(string_example3.lstrip(' *'))
# print(string_example3.rstrip(' *'))

# print(string_example1.replace('world', 'planet', 1))
# print(string_example1.replace(' ', ''))

# print(string_example1.count('world', 7))

# print(string_example1.replace('world', 'planet').upper())

# print(string_example1.find('world', 7))

# print(help(str.find))

# a = 'Hello'
# b = 'World'

# print(a + ' ' + b + str(True))
# print()
# print(a, b, 'planet', 'people', True, 123, 23.2323, sep='\n', end='!')
# print('test')

# print('world', 'planet', sep="******")

# name = 'John'
# salary = 2000
# string = "{0}s salary is {1}$ {0}"
# print(string.format(name, salary))

p = 'computer'
pr = 3000

string = 'This {product} costs {price:.2f}$'
print(string.format(product=p, price=pr))

# Formated string used in Python 2
# x = 12231.3456789
# y = 131.1314
# print('The value of x is %.4f' % x)
# print('The value of y is %.2f' % y)

# emp_name = 'John'
# emp_age = 30
# emp_salary = 1500

# emp_string = 'Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f' % {'name': emp_name, 'salary': emp_salary, 'age': emp_age}
# print(emp_string)

name = 'Jack'
salary = 3000

print(f'{name}s salary is {salary:.2f}$')
print(r'a\nb')

byte_string = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(byte_string.decode('utf-8'))