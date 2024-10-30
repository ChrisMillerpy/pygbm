__author__ = "Chris Miller"

from .version import __version__

from .gbm_simulator import GBMSimulator
from .bm_simulator import BMSimulator

print(f"PYGBM version: {__version__}")