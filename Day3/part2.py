#!/usr/bin/env python3

import day3, sys

filename = sys.argv[1]
inputs = day3.read_inputs(filename)
lines = []
value = []
common = []
loc = [0,0]

for input in inputs:
    line = day3.calc_coords(input, loc)
    lines.append(line)

for point in lines[0]:
    if point in lines[1]:
        common.append(point)

# common points in common at this point
# need to figure out sum of lines 1 and 2 up to each point

for point in common:
    value.append(day3.distance_to_point(loc, point, inputs))
value.sort()
print("Shortest path is: %s" % value[0])
