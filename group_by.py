#!/usr/bin/env python

import sys
from optparse import OptionParser

parser = OptionParser(usage="usage: %prog [options] filename", version="%prog 1.0")
parser.add_option("-k", "--key", dest="group_by_key", default=0, help="Key to group by")
parser.add_option("-c", "--column", dest="sum_column", default=1, help="Column to sum")
parser.add_option("-t", action="store_true", dest="title_row", default=False, help="Is there a title row / header")
(options, args) = parser.parse_args()

keys = [ int(k)-1 for k in options.group_by_key.split(',')]
columns = [ int(k)-1 for k in options.sum_column.split(',')]
 
grouped = {}

if options.title_row:
    l = next(sys.stdin).strip().split("\t")
    keys_title = "\t".join([l[x] for x in keys])
    columns_title = "\t".join([l[x] for x in columns])
    title_row = "%s\t%s" % (keys_title, columns_title)

for line in sys.stdin:
    l = line.strip().split("\t")
    k = "\t".join([l[x] for x in keys])
    grouped.setdefault(k, {})
    for column in columns:
        grouped[k][column] = grouped[k].get(column, 0) + float(l[column])

if options.title_row:
    print title_row

for k,columns in grouped.iteritems():
    summed_columns = "\t".join([str(x) for x in columns.values()])
    print "%s\t%s" % (k, summed_columns)
