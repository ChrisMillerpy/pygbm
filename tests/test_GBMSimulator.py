from pygbm import GBMSimulator
import numpy as np

def test_GBMSimulator_init():
    gbmsim = GBMSimulator(42, 0.1, 0.25)
    assert gbmsim.y0 == 42
    assert gbmsim.mu == 0.1
    assert gbmsim.sigma == 0.25

def test_GBMSimulator_simulate_path():
    gbmsim = GBMSimulator(1, 0.05, 0.2)
    t, y = gbmsim.simulate_path(1, 100)
    t_test = np.linspace(0, 1, 101)
    assert len(t) == 101
    np.testing.assert_allclose(t, t_test, rtol=1e-5)
    assert len(y) == 101
    assert y[0] == 1