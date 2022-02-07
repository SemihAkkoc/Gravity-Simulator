from math import pi
from turtle import position
import numpy as np


class Particals:
    G = 6.67408 * (10**(0))
    time_interval = 1/30

    def __init__(self, main_frame, position=[.0,.0], diameter=10, density=10, color='black'):
        self.density = density
        self.diameter = diameter
        self.mass = self.density * self.area()
        self.velocity, self.acceleration, self.force, self.dposition = np.array([.0,.0]),np.array([.0,.0]),np.array([.0,.0]),np.array([.0,.0])
        self.position = np.array(self.cm(position))
        
        self.main_frame = main_frame
        self.partical = main_frame.create_oval(position[0], position[1], position[0]+diameter, position[1]+diameter, fill=color)
    
    def area(self):
        # calculating area
        return pi*((self.diameter/2)**2)

    def cm(self, position):
        # determines the position of center of mass
        return [position[0]+(self.diameter/2), position[1]+(self.diameter/2)]

    def sign(self):
        HEIGHT = self.main_frame.winfo_height()
        WIDTH = self.main_frame.winfo_width()

        if self.position[0] >= WIDTH/2 and self.position[1] >= HEIGHT/2:
            return [-1, -1]
        elif self.position[0] >= WIDTH/2 and self.position[1] < HEIGHT/2:
            return [-1, 1]
        elif self.position[0] < WIDTH/2 and self.position[1] >= HEIGHT/2:
            return [1, -1]
        elif self.position[0] < WIDTH/2 and self.position[1] < HEIGHT/2:
            return [1, 1]

    def distance(self, other, i):
        return abs(int(self.position[i]) - int(other.position[i]))

    def update_velocity(self, other):
        force_x, force_y = 0, 0
        if self.distance(other, 0) > 3:
            try:
                force_x = (Particals.G * self.mass * other.mass) / (self.distance(other, 0) ** 2)
            except ZeroDivisionError:
                force_x = 0
        if self.distance(other, 1) > 3:
            try:
                force_y = (Particals.G * self.mass * other.mass) / (self.distance(other, 1) ** 2)
            except ZeroDivisionError:
                force_y = 0

        print(self.sign(), other.sign())
        print(self.force, other.force)
        print(force_x)
        print(self.dposition, other.dposition)

        # i am really not sure about this math here especially position and velocity transition
        self.force = np.array([self.sign()[0]*force_x, self.sign()[1]*force_y])
        self.acceleration += (self.force / self.mass)
        self.velocity += self.acceleration * Particals.time_interval
        past_position = np.array(self.position)
        self.position += self.velocity + 0.5 * self.acceleration * (Particals.time_interval**2)
        self.dposition = [self.position[0]-past_position[0], self.position[1]-past_position[1]]
        # print(f' force {self.force}\n acceleration {self.acceleration}\n velocity {self.velocity}\n *POSITION {self.position}\n *PAST POSITION {past_position}')
        
        other.force = np.array([other.sign()[0]*force_x, other.sign()[1]*force_y])
        other.acceleration += (other.force / other.mass)
        other.velocity += other.acceleration * Particals.time_interval
        past_position = np.array(other.position)
        other.position += other.velocity + 0.5 * other.acceleration * (Particals.time_interval**2)
        other.dposition = [other.position[0]-past_position[0], other.position[1]-past_position[1]]
        

    def update(self):
        # check if we need to turn this into integers
        if self.position[0] >= self.main_frame.winfo_width() or self.position[0]<0:
            self.velocity[0] = -self.velocity[0]

        if self.position[1] >= self.main_frame.winfo_height() or self.position[1]<0:
            self.velocity[1] = -self.velocity[1]

        self.main_frame.move(self.partical, int(self.dposition[0]), int(self.dposition[1]))
