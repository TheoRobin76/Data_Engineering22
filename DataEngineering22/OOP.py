# # class Dog:
# #     # Class attribute
# #     species = "Canis familiaris"
# #
# #     # Instance attributes
# #     def __init__(self, name, age, cuteness_factor):
# #         self.name = name
# #         self.age = age
# #         self.cuteness_factor = cuteness_factor
# #
# #     # Instance method
# #     def __str__(self):
# #         return (f"{self.name} is {self.age} years old with a cuteness factor of {self.cuteness_factor}")
#
#
# #
# # # Instantiating
# # Myles = Dog("Myles", 9, 4)
# # Oscar = Dog("Oscar", 2, 1000)
# #
# # print(Myles)
#
# #
# # class Dog:
# #
# #     animal_kind = "Dolphin" # class_variable
# #
# #     def bark(self): # method
# #       return "woof"
# #
# # Myles = Dog()
# # Oscar = Dog()
# #
# # print(type(Myles))
# # print(type(Oscar))
# # print(Myles.animal_kind)
# # print(Oscar.animal_kind)
# #
# # Oscar.animal_kind = "Big Dog"
# # print(Myles.animal_kind)
# # print(Oscar.animal_kind)
# # print(Myles.bark())
# # print(Oscar.bark())
#
#
# # class Dog:
# #
# #     def __init__(self, name, colour):
# #         self.animal_kind = "canine"
# #         self.name = name
# #         self.colour = colour
# #         self.bark()
# #
# #
# #     def bark(self): # method
# #       return "woof"
# #
# # Amy = Dog("Amy", "Golden")
# # print(Amy.name)
# # print(Amy.colour)
# #

# class Car:
#     def __init__(self, max_speed, fuel_econ, max_fuel):
#         self.wheels = 4
#         self.speed = 0
#         self.max_speed = max_speed
#         self.fuel_econ = fuel_econ
#         self.max_fuel = max_fuel
#         self.fuel_level = 10
#
#     def Accelerate(self, speed_increase):
#         print("Vroom Vroom")
#         if self.speed + speed_increase > self.max_speed:
#             self.speed = self.max_speed
#         else:
#             self.speed += speed_increase
#
#     def Deccelerate(self, speed_decrease):
#         print("Cat in the road!")
#         if self.speed - speed_decrease > 0:
#             self.speed -= speed_decrease
#         else:
#             self.speed = 0
#
#     def FillTank(self, amount_filled):
#         print("Please refuel, I don't want to break down again")
#         if self.fuel_level + amount_filled > self.max_fuel:
#             self.fuel_level = self.max_fuel
#         else:
#             self.fuel_level += self.fuel_level
#
#
# lambo = Car(250, 10, 80)
# fiat500 = Car(110, 40, 35)
#
# lambo.Accelerate(300)
# print(lambo.speed)
#
# fiat500.Accelerate(300)
# print(fiat500.speed)
#
# lambo.Deccelerate(200)
# print(lambo.speed)
# #
# def century(year):
#     return math.ceil(year/100)
#
# print(century(1980))

# def reverse_seq(n):
#     reverse = list(range(1, n+1))
#     return reverse[::-1]
#
# print(reverse_seq(5))

# class Car:
#     wheels = 4
#     def __init__(self, max_speed, mileage, model, colour):
#         self.max_speed = max_speed
#         self.mileage = mileage  # miles per gallon
#         self.model = model
#         self.colour = colour
#         self.fuel_tank_size = 12  # gallons of fuel
#         self.fuel_level = 0
#         self.speed = 0
#     def description(self):
#         print(f"This car is a {self.colour} {self.model} with a maximum speed of {self.max_speed} mph")
#     def fuel_up(self):
#         self.fuel_level = self.fuel_tank_size
#         print("Fuel tank is now full.")
#     def drive(self):
#         print(f"The {self.model} is now driving")
#     def refuel(self):
#         print("Fuel is currently £5 a gallon.")
#         new_level = int(input("How many gallons would you like to refuel? "))
#         while self.fuel_tank_size - self.fuel_level <= new_level:
#             print(f"Exceeded capacity, please enter an amount lower than {self.fuel_tank_size - self.fuel_level}.")
#             new_level = int(input("How many gallons would you like to refuel? "))
#         else:
#             self.fuel_level += new_level
#             print(f"This is going to cost £{5*new_level}")
#     def distance_to_travel(self):  # max distance a car can travel with amount of fuel
#         print(f"The maximum distance you can travel is {self.mileage * self.fuel_level}")
#     def acceleration(self, speed_increase):
#         if self.speed + speed_increase > self.max_speed:
#             self.speed = self.max_speed
#             print(self.speed)
#         else:
#             self.speed += speed_increase
#             print(self.speed)
#
# Ford = Car(120, 40, "Fiesta", "Red")

# def reverse_seq(n):
#     reverse = list(range(1, n+1))
#     return reverse[::-1]



