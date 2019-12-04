def read_inputs(file):
    loaded = list()
    f = open(file, "r")
    for line in f:
        loaded += line.split(",")
    return inputs


def length_is_six(num):
    length = len(str(num))
    if length == 6:
        return True
    return False

def in_range(start, end, num):
    if start <= num <= end:
        return True
    return False


def has_double(num):
    has_double = 0
    chrs = str(num)
    length = len(chrs)
    n = 1
    while n < length:
        if chrs[n] == chrs[n-1]:
            return True
        n += 1
    return False


def increases(num):
    chrs = str(num)
    length = len(chrs)
    n = 1
    while n < length:
        if chrs[n] < chrs[n-1]:
            return False
        n += 1
    return True
