#2차원 배열 기본
'''
Array = [[1,2,3,4],[5,6,7,8]]
m = len(Array[0])

for i in range(len(Array)): # 정방향 순회
    print()
    for j in range(len(Array[i])):
        print(Array[i][j], end ='') 

print()

for j in range(len(Array[0])): # 열 우선 순회
    print()
    for i in range(len(Array)):
        print(Array[i][j], end ='')

print()

for i in range(len(Array)): # 지그재그 순회
    print()
    for j in range(len(Array[0])):
        print(Array[i][j + (m-1-2*j) * (i % 2)], end ='')

'''

#2차원 배열 완전탐색

Array = [[1,2,3,4],[5,6,7,8],[9,1,5,2],[2,7,6,9]]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

print(Array)
for x in range(len(Array)):
    for y in range(len(Array[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if testX < 0 or testY<0:
                continue
            elif testX>=4 or testY>=4:
                continue
            print(Array[testX][testY], end=' ')
        print()

'''
#2차원 배열 전치행렬
arr = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
    print()
    for j in range(3):
        if i<j :
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        print(arr[i][j], end= '')
'''