# Data Structures Practice

# ── Lists ──────────────────────────────────────────────────────────────────────
print("=== LISTS ===")
fruits = ["apple", "banana", "cherry"]
print("Original:", fruits)

fruits.append("date")
print("After append:", fruits)

fruits.insert(1, "avocado")
print("After insert at index 1:", fruits)

fruits.remove("banana")
print("After remove 'banana':", fruits)

popped = fruits.pop()
print(f"Popped '{popped}', list is now:", fruits)

print("Slice [1:3]:", fruits[1:3])
print("Reversed:", fruits[::-1])
print("Length:", len(fruits))

# List comprehension
squares = [x ** 2 for x in range(1, 6)]
print("Squares:", squares)

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Even squares:", even_squares)

# ── Tuples ─────────────────────────────────────────────────────────────────────
print("\n=== TUPLES ===")
coordinates = (10.5, 20.3)
x, y = coordinates           # tuple unpacking
print(f"x={x}, y={y}")

rgb = (255, 128, 0)
print("Red channel:", rgb[0])
print("Tuple is immutable – cannot change values")

# ── Sets ───────────────────────────────────────────────────────────────────────
print("\n=== SETS ===")
colors = {"red", "green", "blue", "red", "green"}
print("Set (unique values):", colors)

colors.add("yellow")
print("After add:", colors)

colors.discard("green")
print("After discard 'green':", colors)

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (a-b):", set_a - set_b)

# ── Dictionaries ───────────────────────────────────────────────────────────────
print("\n=== DICTIONARIES ===")
person = {
    "name": "Abdullah",
    "age": 25,
    "city": "Lahore"
}
print("Dictionary:", person)
print("Name:", person["name"])
print("Age (via .get):", person.get("age"))
print("Country (default):", person.get("country", "Pakistan"))

person["email"] = "abdullah@example.com"
print("After adding email:", person)

person.pop("city")
print("After removing 'city':", person)

print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

# Dict comprehension
word_lengths = {word: len(word) for word in ["apple", "banana", "cherry"]}
print("Word lengths:", word_lengths)
