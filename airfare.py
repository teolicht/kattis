import sys

input = sys.stdin.readlines()

num_flights = int(input[0])
prices = [int(p) for p in input[1:]]

cheapest_ticket = min(prices)
most_expensive_ticket = max(prices)
to_pay = cheapest_ticket - (most_expensive_ticket / 2)

if to_pay < 0:
    to_pay = 0

print(int(to_pay))

