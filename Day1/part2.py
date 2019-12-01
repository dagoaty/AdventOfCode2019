#!/usr/bin/env python3

import sys
from day1 import read_inputs, total_fuel

filename = sys.argv[1]
inputs = read_inputs(filename)

print("Total fuel: %s" % total_fuel(inputs))
