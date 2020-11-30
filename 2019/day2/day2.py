file = "input.txt"

error = 1202


def calculate(program, input):
    for i in range(len(program)//4):

        opcode = program[i*4 + 0]
        input1 = program[i*4 + 1]
        input2 = program[i*4 + 2]
        output = program[i*4 + 3]

        if opcode == 99:
            return program
        elif opcode == 1:
            program[output] = program[input1] + program[input2]
        elif opcode == 2:
            program[output] = program[input1] * program[input2]

    return program


if __name__ == '__main__':
    with open(file) as f:
        for line in f:
            program = [int(i) for i in line.split(',')]

            program[1] = error // 100
            program[2] = error % 100

            print calculate(program)[0]