# n = 0.00483472
#
# print(f"Fixed point: {n:f}")
# print(f"Exponential Notation: {n:e}")

class Dog:

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age*7} year old dog in dog_years"
        else:
            return self.__str__()

Rover = Dog(5)
print(f"{Rover}")
print(f"{Rover:dog}")