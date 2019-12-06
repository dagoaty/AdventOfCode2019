import sys

def apply_state(inputs, noun, verb):
    inputs[1] = noun
    inputs[2] = verb
    return inputs


def run_opscode(inputs, user_input):
    pos = 0
    size = len(inputs)
    while pos <= size:
        action = str(inputs[pos]).zfill(5)[-2:]
        if action == '01' or action == '02':
            chunk_size = 4
        elif action == '03' or action == '04':
            chunk_size = 2
        elif inputs[pos] == 99:
            break
        else:
            sys.stderr.write("Unknown Opscode instruction: %s" % action)
            exit(1)
        inputs = run_chunk(chunk_size, inputs, pos, user_input)
        pos += chunk_size
    return inputs


def run_chunk(chunk_size, inputs, pos, user_input):
    action, params = str(inputs[pos]).zfill(5)[-2:], str(inputs[pos]).zfill(5)[-3::-1]
    nums = []
    if action == '01' or action == '02':
        if params[0] == '0':
            nums.append(inputs[inputs[pos+1]])
        else:
            nums.append(inputs[pos+1])

        if params[1] == '0':
            nums.append(inputs[inputs[pos+2]])
        else:
            nums.append(inputs[pos+2])

        if action == '01':
            inputs[inputs[pos+3]] = nums[0] + nums[1]
        if action == '02':
            inputs[inputs[pos+3]] = nums[0] * nums[1]
        return inputs

    elif action == '03':
        inputs[inputs[pos+1]] = user_input
        return inputs

    elif action == '04':
        print(inputs[inputs[pos+1]])
        return inputs

    elif action == '05':
        return inputs

    elif action == '06':
        return inputs

    elif action == '07':
        return inputs

    elif action == '08':
        return inputs


def read_inputs(file):
    loaded = list()
    f = open(file, "r")
    for line in f:
        loaded += line.split(",")
    inputs = [int(i) for i in loaded]
    return inputs
