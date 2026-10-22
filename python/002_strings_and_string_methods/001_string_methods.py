# ============================================
# Python: Strings & String Methods
# ============================================

string_sample = "Hello world world"
string_case = "first letteR is lowErcase"
string_spaces = "  extra whitespace string  "
german_sample = "der Fluß"

# --------------------------------------------
# String indexing
# --------------------------------------------
# Strings are sequences, indexing starts from 0

print(string_sample[1])      # 'e' (second character)
print(string_sample[-1])     # 'd' (last character)


# --------------------------------------------
# String slicing
# --------------------------------------------
# string[start:end:step]

print(string_sample[4:])     # from index 4 to the end
print(string_sample[:14])    # from start to index 14 (not included)
print(string_sample[5:12])   # part of a string
print(string_sample[1:10:2]) # every second character
print(string_sample[::-1])   # reverse string


# --------------------------------------------
# String length
# --------------------------------------------

print(len(string_sample))    # number of characters


# --------------------------------------------
# Membership test
# --------------------------------------------
# Check if substring exists

print("world" in string_sample)     # True
print("python" not in string_sample) # True


# --------------------------------------------
# Case conversion
# --------------------------------------------

print(string_sample.upper())         # HELLO WORLD WORLD
print(string_sample.lower())         # hello world world

# Case-insensitive comparison (important for some languages)
print(german_sample.lower())
print(german_sample.casefold())      # stronger lowercase conversion


# --------------------------------------------
# Capitalization
# --------------------------------------------

print(string_case.capitalize())      # First letter uppercase
print(string_case.title())           # Every word starts uppercase


# --------------------------------------------
# Whitespace handling
# --------------------------------------------

print(string_spaces.strip())          # remove spaces from both ends
print(string_spaces.lstrip())         # left side only
print(string_spaces.rstrip())         # right side only


# --------------------------------------------
# Replacing text
# --------------------------------------------

print(string_sample.replace("world", "people"))
print(string_sample.replace("world", "people", 1))  # replace first only


# --------------------------------------------
# Splitting strings
# --------------------------------------------

print(string_sample.split(" "))       # split by spaces
print("a,b,c".split(","))             # split by comma


# --------------------------------------------
# Counting and searching
# --------------------------------------------

print(string_sample.count("o"))       # number of occurrences
print(string_sample.find("world"))    # index of first occurrence
print(string_sample.find("python"))   # -1 if not found


# --------------------------------------------
# Useful checks
# --------------------------------------------

print("123".isdigit())                # True
print("abc".isalpha())                # True
print("abc123".isalnum())             # True
print(" ".isspace())                  # True
