def evaluate_population(population, benchmark):
    return [benchmark(ind[0]) for ind in population]