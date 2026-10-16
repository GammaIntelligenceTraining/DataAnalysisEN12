# ============================================
# Python Basics: Student Handout
# Module 001: Simple Data Types & Basics
# ============================================


# ============================================
# 1. Simple Data Types
# ============================================
# Python has several built-in basic types:
# - int       : Integer numbers (e.g., 500, -10, 0)
# - float     : Floating-point decimal numbers (e.g., 50.0, 3.14)
# - str       : Text / Strings in quotes (e.g., "Hello, Python!")
# - bool      : Boolean truth values (True or False)
# - NoneType  : Absence of value (None)

# Variables act as labels pointing to values in memory:
int_var = 500
float_var = 50.9
str_var = "Hello, Python!"
bool_var = True
none_var = None

# Printing values to the console:
print("--- 1. Simple Data Types ---")
print("Integer:", int_var)
print("Float:", float_var)
print("String:", str_var)
print("Boolean:", bool_var)
print("None:", none_var)

# type() returns the data type of any variable or value:
print("type(int_var):", type(int_var))      # <class 'int'>
print("type(float_var):", type(float_var))  # <class 'float'>
print("type(str_var):", type(str_var))      # <class 'str'>
print("type(bool_var):", type(bool_var))    # <class 'bool'>
print("type(none_var):", type(none_var))    # <class 'NoneType'>
print()


# ============================================
# 2. Arithmetic Operators
# ============================================
a = 10
b = 3

print("--- 2. Arithmetic Operators ---")
print("a =", a, ", b =", b)

# + Addition
print("Addition (a + b):", a + b)                  # 13

# - Subtraction
print("Subtraction (a - b):", a - b)               # 7

# * Multiplication
print("Multiplication (a * b):", a * b)            # 30

# / Division (always returns float, even for whole numbers)
print("Division (a / b):", a / b)                  # 3.3333333333333335
print("Division (8 / 2):", 8 / 2)                  # 4.0
print("type(8 / 2):", type(8 / 2))                 # <class 'float'>

# // Floor Division (integer division - drops decimals without rounding)
print("Floor division (a // b):", a // b)          # 3
print("Floor division (7 // 2):", 7 // 2)          # 3

# % Modulus (finds remainder of division - useful for even/odd check)
print("Modulus (a % b):", a % b)                   # 1
print("Is 10 even? (10 % 2 == 0):", 10 % 2 == 0)   # True

# ** Exponentiation (power)
print("Exponentiation (2 ** 3):", 2 ** 3)          # 8
print()


# ============================================
# 3. Data Type Conversion (Type Casting)
# ============================================
print("--- 3. Type Conversion ---")

# int -> float
num_int = 100
converted_float = float(num_int)
print("int -> float:", converted_float, type(converted_float))  # 100.0 <class 'float'>

# float -> int (decimals are truncated, NOT rounded)
num_float = 99.9
converted_int = int(num_float)
print("float -> int:", converted_int, type(converted_int))      # 99 <class 'int'>

# str -> int and str -> float
str_integer = "42"
str_decimal = "3.14"

num_from_str = int(str_integer)
float_from_str = float(str_decimal)
print("str -> int:", num_from_str, type(num_from_str))          # 42 <class 'int'>
print("str -> float:", float_from_str, type(float_from_str))    # 3.14 <class 'float'>

# number -> str
str_from_num = str(12345)
print("int -> str:", str_from_num, type(str_from_num))          # "12345" <class 'str'>

# NOTE: Converting invalid strings raises ValueError:
# int("hello")  # ❌ ValueError: invalid literal for int()
print()


# ============================================
# 4. Truthy and Falsy Values (Conversion to bool)
# ============================================
print("--- 4. False Values in Python ---")

# In Python, any value can be evaluated in a boolean context using bool().
# The following values are considered FALSE (falsy):
# - Number zero: 0, 0.0
# - Empty string: ""
# - None: None
# - Boolean False: False

print("bool(0):", bool(0))              # False
print("bool(0.0):", bool(0.0))          # False
print("bool(''):", bool(""))            # False (empty string)
print("bool(None):", bool(None))        # False
print("bool(False):", bool(False))      # False

# Almost everything else is considered TRUE (truthy):
print("bool(1):", bool(1))              # True
print("bool(-5):", bool(-5))            # True (any non-zero number is True)
print("bool(0.1):", bool(0.1))          # True
print("bool(' '):", bool(" "))          # True (whitespace is a non-empty string)
print("bool('False'):", bool("False"))  # True (non-empty string!)
print()


# ============================================
# 5. User Input with input()
# ============================================
print("--- 5. Example with input() ---")

# input() reads text entered by the user.
# IMPORTANT: input() ALWAYS returns a string (str), even if the user types digits!

user_name = input("Enter your name: ")
user_age_str = input("Enter your age: ")

# Convert string input to integer for numeric calculations
user_age = int(user_age_str)

print("Hello,", user_name + "!")
print("Currently you are", user_age, "years old.")
print("Next year you will be", user_age + 1, "years old.")
