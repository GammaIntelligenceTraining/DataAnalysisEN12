# empty_lst = []
# empty_lst = list()

# print(type(empty_lst))

# var = "Hello World!"
# not_empty_lst = [100, 0.43, "hello", True, [1, 2, [10, 20, 30, 40], 4, 5], None, var]
# var = 123

# print(type(not_empty_lst[2]))
# print(len(not_empty_lst))
# print(not_empty_lst[4][2][1])
# print(not_empty_lst[::-1])

# var1, *var2, var3 = [1, 2, 3, 4, 5]

# print(var1, var2, var3)

# x = [1, 2, 3, 4]
# y = [10, 20, *x, 40, 50]
# print(y)

courses = ['Math', 'Algebra', 'English', 'Art', 'Physics', 'Art',]
numbers = [1, 2, 3, 4, 5, 6,]

# print(courses)
# courses[1] = 'History'
# print(courses)

# courses.append('History')
# print(courses[3])
# courses.insert(0, 'History')
# print(courses[3])

# extra_courses = ['History', 'Estonian']

# courses.extend(extra_courses)
# print(courses)

# if 'Math' in courses:
#     courses.remove('Math')

# x = courses.pop(0)

# print(courses)
# print(x)

# courses.sort(reverse=True)
# print(courses)

# print(courses.index("Art"))
# print(courses.count("Art"))

# text = "Hello people of planet Earth. Are you ok?"
# text_lst = text.split('. ')
# print(text_lst)

# lst_to_text = ' - '.join(courses)
# print(lst_to_text)
# courses.clear()
# print(courses)

# print(min(courses))
# print(max(courses))
# print(sum(numbers))

# a = [1, 2, 3]
# b = a.copy()
# print('A.id', id(a))
# print('B.id', id(b))
# a.append(4)
# b.append(5)

# print('A', a)
# print('B', b)

# print([1, 2, 3] + [4, 5, 6])
# print([1, 2, 3] * 10)

# x = [1, 2, 3]
# x[0] = 4

# print(x)

# empty_tup = ('hello',)
# # empty_tup = tuple()
# print(type(empty_tup))



courses = ('Math', 'Algebra', 'English', 'Art', 'Physics', 'Art',)

# courses2 = ('Estonian', 'Programming')

# print(id(courses))

# courses = list(courses)
# print(id(courses))
# courses.append('Programming')
# courses = tuple(courses)
# print(id(courses))


# courses = {'Math', 'Algebra', 'English', 'Art', 'Physics', 'Art',}

# empty_set = set()

# print(type(empty_set))

# courses.add("Estonian")
# courses.remove('Math')
# x = courses.pop()

# print(courses)
# print(x)

# courses1 = {'Math', 'Art', 'Physics', 'History',}
# courses2 = {'Art', 'Physics', 'Programming', 'Music'}

# print(courses1.intersection(courses2))

# print(courses1.difference(courses2))
# print(courses2.difference(courses1))

# print(courses1.symmetric_difference(courses2))

# print(courses1.union(courses2))

# nums = {1, 2, 3, 4, 5, 6, 7, 8,}

# for num in nums:
#     if num % 2 == 0:
#         print(num, 'even')
#     else:
#         print(num, 'odd')

# print('Good bye')

# for letter in "hello world":
#     print(letter)

# people = [
#     ('Jack', 'Smith', 25),
#     ('Mary', 'Gold', 20),
#     ('Simon', 'Bold', 30),
#     ('James', 'Green', 15),
#     ('Sarah', 'Smith', 17),
# ]
# adults = []
# for person in people:
#     if person[2] >= 18:
#         adults.append(f"{person[0]} {person[1]}")

# print(adults)


# for person in people:
#     print(f'Hello {person[0]} {person[1]}. You are {person[2]} years old.')

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# odds = []
# evens = []

# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
#     else:
#         odds.append(num)

# print(odds)
# print(evens)


# names = ['Jack', 'Sarah', 'Mary', 'Bob']
# surnames = ['Smith', 'Gold', 'Green', 'Dylan']
# ages = [10, 40, 34, 23]

# for index in range(len(names)):  # [0, 1, 2, 3]
#     print('INDEX', index)
#     print(names[index], surnames[index], ages[index])


for num1 in range(10):  # 10 times
    for num2 in range(10):  # 10 x 10 = 100 times
        for num3 in range(10):  # 10 x 100 = 1000 times
            print(num1, num2, num3)