import sys
sys.stdin = open("노드의거리_input.txt","r")
from collections import deque

def bfs(S,G,dq):
    global cnt,result
    visited = [S]
    dq.append([S,1])
    while dq:
        node_y,cnt = dq.popleft()
        for i in range(V+1):
            if graph[node_y][i] == 1 and i not in visited :
                visited.append(i)
                if i == G:
                    return cnt
                else:
                    dq.append([i,cnt+1])
    return 0



T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    graph = [[0]*(V+1) for GRAPH in range(V+1)]
    lines = [list(map(int,input().split())) for LINES in range(E)]
    S,G = map(int,input().split())
    for l in lines:
        graph[l[0]][l[1]] = 1
        graph[l[1]][l[0]] = 1

    dq = deque()
    result = bfs(S,G,dq)
    print("#{} {}".format(tc,result))