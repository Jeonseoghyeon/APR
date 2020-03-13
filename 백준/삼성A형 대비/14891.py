# 1530 시작 1645 종료
def rotate_id(start,tim):
    if tim == -1:
        cog[start] = cog[start][1:] + cog[start][0]
    else:
        cog[start] = cog[start][-1] + cog[start][0:-1]

def rotate(start,tim):
    global ifchange
    timr = timl = tim
    rotate_id(start,tim)

    for i in range(start+1,5): # 들어온 기준 오른쪽까지 4
        if ifchange[i-1] == False:
            timr = -(timr)
            rotate_id(i,timr)
        else:
            break

    for j in range(start-1,0,-1): # 들어온 기준 왼쪽까지 2, 1
        if ifchange[j] == False:
            timl = -(timl)
            rotate_id(j,timl)
        else:
            break
    return cog

cog = [''] + [input() for x in range(4)]
K =int(input())
cnum = [list(map(int,input().split())) for x in range(K)]
for i in cnum:
    ifchange = [0,cog[1][2]==cog[2][6],cog[2][2]==cog[3][6],cog[3][2]==cog[4][6]]
    rotate(i[0],i[1])
sumX = 0
for summ in range(1,5):
    if cog[summ][0] == '1':
        sumX+=(1<<summ-1)
        
print(sumX)