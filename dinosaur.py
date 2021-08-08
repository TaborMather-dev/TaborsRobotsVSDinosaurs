class Dinosaur:


    def __init__(self, name, strength, defense, health):
        self.name = name
        self.strength = strength
        self.defense = defense
        self.health = health

    def dino_name(self):
        self.name = input("Enter your dino's name.")
        print(self.name)