import random
from binary_utils import *

class Flower:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.pollens = []


    def crossover(self, flower):
        color = crossover_bin_lists(self.color, flower.color)
        x = crossover_ints(self.x, flower.x, 7)
        y = crossover_ints(self.y, flower.y, 7)
        return Flower(color, x, y)

    def __str__(self):
        return '<✿{}rgb {}x{}y>'.format(''.join(str(val) for val in self.color), self.x, self.y)


    def __repr__(self):
        return self.__str__()
