#!/bin/python3

# ---------- Ingress script
# This script takes a specified CSV file and reads into a row,
# logging the contents to the console (as a proof of concept).

# ---------- Imported Modules

import csv
#import sys FIXME: will be added in later

numdata = []

with open('./output.csv') as f:
    readhead = csv.reader(f)
    for row in readhead:
        for col in range(len(row)):
            numdata.append(row[col])


#f = open('./output.csv',)
#readhead = csv.reader(f)

#numlist = list(readhead)

print(numdata)

f.close()
