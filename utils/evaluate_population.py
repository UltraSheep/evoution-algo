def evaluate_population(population, benchmark):
    try:
        return [benchmark(ind) for ind in population]
    except TypeError as e:
        print(f"Error evaluating population (dimensionality or type mismatch): {e}")
        return []
