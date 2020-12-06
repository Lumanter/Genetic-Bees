import random
from bee import Bee
from binary_utils import *
from flower_genetic import generate_initial_flowers


bee_population = 50
bee_mutation_chance = 0.2
max_deviation_angle = 31
deviation_angle_bits = len(list(bin(max_deviation_angle)[2:]))
max_search_radius = 90
search_radius_bits = len(list(bin(max_search_radius)[2:]))
fitness_flowers_factor = 50
top_bees_percent = 0.2


def get_random_bee():
    fav_dir = random.randint(0, 7)
    fav_color = [random.randint(0, 1) for _ in range(3)]
    deviation_angle = random.randint(0, max_deviation_angle)
    search_radius = random.randint(0, max_search_radius)
    search_strategy = random.randint(0, 2)
    honeycomb_start = bool(random.randint(0, 1))
    return Bee(fav_dir, fav_color, deviation_angle, search_radius, search_strategy, honeycomb_start)


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
            offspring.append(first_parent.crossover(second_parent))
        else:
            second_parent = bees[i + 1]
            offspring.append(first_parent.crossover(second_parent))
            offspring.append(second_parent.crossover(second_parent))
    return offspring


def mutate_bees(bees):
    for bee in bees:
        bee.fav_dir = mutate_int(bee.fav_dir, 3, bee_mutation_chance)
        mutate_bin_list(bee.fav_color, bee_mutation_chance)
        bee.deviation_angle = mutate_int(bee.deviation_angle, deviation_angle_bits, bee_mutation_chance)
        bee.search_radius = mutate_int_with_max(bee.search_radius, search_radius_bits, bee_mutation_chance, max_search_radius)
        bee.search_strategy = mutate_int_with_max(bee.search_strategy, 2, bee_mutation_chance, 2)
        bee.honeycomb_start = bool(mutate_int(int(bee.honeycomb_start), 1, bee_mutation_chance))


def add_missing_bees(bees):
    missing_bees = bee_population - len(bees)
    for _ in range(missing_bees):
        bees.append(get_random_bee())


def fake_flower_search(bees):
    flowers = generate_initial_flowers()
    for _ in range(len(bees)):
        bee = random.choice(bees)
        flower = random.choice(flowers)
        bee.pollinate(flower)
        bee.traveled_distance += random.randint(1, 50)
