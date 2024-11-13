def evaluate_population(population, benchmark):
    return [benchmark(ind) for ind in population]