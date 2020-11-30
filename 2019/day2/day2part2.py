file = "input.txt"

def calculate(program):
    pointer = 0

    while(pointer < len(program)):
        print program[pointer]
        opcode = program[pointer]


        if opcode == 99:
            return program
        if opcode == 1:
            param1, param2, param3 = program[pointer+1], program[pointer+2], program[pointer+3]
            program[param3] = program[param1] + program[param2]
            pointer += 4
        if opcode == 2:
            param1, param2, param3 = program[pointer+1], program[pointer+2], program[pointer+3]
            program[param3] = program[param1] * program[param2]
            pointer += 4
        if opcode == 3:
            param1 = program[pointer+1]
            program[param1] = program[input_val]
            pointer += 2
        if opcode == 4:
            param1 = program[pointer+1]
            program[output_val] = program[param1]
            pointer += 2

    return program


if __name__ == '__main__':
    for error in range(10000):
        noun = error // 100
        verb = error % 100

        with open(file) as f:
            for line in f:
                program = [int(i) for i in line.split(',')]

                program[1] = noun
                program[2] = verb

                print error, calculate(program)[0]