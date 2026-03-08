# Functions Practice

# Basic function
def greet(name):
    return f"Hello, {name}!"

print(greet("Abdullah"))

# Default parameter
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Virk"))
print(greet_with_title("Smith", "Dr."))

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 5, 7])
print(f"Min: {low}, Max: {high}")

# *args – variable number of positional arguments
def add_all(*args):
    return sum(args)

print("Sum:", add_all(1, 2, 3, 4, 5))

# **kwargs – variable number of keyword arguments
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Person info:")
show_info(name="Abdullah", age=25, city="Lahore")

# Lambda function
square = lambda x: x ** 2
print("Square of 7:", square(7))

# Using lambda with built-in functions
numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = sorted(numbers)
print("Sorted:", sorted_numbers)

words = ["banana", "apple", "cherry", "date"]
words_by_length = sorted(words, key=lambda w: len(w))
print("Sorted by length:", words_by_length)

# Recursive function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("5! =", factorial(5))

# Function with type hints (Python 3.5+)
def multiply(a: float, b: float) -> float:
    return a * b

print("3.5 x 2 =", multiply(3.5, 2))
