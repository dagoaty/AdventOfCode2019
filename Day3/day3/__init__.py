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


def distance_to_point(start, end, lines):
    distance = 0
    for line in lines:
        distance += measure_path(start, end, line)
    return distance


def measure_path(start, end, line):
        x = start[0]
        y = start[1]
        coords = []
        distance = 1
        for path in line:
            d, l = path[0], int(path[1:])
            step = 0
            if d == "R":
                while step < l:
                    x += 1
                    now = [x, y]
                    if now == end:
                        distance += step
                        return distance
                    coords += [now]
                    step += 1
                distance += l
            if d == "L":
                while step < l:
                    x -= 1
                    now = [x, y]
                    if now == end:
                        distance += step
                        return distance
                    coords += [now]
                    step += 1
                distance += l
            if d == "U":
                while step < l:
                    y += 1
                    now = [x, y]
                    if now == end:
                        distance += step
                        return distance
                    coords += [now]
                    step += 1
                distance += l
            if d == "D":
                while step < l:
                    y -= 1
                    now = [x, y]
                    if now == end:
                        distance += step
                        return distance
                    coords += [now]
                    step += 1
                distance += l
        return distance


def find_closest(common, loc):
    common_distance = {}
    for coord in common:
        x0, y0 = loc[0], loc[1]
        x1, y1 = coord[0], coord[1]
        x_distance = abs(x1 - x0)
        y_distance = abs(y1 - y0)
        sum_distance = x_distance + y_distance
        common_distance[sum_distance] = coord
    return sorted(common_distance.keys())[1]
