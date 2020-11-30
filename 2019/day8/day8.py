import numpy as np
import matplotlib.pyplot as plt

file = "input.txt"
# file = "test2.txt"


def part1():
    width = 25
    height = 6
    layer_size = width * height

    with open(file) as f:
        for line in f:
            min_zeros = 9999999999999
            mult = 0

            layers = len(line) / (layer_size)

            layer_images = []
            for i in range(layers):
                value_counts = {}
                layer = list(line[(i * layer_size): ((i+1) * layer_size)])

                for i in set(layer):
                    value_counts[i] = sum([x == i for x in layer])
                layer_images.append(value_counts)

            for layer_image in layer_images:
                print layer_image
                if "0" in layer_image.keys():
                    if layer_image["0"] < min_zeros:
                        min_zeros = layer_image["0"]

                        if ("1" in layer_image.keys()) & ("2" in layer_image.keys()):
                            mult = layer_image["1"] * layer_image["2"]

            print min_zeros, mult

def part2():
    width = 25
    height = 6
    layer_size = width * height

    with open(file) as f:
        for line in f:

            layers = len(line) / (layer_size)

            layer_images = []
            final_image = np.ones((height, width)) * 2
            for i in range(layers):
                layer = list(line[(i * layer_size): ((i+1) * layer_size)])
                image = np.array(layer).reshape(height, width)
                # print image

                for i in range(height):
                    for j in range(width):
                        if (image[i][j] != 2) & (final_image[i][j] == 2):
                            final_image[i][j] = image[i][j]

            for i in final_image:
                print i

            plt.imshow(final_image)
            plt.show()

if __name__ == '__main__':

    part2()