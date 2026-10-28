# empty = {}
# empty = dict()

# print(type(empty))


# KEYS: strings, integers, floats and tuple
# VALUES: ANY data type
# student = {
#     "first_name": "Jack",
#     "last_name": "Smith",
#     "age": 25,
#     "courses": [
#         "Math",
#         "Art",
#         "Programming"
#     ],
#     "information": {
#         "height": 179,
#         "weight": 94,
#         "eye_color": "blue",
#     },
#     (1, 2): "coordinate key",
# }

# # print(student["first_name"])
# # print(student.get("first_name"))

# # print(student.get("car", ""))

# # print(student["courses"][2])
# # print(student["information"]["eye_color"])

# # student["first_name"] = "Bob"
# # student["last_name"] = "Green"
# # student["phone"] = "555-555-5555"
# # var_key = "citezenship"
# # student[var_key] = "Estonia"


# # student.update({
# #     "first_name": "mary",
# #     "phone": "555-333-2222",
# #     "is_married": True,
# # })

# # student.update(first_name="Mary", is_married=True)

# # # d = student.pop("information")
# # d = student.popitem()
# # print(d)
# # print(student)

# # print(student.keys())
# # print(student.values())
# # print(student.items())

# print(123 == 124)  # equal
# print(123 != 124)  # not equal
# print(123 > 100)  # greater than
# print(123 < 100)  # less than
# print(123 >= 100)  # greater or equal
# print(123 <= 100)  # less or equal


# print(False and True)  
# print(True or False)

# x = 15
# print(x > 0 and x < 10)
# print(x > 0 or x < 10)

# print(not True)
# print(not x == 15)


# idcode = "388031602720"


# if len(idcode) == 11:
#     print('ID code is correct')
#     print('Good boy! Bye now!')
# elif len(idcode) > 11:
#     print('ID code is too long')
#     print('Bye ')
# else:
#     print('ID code is too short')

#     print('Good bye!')


# x = 100

# if x > 0:
#     print('Greater than 0')
# if x < 1000:
#     print('Less than 1000')
# if x == 100:
#     print('X is 100')


# age = 42

# # if age <= 12 and age >= 0:
# if 0 < age <= 12:
#     print('Child')
# elif age <= 18:
#     print('Teenager')
# elif age <= 65:
#     print('Adult')
# else:
#     print('Senior')

# idcode = '38803160272'

# if len(idcode) == 11:
#     print('ID code is correct')
# else:
#     if len(idcode) > 11:
#         print('ID code is too long')
#     else:
#         print('ID code is too short')


# print(list(range(0, 10)))
# [0, 1, 2, 3......9]
# for num in range(10):
#     print(num)
#     print(num ** 2)
#     print(num ** 3)
#     print('#' * 20)

# for letter in 'python':
#     if letter == 't':
#         print('WE FOUND T')
#     print(letter)


# for name in ['Jack', 'Mary', 'Sarah', 'Simon']:
#     print(f'Hello {name}')


# squares = []

# for num in range(100):
#     squares.append(num ** 2)

# print(squares)

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for num in x:
#     # x.append(num ** 2)
#     num = num ** 2

# print(x)


# for num1 in range(10):                  # 10 times
#     for num2 in range(10):              # 10 * 10 = 100 times
#         for num3 in range(10):          # 10 * 10 * 10 = 1000 times
#             print(num1, num2, num3)


# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# y = [3, 4, 5, 6, 7, 8, 9, 1, 2]

# for index in range(len(y)):  # range(0, len(x), 2)
#     print(x[index] + y[index])



# while True:
#     print('I can\'t stop!')


# x = 0
# while x > 100:
#     print(x)
#     x += 1

# print(x)  # 100

# while True:
#     idcode = input("Enter Estonian national ID: ")
#     if len(idcode) == 11:
#         print("ID", idcode)
#         break
#     elif len(idcode) > 11:
#         print("ID is too long")
#         continue
#     else:
#         print("ID is too short")
#         continue

#     print("FINALLY")


# condition = True

# while condition:
#     condition = False
#     print('Hello')
#     print('Something happens')
#     print('Ending')
    
#     print('Finally')