# import sys
# sys.stdin=open("그래프경로_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    lines = [list(map(int,input().split())) for x in range(E)]
    check = list(map(int,input().split()))
    # print(V,E)
    # print(lines)
    # print(check)
    arr = [[0]*(V+1) for ARR in range(V+1)]
    for y in range(V+1):
        for x in range(V+1):
            if [y,x] in lines:
                arr[y][x] = 1

    # for ar_r in range(V+1):
    #     print(arr[ar_r])

    stack = [check[0]]
    result = 0
    visit = [[0]*(V+1) for ARR in range(V+1)]
    while stack:
        node = stack.pop()
        for i in range(V+1):
            if arr[node][i]==1 and visit[node][i]==0:
                visit[node][i] = 1
                stack.append(i)
        if check[1] in stack:
            result = 1
            break
    print("#{} {}".format(tc,result))


# 추가 Case
'''
3
5 6
1 3
1 5
3 5
3 4
4 2
5 2
1 2
6 8
1 2
1 3
2 3
3 4
4 2
4 5
4 6
6 2
1 5
6 8
1 2
1 3
2 3
3 4
4 2
4 5
4 6
6 2
2 1
'''