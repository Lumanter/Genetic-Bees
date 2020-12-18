import random
import numpy.random
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
        bee.fitness = max(0, bee.fitness)
    bees = sorted(bees, key=lambda bee: bee.fitness, reverse=True)
    return bees


def select_bee(bees):
    fitness_sum = sum([bee.fitness for bee in bees])
    selection_probabilities = [(bee.fitness/fitness_sum) for bee in bees]
    selected_bee = bees[numpy.random.choice(len(bees), p=selection_probabilities)]
    return selected_bee


def crossover_bees(bees):
    offspring = []
    for i in range(int(len(bees)/2)):
        first_parent = select_bee(bees)
        second_parent = select_bee(bees)

        first_child, second_child = first_parent.crossover(second_parent)
        offspring.append(first_child)
        if len(offspring) < len(bees):
            offspring.append(second_child)
    return offspring


def mutate_bees(bees):
    for bee in bees:
        original_genes = str(bee.genes())
        genes = bee.genes()
        mutate_bin_list(genes, bee_mutation_chance)
        bee.parse_genes(genes)
        bee.adjust_gene_values()
        bee.is_mutant = (original_genes != str(bee.genes()))

def avg_fitness(bees):
    return int(sum([bee.fitness for bee in bees]) / len(bees))


def run_genetic_generations():
    flower_generations = []
    bee_generations = []
    bees = generate_initial_bees()
    flowers = generate_initial_flowers()
    fitness_goal_reached = False
    for i in range(generations):
        search_bees(bees, flowers)
        flower_generations.append(copy.copy(flowers)) # flowers gen snapshot

        bees = fitness_bees(bees)
        bee_generations.append(copy.copy(bees)) # bee gen snapshot

        print('(gen {}) avg fit {}'.format(i+1, avg_fitness(bees)))

        if (avg_fitness(bees) >= goal_avg_gen_fitness):
            fitness_goal_reached = True
            break
        else:
            bees = crossover_bees(bees)
            flowers = crossover_flowers(flowers)

            mutate_bees(bees)
            mutate_flowers(flowers)

            add_missing_flowers(flowers)
    return flower_generations, bee_generations, fitness_goal_reached