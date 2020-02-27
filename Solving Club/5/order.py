import sys
sys.stdin = open("order_input.txt","r")

def bfs(start):
    visit = [start[0]]
    queue = start
    while queue:
        # print(queue)
        node = queue.pop(0)
        for c in range(V+1):
            if arr[node][c] == 1 and c not in visit:
                visit.append(c)
                queue.append(c)
    print(len(visit))
    return visit


for tc in range(1,11):
    V,E = list(map(int,input().split())) # V : 노드 갯수 E : 간선 갯수
    line = list(map(int,input().split()))
    lines = []
    for e in range(0,E*2,2):
        lines.append([line[e],line[e+1]])
    arr = [[0]*(V+1) for ar in range(V+1)]
    # print(lines)
    for n in lines:
        arr[n[0]][n[1]] = 1
    # for arrr in range(V+1):
    #     print(arr[arrr])

    start = []
    for st in range(len(lines)):
        start.append(lines[st][0])
    # print(start)
    
    print(bfs(start))
    