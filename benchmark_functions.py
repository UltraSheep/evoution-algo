import numpy as np

# 1. Sphere Function
def sphere(x):
    return np.sum(x**2)

# 2. Schwefel 2.22
def schwefel_2_22(x):
    abs_x = np.abs(x)
    return np.sum(abs_x) + np.prod(abs_x)

# 3. Schwefel 1.2
def schwefel_1_2(x):
    return np.sum([np.sum(x[:i+1])**2 for i in range(len(x))])

# 4. Schwefel 2.21
def schwefel_2_21(x):
    return np.max(np.abs(x))

# 5. Rosenbrock
def rosenbrock(x):
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

# 6. Step Function
def step(x):
    return np.sum(np.floor(x + 0.5)**2)

# 7. Quartic Function with Noise
def quartic_noise(x):
    return np.sum([(i + 1) * xi**4 for i, xi in enumerate(x)]) + np.random.uniform(0, 1)

# 8. Generalized Schwefel 2.26
def schwefel_2_26(x):
    return 418.9829 * len(x) - np.sum(x * np.sin(np.sqrt(np.abs(x))))

# 9. Rastrigin Function
def rastrigin(x):
    return np.sum(x**2 - 10 * np.cos(2 * np.pi * x) + 10)

# 10. Ackley Function
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

# 11. Griewank Function
def griewank(x):
    sum_sq_term = np.sum(x**2) / 4000
    prod_cos_term = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
    return sum_sq_term - prod_cos_term + 1
