#!/usr/bin/env python

import sys

data = []
widths = {}

for line in sys.stdin:
    l = line.strip().split('\t')
    data.append(l)
    
    i = 0
    for x in l:
        if len(x) > widths.get(i, 0):
            widths[i] = len(x)
        i += 1

for row in data:
    i = 0
    formatted_row = []
    for element in row:
        meta_str = '%+' + str(widths.get(i,10)) + 's'
        i += 1
        formatted_row.append(meta_str % element)

    print ' | '.join(formatted_row)
