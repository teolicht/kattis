import sys
 
input = sys.stdin.readline()

VOWELS = ["a", "e", "i", "o", "u"]

vowels_amount = 0
for char in input:
    if char == " ":
        continue
    if char.lower() in VOWELS:
        vowels_amount += 1
print(vowels_amount)

