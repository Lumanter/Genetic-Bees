import random
from binary_utilities import crossover_ints

class Flower:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.pollens = []


    def crossover(self, pollen):
        gen_cut_index = random.randint(0, 2)
        color = self.color[0:gen_cut_index] + pollen.color[gen_cut_index:]
        x = crossover_ints(self.x, pollen.x, 7)
        y = crossover_ints(self.y, pollen.y, 7)
        return Flower(color, x, y)


    def __str__(self):
        return '✿rgb{}-({}x,{}y){}'.format(''.join(str(val) for val in self.color), self.x, self.y, str(''))


    def __repr__(self):
        return self.__str__()
