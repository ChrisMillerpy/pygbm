import numpy as np

from .bm_simulator import BMSimulator

class GBMSimulator(BMSimulator):
    """
    A class representing a simulation of Geometric Brownian Motion
    """
    def __init__(self, y0 = 1, mu = 0.05, sigma = 0.2):
        super().__init__(y0)
        self.mu = mu
        self.sigma = sigma

    def _update_rule(self, y, T, N):
        """
        Defines the update rule of a Geometric Brownian Motion
        """
        x = np.random.normal(0, np.sqrt(T/N))
        return y * np.exp((self.mu - self.sigma**2/2)*T/N + self.sigma*x)
    
