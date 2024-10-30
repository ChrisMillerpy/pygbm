from pygbm.bm_simulator import BMSimulator
import matplotlib.pyplot as plt

y0 = 0

BMSim = BMSimulator(y0)

T = 1
N = 100

t_values, y_values = BMSim.simulate_path(T, N)

fig, ax = plt.subplots()

ax.plot(t_values, y_values, label="BM Path")

ax.set_title("Brownian Motion Simulation")
ax.set_xlabel("Time")
ax.set_ylabel("Y(t)")
ax.legend()
fig.text(0.01, 0.01, f"y0={y0}")
plt.show()