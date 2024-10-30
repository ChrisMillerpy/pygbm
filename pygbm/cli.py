import argparse
from pygbm import BMSimulator, GBMSimulator
import matplotlib.pyplot as plt


def simulate_bm(y0, T, N, output):
    """
    simulates a Brownian Motion starting from y0 for time T and N steps
    """
    BMSim = BMSimulator(y0)
    t_values, y_values = BMSim.simulate_path(T, N)

    fig, ax = plt.subplots()

    ax.plot(t_values, y_values, label="BM Path")

    ax.set_title("Brownian Motion Simulation")
    ax.set_xlabel("Time")
    ax.set_ylabel("Y(t)")
    ax.legend()
    fig.text(0.01, 0.01, f"y0={y0}")

    fig.savefig(output)


def simulate_gbm(y0, mu, sigma, T, N, output):
    """
    simulates a Brownian Motion starting from y0 for time T and N steps
    """
    GBMSim = GBMSimulator(y0, mu, sigma)
    t_values, y_values = GBMSim.simulate_path(T, N)

    fig, ax = plt.subplots()

    ax.plot(t_values, y_values, label="GBM Path")

    ax.set_title("Geometric Brownian Motion Simulation")
    ax.set_xlabel("Time")
    ax.set_ylabel("Y(t)")
    ax.legend()
    fig.text(0.01, 0.01, f"y0={y0}, mu={mu}, sigma={sigma}")

    fig.savefig(output)


def main():
    """
    Main function for the CLI tool.
    """
    parser = argparse.ArgumentParser(description="pygbm CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Sub-command for simulating a brownian motion
    parser_bm = subparsers.add_parser("simulate_bm", help="Simulate a Brownian Motion")
    parser_bm.add_argument("--y0", type=float, required=True, help="Initial value (e.g., 0)")
    parser_bm.add_argument("--T", type=float, required=True, help="Length of time (e.g., 1)")
    parser_bm.add_argument("--N", type=int, required=True, help="Number of steps (e.g., 100)")
    parser_bm.add_argument("--output", type=str, required=True, help="Output file (e.g., out.png)")

    parser_gbm = subparsers.add_parser("simulate_gbm", help="Simulate a Geometric Brownian Motion")
    parser_gbm.add_argument("--y0", type=float, required=True, help="Initial value (e.g., 0)")
    parser_gbm.add_argument("--mu", type=float, required=True, help="Drift (e.g., 0.05)")
    parser_gbm.add_argument("--sigma", type=float, required=True, help="Diffusion coefficient (e.g., 0.2)")
    parser_gbm.add_argument("--T", type=float, required=True, help="Length of time (e.g., 1)")
    parser_gbm.add_argument("--N", type=int, required=True, help="Number of steps (e.g., 100)")
    parser_gbm.add_argument("--output", type=str, required=True, help="Output file (e.g., out.png)")
    
    args = parser.parse_args()

    if args.command == "simulate_bm":
        simulate_bm(args.y0, args.T, args.N, args.output)
    
    if args.command == "simulate_gbm":
        simulate_gbm(args.y0, args.mu, args.sigma, args.T, args.N, args.output)

if __name__ == "__main__":
    main()