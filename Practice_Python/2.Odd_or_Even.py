# number = int(input("Please enter a number: "))
# if number % 4 == 0:
#     print(f"{number} is a multiple of 4")
# elif number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")

num = int(input("Please enter a number: "))
check = int(input("Please enter another number: "))

if num % check == 0:
    print(f"Congratulations! {num} divides evenly by {check}")
else:
    print(f"Condolences, {num} doesn't divide evenly by {check}")


