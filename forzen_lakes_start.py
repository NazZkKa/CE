import sys
import random
import evo_algorithm as ea
import test_frozen_lake as tfl
from maps_to_evaluate import *
from variation_operators import one_point, one_action_flip, line_flip
from evo_algorithm import *




if __name__ == '__main__':
    # Dictonary with Configurations for the Simple Evolutionary Algorithm 🥰
    config = {
        'population_size' : 30,
        'generations' : 30,
        'genotype_size' : REP_1_SIZE_8_by_8,
        'max_steps' : REP_1_SIZE_8_by_8/2,
        'prob_crossover' : 0.9,
        'prob_mutation' : 0.2,
        'elite_size' : 0.1,
        'generate_individual' : gen_individual_rep1,
        'genarate_son': gen_desc,
        'mutation' : line_flip,
        'crossover' : one_point,
        'parent_selection' : tournament_selection,
        'fitness_function' : function_fitness,
    }
    top_fitness, avg_fitness = tfl.evo(config)
    