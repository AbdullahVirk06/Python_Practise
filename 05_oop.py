# Object-Oriented Programming (OOP) Practice

# ── Basic class ────────────────────────────────────────────────────────────────
class Animal:
    # Class variable (shared by all instances)
    kingdom = "Animalia"

    def __init__(self, name, sound):
        # Instance variables
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def __str__(self):
        return f"Animal({self.name})"

    def __repr__(self):
        return f"Animal(name={self.name!r}, sound={self.sound!r})"


dog = Animal("Dog", "Woof")
cat = Animal("Cat", "Meow")

print(dog.speak())
print(cat.speak())
print("Kingdom:", Animal.kingdom)
print(str(dog))

# ── Inheritance ────────────────────────────────────────────────────────────────
class Pet(Animal):
    def __init__(self, name, sound, owner):
        super().__init__(name, sound)
        self.owner = owner

    def info(self):
        return f"{self.name} is owned by {self.owner}"


my_pet = Pet("Buddy", "Woof", "Abdullah")
print(my_pet.speak())      # inherited method
print(my_pet.info())       # new method

# ── Encapsulation (private attributes with getters/setters) ────────────────────
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance    # "private" attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    @property
    def balance(self):
        return self.__balance


account = BankAccount("Abdullah", 100)
account.deposit(50)
account.withdraw(30)
print("Balance:", account.balance)

# ── Class and static methods ───────────────────────────────────────────────────
class MathHelper:
    pi = 3.14159

    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

    @staticmethod
    def add(a, b):
        return a + b


print(f"Circle area (r=5): {MathHelper.circle_area(5):.2f}")
print("3 + 4 =", MathHelper.add(3, 4))
