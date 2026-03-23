# Variables and Data Types Practice

# Integer
age = 25
print("Age:", age, "| Type:", type(age))

# Float
height = 5.9
print("Height:", height, "| Type:", type(height))

# String
name = "Abdullah"
print("Name:", name, "| Type:", type(name))

# Boolean
is_student = True
print("Is Student:", is_student, "| Type:", type(is_student))

# None
address = None
print("Address:", address, "| Type:", type(address))

# String operations
greeting = "Hello, " + name + "!"
print(greeting)
print("Name in uppercase:", name.upper())
print("Name length:", len(name))
print("Name repeated:", name * 2)

# Type conversion
num_str = "42"
num_int = int(num_str)
print("Converted string to int:", num_int, "| Type:", type(num_int))

pi = 3.14159
print("Pi rounded to 2 decimal places:", round(pi, 2))

# f-strings (formatted strings)
print(f"My name is {name} and I am {age} years old.")
