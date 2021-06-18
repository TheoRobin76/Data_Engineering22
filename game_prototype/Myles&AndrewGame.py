from random import randrange
from sys import exit

class Adventurer:
    def __init__(self, name, level=1, attack=5, health=10, mana=5, coins=0):
        self.name = name
        self.level = level
        self.attack = attack
        self.health = health
        self.mana = mana
        self.coins = coins

class Mage(Adventurer):
    def __init__(self, mana=10):
        self.mana = mana

class Warrior(Adventurer):
    def __init__(self, health=20):
        self.health = health

class Knight(Adventurer):
    def __init__(self, attack=10):
        self.attack = attack

class Enemy:
    def __init__(self, level=1, health=5, attack=2):
        self.level = level
        self.health = health
        self.attack = attack

new_game_prompt = input("Would you like to start a new game? y or n? ")
while new_game_prompt != "y" or "n":
    if new_game_prompt == "y":
        player = Adventurer(input("And when tales are told of you, what name shall they sing praise of? "))
        break
    elif new_game_prompt == "n":
        exit(0)
    else:
        print("I'm sorry, I didn't understand your input! Please try again!")
        new_game_prompt = input("Would you like to start a new game? y or n? ")
print("You enter the small village of Upper Fuffner-Figgle, famed for it's prize winning peach cheese. The township have clearly tired of the burden of guiding a seemingly endless queue of keen young adventurers waiting behind a small red rope at the boundary of the village. The nearby yokel posing like a bouncer to a city's most popular nightclub leers at you and ushers you in. They follow a well trodden path inundated with a number of crooked wooden signs accompanying it's full length. The path is met by the foot of a nearby rocky cliff face where a large red panelled door confronts you. You hand off the stub of your 'admit one' ticket and head inside.")
encounter_enemy = Enemy(randrange(player.level, player.level + 2, 1))
encounter = input("You encounter a level {} goblin. Will you fight or flee? ".format(encounter_enemy.level))

if encounter == "fight":
    if encounter_enemy.level > player.level:
        print(f"You valiantly attempt to slay the goblin, but as you step forwards to attack, a stray pebble trips you up and you impale yourself on your sword. Better luck next time BRAVE {player.name}!")
        exit(0)
    else:
        print("You heroically defeat the goblin. Continue through to the next area.")
        player.level += 1
        print(f"Congratulations, you have levelled up. You are now level {player.level}. Enjoy a strong tankard of Mead.")
elif encounter == "flee":
    print("You bravely run away, making sure to grab a t-shirt emblazoned with the logo 'Battle Dungeon: Re-Live the days of old!' on your way out.")
    exit(0)
else:
    print("I'm sorry, I didn't understand your input!")
    encounter = input(f"You encounter a level {enemy_level} goblin. Will you fight or flee? ")
