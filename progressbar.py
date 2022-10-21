#!/bin/python3

# progress bar proof-of-concept

import sys
import time

for i in range(0,51):
    time.sleep(0.1)
    sys.stdout.write("{} [{}{}]\r".format(i, "#"*i, "."*(50-i)))
    sys.stdout.flush()
sys.stdout.write("\n")