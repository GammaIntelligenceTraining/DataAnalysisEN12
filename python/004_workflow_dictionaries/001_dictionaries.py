# ============================================
# Python: Dictionaries — Realistic Example
# ============================================

# Dictionary = structured data (like a real object)

student = {
    "name": "John",
    "age": 20,
    "email": "john@example.com",
    "courses": ["Math", "Programming", "Art"],
    "active": True,
}

print(student)


# --------------------------------------------
# Accessing values
# --------------------------------------------

print(student["name"])
print(student["courses"])


# --------------------------------------------
# Safe access with get()
# --------------------------------------------

print(student.get("email"))
print(student.get("phone"))                 # None
print(student.get("phone", "Not provided"))


# --------------------------------------------
# Adding and updating values
# --------------------------------------------

student["phone"] = "555-1234"
student["age"] = 21

student.update({
    "email": "john.doe@example.com",
    "active": False,
})

print(student)


# --------------------------------------------
# Removing values
# --------------------------------------------

removed_phone = student.pop("phone")
print("Removed phone:", removed_phone)
print(student)


# --------------------------------------------
# Dictionary information
# --------------------------------------------

print(len(student))
print(student.keys())
print(student.values())
print(student.items())


# --------------------------------------------
# Looping through dictionary
# --------------------------------------------

for key in student:
    print(key)

for key, value in student.items():
    print(key, "→", value)