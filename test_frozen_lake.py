import numpy as np
import gymnasium as gym
from maps_to_evaluate import *
from evo_algorithm import *

RENDER_MODE = None


def running_in_the_90s(ind, gen):
    if gen > 48:
        env = gym.make(
        "FrozenLake-v1", desc=map_4_by_4, is_slippery=False, render_mode="human"
        )
    else:
        env = gym.make(
            "FrozenLake-v1", desc=map_4_by_4, is_slippery=False, render_mode=RENDER_MODE
        )
    pos, information = env.reset(seed=42)
    run = ind["run"]
        
    for step in range(MAX_ITERATIONS_4_by_4):
        obs, reward, terminated, truncated, info = env.step(ind["genotype"][pos])
        if RENDER_MODE != None:
            env.render()
        pos = obs
        run["n_steps"] += 1
        run["route"].append(obs)

        if RENDER_MODE is not None:
            env.render()
        if terminated:
            run["reward"] = 1
            break

    return ind


def evo(config):
    # genotype
    population = [
        config["generate_individual"]() for _ in range(config["population_size"])
    ]

    top_fitness = []
    avg_fitness = []

    for i in range(config["generations"]):

        for ind in population:
            ind = running_in_the_90s(ind,i)
            ind["fitness"] = config['fitness_function'](ind["run"])
        
        top_performer = sorted(population, key=lambda d: d["fitness"], reverse=True)[0]
        print(top_performer["fitness"])
        top_fitness.append(top_performer["fitness"])
        #avg_fitness.append(np.mean([ind["fitness"] for ind in population]))

        population = [
            config["genarate_son"](population, config) for _ in range(config["population_size"])
        ]
    return top_fitness, avg_fitness
