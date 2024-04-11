import numpy as np
import gymnasium as gym
import random
from maps_to_evaluate import *
from evo_algorithm import *

RENDER_MODE = None


def running_in_the_90s(ind, gen):
    """
    Runs the given individual in the environment for a maximum number of iterations.

    Args:
        ind (dict): The individual to be run.

    Returns:
        dict: The updated individual after running in the environment.
    """
    if gen > 48:
        env = gym.make(
        "FrozenLake-v1", desc=map_4_by_4, is_slippery=False, render_mode="human"
        )
        print(ind["genotype"])
    else:
        env = gym.make(
            "FrozenLake-v1", desc=map_4_by_4, is_slippery=False, render_mode=RENDER_MODE
        )
    pos, information = env.reset(seed=42)
    run = ind["run"]

    if RENDER_MODE != None:
        env.render()

    for step in range(MAX_ITERATIONS_4_by_4):
        obs, reward, terminated, truncated, info = env.step(ind["genotype"][pos])
        if RENDER_MODE != None:
            env.render()
        pos = obs
        run["n_steps"] += 1
        run["route"].append(obs)

        #print(f"Step {step}:")
        #print(f"  observation: {obs}")

        if RENDER_MODE is not None:
            env.render()
        if terminated:
            #print(f"  terminated: {terminated}")
            run["reward"] = 1
            break

    #print(f"  terminated: {terminated}")

    return ind


def evo(config):
    """
    Runs an evolutionary algorithm based on the given configuration.

    Args:
        config (dict): Configuration parameters for the evolutionary algorithm.

    Returns:
        tuple: A tuple containing the lists of top fitness and average fitness values for each generation.
        
    """
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
        
        top_fitness.append(sorted(population, key=lambda d: d["fitness"]))
        avg_fitness.append(np.mean([ind["fitness"] for ind in population]))

        population = [
            config["genarate_son"](population, config) for _ in range(config["population_size"])
        ]
    return top_fitness, avg_fitness
