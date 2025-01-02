#! /usr/bin/python3
import sys
 
decimal = int(sys.stdin.read())

binary = bin(decimal)[2:] # ignore '0b'
reversed_binary = binary[::-1]

reversed_decimal = int(reversed_binary, 2)

print(reversed_decimal)

