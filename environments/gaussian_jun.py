import numpy as np
from bandit import Bandit


def linear_means(n_arms):
    mean_fn = lambda i: .9 * (n_arms - i) / (n_arms - 1)
    means = list(map(mean_fn, range(n_arms)))
    return means

def linear_bandit(n_arms, variance):
    means = linear_means(n_arms)
    stddev = np.sqrt(variance)
    def reward_fn(mu):
        return lambda: np.random.normal(mu, stddev)
    arms = list(map(reward_fn, means))
    return Bandit(arms)

def polynomial_means(n_arms):
    mean_fn = lambda i: .9 * (1 - np.sqrt(i / n_arms))
    means = list(map(mean_fn, range(n_arms)))
    return means

def polynomial_bandit(n_arms, variance):
    means = polynomial_means(n_arms)
    stddev = np.sqrt(variance)
    def reward_fn(mu):
        return lambda: np.random.normal(mu, stddev)
    arms = list(map(reward_fn, means))
    return Bandit(arms)

def sparse_means(n_arms):
    means = [0.0 for i in range(n_arms)]
    means[0] = 0.5
    return means

def sparse_bandit(n_arms, variance):
    means = sparse_means(n_arms)
    stddev = np.sqrt(variance)
    def reward_fn(mu):
        return lambda: np.random.normal(mu, stddev)
    arms = list(map(reward_fn, means))
    return Bandit(arms)

