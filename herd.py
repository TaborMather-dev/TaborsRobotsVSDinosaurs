from dinosaur import Dinosaur


class Herd:

    def __init__(self):
        self.dinosaur_list = []
        self.create_dinosaurs()

    def create_dinosaurs(self):
        dinosaur1 = Dinosaur('Little Foot')
        dinosaur2 = Dinosaur('Petrie')
        dinosaur3 = Dinosaur('Sarah')
        self.dinosaur_list.append(dinosaur1)
        self.dinosaur_list.append(dinosaur2)
        self.dinosaur_list.append(dinosaur3)
