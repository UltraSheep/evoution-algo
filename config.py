from utils.benchmark_functions import Sphere as benchmark  # change import to any function listed below
BENCHMARK = benchmark
DIM = 30
GENERATIONS = 100
POP_SIZE = 50
RUNS = 1
SEED = 123
TOURNAMENT_SIZE = 10
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