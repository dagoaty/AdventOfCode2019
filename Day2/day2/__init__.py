def restore_state(inputs):
    inputs[1] = 12
    inputs[2] = 2
    return inputs


def run_opscode(inputs):
    pos = 0
    size = len(inputs)
    while pos <= size:
        if inputs[pos] == 99:
            break
        chunk = inputs[pos:pos+3]
        value = run_chunk(chunk, inputs)
        inputs[inputs[pos+3]] = value
        pos += 4
    return inputs


def run_chunk(chunk, inputs):
    action = chunk[0]
    num1 = inputs[chunk[1]]
    num2 = inputs[chunk[2]]
    if action == 1:
        return num1 + num2
    if action == 2:
        return num1 * num2


def read_inputs(file):
    loaded = list()
    f = open(file, "r")
    for line in f:
        loaded += line.split(",")
    inputs = [int(i) for i in loaded]
    return inputs
