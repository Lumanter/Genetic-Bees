import random
from binary_utils import *
from genetic_consts import *


class Bee:
    def __init__(self, genes, parents=None):
        self.fav_dir = 0
        self.fav_color = 0
        self.deviation_angle = 0
        self.search_radius = 0
        self.search_strategy = 0
        self.honeycomb_start = False
        self.parse_genes(genes)
        self.pollinated_flowers = []
        self.traveled_distance = 0
        self.is_mutant = False
        self.fitness = -1
        self.non_mutated_genes = ''.join(str(gene) for gene in self.genes())
        self.parents = parents


    def pollinate(self, flower):
        flower.pollens.extend(self.pollinated_flowers)
        self.pollinated_flowers.append(flower)


    def crossover(self, bee):
        self_genes = self.genes()
        other_genes = bee.genes()

        cut_index = random.randint(0, len(self_genes))
        first_child_genes = self_genes[:cut_index] + other_genes[cut_index:]
        second_child_genes = other_genes[:cut_index] + self_genes[cut_index:]

        parents = (self, bee)
        first_child = Bee(first_child_genes, parents)
        second_child = Bee(second_child_genes, parents)

        first_child.adjust_gene_values()
        second_child.adjust_gene_values()
        return first_child, second_child


    def parse_genes(self, genes):
        self.fav_dir = bin_list_to_int(genes[:3])
        self.fav_color = genes[3:6]
        self.deviation_angle = bin_list_to_int(genes[6:(6+deviation_angle_bits)])
        self.search_radius= bin_list_to_int(genes[(6+deviation_angle_bits):(6+deviation_angle_bits+search_radius_bits)])
        self.search_strategy = bin_list_to_int(genes[-3:-1])
        self.honeycomb_start = bool(genes[-1])


    def adjust_gene_values(self):
        if (self.search_radius > max_search_radius):
            self.search_radius = self.search_radius - random.randint(2**search_radius_bits - max_search_radius, max_search_radius)
        if (self.search_strategy >= 2):
            self.search_strategy = random.randint(0, 2) # avoid illegal 3


    def genes(self):
        return bin_list(self.fav_dir, 3) + self.fav_color + bin_list(self.deviation_angle, deviation_angle_bits) + bin_list(self.search_radius, search_radius_bits) + bin_list(self.search_strategy, 2) + [int(self.honeycomb_start)]


    def get_fav_dir(self):
        return dirr(self.fav_dir)
        

    def get_honeycomb_start(self):
        return self.honeycomb_start

    def __str__(self):
        return '<🐝 {}fit {} {} {}° {}radius ({},{})✈ {}✿ {}⚐ {}☢>'.format(self.fitness, str_dirs[self.fav_dir], rgb_name(self.fav_color), self.deviation_angle, self.search_radius, str_search_strategies[self.search_strategy], self.honeycomb_start, len(self.pollinated_flowers), int(self.traveled_distance), self.is_mutant)


    def __repr__(self):
        return self.__str__()


str_dirs = ['N', 'E', 'S', 'W', 'NE', 'SE', 'SW', 'NW']
str_search_strategies = ['depth', 'breadth', 'random']


def rgb_name(rgb_color):
    str_color = ''.join(str(i) for i in rgb_color)
    color_names = {
        '000': "black",
        '111': "white",
        '100': "red",
        '010': "green",
        '001': "blue",
        '110': "yellow",
        '011': "cyan",
        '101': "magenta"
    }
    return color_names.get(str_color, '-')


def dirr(fav_dir):
    if fav_dir == 0:
        return 270 
    if fav_dir == 1:
        return 0 
    if fav_dir == 2:
        return 90 
    if fav_dir == 3:
        return 180 
    if fav_dir == 4:
        return 315 
    if fav_dir == 5:
        return 45 
    if fav_dir == 6:
        return 135 
    if fav_dir == 7:
        return 225


