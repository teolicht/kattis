import sys

input = sys.stdin.readlines()

# n = number of board squares
# s = index of frog's starting square
# m = magic number
n, s, m = [int(i.strip()) for i in input[0].split(" ")]
n -= 1 
s -= 1
board_nums = [int(i.strip()) for i in input[1].split(" ")]

def game(n, s, m, board_nums):
    fate = None
    hops = 0
    visited_indexes = []
    while fate is None:
        if s < 0:
            fate = "left"
            break
        if s > n:
            fate = "right"
            break
        k = board_nums[s]
        if k == m:
            fate = "magic"
            break
        if s in visited_indexes:
            fate = "cycle"
            break
        visited_indexes.append(s)
        s += k
        hops += 1
    return (fate, hops)

print("{}\n{}".format(*game(n, s, m, board_nums)))


    


