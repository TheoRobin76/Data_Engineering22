from random import randrange

rand_number = randrange(1, 10)
# print(f"Random number is {rand_number}")

guess = int(input("Please guess the random number between 1 and 9: "))

guess_counter = 1
while guess != rand_number:
    if guess < rand_number:
        guess = int(input(f"{guess} is too low, please guess again: "))
        guess_counter += 1
    elif guess > rand_number:
        guess = int(input(f"{guess} is too high, please guess again: "))
        guess_counter += 1
print(f"Congratulations, {guess} is the correct number!")
print(f"You needed {guess_counter} guesses")


