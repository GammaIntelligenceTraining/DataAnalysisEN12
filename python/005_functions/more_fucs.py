"""
Python Functions Masterclass
A comprehensive guide covering basic to advanced function concepts.
"""

# 1. Basic Function: No parameters, no return
def greet():
    """Simple greeting function."""
    print("Hello, Python Student!")

# 2. Positional Parameters & Return Value
def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# 3. Default Arguments
def describe_pet(name, animal_type="dog"):
    """Uses a default value if one isn't provided."""
    print(f"I have a {animal_type} named {name}.")

# 4. Keyword Arguments
# This allows calling functions out of order: describe_pet(animal_type="cat", name="Whiskers")

# 5. Arbitrary Positional Arguments (*args)
def make_pizza(size, *toppings):
    """Collects an arbitrary number of arguments into a tuple."""
    print(f"\nMaking a {size}-inch pizza with:")
    for topping in toppings:
        print(f"- {topping}")

# 6. Arbitrary Keyword Arguments (**kwargs)
def build_profile(first, last, **user_info):
    """Collects an arbitrary number of keyword arguments into a dictionary."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# 7. Docstrings and Type Hinting (Modern Python)
def calculate_area(radius: float) -> float:
    """
    Calculates the area of a circle.
    Uses type hints to suggest input and output types.
    """
    import math
    return math.pi * (radius ** 2)

# 8. Scope: Local vs. Global
count = 10 # Global variable

def update_count():
    global count # Accessing the global variable
    count += 5
    local_val = "I only exist inside here"
    return count

# 9. Lambda Functions (Anonymous)
# Good for short, one-time use logic
square = lambda x: x * x

# 10. Higher-Order Functions (Functions as arguments)
def apply_operation(x, y, func):
    """Takes a function as an argument and applies it."""
    return func(x, y)

# --- EXECUTION EXAMPLES ---
if __name__ == "__main__":
    greet()
    print(f"Add result: {add(5, 3)}")
    describe_pet("Buddy") # Uses default
    describe_pet("Luna", "hamster") # Overrides default
    make_pizza(12, "mushrooms", "peppers", "extra cheese")
    
    user = build_profile("Albert", "Einstein", location="Princeton", field="Physics")
    print(user)
    
    print(f"Area: {calculate_area(5.0):.2f}")
    print(f"Squared using Lambda: {square(4)}")
    print(f"Higher Order (Subtraction): {apply_operation(10, 4, lambda x, y: x - y)}")