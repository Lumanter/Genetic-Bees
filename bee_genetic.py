import random
import copy
from bee import Bee
from binary_utils import *
from genetic_consts import *
from flower_genetic import *
from search import search_bees

def get_random_bee():
    bee_genes_len = 9 + deviation_angle_bits + search_radius_bits
    random_genes = [random.randint(0, 1) for _ in range(bee_genes_len)]
    random_bee = Bee(random_genes)
    random_bee.adjust_gene_values()
    return random_bee


def generate_initial_bees():
    return [get_random_bee() for _ in range(bee_population)]


def fitness_bees(bees):
    for bee in bees:
        bee.fitness = int(len(bee.pollinated_flowers) * fitness_flowers_factor - bee.traveled_distance)
    bees = sorted(bees, key=lambda bee: bee.fitness, reverse=True)
    return bees


def select_bees(bees):
    cut_index = int(top_bees_percent * len(bees))
    for i in range(len(bees)-1, -1, -1):
        if i >= cut_index:
            bees.pop(i)


def crossover_bees(bees):
    offspring = []
    for i in range(0, len(bees) - 1, 2):
        first_parent = bees[i]
        if (i + 1 == len(bees)): # odd parent
            second_parent = bees[random.randin(0, len(bees))]
        else:
            second_parent = bees[i + 1]
        first_child, second_child = first_parent.crossover(second_parent)
        offspring.extend([first_child, second_child])
    return offspring


def mutate_bees(bees):
    for bee in bees:
        original_genes = str(bee.genes())
        genes = bee.genes()
        mutate_bin_list(genes, bee_mutation_chance)
        bee.parse_genes(genes)
        bee.adjust_gene_values()
        bee.is_mutant = (original_genes != str(bee.genes()))


def add_missing_bees(bees):
    missing_bees = bee_population - len(bees)
    for _ in range(missing_bees):
        bees.append(get_random_bee())


def fake_flower_search(bees, flowers):
    for _ in range(len(bees)):
        bee = random.choice(bees)
        flower = random.choice(flowers)
        bee.pollinate(flower)
        bee.traveled_distance += random.randint(1, 50)


def run_genetic_generations():
    flower_generations = []
    bee_generations = []
    bees = generate_initial_bees()
    flowers = generate_initial_flowers()
    for i in range(generations):
        print('generating gen ', i+1)
        flower_generations.append(copy.copy(flowers))

        bees = search_bees(bees, flowers)

        bees = fitness_bees(bees)
        bee_generations.append(copy.copy(bees))

        select_bees(bees)
        select_flowers(flowers)

        bees = crossover_bees(bees)
        flowers = crossover_flowers(flowers)

        mutate_bees(bees)
        mutate_flowers(flowers)

        add_missing_bees(bees)
        add_missing_flowers(flowers)
    return flower_generations, bee_generations