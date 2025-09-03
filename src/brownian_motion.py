import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot

class BrownianMotion:
    def __init__(self, time_step: float, num_steps: int, seed: int | None = None) -> None:
        '''
        Initialize a 3D brownian motion simulator of a particle with temperature o 300 kelvin and radius 1e-6 meters
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
        Simulate the brownian motion of one particle in 3 dimensions
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
    
    def animate(self, frame_duration: int = 50, output_file: str = None, auto_open: bool = False) -> str:
        '''
        Generate an interactive animated 3D plot using Plotly
        Args:
            frame_duration: milliseconds between frames
            output_file: optional filename to save HTML
        '''
        if self.brownian_motion is None:
            raise ValueError('You must call simulate() before animate()')
        
        # Create figure
        fig = go.Figure()
        
        # Add initial trace
        fig.add_trace(go.Scatter3d(
            x=self.brownian_motion['x'].iloc[:1],
            y=self.brownian_motion['y'].iloc[:1],
            z=self.brownian_motion['z'].iloc[:1],
            mode='lines',
            line=dict(color='#66BD63', width=4),
            name='Motion'
        ))

        fig.add_trace(go.Scatter3d(
            x=self.brownian_motion['x'].iloc[:1],
            y=self.brownian_motion['y'].iloc[:1],
            z=self.brownian_motion['z'].iloc[:1],
            mode='markers',
            marker=dict(size=8, color='#006837'),
            name='Particle'
        ))
        
        # Create frames for animation
        frames = []
        for i in range(1, len(self.brownian_motion)):
            frames.append(go.Frame(
                data=[
                    go.Scatter3d(
                        x=self.brownian_motion['x'].iloc[:i],
                        y=self.brownian_motion['y'].iloc[:i],
                        z=self.brownian_motion['z'].iloc[:i],
                        mode='lines',
                        line=dict(color='#66BD63', width=4)
                    ),
                    go.Scatter3d(
                        x=[self.brownian_motion['x'].iloc[i-1]],
                        y=[self.brownian_motion['y'].iloc[i-1]],
                        z=[self.brownian_motion['z'].iloc[i-1]],
                        mode='markers',
                        marker=dict(size=8, color='#006837')
                    )
                ],
                name=f'frame_{i}'
            ))
        
        # Add frames to figure
        fig.frames = frames
        
        # Animation settings
        fig.update_layout(
            updatemenus=[dict(
                type='buttons',
                buttons=[dict(
                    label='Play',
                    method='animate',
                    args=[None, dict(
                        frame=dict(duration=frame_duration, redraw=True),
                        fromcurrent=True,
                        mode='immediate'
                    )]
                )]
            )],
            sliders=[dict(
                steps=[dict(
                    method='animate',
                    args=[[f'frame_{k}'], dict(mode='immediate', frame=dict(duration=frame_duration))],
                    label=f'{self.brownian_motion.index[k]*10e5:.2f}µs'
                ) for k in range(0, len(self.brownian_motion),len(self.brownian_motion)//10)],
                active=0
            )]
        )
        
        # Set layout
        fig.update_layout(
            scene=dict(
                xaxis_title='X',
                yaxis_title='Y',
                zaxis_title='Z',
                aspectmode='cube'
            ),
            title='Brownian Motion Animation'
        )
        
        if output_file:
            fig.write_html(output_file, auto_open=auto_open)

        plot(fig, auto_open=True)
        
        return plot(fig, output_type='div')