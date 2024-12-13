from .utils.benchmark_functions import Sphere as benchmark  # change import to any function listed below
BENCHMARK = benchmark

GENERATIONS = 100
RUNS = 20

POP_SIZE = 5
TOURNAMENT_SIZE = 2

ENEMY_COUNT = 5
ENEMY_PARAMS = 4
DIM = ENEMY_COUNT * ENEMY_PARAMS

SEED = 123
RESULTS_FILE = "test"
PLOT = False

# available benchmark functions:
# Sphere
# Schwefel_2_22
# Schwefel_1_2
# Schwefel_2_21
# Rosenbrock
# Step
# QuarticNoise
# Schwefel_2_26
# Rastrigin
# Ackley
# Griewank