from Animal import Animal # importing functionality from Animal file

class Reptile(Animal): # inheritance

    def __init__(self):
        super().__init__() # keyword relating to parent class. calling init function of animal class
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's chilly, where is he sun at?")

    def hunt(self):
        print("Wait for it.... wait for it... pounce")

    def use_venom(self):
        print("If i have it, i am going to use it")

    def attract_mate_through_scent(self):
        print("Time to throw on the parfum")

Jeremy_the_reptile = Reptile() # members of the sub-class can use super-class methods too

sue_the_animal = Animal() # members of the super-class cannot access methods of the sub-class



