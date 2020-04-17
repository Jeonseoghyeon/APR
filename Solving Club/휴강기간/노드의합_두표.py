import sys
sys.stdin = open('노드의합_input.txt','r')


T = int(input())
for tc in range(1, 1+1):W
    N, M, E = map(int, input().split())
    print(N,M,E)
    ad_list = [0 for _ in range(N+1)]
    for _ in range(M):
        node, value = map(int, input().split())
        ad_list[node] = value
    print(ad_list)
    result = 0
    stack = [E]
    while stack:
        print(stack)
        v = stack.pop()
        if v <= N: # 5
            if ad_list[v]:
                result += ad_list[v]
            else:
                stack += [2*v, 2*v + 1]
    print(f'#{tc} {result}')