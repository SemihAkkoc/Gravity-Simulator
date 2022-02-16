from math import sqrt


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)
        self.magnitude = sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        return Vector2(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Vector2(self.x-other.x, self.y-other.y)

    def __mul__(self, scale):
        return Vector2(self.x*scale, self.y*scale)

    def cross_product(self, other):
        Cz = self.x * other.y - self.y * other.x
        return Vector3(0, 0, Cz)

    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def copy(self):
        return Vector2(self.x, self.y)


class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        return Vector3(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Vector3(self.x-other.x, self.y-other.y, self.z-other.z)

    def cross_product(self, other):
        Cx = self.y*other.z - self.z-other.y
        Cy = other.x*self.z - other.z*self.x
        Cz = self.x*other.y - self.y*other.x
        return Vector3(Cx, Cy, Cz)

    def dot_product(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'


