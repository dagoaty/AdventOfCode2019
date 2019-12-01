#!/usr/bin/env python3

import sys
from day1 import read_inputs, calc_fuel

filename = sys.argv[1]
inputs = read_inputs(filename)
total_fuel = 0

for input in inputs:
    total_fuel += calc_fuel(input)

print("Total fuel: %s" % total_fuel)
