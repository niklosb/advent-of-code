import numpy as np
import matplotlib.pyplot as plt

file = "input.txt"
# file = "test.txt"


def dist(a,b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def collinear(i,j,k):
    return (i[1] - j[1]) * (i[0] - k[0]) == (i[1] - k[1]) * (i[0] - j[0])


def part1():
    grid = []
    asteroids = []
    line_of_sight = {}

    with open(file) as f:
        for line in f:
            grid.append(list(line.strip()))

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                asteroids.append((x,y))

    print "asteroids:", asteroids

    for station_location in asteroids[:]:
        detected_asteroids = set()
        for asteroid in asteroids:
            if station_location != asteroid:
                vector = (station_location[0]-asteroid[0], station_location[1]-asteroid[1])
                distance = dist((0,0), vector)
                unit_vector = (round(vector[0] / distance,5) , round(vector[1] / distance,5))
                if unit_vector not in detected_asteroids:
                    if station_location == (1,0):
                        print unit_vector
                    detected_asteroids.add(unit_vector)

        line_of_sight[station_location] = len(detected_asteroids)
    print line_of_sight

    most_visible = 0
    best_station_location = (-1,-1)
    for station_location in asteroids:
        if line_of_sight[station_location] > most_visible:
            most_visible = line_of_sight[station_location]
            best_station_location = station_location

    print best_station_location, most_visible

def part2():
    pass

if __name__ == '__main__':
    part1()