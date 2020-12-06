import random


def int_to_bin_list(integer, bits):
    bitfield = list(bin(integer)[2:])
    while len(bitfield) < bits:
        bitfield.insert(0, 0)
    return bitfield


def bin_list_to_int(bin_list):
    return int(''.join(str(i) for i in bin_list), 2)


def crossover_bin_lists(a, b):
    cut_index = random.randint(0, len(a))
    return a[0:cut_index] + b[cut_index:]


def crossover_ints(a, b, bits):
    list_a = int_to_bin_list(a, bits)
    list_b = int_to_bin_list(b, bits)
    offspring_list = crossover_bin_lists(list_a, list_b)
    offspring_int = bin_list_to_int(offspring_list)
    return offspring_int


def mutate_bin_list(bin_list, chance):
    for i in range(len(bin_list)):
        if random.uniform(0.0, 1.0) <= chance:
            if bin_list[i] == '0':
                bin_list[i] = '1'
            else:
                bin_list[i] = '0'


def mutate_int(integer, bits, chance):
    bin_list = int_to_bin_list(integer, bits)
    mutate_bin_list(bin_list, chance)
    return bin_list_to_int(bin_list)


def mutate_int_with_max(integer, bits, chance, max_integer):
    original = integer
    mutated = mutate_int(integer, bits, chance)
    if mutated > max_integer:
        return original
    else:
        return mutated
