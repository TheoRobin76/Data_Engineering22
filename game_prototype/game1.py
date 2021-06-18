# Slug Knights
# Win draw lose
#
#
#
#
import random as rand

print(
    """
    -----------------------
        SLUG KNIGHTS
    -----------------------
    """
)

attack_options = (
    "Your attack choices are:\n[1] Strike\n[2] Parry\n[3] Block\n[4] Heal"
)

class Character:
    def __init__(self, name, slime=10, health=100):
        self.name = name
        self.slime = slime
        self.health = health

    def __repr__(self):
        return f"Character({self.name}, {self.slime}, {self.health}"

    def take_damage(self, dmg):
        self.health = self.health - dmg

    def strike(self):
        print(f"{self.name} has damaged the Snail!")
        self.slime -= 4
        return 30

    def parry(self):
        print(f"{self.name} has parried the Snail's attack!")
        self.slime -= 3
        return 40

    def block(self):
        print(f"{self.name} has blocked the Snail's attack!")
        self.slime -= 2
        return 30

    def heal(self):
        self.slime -= 3
        self.health += 30

def attacks(p1_choice, comp_choice):
    choice = {1: "Strike", 2: "Parry", 3: "Block", 4: "Heal"}

    if p1_choice == 1:
        player1.strike()
        if comp_choice == 3:
            computer.block()
        elif comp_choice == 2:
            computer.parry()
            player1.take_damage(40)
        else:
            computer.take_damage(30)

    if comp_choice == 1:
        if player_choice == 3:
            player1.block()
        elif player_choice == 2:
            player1.parry()
            computer.take_damage(40)
        else:
            player1.take_damage(30)

    if p1_choice == 4:
        player1.Heal()

    if comp_choice == 4:
        computer.Heal()

player_name = input("What is your slug's name?  ")
player1 = Character(player_name)
computer = Character("Snail")

run = True

while run:
    if player1.slime <= 10:
        player1.slime += 2
        if player1.slime > 10:
            player1.slime = 10
    print(attack_options)
    player_move = input(f"What will you do, {player_name.title()}?  ")


    computer_choice = rand.randint(1, 4)
    if computer.health <= 0:
        run = False
        print("You are victorious! You have earned your shell")

    if player1.health <= 0:
        run = False
        print("SPLAT! Unfortunately you have perished...")