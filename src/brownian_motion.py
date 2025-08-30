import numpy as np
import pandas as pd
import plotly.express as px
from plotly.offline import plot

class BrownianMotion:
    def __init__(self, time_step: float, num_steps: int, seed: int | None = None) -> None:
        '''
        Initialize a 3D brownian motion simulator of a particule with temperature o 300 kelvin and radius 1e-6 meters
        Args:
            time_step (float): time step size
            num_stp (int): number of steps to simulate
            seed (int | None, optional): random seed for reproductibility. Default None
        '''
        self.time_step = time_step
        self.num_steps = num_steps
        self.seed = seed
        self.brownian_motion = None

    def simulate(self) -> pd.DataFrame:
        '''
        Simulate the brownian motion of one particule in 3 dimensions
        Returns a pandas dataframe with the trajectory of shape(num_steps, 3) and columns ['x','y','z']
        '''
        if self.seed is not None:
            np.random.seed(self.seed)

        boltzmann_const = 1.38e-23
        temperature = 300
        radius = 1e-6
        diffusion_coeff = (boltzmann_const * temperature) / radius

        time = np.arange(self.num_steps) * self.time_step
        random_steps = np.random.normal(0,1,(self.num_steps,3))
        self.brownian_motion = pd.DataFrame(
            np.cumsum((np.sqrt(2 * self.time_step * diffusion_coeff)* random_steps), axis = 0),
            index = time,
            columns = ['x', 'y', 'z']
        )

        return self.brownian_motion
    
    def plot(self) -> str:
        '''
        Generate and return a 3D interactive plot of the brownian motion trajectory
        '''
        if self.brownian_motion is None:
            raise ValueError('You must call simulate() before plot()')
        
        fig = (px.line_3d(data_frame = self.brownian_motion, x = 'x', y = 'y', z = 'z'))
        fig.update_traces(line_color='blue', line={'width': 6})

        return plot(fig)