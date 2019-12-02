#!/usr/bin/env python3

import sys
import day2

filename = sys.argv[1]
inputs = day2.read_inputs(filename)

state = day2.restore_state(inputs)
outputs = day2.run_opscode(state)

print("Position 0 is: %s" % outputs[0])
