def part1():
    pass


def part2():
    pass


def read_input(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines


if __name__ == '__main__':
    data = read_input("./resources/template.txt")
    part1(data)
    part2(data)