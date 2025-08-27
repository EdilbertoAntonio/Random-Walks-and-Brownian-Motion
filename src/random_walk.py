import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from numpy.typing import NDArray

class RandomWalk:
    def __init__(self, time_step: float, num_steps: int, num_walks: int, seed: int | None = None):
        self.time_step = time_step
        self.num_steps = num_steps
        self.num_walks = num_walks
        self.seed = seed
        self.time: NDArray = np.array([])
        self.walks: NDArray = np.array([])
        
    def simulate(self) -> np.ndarray:
        ''' Generate num_walks random walks, each with num_steps steps.
            Returns a ndarray of shape (num_steps, num_walks) containing the simulated walks.
        '''
        if self.seed is not None:
            np.random.seed(self.seed)
            
        self.time = np.arange(self.num_steps) * self.time_step
        random_steps = np.random.normal(0,1,(self.num_steps, self.num_walks))
        self.walks = np.cumsum(np.sqrt(self.time_step) * random_steps, axis=0)

        return self.walks
        
    def plot(self) -> Figure:
        ''' Generate and return a graph containing all walks '''
        if self.walks.size ==0:
            raise ValueError('You must first generate the walks with .simulate()')
        
        fig = plt.figure(figsize=(15, 8))

        plt.title(f'{self.num_walks} Randon Walks', fontsize=16)
        plt.xlabel("Time", fontsize=14)
        plt.ylabel("X_i", fontsize=14)
        plt.grid()
      
        plt.plot(self.time, self.walks)
            
        return fig 