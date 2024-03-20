import random as rand

actions = {
    'esquerda': 0,
    'baixo' : 1,
    'direita' : 2,
    'cima' : 3,
}

def gen_individual_rep1():

    return 0

def tournament_selection(population, tournament_size):
    pop_size = population.size()
    candidates_idex = [rand.randint(0, pop_size-1) for i in range(tournament_size)]
    candidates = population[candidates_idex]
    winner = sorted(candidates, key=lambda d: d['fitness'])[0]
    return winner

def function_fitness(ind, run):

    return 0

def elitism(population, options):
    elite = sorted(population, key=lambda d: d['fitness'])[0:int(options['elite_size']*options['population_size'])]
    return elite

def gen_desc(population, n_parents):

    return 0

