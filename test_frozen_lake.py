import numpy as np
import gymnasium as gym
import random
from maps_to_evaluate import *
from evo_algorithm import *
import temp

RENDER_MODE = "human"

# To load temp.py
# modelo de um indíviduo
ind = {"genotype": [], "fitness": 0, "run": {"n_steps": 0, "reward": 0, "route": []}}


def running_in_the_90s(ind):
    """
    Runs the given individual in the environment for a maximum number of iterations.

    Args:
        ind (dict): The individual to be run.

    Returns:
        dict: The updated individual after running in the environment.
    """
    
    env = gym.make(
        "FrozenLake-v1", desc=map_4_by_4, is_slippery=False, render_mode=RENDER_MODE
    )
    pos, information = env.reset(seed=42)
    run = ind["run"]

    for step in range(MAX_ITERATIONS_4_by_4):

        obs, reward, terminated, truncated, info = env.step(ind["genotype"][pos])
        pos = obs
        run["n_steps"] += 1
        run["route"].append(obs)
        print(f"Step {step}:")
        print(f"  observation: {obs}")
        print(f"  reward: {reward}")
        print(f"  terminated: {terminated}")
        print(f"  truncated: {truncated}")
        print(f"  info: {info}")

        if RENDER_MODE is not None:
            env.render()
        if terminated:
            run["reward"] = 1
            break

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
            ind = running_in_the_90s(ind)
            ind["fitness"] = config['fitness_function'](ind["run"])

        top_fitness.append(sorted(population, key=lambda d: d["fitness"]))
        avg_fitness.append(np.mean([ind["fitness"] for ind in population]))

        # plot fitness
        population = [
            gen_desc(population, config) for _ in range(config["population_size"])
        ]

    return top_fitness, avg_fitness
