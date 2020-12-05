import random


def int_to_bin_list(integer, length):
    bitfield = list(bin(integer)[2:])
    while len(bitfield) < length:
        bitfield.insert(0, 0)
    return bitfield


def bin_list_to_int(bin_list):
    return int(''.join(str(i) for i in bin_list), 2)


def crossover_ints(a, b, bin_len):
    bin_list_a = int_to_bin_list(a, bin_len) #
    bin_list_b = int_to_bin_list(b, bin_len)
    gen_cut_index = random.randint(0, bin_len)
    offspring_list = bin_list_a[0:gen_cut_index] + bin_list_b[gen_cut_index:]
    offspring_int = bin_list_to_int(offspring_list)
    return offspring_int


def mutate_bin_list(bin_list, chance):
    for i in range(len(bin_list)):
        if random.uniform(0.0, 1.0) <= chance:
            if bin_list[i] == '0':
                bin_list[i] = '1'
            else:
                bin_list[i] = '0'


def mutate_int(integer, bin_len, chance):
    bin_list = int_to_bin_list(integer, bin_len)
    mutate_bin_list(bin_list, chance)
    return bin_list_to_int(bin_list)
