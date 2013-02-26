#!/usr/bin/env python

import sys
from optparse import OptionParser


def is_numeric(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

parser = OptionParser(usage="usage: %prog [options] filename", version="%prog 1.0")
parser.add_option("-c", "--column", dest="columns_to_round", default=0, help="Columns to round")
parser.add_option("-p", "--precision", dest="precision", default=0, help="Precision")
(options, args) = parser.parse_args()

keys = [ int(k)-1 for k in options.columns_to_round.split(',')]
precision = int(options.precision)

for line in sys.stdin:
    l = line.strip().split("\t")
    for k in keys:
        if is_numeric(l[k]):
            if precision == 0:
                l[k] = int(float(l[k]))
            else:
                l[k] = round(float(l[k]), precision)

    print "\t".join([str(x) for x in l])
