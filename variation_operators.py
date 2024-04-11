import random

def one_action_flip(ind):
    mutation_point = random.randint(0,15)
    action_extra = random.randint(1,3)
    new_action = ind["genotype"][mutation_point]+action_extra
    ind["genotype"][mutation_point]=new_action%4

def one_point(ind1, ind2, genotype):
    crossing_point = random.randint(0,15)
    parte1=ind1["genotype"][:crossing_point]
    parte2=ind2["genotype"][crossing_point:]
    genotype[:] = parte1 + parte2
