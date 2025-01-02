#! /usr/bin/python3
import sys
 
lines = sys.stdin.readlines()

limits = [int(x) for x in lines[0].split(" ")]
score = int(lines[1])

def grade(limits, score):
    grades = ["A", "B", "C", "D", "E"] 
    for limit, grade in zip(limits, grades):
        if score >= limit:
            return grade
    return "F"
    # a, b, c, d, e = limits
    # if score >= a:
    #     return "A"
    # elif score >= b:
    #     return "B"
    # elif score >= c:
    #     return "C"
    # elif score >= d:
    #     return "D"
    # elif score >= e:
    #     return "E"
    # else:
    #     return "F"

print(grade(limits, score))

