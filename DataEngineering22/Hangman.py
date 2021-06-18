# # print("Welcome to Hangman: Your Worst Nightmare")
# # word = input("Player 1, please choose a wonderful word: ")
# # guesses = []
# # turns = 12
# #
# # while turns > 0:
# #     guess = input("Player 2, Guess a character: ")
# #     guesses += guess
# #     failed = 0
# #     for char in word:
# #         if char in guesses:
# #             print(char)
# #         else:
# #             print("_")
# #             failed += 1
# #     if failed == 0:
# #         print("You won")
# #         break
# #     if guess not in word:
# #         turns -= 1
# #         print("Wrong")
# #         print(f"You have {turns} more guesses")
# #     if turns == 0:
# #         print("You Lose... time for the eternal slumber")
#
# # user inputs word
# # hidden word is generated "_____"
# # whilst the user has lives left,
#     # guess a letter
#     # if letter is in word and has not been guessed before,
#         # then reveal the letter "_e___"
#     # else if letter not in word, then take away a life
#
# word_to_guess = input("Please pick a word to guess...")
# wrong_counter = 0
# max_lives = 10
# previous_letters = []
# hidden_word = ""
# for letter in word_to_guess: # generates underscore hidden word
#     hidden_word = hidden_word + "_"
# print(hidden_word)
#
# def reveal_letter(letter_picked, word_to_guess, underscore_word):
#     counter = 0
#     underscore_word_list = list(underscore_word)
#     # for letter in word_to_guess:
#         if letter == letter_picked:
#             underscore_word_list[counter] = letter_picked
#         counter += 1
#     return ''.join(underscore_word_list)
#
# while wrong_counter <= max_lives and not hidden_word.isalpha(): # whilst the user has lives left
#     guessed_letter = input("Please guess a letter...")
#     if guessed_letter in previous_letters: # letter already picked
#         print("Silly, you have already guessed this letter...")
#         wrong_counter += 1
#     elif guessed_letter in word_to_guess: # user picked letter in word
#         print("correct")
#         hidden_word = reveal_letter(guessed_letter, word_to_guess, hidden_word)
#         print(hidden_word)
#         previous_letters.append(guessed_letter)
#     else: # user picks letter not in word
#         wrong_counter += 1
#         previous_letters.append(guessed_letter)
#         print("This letter was not in the word, try again...")

import random

def function_guesses(guesses_no, wrong_x):
    print('Incorrect')
    guesses_no = guesses_no - 1
    print(wrong_x)
    print(f'You now have {guesses_no} guesses')
    print(' '.join(hidden_word))

hangman_dict = {
6 : "___________\n|      |\n|      O\n|     \n|      \n|     \n|_____________\n",
5 : "___________\n|      |\n|      O\n|      |\n|      |\n|     \n|_____________\n",
4 : "___________\n|      |\n|      O\n|      |/\n|      |\n|     \n|_____________\n",
3 : "___________\n|      |\n|      O\n|     \\|/\n|      |\n|     \n|_____________\n",
2 : "___________\n|      |\n|      O\n|     \\|/\n|      |\n|     / \n|_____________\n",
1 : "___________\n|      |\n|      O\n|     \\|/\n|      |\n|     / \\\n|_____________\n   YOU LOSE!"}
# index is number of guesses left, value is what outputs if that quess is incorrect

#word_guess = list(input('Please choose a word to guess: ').lower())

word_list = ['fart', 'crisps', 'salad', 'horses', 'imagination', 'forest', 'lunar', 'miles'
             'saxophone', 'liberty', 'sandwich']
word_guess = list(random.choice(word_list)) # chooses random word to guess
guesses = 6
# assigns number of guesses

print("Let's play Hangman!" )
print('You have 6 guesses')
hidden_word =list('_'* len(word_guess)) # creates hidden word with # of _ = to length of word to guess as a list
print(' '.join(hidden_word)) # displays hidden word

while hidden_word != word_guess:
    letter_guess = input('Please enter a letter to guess: ').lower()
    if letter_guess in word_guess:
        counter = 0
        for letter in word_guess:
            if letter == letter_guess:
                hidden_word[counter] = letter_guess
            counter +=1
        print('Correct')
        print(f'You still have {guesses} guesses')
        print(' '.join(hidden_word))

    elif guesses == 1:
        print('You have run out of guesses')
        print(hangman_dict[guesses])
        print('Your word was,')
        print(' '.join(word_guess))
        break
    else:
        function_guesses(guesses, hangman_dict[guesses])
        guesses = guesses - 1
else:
    print('Congratulations, you win!')