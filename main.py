from src.random_walk import RandomWalk                                      
import matplotlib.pyplot as plt

random_walk = RandomWalk(time_step=0.5, num_steps=50, num_walks=5)
walks = random_walk.simulate()
fig = random_walk.plot()

# print(walks)
plt.show()