from time import sleep
from Player import Player
from random import randint
from Dogs import dogs
from Ladders import ladders

# args and kwargs
# 2 players for now
# roll even = dog, odd = ladder
# dog and ladder is fixed number

num_players = 2
player1 = Player(input("What is your name?! "))
player2 = Player(input("What is your name?! "))

if player1 == "Jerry Seinfeld":
    bee = [x for x in open("bee.txt", "r").readlines()]
    for row in bee:
        print(row)

def dice_roll():
    return randint(1,6)

turn = 0
counter1 = 0
counter2 = 0

while (counter1 < 100 and counter2 < 100):
    if turn == 0:
        select = input(f"{player1.name}, virtual please virtually roll the virtual dice, virtually, and don't call me Virgil: y/n  " )
        if select == "y":
            diceroll = dice_roll()
            print(f"{player1.name}, congratulations, you have successfully rolled a {diceroll}, I am proud of you")
            counter1 += diceroll
            print(f"You have taken a leisurely stroll to counter {counter1}")
            if counter1 in dogs:
                counter1 = dogs.get(counter1)
                print(f"Oh no you have been viciously mauled by a stray poodle. The poodle sensed your fear and as the tears rushed down your cheek you ran back to counter {counter1}")
            elif counter1 in ladders:
                counter1 = ladders.get(counter1)
                print(f"Fantastic! Your dreams have come true on this day. You have been handed the lifeline of a lifetime in the form of a beautiful and elegant ladder, it's beauty matched only by its grace. As the tears of joy parade down your cheek you ascend to {counter1}")
            turn = 1
        else:
            print("Stop virtually wasting our time, you have been fined $30")
            continue

    if turn == 1:
        select = input(f"{player2.name}, virtual please virtually roll the virtual dice, virtually, and don't call me Shirley: y/n  ")
        if select == "y":
            diceroll = dice_roll()
            print(f"{player2.name}, congratulations, you have successfully rolled a {diceroll}, I am proud of you")
            counter2 += diceroll
            print(f"You have stumbled aimlessly to counter {counter2}")
            if counter2 in dogs:
                counter2 = dogs.get(counter2)
                print(f"Oh no you have been viciously mauled by a stray poodle. The poodle sensed your fear and as the tears rushed down your cheek you ran back to counter {counter2}")
            elif counter2 in ladders:
                counter2 = ladders.get(counter2)
                print(f"Fantastic! Your dreams have come true on this day. You have been handed the lifeline of a lifetime in the form of a beautiful and elegant ladder, it's beauty matched only by its grace. As the tears of joy parade down your cheek you ascend to counter {counter2}")
            turn = 0
        else:
            print("Stop virtually wasting our time, you have been fined $30")
            continue

if counter1 >= 100:
    print(f"{player1.name} you win! Now go wash the dishes you silly gerblerdlop.")
if counter2 >= 100:
    print(f"{player2.name} you win! Now go wash the dishes you silly gerblerdlop.")









