#! /usr/bin/python3
import sys
 
for line in sys.stdin:
    n = int(line)

if n % 10 == 0:
    print("Jebb")
else:
    print("Neibb")
