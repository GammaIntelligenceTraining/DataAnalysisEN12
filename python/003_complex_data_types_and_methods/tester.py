# empty = []  # list()
# empty = list()
# print(type(empty))

# a = 1231
# filled_list = [123, 0.213, True, True, 'Hello world', [1, [999, 888, 777], 3], a]
# # print(filled_list[0:1])
# print(len(filled_list))
# print(filled_list[5][1][1])
# print(filled_list[::-1])

# var1, var2, var3 = [1, 2, 3]
# print(var1, var2, var3)

# var1, *var2, var3 = [1, 2, 3, 4, 5, 6, 7, 8]
# print(var1, var2, var3)

# print(*var2)


# courses = ['Art', 'Math', 'Physics', 'History', 'Programming']
# numbers = [1, 4, 6, 3, 8, 3, 4, 2]

# courses[0] = 'English'
# print(courses)

# courses.append('English')
# courses.insert(2, 'Science')
# courses.extend(['Chemistry', 'Estonian'])

# courses.remove('Art')
# deleted = courses.pop(0)
# courses.insert(2, deleted)
# print(deleted)
# print(courses)

# x = numbers + courses
# print(x)

# courses.reverse()
# print(courses[::-1])
# courses.sort(reverse=True)
# print(sorted(courses))

# print(courses.index('Programming', 1, 3))
# print(courses.count('Physics'))

# print(str(courses))
# print(bool([]))
# print(courses)

# message = 'Hello, people, of, planet, Earth. How are you doing?'
# print(message.split(' ', maxsplit=4))
# print(' '.join(courses))

# courses.clear()
# print(courses)

# a = [1, 2, 3]
# b = a.copy()

# a.append(4)
# b.append(5)
# print(a, b)

# print(id(a))
# print(id(b))

# print(sum(numbers))
# print(max(courses))
# print(min(courses))

# courses = ('Art', 'Math', 'Physics', 'History', 'Programming')
# numbers = (1, 4, 6, 3, 8, 3, 4, 2)

# empty = ()
# empty = tuple()
# print(type(empty))

# one_element = (1,)
# print(type(one_element))

# courses = list(courses)
# print(courses)
# courses = tuple(courses)
# print(courses + numbers)

# courses = {'Art', 'Math', 'Physics', 'History', 'Programming'}

# empty = set()
# print(type(empty))
# courses.add('English')
# courses.discard('Estonian')
# # courses.remove('Maths')
# deleted = courses.pop()
# print(deleted)
# courses.update(('Estonian', 'Estonian', 'Math'))
# print(courses)

x = ['a', 'a', 'b', 'c', 'c', 'd', 'd', 'd']
x = list(set(x))
print(x)

set1 = {'Math', 'Physics', 'History', 'Art'}
set2 = {'Math', 'Art', 'English', 'Chemistry'}

print(set1.difference(set2))
print(set2.difference(set1))
# set1.difference_update(set2)
print(set1.intersection(set2))

print(set1.symmetric_difference(set2))
print({'Math', 'Estonian'}.issubset(set1))
print({'Math', 'Estonian'}.intersection(set1))

# print(set1.issuperset({'Math', 'Art'}))