import sys
from itertools import permutations

sys.stdin = open("array_sum_input.txt","r")

tc = int(input())
for i in range(1,tc+1):
    N = int(input())
    arr = [list(map(int,input().split())) for x in range(N)]
    nums = list(range(N))
    # print(nums)
    per = permutations(range(N))
    # print(per)
    sum_1 = 0
    sum_min = 9999
    for x in per:
        # print(x)
        sum_1 = 0
        for y in range(N):
            # print(y,x[y])
            sum_1 += arr[y][x[y]]
            if sum_1 >=sum_min:
                break
        if sum_1 <= sum_min:
            sum_min = sum_1     
            # print(sum_min)
    print("#{} {}".format(i,sum_min))