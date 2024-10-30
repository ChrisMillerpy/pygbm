import numpy as np

class GBMSimulator:
    """
    A class representing a simulation of Geometric Brownian Motion
    """
    def __init__(self, y0, mu, sigma):
        self.y0 = y0
        self.mu = mu
        self.sigma = sigma
    
    def simulate_path(self, T, N):
        """
        Simulate a geometric brownian motion from time 0 to time T
        With N steps in the motion, and sigma, mu and y0 defined
        by the constructor
        """
        t_values = np.linspace(0, T, N+1)
        y_values = np.zeros(N+1) # list to store the GBM
        y_values[0] = self.y0 # initial value declared
        dt = T/N
        B = 0

        for i in range(1, N+1):
            X = np.random.randn()*dt
            y_values[i] = y_values[i-1]*np.exp((self.mu - (self.sigma**2 / 2))*dt + self.sigma*X)
        
        return t_values, y_values

    def print_parameters(self):
        print(f"The GBM has parameters:")
        print(f"y0 = {self.y0}")
        print(f"mu = {self.mu}")
        print(f"sigma = {self.sigma}")
