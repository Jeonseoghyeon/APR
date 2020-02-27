#BFS 시작하자!
    visited = []
    stack = [lines[x][0] for x in range(len(lines))]
    print("33",stack)
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
    