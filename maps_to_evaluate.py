import gymnasium as gym
from gymnasium.envs.toy_text.frozen_lake import generate_random_map

map_4_by_4 = generate_random_map(size=4, seed=42)
map_8_by_8 = generate_random_map(size=8, seed=42)
map_12_by_12 = generate_random_map(size=12, seed=42)

REP_1_SIZE_4_by_4 = 16
REP_1_SIZE_8_by_8 = 64
REP_1_SIZE_12_by_12 = 144
MAX_ITERATIONS_4_by_4 = 16
MAX_ITERATIONS_8_by_8 = 64
MAX_ITERATIONS_12_by_12 = 144