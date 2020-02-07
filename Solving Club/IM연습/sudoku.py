import sys
sys.stdin = open("sudoku input.txt","r")

tc = int(input())
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]
for i in range(1,tc+1):
    x = []
    sum_pa = set()
    sum_ver = set()
    sum_sq = set()
    result = 1
    for j in range(9): # 리스트 형성
        x += [list(map(int,input().split()))]
    for k in range(9):
        sum_pa=set()
        sum_ver=set()
        for l in range(9):
            sum_pa.add(x[k][l])
            sum_ver.add(x[l][k])   
        if len(sum_pa) == 9 and len(sum_ver) == 9:
            result *=1
        else:
            result *=0
        

    for m in range(1,8,3):
        for n in range(1,8,3):
            sum_sq = set()
            for p in range(8):
                testX = m + dx[p]
                testY = n + dy[p]
                sum_sq.add(x[testX][testY])
                sum_sq.add(x[m][n])
                
        if len(sum_sq) == 9:
            result *= 1
        else:
            result *=0
    print("#{} {}".format(i,result))
                






#1 1
#2 0
#3 1
#4 0
#5 0
#6 1
#7 0
#8 1
#9 1
#10 0



