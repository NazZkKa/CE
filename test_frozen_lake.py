import gymnasium as gym
import random
from maps_to_evaluate import *
import temp

RENDER_MODE = 'human'
env = gym.make('FrozenLake-v1', desc=map_4_by_4, is_slippery=False, render_mode=RENDER_MODE)
observation, info = env.reset(seed=42)
if RENDER_MODE is not None:
    env.render()

#To load temp.py

ind = {
    'genotype': [],
    'fitness': 0
}



def single_run(ind):

    fitness_best = 0

    for step in range(MAX_ITERATIONS_4_by_4):

        fitness = 0
        
        action = random.randint(0,3)

        ind['genotype'].append(action)

        observation, reward, terminated, truncated, info = env.step(action)
        print(f"Step {step}:")
        print(f"  observation: {observation}")
        print(f"  reward: {reward}")
        print(f"  terminated: {terminated}")
        print(f"  truncated: {truncated}")
        print(f"  info: {info}")

        current_x = observation%4
        current_y = observation//4

        distance_to_goal = abs(3 - current_x) + abs(3 - current_y)
        
        print(f"  distance_to_goal: {distance_to_goal}")

        fitness = 1/distance_to_goal

        print(f"  fitness: {fitness}")

        if RENDER_MODE is not None:
            env.render()
        if terminated:
            break

    return ind

single_run(ind)