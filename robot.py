from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.weapon = Weapon('Sword', 3)

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
        print(f"Hit! Dinosaur health is now { dinosaur.health } ")
