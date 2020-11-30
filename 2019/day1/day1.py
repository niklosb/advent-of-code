file = "input.txt"


def get_fuel_requirement(mass, fuel_mass):
    mass_fuel_requirement = mass // 3 - 2

    if mass_fuel_requirement <= 0:
        return fuel_mass
    else:
        fuel_mass += mass_fuel_requirement
        return get_fuel_requirement(mass_fuel_requirement, fuel_mass)


if __name__ == '__main__':
    total_fuel_requirement = 0

    with open(file) as f:
        for line in f:
            mass = int(line.strip())
            total_fuel_requirement += get_fuel_requirement(mass, 0)

    print total_fuel_requirement