from src.random_walk import CaminataAleatoria
import matplotlib.pyplot as plt

# Crear simulación
prueba = CaminataAleatoria(deltaT=0.5, N=200, P=50)
prueba.generar()
fig = prueba.graficar()

plt.show()
