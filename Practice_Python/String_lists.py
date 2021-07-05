word = input("Please enter a word and I will tell you if it is a palindrome: ")
if word == word[::-1]:
    print(f"Congratulations, {word} is a palindrome")
else:
    print(f"My Condolences, {word} is not a palindrome")
