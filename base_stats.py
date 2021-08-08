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