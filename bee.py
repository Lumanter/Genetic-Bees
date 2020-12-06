import random
from binary_utils import *
from bee_genetic import max_search_radius, deviation_angle_bits, search_radius_bits


class Bee:


    def __init__(self, fav_dir, fav_color, deviation_angle, search_radius, search_strategy, honeycomb_start):
        self.fav_dir = fav_dir
        self.fav_color = fav_color
        self.deviation_angle = deviation_angle
        self.search_radius = search_radius
        self.search_strategy = search_strategy
        self.honeycomb_start = honeycomb_start
        self.pollinated_flowers = []
        self.traveled_distance = 0
        self.fitness = -1


    def pollinate(self, flower):
        flower.pollens.extend(self.pollinated_flowers)
        self.pollinated_flowers.append(flower)


    def crossover(self, bee):
        fav_dir = crossover_ints(self.fav_dir, bee.fav_dir, 3)
        fav_color = crossover_bin_lists(self.fav_color, bee.fav_color)
        deviation_angle = crossover_ints(self.deviation_angle, bee.deviation_angle, deviation_angle_bits)

        search_radius = max_search_radius + 1
        while search_radius > max_search_radius:
            search_radius = crossover_ints(self.search_radius, bee.search_radius, search_radius_bits)

        search_strategy = crossover_ints(self.search_strategy, bee.search_strategy, 2)
        search_strategy = search_strategy if search_strategy <= 2 else random.randint(0, 2) # avoid illegal 3

        honeycomb_start = random.choice([self.honeycomb_start, bee.honeycomb_start])
        return Bee(fav_dir, fav_color, deviation_angle, search_radius, search_strategy, honeycomb_start)


    def __str__(self):
        return '<🐝{}fit {} {}rgb {}° {}radius ({},{})🔍 {}⚐>'.format(self.fitness, str_dirs[self.fav_dir], ''.join(str(val) for val in self.fav_color), self.deviation_angle, self.search_radius, str_search_strategies[self.search_strategy], self.honeycomb_start, self.traveled_distance)


    def __repr__(self):
        return self.__str__()


str_dirs = ['N', 'E', 'S', 'W', 'NE', 'SE', 'SW', 'NW']
str_search_strategies = ['depth', 'breadth', 'random']
