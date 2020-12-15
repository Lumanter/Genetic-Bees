

generations = 100

flower_population = 90
flower_mutation_chance = 0.05
flower_max_pos = 127
flower_pos_bits = 7

bee_population = 30
bee_mutation_chance = 0.2
max_deviation_angle = 31
deviation_angle_bits = len(list(bin(max_deviation_angle)[2:]))
max_search_radius = 90
search_radius_bits = len(list(bin(max_search_radius)[2:]))
fitness_flowers_factor = 100
top_bees_percent = 0.4

visiting_a_node_chace = (10/100)
random_bee_movements = 5
