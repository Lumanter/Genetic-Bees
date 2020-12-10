from bee_genetic import *
from flower_genetic import *

generations = 50

bees = generate_initial_bees()
flowers = generate_initial_flowers()
for _ in range(generations):
    fake_flower_search(bees, flowers)

    bees = fitness_bees(bees)
    print(bees)

    select_bees(bees)
    select_flowers(flowers)
    print(flowers, '\n')

    bees = crossover_bees(bees)
    flowers = crossover_flowers(flowers)

    mutate_bees(bees)
    mutate_flowers(flowers)

    add_missing_bees(bees)
    add_missing_flowers(flowers)
