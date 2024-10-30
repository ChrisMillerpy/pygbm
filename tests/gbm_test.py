from pygbm.gbm_simulator import GBMSimulator
import matplotlib.pyplot as plt

y0 = 1.0
mu = 0.05
sigma = 0.2

GBMSim = GBMSimulator(y0, mu, sigma)

T = 1
N = 100

t_values, y_values = GBMSim.simulate_path(T, N)

fig, ax = plt.subplots()

ax.plot(t_values, y_values, label="GBM Path")

ax.set_title("Geometric Brownian Motion Simulation")
ax.set_xlabel("Time")
ax.set_ylabel("Y(t)")
ax.legend()
fig.text(0.01, 0.01, f"y0={y0}, mu={mu}, sigma={sigma}")

plt.show()