# x = 0
#
# while x < 10:
#     print(f"It's working -> {x}")
#     if x == 4:
#         break
#     x += 1

user_bool = True

while user_bool:
    age = input("What is your age? ")
    if age.isdigit() and 0 < int(age) < 130:
        user_bool = False
        print("Thanks for providing your age")
    else:
        print("Please enter a number")

