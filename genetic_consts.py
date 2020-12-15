

generations = 60

flower_population = 80
flower_mutation_chance = 0.2
flower_max_pos = 127
flower_pos_bits = 7

bee_population = 20
bee_mutation_chance = 0.2
max_deviation_angle = 31
deviation_angle_bits = len(list(bin(max_deviation_angle)[2:]))
max_search_radius = 90
search_radius_bits = len(list(bin(max_search_radius)[2:]))
fitness_flowers_factor = 150
top_bees_percent = 0.3

visiting_a_node_chace = (15/100)                #NEW
random_bee_movements = 5                        #NEW
