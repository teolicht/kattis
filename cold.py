#! /usr/bin/python3
import sys
 
lines = sys.stdin.readlines()

below_zero = 0
temps = lines[1].split(" ")
for t in temps:
    if int(t) < 0:
        below_zero += 1
print(below_zero)

