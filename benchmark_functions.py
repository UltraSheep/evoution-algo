import numpy as np

def sphere(x):
    return np.sum(x**2)

def schwefel_2_22(x):
    abs_x = np.abs(x)
    return np.sum(abs_x) + np.prod(abs_x)

def schwefel_1_2(x):
    return np.sum([np.sum(x[:i+1])**2 for i in range(len(x))])

def schwefel_2_21(x):
    return np.max(np.abs(x))

def rosenbrock(x):
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

def step(x):
    return np.sum(np.floor(x + 0.5)**2)

def quartic_noise(x):
    return np.sum([(i + 1) * xi**4 for i, xi in enumerate(x)]) + np.random.uniform(0, 1)

def schwefel_2_26(x):
    return 418.9829 * len(x) - np.sum(x * np.sin(np.sqrt(np.abs(x))))

def rastrigin(x):
    return np.sum(x**2 - 10 * np.cos(2 * np.pi * x) + 10)

def ackley(x):
    a = 20
    b = 0.2
    c = 2 * np.pi
    n = len(x)
    sum_sq = np.sum(x**2)
    sum_cos = np.sum(np.cos(c * x))
    term1 = -a * np.exp(-b * np.sqrt(sum_sq / n))
    term2 = -np.exp(sum_cos / n)
    return term1 + term2 + a + np.e

def griewank(x):
    sum_sq_term = np.sum(x**2) / 4000
    prod_cos_term = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
    return sum_sq_term - prod_cos_term + 1
