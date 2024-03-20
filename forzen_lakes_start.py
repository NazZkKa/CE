import evo_algorithm as ea
import variation_operators as vo
import random
import test_frozen_lake as tfl
from maps_to_evaluate import *
import sys


if __name__ == '__main__':
    # Dictonary with Configurations for the Simple Evolutionary Algorithm 
    config = {
        'population_size' : 10,
        'generations' : 25,
        'genotype_size' : REP_1_SIZE_4_by_4,
        'max_steps' : REP_1_SIZE_4_by_4/2,
        'prob_crossover' : 0.9,
        'prob_mutation' : 0.05,
        'elite_size' : 0.1,
        'seed' : int(sys.argv[1]),
        'generate_individual' : ea.gen_individual_rep1(),
        'mapping' : ea.mapping(),
        'mutation' : vo.mutation_rep1(),
        'crossover' : vo.crossover_rep1(),
        'gen_desc' : ea.gen_desc(),
        'parent_selection' : ea.tournament_selection(5, maximization=False),
        'fitness_function' : ea.function_fitness(),
    }


    random.seed(config['seed'])
    bests = tfl.evo(config)
    #print(bests)
    