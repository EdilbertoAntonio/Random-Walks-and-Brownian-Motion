from src.random_walk import RandomWalk                                      
import matplotlib.pyplot as plt

random_walk = RandomWalk(time_step=0.5, num_steps=200, num_walks=50)
walks = random_walk.simulate()
fig = random_walk.plot()

plt.show()
