#!/bin/python3

# Python number generator
# outputs to a csv file for feeding into other programs
# intended purpose is for testing algorithms

import csv
import random

f = open('./output.csv','w')

row = []

writehead = csv.writer(f)

for i in range(1,10):
    row.append(random.randint(1,1000))

writehead.writerow(row)

#print("end of row, writing another!")

#wor = [110,220,330,440,550,660,770,880,990,1100]

#writehead.writerow(wor)

f.close()
