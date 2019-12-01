def read_inputs(file):
    inputs = list()
    f = open(file, "r")
    for line in f:
        inputs.append(int(line.rstrip()))
    return inputs


def calc_fuel(mass):
    fuel = mass // 3 - 2
    return fuel


def total_fuel(masses):
    total = 0
    for mass in masses:
        extra_fuel = calc_fuel(mass)
        if extra_fuel > 0:
            total += extra_fuel
            masses.append(extra_fuel)
    return total