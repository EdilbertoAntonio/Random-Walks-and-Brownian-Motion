import numpy as np
import pandas as pd

class RandomWalk3D:
    def __init__(self, time_step: float, num_steps: int, D:float, seed: int | None = None):
        self.time_step = time_step
        self.num_steps = num_steps
        self.D = D
        self.seed = seed