from vector import Vector2
from math import pi

dt = 1 / 60


class Particles:
    G = 6.67408 * 10 ** (-1)

    def __init__(self, main_frame, position=[.0, .0], velocity=[.0, .0], diameter=10, density=280, color='black'):
        self.dead = False

        self.density = density
        self.diameter = diameter
        self.mass = self.density * pi * ((self.diameter / 2) ** 2)

        self.position = self.cm(position)
        self.velocity = Vector2(velocity[0], velocity[1])
        self.acceleration = Vector2(0, 0)

        self.main_frame = main_frame
        self.particle = main_frame.create_oval(self.position.x, self.position.y, self.position.x + diameter, self.position.y + diameter, fill=color)


    def cm(self, position):
        # determine the position of the center of mass
        return Vector2(position[0] + (self.diameter / 2), position[1] + (self.diameter / 2))

    def update_velocity(self, other):
        position = self.position - other.position
        if not (position.magnitude < self.diameter):
            force = position * (1 / position.magnitude) * (Particles.G * self.mass * other.mass / position.magnitude ** 2)
            self.acceleration += force * (-1 / self.mass)
            other.acceleration += force * (1 / other.mass)
            # print(self.acceleration.magnitude)
        else:
            self.dead = True
            other.dead = True

    def update(self):
        temp = self.position.copy()

        self.position += self.velocity * dt + self.acceleration * (0.5 * (dt ** 2))
        self.velocity += self.acceleration * dt

        dposition = self.position - temp

        self.main_frame.move(self.particle, dposition.x, dposition.y)
