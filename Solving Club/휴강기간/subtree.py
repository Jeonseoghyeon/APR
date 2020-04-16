import sys
sys.stdin = open("subtree_input.txt","r")

def dfs(N,arr):
    global cnt,E
    stack = [N]
    visited = [[0]*(E+2) for ARR in range(E+2)]
    while stack:
        node = stack.pop()
        for i in range(E+2):
            if arr[node][i] == 1 and visited[node][i] ==0:
                visited[node][i] = 1
                stack.append(i)
                cnt+=1
    return cnt
T = int(input())
for tc in range(1,T+1):
    E,N  = map(int,input().split())
    n = list(map(int,input().split()))
    nodes = []
    for i in range(E):
        nodes.append([n.pop(0),n.pop(0)])
    arr = [[0]*(E+2) for ARR in range(E+2)]
    for j in nodes:
        arr[j[0]][j[1]] = 1
    cnt = 1
    print("#{} {}".format(tc,dfs(N,arr)))
