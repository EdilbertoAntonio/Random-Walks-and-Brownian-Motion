from src.random_walk import RandomWalk      
from src.brownian_motion import BrownianMotion                               
import matplotlib.pyplot as plt

print('Welcome, what do you want to simulate')
print('1 for random walk, 2 for 3D random walk')
simulation = int(input('Enter your selection: '))

if simulation == 1:
    random_walk = RandomWalk(time_step=0.5, num_steps=50, num_walks=5)
    walks = random_walk.simulate()
    fig = random_walk.plot()
    print(walks)
    plt.show()

elif simulation == 2:
    random_walk_3d = BrownianMotion(time_step=1*10**(-6), num_steps=300)
    motion = random_walk_3d.simulate()
    # print(motion)
    # random_walk_3d.plot()
    animation = random_walk_3d.animate(frame_duration=50, output_file='brownian_animation.html')