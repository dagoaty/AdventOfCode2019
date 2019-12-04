#!/usr/bin/env python3

import day4, sys

start = int(sys.argv[1])
end = int(sys.argv[2])

results = list()
cur_num = start

while cur_num <= end:
    if not day4.length_is_six(cur_num):
        cur_num += 1
        continue

    if not day4.in_range(start, end, cur_num):
        cur_num += 1
        continue

    if not day4.increases(cur_num):
        cur_num += 1
        continue

    if not day4.pair_exists(cur_num):
        cur_num += 1
        continue

    results.append(cur_num)
    cur_num += 1

print("There are %s possible passwords" % len(results))