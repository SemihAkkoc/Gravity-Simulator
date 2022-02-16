from particles import Particles, dt
from math import sin, cos, pi
import random

INITIAL_VELOCITY = 100

class Groups:
    def __init__(self, main_frame, num):
        self.num = num
        self.group = [Particles(main_frame, position=distribute(self.num, x, main_frame), velocity=distribute_velocity(self.num, x), color=random_color()) for x in range(self.num)]

    def update(self):
        for i in range(self.num):
            for j in range(1+i, self.num):
                self.group[i].update_velocity(self.group[j])
        
        # print(self.group[0].position, self.group[1].position)
        for particle in self.group:
            if not particle.dead:
                particle.update()


def distribute(num, i, size, radius=300):
    # complex math
    origin = [(size.winfo_height()-6)/2, (size.winfo_width()-6)/2]
    degree = 2*pi/num
    pos = [origin[0]+radius*cos(degree*i), origin[1]+radius*sin(degree*i)]
    return pos


def distribute_velocity(num, i, velocity=INITIAL_VELOCITY):
    # complex math
    degree = 2*pi/num
    vel = [velocity*sin(degree*i), velocity*cos(degree*i)]
    return vel


def random_color():
    colors = ['red', 'green', 'black', 'blue', 'cyan', 'magenta']
    return random.choice(colors)
