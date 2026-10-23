# sample1 = "Hello world world"
#           #0123456789........
#           #       -5-4-3-2-1
# sample2 = "fiRst LeTtEr is loWerCasE"
# sample3 = "   ***   extra whitespace **    "
# sample4 = "der Fluß"

# # print(sample1.count('wor'))
# # print(sample1.find('planet'))


# # print(sample1.replace(' world', ''))  # substring


# # print(sample3.lstrip(' *'))


# # print(sample2.upper())

# # print(sample4.lower())
# # print(sample4.casefold())

# # print(sample2.capitalize())
# # print(sample2.title())

# # print(sample1.swapcase())

# # print(len(sample1))

# # print(sample1[-1])

# # # [START:STOP:STEP]
# # print(sample1[0:5] + " people")
# # print(sample1[7:])
# # print(sample1[-5:])
# # print(sample1[::-1])

# # print('hello'[2::2])

# sample = "My favourite book is \"Metro 2033\""
# sample2 = '\\that\'s'
# print(sample2)

# print("Hello\tworld")
# sample = """asda
# asd
# dsa
# asd
#             dsads   d       
#     asdasda"""
# # print(sample)

# print()
# print('hello', 123, True, sep="\n", end="!")
# print('END')

# name = "Jack Smith"
# salary = 2000

# template = "Hello {0}. Salary: {1}.{0}{1}{0}{1}"
# print(template.format(name, salary))

# product = 'Computer'
# price = 10000000.219

# # template = "This {product} costs {price}$"
# # print(template.format(product=product, price=price))

# print(f"This {product.lower()} costs {price:.2f}$")



# # Formated string used in Python 2
# x = 12231.3456789
# y = 131.1314
# print('The value of x is %.4f' % x)
# print('The value of y is %.2f' % y)

# emp_name = 'John'
# emp_age = 30
# emp_salary = 1500

# emp_string = 'Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f'% {'name': emp_name, 'salary': emp_salary, 'age': emp_age}
# print(emp_string)

# byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
# print(byte_sting.decode('utf-16'))

# x = 10

# if x == 100:
#     print("X equals 100")
# else:
#     print("X is not equal to 100")

# name = input('Enter name: ')
# if not name:
#     print("Hello stranger!")
# else:
#     print(f"Hello {name}")

# print(not True)

# age = 10

# if age < 12:
#     print('Child')
# elif age < 18:
#     print('Teenager')
# elif age < 65:
#     print('Adult')
# else:
#     print('Senior')

# print("Hello world".endswith("worlt"))
# print("123.4".isdecimal())

# print('asd Asd'.islower())

sample = 'Hello world'

if 'world' in sample:
    print('OK')

print("Good Bye")