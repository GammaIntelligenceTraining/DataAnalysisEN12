# ============================================
# Python: Lists (Basics & Core Operations)
# ============================================

courses = ["History", "Programming", "Math", "Literature", "Physics"]
nums = [1, 5, 6, 8, 3, 4, 2]


# --------------------------------------------
# Replacing list values
# --------------------------------------------

test_list = [1, 2, 3]
print(test_list)

test_list[1] = 555
print(test_list)


# --------------------------------------------
# Adding items to a list
# --------------------------------------------

# append() — adds item to the end of the list
courses.append("Art")
print(courses[-1])
print(courses)

# insert() — inserts item at a specific index
courses.insert(0, "English")
print(courses[0])
print(courses)

# extend() — adds items from another list
# (append() would add the list as ONE item)
courses2 = ["Economics", "Marketing"]
courses.extend(courses2)
print(courses)


# --------------------------------------------
# Removing items from a list
# --------------------------------------------

# remove() — removes item by value
courses.remove("Math")
print(courses)

# pop() — removes last item
courses.pop()
print(courses)

# pop() also RETURNS the removed item
popped_item = courses.pop()
print(popped_item)
print(courses)


# --------------------------------------------
# Sorting lists
# --------------------------------------------

print(courses)

# reverse() — reverses list order
courses.reverse()
print(courses)

# sort() — sorts alphabetically / numerically
courses.sort()
print(courses)

print(nums)
nums.sort()
print(nums)

# reverse=True — sort in reverse order
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

# sorted() — returns sorted list WITHOUT changing original
print(sorted(courses))
print(courses)

# overwrite original list if needed
courses = sorted(courses)
print(courses)


# --------------------------------------------
# Statistical functions
# --------------------------------------------

print(min(courses))   # smallest value
print(max(nums))      # largest value
print(sum(nums))      # sum of numbers


# --------------------------------------------
# Finding items
# --------------------------------------------

print(courses.index("Programming"))  # index of item
print(courses[1])

print("Sports" in courses)           # membership check


# --------------------------------------------
# List ↔ String conversion
# --------------------------------------------

# join() — list → string
courses_str = ", ".join(courses)
print(courses_str)

print(type(courses), "courses")
print(type(courses_str), "courses_str")

# split() — string → list
new_list = courses_str.split(", ")
print(new_list)


# --------------------------------------------
# Merging lists
# --------------------------------------------

new_joined_list = courses + nums
print(new_joined_list)


# --------------------------------------------
# Copying lists
# --------------------------------------------

# Reference copy (both variables point to same list)
list_1 = ["Math", "History", "Programming", "Physics"]
list_2 = list_1

list_1[2] = "Sports"
list_2[0] = "Art"

print(list_1)
print(list_2)

# Real copy using copy()
list_1 = ["Math", "History", "Programming", "Physics"]
list_2 = list_1.copy()

list_1[2] = "Sports"
list_2[0] = "Art"

print(list_1)
print(list_2)
