#!/bin/bash

# runs programs and ouputs the generated csv file
# takes command line arguments for numgen.py (pass through)
./numgen.py $1 $2 && cat output.csv;
