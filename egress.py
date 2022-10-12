#!/bin/python3

# ---------- Imported Modules
import csv
import random
import sys

def csvGenerator(span,limit,output):
    row = []
    f = open(output, 'w')
    writehead = csv.writer(f)

    for i in range(1,span):
        row.append(random.randint(1,limit))

    writehead.writerow(row)
    f.close()

# Sanity check: command-line args initialized and captured before passing to function
rowspan = int(sys.argv[1])
genlimit = int(sys.argv[2])
dirpath = sys.argv[3]

# calling the function
csvGenerator(rowspan, genlimit, dirpath)

