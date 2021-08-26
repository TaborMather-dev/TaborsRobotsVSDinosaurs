from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def start_game(self):
        self.display_welcome_msg()
        self.battle()
        self.display_winners()

    def display_welcome_msg(self):
        print(f"Welcome to Robots vs. Dinosaurs!")

    def battle(self):
        while len(self.herd.dinosaur_list) > 0 and len(self.fleet.robot_list) > 0:
            self.robot_turn()
            self.dinosaur_turn()

    def dinosaur_turn(self):
        self.show_robot_opponent_options()
        robot_choice = int(input("Choose which dinosaur will attack."))
        self.show_dinosaur_opponent_options()
        dinosaur_choice = int(input("Choose which robot will defend."))
        self.fleet.robot_list[robot_choice].attack(
            self.herd.dinosaur_list[dinosaur_choice])
        if self.herd.dinosaur_list[dinosaur_choice].health <= 0:
            self.herd.dinosaur_list.remove(
                self.herd.dinosaur_list[dinosaur_choice])

    def robot_turn(self):
        self.show_robot_opponent_options()
        robot_choice = int(input("Choose which robot will attack."))
        self.show_dinosaur_opponent_options()
        dinosaur_choice = int(input("Choose which dinosaur will defend."))
        self.fleet.robot_list[robot_choice].attack(
            self.herd.dinosaur_list[dinosaur_choice])
        if self.herd.dinosaur_list[dinosaur_choice].health <= 0:
            self.herd.dinosaur_list.remove(
                self.herd.dinosaur_list[dinosaur_choice])

    def show_dinosaur_opponent_options(self):
        print("Choose your dinosaur.")
        index = 0
        for dinosaur in self.herd.dinosaur_list:
            print(
                f"Press {index}  for {dinosaur.name} with {dinosaur.health}!")
            index += 1

    def show_robot_opponent_options(self):
        print("Choose your robot.")
        index = 0
        for robot in self.fleet.robot_list:
            print(f"Press {index}  for {robot.name} with {robot.health}!")
            index += 1

    def display_winners(self):
        if len(self.fleet.robot_list) > len(self.herd.dinosaur_list):
            print("Robots Win!")
        else:
            print("Dinosaurs Win!")
