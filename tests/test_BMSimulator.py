from pygbm import BMSimulator
import numpy as np

def test_BMSimulator_init():
    bmsim = BMSimulator(42)
    assert bmsim.y0 == 42

def test_BMSimulator_simulate_path():
    bmsim = BMSimulator(0)
    t, y = bmsim.simulate_path(1, 100)
    t_test = np.linspace(0, 1, 101)
    assert len(t) == 101
    np.testing.assert_allclose(t, t_test, rtol=1e-5)
    assert len(y) == 101
    assert y[0] == 0
