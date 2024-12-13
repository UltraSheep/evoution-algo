from .utils.benchmark_functions import Sphere as benchmark  # change import to any function listed below
BENCHMARK = benchmark
DIM = 30
GENERATIONS = 100
POP_SIZE = 5
RUNS = 20
SEED = 123
TOURNAMENT_SIZE = 2
RESULTS_FILE = "test"
PLOT = False
ENEMY_COUNT = 5

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