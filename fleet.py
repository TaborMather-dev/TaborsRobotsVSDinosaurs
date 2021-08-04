from weapons import Weapon
from robots import Robot


class Fleet:
    def __init__(self):
        self.Robot_List = []
        self.create_robots()
        self.weapon_list = []
        self.create_weapons = ()

    def create_robots(self):
        robot1 = Robot()
        robot2 = Robot()
        robot3 = Robot()
        self.Robot_List.append(robot1)
        self.Robot_List.append(robot2)
        self.Robot_List.append(robot3)