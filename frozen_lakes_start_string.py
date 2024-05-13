import sys
import random
import evo_algorithm as ea
import test_frozen_lake_string as tfl
from maps_to_evaluate import *
from variation_operators import *
from evo_algorithm import *




if __name__ == '__main__':

    # Dictonary with Configurations for the Simple Evolutionary Algorithm 🥰
    config = {
        'population_size' : 100,
        'generations' : 100,
        'genotype_size' : MAX_ITERATIONS_8_by_8,
        'prob_crossover' : 0.9,
        'prob_mutation' : 0.2,
        'elite_size' : 2,
        'generate_individual' : gen_individual_rep_string,
        'genarate_son': gen_desc_string,
        'mutation' : mutations_string,
        'crossover' : one_point_string,
        'parent_selection' : tournament_selection,
        'fitness_function' : function_fitness,
    }

    #Open csv file to write results
    file = open(f'./results/StringAction_map_{math.sqrt(config["genotype_size"])}_pcross_{config["prob_crossover"]}_pmut_{config["prob_mutation"]}_elite_{config["elite_size"]}_cross_one_point_mut_square_flip.csv', 'w')

    # Write the header of the csv file
    file.write('run,top_fitness,avg_fitness\n')

    for i in range(30):
        print('Run: ', i+1)
        top_fitness, avg_fitness = tfl.evo(config)
        best_top_fitness = sorted(top_fitness, reverse=True)
        best_avg_fitness = sorted(avg_fitness, reverse=True)
        best_best_top_fitness = best_top_fitness[0]
        best_best_avg_fitness = best_avg_fitness[0]
        file.write(str(i+1) + ',' + str(best_best_top_fitness) + ',' + str(best_best_avg_fitness) + '\n')
        


    file.close()
    