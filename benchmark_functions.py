import numpy as np

class benchmark_function:
    SMax = 100
    SMin = -100
    n = 30
    FMin = 0
    def function(x):
        pass

class sphere(benchmark_function):
    def function(x):
        return np.sum(x**2)

class schwefel_2_22(benchmark_function):
    SMax = 10
    SMin = -10
    def function(x):
        abs_x = np.abs(x)
        return np.sum(abs_x) + np.prod(abs_x)

class schwefel_1_2(benchmark_function):
    def function(x):
        return np.sum([np.sum(x[:i+1])**2 for i in range(len(x))])

class schwefel_2_21(benchmark_function):
    def function(x):
        return np.max(np.abs(x))

class rosenbrock(benchmark_function):
    SMax = 30
    SMin = -30
    def function(x):
        return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

class step(benchmark_function):
    def function(x):
        return np.sum(np.floor(x + 0.5)**2)

class quartic_noise(benchmark_function):
    SMax = 1.28
    SMin = -1.28
    def function(x):
        return np.sum([(i + 1) * xi**4 for i, xi in enumerate(x)]) + np.random.uniform(0, 1)

class schwefel_2_26(benchmark_function):
    SMax = 500
    SMin = -500
    FMin = -12569.5
    def function(x):
        return 418.9829 * len(x) - np.sum(x * np.sin(np.sqrt(np.abs(x))))

class rastrigin(benchmark_function):
    SMax = 5.12
    SMin = -5.12
    def function(x):
        return np.sum(x**2 - 10 * np.cos(2 * np.pi * x) + 10)

class ackley(benchmark_function):
    SMax = 32
    SMin = -32
    def function(x):
        a = 20
        b = 0.2
        c = 2 * np.pi
        n = len(x)
        sum_sq = np.sum(x**2)
        sum_cos = np.sum(np.cos(c * x))
        term1 = -a * np.exp(-b * np.sqrt(sum_sq / n))
        term2 = -np.exp(sum_cos / n)
        return term1 + term2 + a + np.e

class griewank(benchmark_function):
    SMax = 600
    SMin = -600
    def function(x):
        sum_sq_term = np.sum(x**2) / 4000
        prod_cos_term = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
        return sum_sq_term - prod_cos_term + 1
