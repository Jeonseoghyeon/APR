import sys
sys.stdin = open("order_input.txt","r")

for tc in range(3):
    print(f"###############{tc+1}#############", end='\n\n\n')
    num_node, num_line = list(map(int,input().split()))
    line = list(map(int,input().split()))
    lines = []
    for x in range(num_line):
        lines.append(line[x*2:x*2+2])
    print(lines)
    ### 간선 받아 왔음

    near_arr = [[0]*(num_node+1) for near in range(num_node+1)] # 인접행렬 완성
    for ne1 in range(num_node+1):
        for ne2 in range(num_node+1):
            if [ne1,ne2] in lines:
                near_arr[ne1][ne2] = 1
    for xxxxx in range(num_line+1):
        print(near_arr[xxxxx])        

#BFS 시작하자!
    nodei = 0
    visited = [lines[nodei][0]]
    stack = [lines[nodei][0]]
    while len(set(visited)) != num_node:
        print("stack:{}END".format(stack))
        # if len(stack) == 0:
        #     print("들어옴")
        #     nodei += 1
        #     stack.append(lines[nodei][0])
        node = stack.pop()
        print("node:{}".format(node))
        for j in range(1,num_node+1):
            print(node,j)   
            if near_arr[node][j] == 1:
                stack.append(j)
                visited.append(j)
                print("추가")
                print(stack)
                print("vs{}".format(visited))
    