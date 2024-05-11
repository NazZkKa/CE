import sys
import random
import evo_algorithm as ea
import test_frozen_lake as tfl
from maps_to_evaluate import *
from variation_operators import *
from evo_algorithm import *




if __name__ == '__main__':
    # Dictonary with Configurations for the Simple Evolutionary Algorithm 🥰
    config = {
        'population_size' : 100,
        'generations' : 100,
        'genotype_size' : REP_1_SIZE_8_by_8,
        'prob_crossover' : 0.9,
        'prob_mutation' : 1,
        'elite_size' : 2,
        'generate_individual' : gen_individual_rep1,
        'genarate_son': gen_desc,
        'mutation' : square_flip,
        'crossover' : one_point,
        'parent_selection' : tournament_selection,
        'fitness_function' : function_fitness,
    }
    top_fitness, avg_fitness = tfl.evo(config)
    print("Top Fitness: ", top_fitness[len(top_fitness)-1])
    