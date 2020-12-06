import random
from flower import Flower
from binary_utils import *

flower_population = 50
flower_mutation_chance = 0.2
flower_max_coordinate = 127
flower_coordinate_bits = 7


def get_random_flower():
    color = [random.randint(0, 1) for _ in range(3)]
    x = random.randint(0, flower_max_coordinate)
    y = random.randint(0, flower_max_coordinate)
    return Flower(color, x, y)


def generate_initial_flowers():
    return [get_random_flower() for _ in range(flower_population)]


def select_flowers(flowers):
    for i in range(len(flowers)-1, -1, -1):
        if not flowers[i].pollens:
            flowers.pop(i)


def crossover_flowers(flowers):
    offspring = []
    for flower in flowers:
        pollen = random.choice(flower.pollens)
        offspring.append(flower.crossover(pollen))
    return offspring


def mutate_flowers(flowers):
    for flower in flowers:
        mutate_bin_list(flower.color, flower_mutation_chance)
        flower.x = mutate_int(flower.x, flower_coordinate_bits, flower_mutation_chance)
        flower.y = mutate_int(flower.y, flower_coordinate_bits, flower_mutation_chance)


def add_missing_flowers(flowers):
    missing_flowers = flower_population - len(flowers)
    for _ in range(missing_flowers):
        flowers.append(get_random_flower())


def fake_pollination(flowers):
    for _ in range(len(flowers)):
        flower = random.choice(flowers)
        pollen = random.choice(flowers)
        flower.pollens.append(pollen)
