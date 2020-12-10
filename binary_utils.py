import random


def bin_list(integer, bits):
    bitfield = list(bin(integer)[2:])
    bitfield = [int(bit) for bit in bitfield] # string to integers
    while len(bitfield) < bits:
        bitfield.insert(0, 0)
    return bitfield


def bin_list_to_int(bin_list):
    return int(''.join(str(i) for i in bin_list), 2)


def crossover_bin_lists(a, b):
    cut_index = random.randint(0, len(a))
    return a[0:cut_index] + b[cut_index:]


def mutate_bin_list(bin_list, chance):
    for i in range(len(bin_list)):
        if random.uniform(0.0, 1.0) <= chance:
            bin_list[i] = 1 if bin_list[i] == 0 else 0
