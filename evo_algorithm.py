import random
import variation_operators as vo
import math
import copy

actions = {
    "esquerda": 0,
    "baixo": 1,
    "direita": 2,
    "cima": 3,
}

run = {"n_steps": 0, "reward": 0, "route": []}


def gen_individual_rep1(len_map):

    ind = {
        "genotype": [],
        "fitness": 0,
        "run": {"n_steps": 0, "reward": 0, "route": []},
    }

    for i in range(len_map):
        ind["genotype"].append(random.randint(0, 3))

    ind["genotype"][0]= random.randint(1,2)
    ind["genotype"][int(math.sqrt(len_map)-1)]= random.randint(0,1)
    ind["genotype"][int(len_map-math.sqrt(len_map))]= random.randint(2,3)

    return ind

def tournament_selection(population, tournament_size):
    candidates = []
    pop_size = len(population)
    candidates_idex = [random.randint(0, pop_size - 1) for i in range(tournament_size)]
    for i in candidates_idex:
        candidates.append(population[i])
    winner = sorted(candidates, key=lambda d: d["fitness"], reverse=True)[0]
    return winner


def function_fitness(run, len_map):
    n_steps = 3
    steps_pre_optimo = 2
    steps_pos_optimo = 0
    proximidade = 3

    optimal_steps = int(math.sqrt(len_map)) * 2

    fitness = 0

    if run["n_steps"] >= optimal_steps:
        fitness += (run["n_steps"]-optimal_steps)* steps_pos_optimo
        fitness += steps_pre_optimo * optimal_steps
    else:
        fitness += steps_pre_optimo * run["n_steps"]

    if run["reward"] == 1:
        print("fiz em:", run["n_steps"])
        fitness += 200 - (run["n_steps"]*n_steps)
    
    
    fitness +=proximidade * manhattan_distance(run["route"][run["n_steps"]],len_map)

    return fitness

def manhattan_distance(end_pos, len_map):
    lines = int(math.sqrt(len_map))
    x_axys = end_pos % lines
    y_axys = end_pos // lines
    return x_axys + y_axys


def elitism(population, options):

    #Sort the population by fitness
    population.sort(key=lambda x: x["fitness"], reverse=True)

    #Select the elite according to options["elite_size"]
    elite = population[:int(options["elite_size"])]

    for ind in elite:
        ind["fitness"] = 0
        ind["run"]["n_steps"] = 0
        ind["run"]["reward"] = 0
        ind["run"]["route"] = []

    return elite


def gen_desc(population, options):
    son = {
        "genotype": [],
        "fitness": 0,
        "run": {"n_steps": 0, "reward": 0, "route": []},
    }
    ind1 = options["parent_selection"](population, 3)
    ind2 = options["parent_selection"](population, 3)

    son["genotype"][:]=ind1["genotype"]
    prob = random.random()
    if prob < options["prob_crossover"]:
        options["crossover"](ind1,ind2,son["genotype"],options["genotype_size"])
    prob2 = random.random()
    if prob2 < options["prob_mutation"]:
        options["mutation"](son,options["genotype_size"])

    return son
