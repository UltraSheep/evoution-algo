from utils.benchmark_functions import Sphere as benchmark  # change import to any function listed below
BENCHMARK = benchmark
DIM = 30
GENERATIONS = 100
POP_SIZE = 50
RUNS = 20
SEED = 123
RESULTS_FILE = "results_summary.txt"

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