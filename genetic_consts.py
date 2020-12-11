
flower_population = 100
flower_mutation_chance = 0.2
flower_max_pos = 127
flower_pos_bits = 7

bee_population = 50
bee_mutation_chance = 0.2
max_deviation_angle = 31
deviation_angle_bits = len(list(bin(max_deviation_angle)[2:]))
max_search_radius = 90
search_radius_bits = len(list(bin(max_search_radius)[2:]))
fitness_flowers_factor = 50
top_bees_percent = 0.2