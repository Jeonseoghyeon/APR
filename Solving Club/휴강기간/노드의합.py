import sys
sys.stdin = open('노드의합_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split()) # 노드 개수 N / 리프 노드 개수 M / 출력할 노드 번호 L
    riff = []
    nodes = [0]*(N+1)
    for i in range(M):
        riff_node, num = map(int,input().split())
        nodes[riff_node] = num

    for j in range(N,0,-1):
        if nodes[j] == 0:
            if (2*j+1) <= N:
                nodes[j] = nodes[2*j]+nodes[2*j+1]
            else:
                nodes[j] = nodes[2*j]
    print("#{} {}".format(tc,nodes[L]))    
    