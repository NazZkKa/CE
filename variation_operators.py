import random
import math

def one_action_flip(ind, len_map):
    mutation_point = random.randint(0,len_map-1)
    action_extra = random.randint(1,3)
    new_action = ind["genotype"][mutation_point]+action_extra
    ind["genotype"][mutation_point]=new_action%4

def line_flip(ind, len_map):
    lines = int(math.sqrt(len_map))
    line_to_mutate = random.randint(0,lines-1)
    for i in range(lines):
        action_extra = random.randint(1,3)
        new_action = ind["genotype"][i + line_to_mutate*lines]+action_extra
        ind["genotype"][i + line_to_mutate*lines]=new_action%4

def one_point(ind1, ind2, genotype,len_map):
    crossing_point = random.randint(0,len_map-1)
    parte1=ind1["genotype"][:crossing_point]
    parte2=ind2["genotype"][crossing_point:]
    genotype[:] = parte1 + parte2
