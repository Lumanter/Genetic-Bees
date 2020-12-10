import random
from genetic_consts import flower_pos_bits
from binary_utils import *


class Flower:
    def __init__(self, genes):
        self.color = []
        self.x = 0
        self.y = 0
        self.pollens = []
        self.parse_genes(genes)


    def parse_genes(self, genes):
        self.color = genes[0:3]
        self.x = bin_list_to_int(genes[3:(3 + flower_pos_bits)])
        self.y = bin_list_to_int(genes[(3 + flower_pos_bits):])


    def genes(self):
        return self.color + bin_list(self.x, flower_pos_bits) + bin_list(self.y, flower_pos_bits)


    def crossover(self, flower):
        self_genes = self.genes()
        other_genes = flower.genes()
        cut_index = random.randint(0, len(self_genes))
        child_genes = self_genes[:cut_index] + other_genes[cut_index:]
        return Flower(child_genes)


    def __str__(self):
        return '<✿{}rgb {}x{}y>'.format(''.join(str(val) for val in self.color), self.x, self.y)


    def __repr__(self):
        return self.__str__()

