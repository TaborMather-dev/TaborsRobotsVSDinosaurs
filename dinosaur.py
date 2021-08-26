from weapon import Weapon


class Dinosaur:

    def __init__(self, name):
        self.name = name
        self.health = 10
        self.weapon = Weapon('Teeth', 3)

    def bite(self, robot):
        robot.health = robot.health - self.attack_power
        print(f"Hit! Robot health is now {robot.health}")
