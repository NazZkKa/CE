import random
import variation_operators as vo

actions = {
    "esquerda": 0,
    "baixo": 1,
    "direita": 2,
    "cima": 3,
}

run = {"n_steps": 0, "reward": 0, "route": []}


def gen_individual_rep1():

    ind = {
        "genotype": [],
        "fitness": 0,
        "run": {"n_steps": 0, "reward": 0, "route": []},
    }

    for i in range(16):
        ind["genotype"].append(random.randint(0, 3))

    return ind

#FIXED
def tournament_selection(population, tournament_size):
    candidates = []
    pop_size = len(population)
    candidates_idex = [random.randint(0, pop_size - 1) for i in range(tournament_size)]
    for i in candidates_idex:
        candidates.append(population[i])
    winner = sorted(candidates, key=lambda d: d["fitness"], reverse=True)[0]
    return winner


def function_fitness(run):
    fitness = -8
    repeated = {i: run["route"].count(i) for i in run["route"]}
    if run["n_steps"] >= 8:
        fitness += (run["n_steps"]-8)*0.5
        fitness += 8
    else:
        fitness += run["n_steps"]
    for i in repeated:
        if repeated[i] > 1:
            fitness -= 1 * (repeated[i] - 1)
    if run["reward"] == 1:
        fitness += 100 / (run["n_steps"] - 8)
    return fitness


def elitism(population, options):
    elite = sorted(population, key=lambda d: d["fitness"])[
        0 : int(options["elite_size"] * options["population_size"])
    ]
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
        options["crossover"](ind1,ind2,son["genotype"])
    prob2 = random.random()
    if prob2 < options["prob_mutation"]:
        options["mutation"](son)

    return son
