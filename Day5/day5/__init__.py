import sys

def apply_state(inputs, noun, verb):
    inputs[1] = noun
    inputs[2] = verb
    return inputs


def run_opscode(inputs):
    pos = 0
    size = len(inputs)
    while pos <= size:
        if inputs[pos] == 1 or inputs[pos] == 2:
            chunk_size = 4
        elif inputs[pos] == 3 or inputs[pos] ==4:
            chunk_size = 2
        elif inputs[pos] == 99:
            break
        else:
            sys.stderr.write("Unknown Opscode instruction")
            exit(1)
        inputs = run_chunk(chunk_size, inputs, pos)
        pos += chunk_size
    return inputs


def run_chunk(chunk_size, inputs, pos):
    action = inputs[pos]
    if action == 1:
        inputs[inputs[pos+3]] = inputs[inputs[pos+1]] + inputs[inputs[pos+2]]
        return inputs
    elif action == 2:
        inputs[inputs[pos+3]] = inputs[inputs[pos+1]] * inputs[inputs[pos+2]]
        return inputs
    elif action == 3:
        return inputs
    elif action = 4:
        return inputs
        


def read_inputs(file):
    loaded = list()
    f = open(file, "r")
    for line in f:
        loaded += line.split(",")
    inputs = [int(i) for i in loaded]
    return inputs
