# 1. Your first question:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.  Find the sum of all the multiples of 3 or 5 below 1000.

# count = 0
# total_count = 0
#
# while count < 1000:
#     if count % 5 == 0:
#         total_count += count
#     elif count % 3 == 0:
#         total_count += count
#     count += 1
#
# print(f"The sum of all the multiples of 3 and 5 below 1000 is {total_count}")
#

# 2. Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
#

# smaller_num = 0
# larger_num = 1
# total = 0
#
# while larger_num <= 4000000:
#     if larger_num % 2 == 0:
#         total += larger_num
#     temp_num = larger_num
#     larger_num = larger_num + smaller_num
#     smaller_num = temp_num
#
# print(f"The sum of all the even-numbered values in the Fibonacci sequence is {total}")

# 3. Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

# import random
# correct_number = random.randint(1,9)
# guess_counter = 1
# guesses = []
# print(correct_number)
#
# guess = int(input("Welcome to hell, to escape you must guess what number I am thinking between 1 and 9:  "))
# while guess != correct_number:
#     if guess < correct_number:
#         guess = int(input("Too low! Guess again! "))
#         guesses.append(guess)
#         guess_counter += 1
#     elif guess > correct_number:
#         guess = int(input("Too high! Guess again! "))
#         guesses.append(guess)
#         guess_counter += 1
# if guess == correct_number:
#     print("Congratulations, here is a certificate, please show this to Hades and he will let you go")
#     print(f"You guessed {guess_counter} times")
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# p = 600851475143 #our prime number
# n = 2 #our potential factor
#
# while n * n < p:
#     while p % n == 0:
#         p = p / n
#     n = n + 1
# print(p)
#
# The sum of the squares of the first ten natural numbers is,
# 12+22+...+102=385
#
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)2=552=3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
#
# haystack = ["hat", "needle"]
# def find_needle(haystack):
#     index = haystack.index("needle")
#     print(f"found the needle at poition {index}")
# find_needle(haystack)