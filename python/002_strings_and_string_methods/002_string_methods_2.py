# ============================================
# Python: String Concatenation & Formatting
# ============================================

a = "Hello"
b = "World"

# --------------------------------------------
# String concatenation (+)
# --------------------------------------------
# + joins strings together

print(a + b)            # HelloWorld
print(a + " " + b)      # Hello World

# + works ONLY with strings
# print(a + 5)          # ❌ error


# --------------------------------------------
# print() with commas
# --------------------------------------------
# print() can separate values with commas
# A space is added automatically

print("First word is", a)

# Using + requires manual spacing and conversion
print("First word is " + a + ".")


# --------------------------------------------
# format() — basic formatting
# --------------------------------------------

salary = 1000
template = "John's salary is {} euros"
print(template.format(salary))


# --------------------------------------------
# format() — multiple values
# --------------------------------------------

apples = 3
bananas = 5
pears = 2

fruit_template = "John has {} bananas, {} apples and {} pears"
print(fruit_template.format(bananas, apples, pears))


# --------------------------------------------
# format() — indexed placeholders
# --------------------------------------------

fruit_template_indexed = "John has {1} bananas, {0} apples and {2} pears"
print(fruit_template_indexed.format(apples, bananas, pears))


# --------------------------------------------
# format() — named placeholders
# --------------------------------------------

price_template = "This {product} costs {price:.2f} euros"
print(price_template.format(product="computer", price=350))


# --------------------------------------------
# Old-style formatting (%) — legacy
# --------------------------------------------
# You may see this in older Python code
# Not recommended for new code

x = 12231.3456789
y = 131.1314

print("The value of x is %.4f" % x)
print("The value of y is %.2f" % y)

emp_name = "John"
emp_age = 30
emp_salary = 1500

emp_string = (
    "Hi, my name is %(name)s! "
    "I am %(age)s old. "
    "My salary is %(salary).2f"
    % {"name": emp_name, "age": emp_age, "salary": emp_salary}
)
print(emp_string)


# --------------------------------------------
# f-strings — modern & recommended (Python 3.6+)
# --------------------------------------------
# Clear, fast, readable — USE THIS

emp_string_f = (
    f"Hi, my name is {emp_name}! "
    f"I am {emp_age} old. "
    f"My salary is {emp_salary:.2f}"
)
print(emp_string_f)


# --------------------------------------------
# Bytes and decoding
# --------------------------------------------
# Bytes represent raw binary data

byte_string = b"\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82"
print(byte_string)

# Convert bytes to string using encoding
print(byte_string.decode("utf-16"))
