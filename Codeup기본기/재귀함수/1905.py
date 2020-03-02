import sys
sys.setrecursionlimit(1000000)

sum_my = 0

def my_sum(x):
    global sum_my
    if x == 1:
        sum_my += x
    else:
        sum_my += x
        my_sum(x-1)
    return sum_my

print(my_sum(int(input())))
