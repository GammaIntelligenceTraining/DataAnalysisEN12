# ============================================
# Python: Lists, Tuples and Sets
# ============================================

# Lists, tuples and sets are iterable objects
# They can store multiple values

# --------------------------------------------
# Lists
# --------------------------------------------
# Lists are:
# - ordered
# - mutable (can be changed)
# - allow duplicates

# Empty lists
empty_list = []
empty_list2 = list()

print(type(empty_list))      # <class 'list'>

# List with mixed data types
world = "world"
filled_list = [1, 0.2, "Hello", world, True, [1, 2, 3]]
print(filled_list)


# --------------------------------------------
# List indexing and slicing
# --------------------------------------------

courses = ["History", "Math", "Literature", "Physics", "Programming"]

print(len(courses))          # number of items
print(courses)               # full list

print(courses[0])            # first item
print(courses[4])            # fifth item
print(courses[-1])           # last item

print(courses[0:2])          # first two items
print(courses[:3])           # from start to index 3 (not included)
print(courses[2:])           # from index 2 to the end
print(courses[::-1])         # reversed list