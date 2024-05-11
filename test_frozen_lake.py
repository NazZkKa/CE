import numpy as np
import gymnasium as gym
from maps_to_evaluate import *
from evo_algorithm import *

RENDER_MODE = None

MAP = map_8_by_8
ITERATIONS = MAX_ITERATIONS_8_by_8//2

def running_in_the_90s(ind, gen):    
    env = gym.make(
        "FrozenLake-v1", desc=MAP, is_slippery=False, render_mode=RENDER_MODE
    )
    env.metadata['render_fps'] = 120
    pos, information = env.reset()
    run = ind["run"]

    run["route"].append(pos)
    visitados = {}
    
    visitados[pos]=True

    for step in range(ITERATIONS):
        obs, reward, terminated, truncated, info = env.step(ind["genotype"][pos])
        if RENDER_MODE != None:
            env.render()
        
        if obs in visitados:
            break
        else:
            run["n_steps"] += 1
            run["route"].append(obs)
            visitados[obs]=True

        pos = obs

        if RENDER_MODE is not None:
            env.render()
        if terminated:
            break

    run["reward"] = reward
    return ind


def evo(config):
    # genotype
    population = [
        config["generate_individual"](config["genotype_size"]) for _ in range(config["population_size"])
    ]

    top_fitness = []
    avg_fitness = []

    for i in range(config["generations"]):
        print("genaration:", i)
        for ind in population:
            ind = running_in_the_90s(ind,i)
            ind["fitness"] = config['fitness_function'](ind["run"],config["genotype_size"])
        
        top_performer = sorted(population, key=lambda d: d["fitness"], reverse=True)[0]
        top_fitness.append(top_performer["fitness"])
        avg_fitness.append(np.mean([ind["fitness"] for ind in population]))
        new_population = [
            config["genarate_son"](population, config) for _ in range(config["population_size"]-int(config["elite_size"]))
        ]
        elite = elitism(population, config)
        
        new_population.extend(elite)
        population = new_population
    return top_fitness, avg_fitness
