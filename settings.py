if __name__ == '__main__':
    # Dictonary with Configurations for the Simple Evolutionary Algorithm 
    config = {
        'population_size' : 100,
        'generations' : 2000,
        'genotype_size' : len(cities),
        'prob_crossover' : 0.9,
        'prob_mutation' : 0.05,
        'seed' : int(sys.argv[1]),
        'generate_individual' : generate_random_individual_permutations,
        'mapping' : mapping(cities),
        'maximization' : False,
        'mutation' : swap_mutation,
        'crossover' : order_crossover,
        'parent_selection' : tournament(5, maximization=False),
        'survivor_selection' : survivor_elitism(.02, maximization=False),
        'fitness_function' : None,
        'interactive_plot' : create_interactive_plot('Evolving...', 'Iteration', 'Quality', (0, 2000), (-2, 20000)),
    }
    config['fitness_function'] = function_fitness(config)


    random.seed(config['seed'])
    bests = sea(config)
    #print(bests)
    