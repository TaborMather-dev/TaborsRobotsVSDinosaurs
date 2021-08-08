class Robot:


    def __init__(self):
        self.name = ""
        self.Health = 10
        self.Defense = 10
        self.Attack = 10
        self.robot_name = ()

    def robot_name(self):
        self.name = input("Enter your dinosaur's name.")
        print("Dinosar's name", (self.name))
    