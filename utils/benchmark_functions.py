import numpy as np
from .. import config

class BenchmarkFunctionBase:
    SMax = 100
    SMin = -100
    FMin = 0

    @staticmethod
    def function(x):
        raise NotImplementedError("Function not implemented in base class.")


class Sphere(BenchmarkFunctionBase):
    @staticmethod
    def function(x):
        return np.sum(x**2)


class Schwefel_2_22(BenchmarkFunctionBase):
    SMax = 10
    SMin = -10

    @staticmethod
    def function(x):
        abs_x = np.abs(x)
        return np.sum(abs_x) + np.prod(abs_x)


class Schwefel_1_2(BenchmarkFunctionBase):
    @staticmethod
    def function(x):
        return np.sum([np.sum(x[:i+1])**2 for i in range(len(x))])


class Schwefel_2_21(BenchmarkFunctionBase):
    @staticmethod
    def function(x):
        return np.max(np.abs(x))


class Rosenbrock(BenchmarkFunctionBase):
    SMax = 30
    SMin = -30

    @staticmethod
    def function(x):
        return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)


class Step(BenchmarkFunctionBase):
    @staticmethod
    def function(x):
        return np.sum(np.floor(x + 0.5)**2)


class QuarticNoise(BenchmarkFunctionBase):
    SMax = 1.28
    SMin = -1.28

    @staticmethod
    def function(x):
        np.random.seed(config.SEED)
        return np.sum([(i + 1) * xi**4 for i, xi in enumerate(x)]) + np.random.uniform(0, 1)


class Schwefel_2_26(BenchmarkFunctionBase):
    SMax = 500
    SMin = -500
    FMin = -12569.5

    @staticmethod
    def function(x):
        return 418.9829 * len(x) - np.sum(x * np.sin(np.sqrt(np.abs(x))))


class Rastrigin(BenchmarkFunctionBase):
    SMax = 5.12
    SMin = -5.12

    @staticmethod
    def function(x):
        return np.sum(x**2 - 10 * np.cos(2 * np.pi * x) + 10)


class Ackley(BenchmarkFunctionBase):
    SMax = 32
    SMin = -32

    @staticmethod
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


class Griewank(BenchmarkFunctionBase):
    SMax = 600
    SMin = -600

    @staticmethod
    def function(x):
        sum_sq_term = np.sum(x**2) / 4000
        prod_cos_term = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
        return sum_sq_term - prod_cos_term + 1
