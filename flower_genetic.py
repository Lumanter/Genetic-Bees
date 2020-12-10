import random
from flower import Flower
from binary_utils import *
from genetic_consts import *


def get_random_flower():
    flower_genes_len = 3 + 2*flower_pos_bits
    random_genes = [random.randint(0, 1) for _ in range(flower_genes_len)]
    return Flower(random_genes)


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
        genes = flower.genes()
        mutate_bin_list(genes, flower_mutation_chance)
        flower.parse_genes(genes)


def add_missing_flowers(flowers):
    missing_flowers = flower_population - len(flowers)
    for _ in range(missing_flowers):
        flowers.append(get_random_flower())


def fake_pollination(flowers):
    for _ in range(len(flowers)):
        flower = random.choice(flowers)
        pollen = random.choice(flowers)
        flower.pollens.append(pollen)
