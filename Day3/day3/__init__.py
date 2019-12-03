def read_inputs(file):
    inputs = []
    f = open(file, "r")
    for line in f:
        inputs.append(line.rstrip().split(","))
    return inputs


def calc_coords(paths, loc):
    coords = [loc]
    for path in paths:
        d, l = path[0], int(path[1:])
        loc, new_coords = get_new_coords(loc, d, l)
        coords += new_coords
    return coords


def get_new_coords(loc, d, l):
    x = loc[0]
    y = loc[1]
    coords = []
    step = 0
    if d == "R":
        while step < l:
            x += 1
            coords += [[x, y]]
            step += 1
    if d == "L":
        while step < l:
            x -= 1
            coords += [[x, y]]
            step += 1
    if d == "U":
        while step < l:
            y += 1
            coords += [[x, y]]
            step += 1
    if d == "D":
        while step < l:
            y -= 1
            coords += [[x, y]]
            step += 1
    return ([x, y], coords)
