#!/usr/bin/env python3

import sys
import day5

filename = sys.argv[1]
inputs = day5.read_inputs(filename)
user_input = 1

outputs = day5.run_opscode(inputs, user_input)
