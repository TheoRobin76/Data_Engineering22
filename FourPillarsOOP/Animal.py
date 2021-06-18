class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("Delicious")

    def procreate(self):
        print("time to find a mate")

    def move(self):
        print("onwards and upwards")

cat = Animal()
cat.breathe() # this is abstraction. we don't type in the whole code. we just type .breathe()
