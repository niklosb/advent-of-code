input = "382345-843167"
#input = "777778-777779"

start = int(input.split("-")[0])
stop = int(input.split("-")[1])


def has_double(number):
    for i in range(len(str(number))-1):
        if str(number)[i] == str(number)[i+1]:
            return True
    return False


def has_double_strict(number):
    for i in range(len(str(number))-1):
        if str(number)[i] == str(number)[i+1]:
            before_strict = True
            after_strict = True

            if i > 0:
                if str(number)[i] == str(number)[i-1]:
                    before_strict = False

            if i < len(str(number))-2:
                if str(number)[i] == str(number)[i+2]:
                    after_strict = False

            if before_strict & after_strict:
                return True

    return False


def is_monotonically_increasing(number):
    for i in range(len(str(number))-1):
        if str(number)[i] > str(number)[i+1]:
            return False
    return True


if __name__ == '__main__':
    count = 0
    for i in range(start, stop):
        if has_double_strict(i) & is_monotonically_increasing(i):
            print i
            count += 1
    print count