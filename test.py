from weakref import WeakKeyDictionary
import random


class BaseStat(int):

    def __str__(self):
        if self == 0:
            return "normal"
        else:
            return "good"


class BaseStatField(object):

    def __init__(self):
        self.default = 0
        self.values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.values.get(instance, self.default)

    def __set__(self, instance, value):
        if value < 0 or value > 1:
            raise ValueError("BaseStat must be either 0 or 1.")
        self.values[instance] = BaseStat(value)

    def __delete__(self, instance):
        del self.values[instance]


class Health(int):

    def __str__(self):
        if self == 2:
            return "healthy"
        elif self == 1:
            return "wounded"
        else:
            return "dead"


class HealthField(object):

    def __init__(self):
        self.default = 2
        self.values = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.values.get(instance, self.default)

    def __set__(self, instance, value):
        if value not in (0, 1, 2):
            raise ValueError("Health must be either 0, 1 or 2.")
        self.values[instance] = Health(value)

    def __delete__(self, instance):
        del self.values[instance]


class Character():
    health = HealthField()

    endurance = BaseStatField()
    accuracy = BaseStatField()
    reaction = BaseStatField()
    luck = BaseStatField()

    stats = ["health", "endurance", "accuracy", "reaction", "luck"]

    def __init__(self, name, health, endurance, accuracy, reaction, luck):
        self.name = name
        self.health = health

        self.endurance = endurance
        self.accuracy = accuracy
        self.reaction = reaction
        self.luck = luck

    def print_stats(self):
        print(self.name)
        print("-----------------")
        for stat in self.stats:
            print("{} is {}.".format(stat, getattr(self, stat)))


class Attack(object):

    def __init__(self, attacker, target, distance):
        self.attacker = attacker
        self.target = target
        self.distance = distance

    @property
    def hit_chance(self):
        return 0.5 + (self.attacker.accuracy * 0.25) - (self.distance * 0.025) + (self.attacker.luck * 0.2) - (self.target.luck * 0.2)

    @property
    def wound_chance(self):
        return 0.75 - (self.target.endurance * 0.25)

    @property
    def death_chance(self):
        return 1 - (self.target.endurance * 0.25) - (self.target.health * 0.25)

    def execute(self):
        if random.random() <= self.hit_chance:
            print("{} hits {}.".format(self.attacker.name, self.target.name))
            print("Death chance is {}".format(self.death_chance))
            if random.random() < self.death_chance:
                self.target.health = 0
                print("{} dies.".format(self.target.name))
            elif random.random() < self.wound_chance:
                self.target.health = 1
                print("{} is wounded.".format(self.target.name))
            else:
                print("{} is not damaged by the attack.".format(self.target.name))
        else:
            print("{} misses.".format(self.attacker.name))


class Duel(object):
    turn_number = 1

    def __init__(self, actor1, actor2, distance):
        self.actors = [actor1, actor2]
        self.distance = distance

    @property
    def initiative(self):
        return 0.5 + (self.actors[0].reaction * 0.25) - (self.actors[1].reaction * 0.25) + (self.actors[0].luck * 0.25) - (self.actors[1].luck * 0.25)

    def start(self):
        print("Duel starts.")
        if random.random() >= self.initiative:
            print("{} failed to attack first.".format(self.actors[0].name))
            self.swap()
        print("\n")
        self.make_turn()

    def swap(self):
        temp = self.actors[0]
        self.actors[0] = self.actors[1]
        self.actors[1] = temp

    def make_turn(self):
        print("Turn {}".format(self.turn_number))
        attack = Attack(self.actors[0], self.actors[1], self.distance)
        attack.execute()
        if all(a.health > 0 for a in self.actors):
            print("\n")
            self.swap()
            self.turn_number += 1
            self.make_turn()
        else:
            print("Duel finished in {} turns.".format(self.turn_number))
            print("\n")


player = Character("Player", 2, 1, 1, 1, 1)
enemy = Character("Enemy", 2, 1, 1, 1, 1)


Duel(player, enemy, 0).start()