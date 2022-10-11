#!/bin/python3

# ---------- Doubler
# Uses the ingress.py as a built-in function,
# and doubles each value in the array

# ---------- Imported Modules

import csv

target = './output.csv'
numdata = []

def csvIngress(sheet,numlist):
    with open(sheet) as f:
        readhead = csv.reader(f)
        for row in readhead:
            for col in range(len(row)):
                numlist.append(int(row[col]))
    return numlist

numdata = csvIngress(target, numdata)

# Basic arithmetic operation (simulates manipulation by algorithm)
for i in range(len(numdata)):
    numdata[i] = 2 * numdata[i]

print(numdata)
