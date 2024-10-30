import numpy as np

class BMSimulator:
    """
    A class representing a simulation of a Brownian Motion
    """
    def __init__(self, y0 = 0):
        self.y0 = y0

    def _update_rule(self, y, T, N):
        """
        Defines the update rule of the Brownian Motion
        """
        x = np.random.normal(0, np.sqrt(T/N))
        return y + x
        
    def simulate_path(self, T, N):
        """
        Simulates a brownian motion from time 0 to time T with N steps
        """
        t_values = np.linspace(0, T, N+1)
        y_values = np.zeros(N+1) 
        y_values[0] = self.y0
        
        for i in range(1, N+1):
            y_values[i] = self._update_rule(y_values[i-1], T, N) # move that direction and update y_values

        return t_values, y_values