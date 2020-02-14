import sys
sys.stdin = open("Graph_input.txt","r")

tc = int(input())
for i in range(1, tc + 1):
    V, E = list(map(int, input().split()))
    result = 0
    nodes_init = [[0] * (V + 1) for x in range(V + 1)]
    nodes_list = [list(map(int, input().split())) for nl in range(E)]  # 노드리스트(
    for changeX in nodes_list:
        nodes_init[changeX[0]][changeX[1]] = 1
    start, end = list(map(int, input().split()))

    stack = [start]
    while stack:
        node = stack.pop()
        for s in range(1, V + 1):
            if nodes_init[node][s] == 1:
                nodes_init[node][s]=0
                stack.append(s)
            if end in stack:
                result = 1
                break
        if result == 1:
            break

    print("#{} {}".format(i, result))

    
# 아마 end를 못만나는 조건에서 비어이있는 stack을 pop해서 오류뜨는거같아요