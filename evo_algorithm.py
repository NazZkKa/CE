import random

run = {
    'n_steps' : 0,
    'reward' : 0,
    'last_observation' : 0,
    
    
}

def gen_individual_rep1():
    
    ind = {
        'genotype' : [],
        'fitness' : 0
    }
    
    for i in range(16):
        ind['genotype'].append(random.randint(0,3))
        
    return ind

def tournament_selection(population, tournament_size):

    return 0

def function_fitness(ind, run):
    
    


def elitism(population):

    return 0

def gen_desc(population, n_parents):

    return 0
