from robot import Robot


class Fleet:
    def __init__(self):

        self.robot_list = []
        self.create_robots()

    def create_robots(self):
        robot1 = Robot('Drone')
        robot2 = Robot('Automatron')
        robot3 = Robot('Android')
        self.robot_list.append(robot1)
        self.robot_list.append(robot2)
        self.robot_list.append(robot3)
