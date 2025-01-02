import math

num_statues = int(input())

min_days = math.ceil(math.log2(num_statues) + 1)

print(min_days)


# The math
"""
The number of printers can grow exponentially: starting with 1 printer on day 1, since you can print at most the number of printers you currently have on a day, then on day k you can have 2^(k-1) printers.

The idea is to make new printers UNTIL you have enough to print all statues on a single day. This means figuring out how many times you have to double the number of printers (as this is the max you can do each day, therefore the fastest) each day.

So what you want is to find the smallest k, so that: 2^(k-1) >= num_statues. Taking log on both sides:

    lg(2^(k-1) >= lg(num_statues)
    k - 1 >= lg(num_statues)
    k >= lg(num_statues) + 1

Since k represents days, it must be an integer. So the result needs to be rounded. And it needs to be rounded UP, to ensure there are
enough printers to print num_statues, as rounding down would underestimate the number of printers needed. So you get:

    k >= ceil(lg(num_statues) + 1) 
"""


