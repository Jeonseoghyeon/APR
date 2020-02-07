import sys
sys.stdin = open("sudoku input.txt","r")

tc = int(input())
for i in range(1,tc+1):
    x = []
    sum_pa = 0
    sum_ver = 0

    for j in range(9):
        x += [list(map(int,input().split()))]
    for k in range(9):
        for l in range(9):
            sum_pa += x[k][l]
            sum_ver += x[l][k]
    if sum_pa != 405 or sum_ver != 405:
        result = 0
        print("#{} {}".format(tc,result))
        continue
    # for g in range(9):
    #     sum_sq = 0
    #     for m in range(3):
    #         for n in range(3):
    #             sum_sq += x[m]
    print("통과")



