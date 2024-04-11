import sys
import random
import evo_algorithm as ea
import test_frozen_lake as tfl
from maps_to_evaluate import *
from variation_operators import one_point
from evo_algorithm import *




if __name__ == '__main__':
    # Dictonary with Configurations for the Simple Evolutionary Algorithm 🥰
    config = {
        'population_size' : 10,
        'generations' : 25,
        'genotype_size' : REP_1_SIZE_4_by_4,
        'max_steps' : REP_1_SIZE_4_by_4/2,
        'prob_crossover' : 0.9,
        'prob_mutation' : 0.05,
        'elite_size' : 0.1,
        'seed' : int(sys.argv[1]),
        'generate_individual' : gen_individual_rep1,
        'mutation' : "mutation_rep1",
        'crossover' : one_point,
        'parent_selection' : tournament_selection,
        'fitness_function' : function_fitness,
    }


    random.seed(config['seed'])
    bests = tfl.evo(config)
    #print(bests)
    