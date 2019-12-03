#!/usr/bin/env python3

import day3, sys

filename = sys.argv[1]
inputs = day3.read_inputs(filename)
lines = []
common = []
loc = [0,0]

for input in inputs:
    line = day3.calc_coords(input, loc)
    lines.append(line)

for point in lines[0]:
    if point in lines[1]:
        common.append(point)

answer = day3.find_closest(common, loc)
print("Closest intersection is: %s" % answer)
