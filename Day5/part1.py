#!/usr/bin/env python3

import sys
import day5

filename = sys.argv[1]
inputs = day5.read_inputs(filename)

state = day5.apply_state(inputs, 12, 2)
outputs = day5.run_opscode(state)

print("Position 0 is: %s" % outputs[0])
