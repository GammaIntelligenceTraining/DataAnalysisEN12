# ============================================
# Python: List vs Tuple vs Set
# ============================================

# --------------------------------------------
# Tuples
# --------------------------------------------
# Tuples are:
# - ordered
# - immutable (cannot be changed)
# - allow duplicates

courses_tuple = ("Math", "History", "Programming", "Physics")
print(courses_tuple)
print(courses_tuple[2])

# tuples cannot be modified
# courses_tuple[2] = 10   # This would raise an error

# Tuples CAN be combined
t1 = (1, 2, 3)
t2 = (3, 4, 5)
print(t1 + t2)


# --------------------------------------------
# Sets
# --------------------------------------------
# Sets are:
# - unordered
# - mutable
# - do NOT allow duplicates

courses_set = {"Math", "History", "Programming", "Physics", "Math"}
print(courses_set)   # duplicates removed automatically

courses_set.remove("Math")
print(courses_set)


# --------------------------------------------
# Set operations
# --------------------------------------------

set1 = {"Math", "History", "Programming", "Physics"}
set2 = {"Art", "Physics", "Design", "History"}

# intersection() — common elements
print(set1.intersection(set2))

# difference() — elements NOT shared
print(set2.difference(set1))
print(set1.difference(set2))

# union() — all unique elements
print(set1.union(set2))


# --------------------------------------------
# Creating empty collections
# --------------------------------------------

# Empty list
empty_list = []
empty_list = list()

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
# {} creates a dictionary, NOT a set
empty_set = set()


# --------------------------------------------
# Sets
# --------------------------------------------
# Sets are:
# - unordered (no index, no fixed order)
# - mutable (can be changed)
# - do NOT allow duplicate values

# Creating a set
courses_set = {"Math", "History", "Programming", "Physics", "Math"}
print(courses_set)      # duplicates are removed automatically

# You cannot access items by index
# print(courses_set[0])   # error

# --------------------------------------------
# Adding and removing items
# --------------------------------------------

courses_set.add("Art")
print(courses_set)

courses_set.remove("Math")   # removes value
print(courses_set)

# discard() does NOT raise an error if value does not exist
courses_set.discard("Biology")
print(courses_set)


# --------------------------------------------
# Set operations (very common use case)
# --------------------------------------------

backend_courses = {"Math", "Programming", "Databases", "Physics"}
design_courses = {"Design", "Physics", "UX", "Math"}

# intersection() — common elements
print(backend_courses.intersection(design_courses))

# difference() — elements in first set but NOT in second
print(backend_courses.difference(design_courses))
print(design_courses.difference(backend_courses))

# union() — all unique elements from both sets
print(backend_courses.union(design_courses))


# --------------------------------------------
# Membership test (VERY fast in sets)
# --------------------------------------------

print("Math" in backend_courses)      # True
print("Biology" in backend_courses)  # False