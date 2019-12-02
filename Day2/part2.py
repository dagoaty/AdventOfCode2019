#!/usr/bin/env python3

import sys
import day2

filename = sys.argv[1]

noun = 0
while noun < 100:
    verb = 0
    while verb < 100:
        inputs = day2.read_inputs(filename)

        state = day2.apply_state(inputs, noun, verb)
        outputs = day2.run_opscode(state)
        if outputs[0] == 19690720:
            calc = 100 * noun + verb
            print("Noun: %s\nVerb: %s\nAnswer: %s\n\n" % (noun, verb, calc))
        verb += 1
    noun += 1
