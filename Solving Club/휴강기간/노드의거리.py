import sys
sys.stdin = open("노드의거리_input.txt","r")
from collections import deque

def bfs(S,G,dq):
    global cnt,result
    visited = [S]
    dq.append(S)
    while dq:
        cnt+=1
        for xxx in range(len(dq)):
            node_y = dq.popleft()
            for i in range(V+1):
                if graph[node_y][i] == 1 and i not in visited :
                    visited.append(i)

                    if i == G:
                        result = 1
                        return
                    else:
                        dq.append(i)



T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    graph = [[0]*(V+1) for GRAPH in range(V+1)]
    lines = [list(map(int,input().split())) for LINES in range(E)]
    S,G = map(int,input().split())
    for l in lines:
        graph[l[0]][l[1]] = 1
        graph[l[1]][l[0]] = 1

    result = 0
    cnt = 0
    dq = deque()
    bfs(S,G,dq)
    print("#{} {}".format(tc,cnt*result))