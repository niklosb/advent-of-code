from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Planet:
    def __init__(self, x=0, y=0, z=0):
        self.px, self.py, self.pz = x, y, z
        self.vx, self.vy, self.vz = 0, 0, 0

    def __repr__(self):
        return "pos=<x={self.px}, y={self.py}, z={self.pz}>, vel=<x={self.vx}, y={self.vy}, z={self.vz}>".format(**locals())

    def __str__(self):
        return "pos=<x={self.px}, y={self.py}, z={self.pz}>, vel=<x={self.vx}, y={self.vy}, z={self.vz}>".format(**locals())

    def update_position(self):
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz

    def update_velocity(self, planets):
        for planet in planets:
            if planet != self:
                x, y, z = planet.get_position()
                delta_x, delta_y, delta_z = x - self.px, y - self.py, z - self.pz

                if delta_x != 0:
                    self.vx += (delta_x) / abs(delta_x)
                if delta_y != 0:
                    self.vy += (delta_y) / abs(delta_y)
                if delta_z != 0:
                    self.vz += (delta_z) / abs(delta_z)

    def get_position(self):
        return self.px, self.py, self.pz

    def get_velocity(self):
        return self.vx, self.vy, self.vz

    def get_potential_energy(self):
        return abs(self.px) + abs(self.py) + abs(self.pz)

    def get_kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def get_total_energy(self):
        return self.get_potential_energy() * self.get_kinetic_energy()


def day12(coordinates):
    planets = []
    steps = 1000
    matches = set()

    for coordinate in coordinates:
        coordinate = coordinate.strip().replace(" ", "")[1:-1].split(",")
        for i, val in enumerate(coordinate):
            coordinate[i] = int(val[2:])
        planets.append(Planet(coordinate[0], coordinate[1], coordinate[2]))

    for step in range(steps+1):
        print "After {step} steps:".format(**locals())
        for planet in planets:
            print planet
        print "Total Energy:", sum([planet.get_total_energy() for planet in planets])
        print ""

        for planet in planets:
            planet.update_velocity(planets)
        for planet in planets:
            planet.update_position()


def day12_2(coordinates):
    planets = []
    steps = 1000
    matches = set()

    for coordinate in coordinates:
        coordinate = coordinate.strip().replace(" ", "")[1:-1].split(",")
        for i, val in enumerate(coordinate):
            coordinate[i] = int(val[2:])
        planets.append(Planet(coordinate[0], coordinate[1], coordinate[2]))

    step, total_energy = 0, 999
    while total_energy != 0:

        for planet in planets:
            planet.update_velocity(planets)
        for planet in planets:
            planet.update_position()

        total_energy = sum([planet.get_total_energy() for planet in planets])
        step +=1

        if step % 10000 == 0:
            print step

    print step, total_energy
    for planet in planets:
        print planet


day12_2(open("test.txt").readlines())
# day12(open("test.txt").readlines())


