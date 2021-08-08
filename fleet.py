from weapons import Sword
from robot import Robot


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

    def create_weapons(self):
        Longsword1 = Sword()
        Longsword2 = Sword()
        Longsword3 = Sword()
        self.weapon_list.append(Longsword1)
        self.weapon_list.append(Longsword2)
        self.weapon_list.append(Longsword3)
