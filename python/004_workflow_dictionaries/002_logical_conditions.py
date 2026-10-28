# ============================================
# Python: Logical Conditions & Control Flow
# ============================================


# --------------------------------------------
# 1. Comparison operators
# --------------------------------------------

a = 7
b = 10

print(a > b)      # False
print(b >= a)     # True
print(a < b)      # True
print(b <= a)     # False
print(a == b)     # False
print(a != b)     # True

# Chained comparison
print(0 < a < 15) # True


# --------------------------------------------
# 2. Comparing characters and strings
# --------------------------------------------

print("a" > "b")          # False
print("b" > "a")          # True
print("A" > "a")          # False (uppercase comes first)

# Character codes
print(ord("a"))           # 97
print(chr(97))            # 'a'

print("apple" == "apple")      # True
print("apple" == "applepie")   # False
print("apple" < "applepie")    # True


# --------------------------------------------
# 3. Boolean operators
# --------------------------------------------

# AND
print(True and True)              # True
print(True and False)             # False
print(5 > 2 and 7 == 5)           # False
print(10 % 2 == 0 and "hello".isalpha())  # True

# OR
print(True or False)              # True
print(False or False)             # False
print(10 ** 3 <= 1000 or None)    # True

# NOT
print(not True)                   # False
print(not False)                  # True
print(not (5 > 0))                # False
print(not [])                     # True


# --------------------------------------------
# 4. Complex condition (example)
# --------------------------------------------

# Example: validating a national ID code (simplified)
code = "51306040387"

is_valid = (
    len(code) == 11
    and code.isdigit()
    and (
        (1 <= int(code[0]) <= 4 and 0 <= int(code[1:3]) <= 99)
        or
        (5 <= int(code[0]) <= 6 and 0 <= int(code[1:3]) <= 23)
    )
)

print(is_valid)


# --------------------------------------------
# 5. if / elif / else
# --------------------------------------------

code = "12345678910"

if len(code) == 11:
    print("Your national ID is:", code)
elif len(code) > 11:
    print("Your ID is too long!")
else:
    print("Your ID is too short!")


# --------------------------------------------
# 6. Multiple elif branches
# --------------------------------------------

age = int(input("Please enter your age: "))

if 0 < age <= 12:
    print("You are a child")
elif age <= 18:
    print("You are a teenager")
elif age <= 65:
    print("You are an adult")
elif age <= 120:
    print("You are a senior")
else:
    print("Wrong input!")


# --------------------------------------------
# 7. Nested if statements
# --------------------------------------------

if code.isdigit():
    if len(code) == 11:
        print("Your national ID is:", code)
    elif len(code) > 11:
        print("Your ID is too long!")
    else:
        print("Your ID is too short!")
else:
    print("Your code must contain only digits")


# --------------------------------------------
# 8. Conditions inside loops
# --------------------------------------------

text = "This string will be iterated soon!"

for i in range(len(text)):
    if text[i] == " ":
        print("_", end="")
    elif text[i] == "i" or i % 2 == 0:
        print(text[i].upper(), end="")
    else:
        print(text[i], end="")
print()


# --------------------------------------------
# 9. One-line if (ternary operator)
# --------------------------------------------

x = 7
print("X more than ten") if x > 10 else print("X less or equal to ten")


# --------------------------------------------
# 10. Other operators
# --------------------------------------------

# in / not in
lst = [1, 2, 3, 4, "a", "b", "c"]
print("a" in lst)        # True
print(2 not in lst)      # False

# is / is not
x = 10
y = 10

print(x == y)            # True (value comparison)
print(x is y)            # True (same object, small int optimization)

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]

print(lst1 == lst2)      # True
print(lst1 is lst2)      # False


# --------------------------------------------
# 11. any() and all()
# --------------------------------------------

numbers = [-2, -1, 0, 1, 2]

print(any(numbers))      # True (at least one truthy value)
print(all(numbers))      # False (0 is falsy)

numbers.remove(0)
print(all(numbers))      # True


# --------------------------------------------
# 12. Example: FizzBuzz
# --------------------------------------------

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, "FizzBuzz")
    elif num % 3 == 0:
        print(num, "Fizz")
    elif num % 5 == 0:
        print(num, "Buzz")


# --------------------------------------------
# 13. Example: find indexes of 's'
# --------------------------------------------

text = "she sells seashells by the seashore"

for i in range(len(text)):
    if text[i] == "s":
        print(i)
