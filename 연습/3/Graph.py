import sys
sys.stdin = open("Graph_input.txt","r")

tc = int(input())
for i in range(1,1+1):
    V,E = list(map(int,input().split()))
    print(V,E)
    result = 0
    nodes_init = [[0]*V for x in range(V)]
    for nodes in range(len(nodes_init)):
        print(nodes_init[nodes])
    

    nodes_list = [list(map(int,input().split())) for nl in range(E)] # 노드리스트(
    for changeX in nodes_list:
        nodes_init[changeX[0]-1][changeX[1]-1] = 1
    print(nodes_list)
    start,end = list(map(int,input().split()))

    
    for nodes in range(len(nodes_init)):
        print(nodes_init[nodes])
        
    stack = [start]
    while len(stack) != 0:
        node = stack.pop()
        for s in range(V):  
            print(node,s)
            if nodes_init[node-1][s] == 1:
                stack.append(s)
                if 5 in stack:
                    result = 1

    print(result)
    


