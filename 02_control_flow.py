# Control Flow Practice

# if / elif / else
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")

# Ternary (one-line if/else)
status = "Pass" if score >= 50 else "Fail"
print("Status:", status)

# for loop with range
print("\nCounting 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# for loop with a list
fruits = ["apple", "banana", "cherry", "date"]
print("\nFruits:")
for fruit in fruits:
    print("-", fruit)

# for loop with enumerate
print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# while loop
print("\nWhile loop countdown:")
count = 5
while count > 0:
    print(count, end=" ")
    count -= 1
print("Go!")

# break and continue
print("\nNumbers 1-10, skipping multiples of 3, stopping at 8:")
for n in range(1, 11):
    if n % 3 == 0:
        continue
    if n > 8:
        break
    print(n, end=" ")
print()

# Nested loops
print("\nMultiplication table (1-3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()
