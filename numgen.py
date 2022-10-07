#!/bin/python3

# Python number generator
# outputs to a csv file for feeding into other programs
# intended future purpose is for testing algorithms

# imported modules
import csv
import random
import sys

# initialize and open the CSV file for writing to
f = open('./output.csv','w')

# ---------- VARIABLE DECLARATIONS 
# initialize the empty row
row = []
span = int(sys.argv[1]) # size of row
limit = int(sys.argv[2]) # upper range for random number generation


# initialize the CSV writer
writehead = csv.writer(f)

# populate the row with randomly generated numbers
for i in range(1,span):
    row.append(random.randint(1,limit))

# write the populated row to the CSV and close the file
writehead.writerow(row)
f.close()
