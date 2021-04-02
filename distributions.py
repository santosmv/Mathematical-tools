import numpy as np
from scipy.special import factorial

def gaussian(x, mu, sigma):
    gauss = 1/np.sqrt(2 * np.pi * sigma**2) * np.exp(- (x - mu)**2 / (2 * sigma**2))
    return gauss

def binomial(n, N, p):
    binom = factorial(N) / (factorial(n) * factorial(N - n)) * p**n * (1-p)**(N-n)
    return binom

def poisson(n, N, p):
    nu = N*p
    pois = nu**n / factorial(n) * np.exp(-nu)
    return pois