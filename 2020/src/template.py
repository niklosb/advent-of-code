def part1(data):
    pass


def part2(data):
    pass


def read_data(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    data = read_data("./resources/template.txt")
    part1(data)
    part2(data)