rm -r cli_test_plots
mkdir cli_test_plots
pygbm simulate_bm --y0=0 --T=1 --N=100 --output="cli_test_plots/bm_plot.png"
pygbm simulate_gbm --y0=1 --mu=0.05 --sigma=0.2 --T=1 --N=100 --output="cli_test_plots/gbm_plot.png"
