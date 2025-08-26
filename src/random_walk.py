import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from numpy.typing import NDArray

class CaminataAleatoria:
    def __init__(self, deltaT: float, N: int, P: int, seed: int | None = None):
        self.deltaT = deltaT
        self.N = N
        self.P = P
        self.seed = seed
        self.tiempo: NDArray = np.array([])
        self.caminatas: NDArray = np.array([])
        
    def generar(self) -> None:
        ''' Generar las P caminatas aleatorias con N pasos '''
        if self.seed is not None:
            np.random.seed(self.seed)
            
        self.tiempo = np.arange(self.N) * self.deltaT
        factor_aleatorio = np.random.normal(0,1,(self.N, self.P))
        self.caminatas = np.cumsum(np.sqrt(self.deltaT) * factor_aleatorio, axis=0)
        
    def graficar(self) -> Figure:
        ''' Realiza y devuelve la gráfica de las P caminatas '''
        if self.caminatas.size ==0:
            raise ValueError('Genera primero lo camniatas con .generar()')
        
        fig = plt.figure(figsize=(15, 8))

        plt.title(f'{self.P} Caminatas aleatorias', fontsize=16)
        plt.xlabel("Tiempo", fontsize=14)
        plt.ylabel("X_i", fontsize=14)
        plt.grid()
      
        plt.plot(self.tiempo, self.caminatas)
            
        return fig 