import sys
sys.stdin = open('prisoner_input.txt','r')
dsero,dgaro = [-1,1,0,0],[0,0,-1,1] #상,하,좌,우 순
def dfs(list):
    global visited,L,dsero,dgaro
    while stack:
        # print(stack)
        sero,garo = stack.pop()
        if t_map[sero][garo]  == '1' :
            for i in range(4):
                nsero = sero + dsero[i]
                ngaro = garo + dgaro[i]
                if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0 and t_map[nsero][ngaro] not in ['0']:
                    visited[nsero][ngaro] = 1
                    stack.append([nsero,ngaro])

        elif t_map[sero][garo]  == '2' :
            for i in range(4):
                nsero = sero + dsero[i]
                ngaro = garo + dgaro[i]
                if i == 0:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','3','4','7']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])
                if i == 1:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','3','5','6']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])

        elif t_map[sero][garo]  == '3' :
            for i in range(4):
                nsero = sero + dsero[i]
                ngaro = garo + dgaro[i]
                if i == 2:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','2','6','7']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])
                if i == 3:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','2','4','5']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])

        if t_map[sero][garo]  == '4' :
            for i in range(4):
                nsero = sero + dsero[i]
                ngaro = garo + dgaro[i]
                if i == 0:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','3','4','7']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])
                if i == 3:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','2','4','5']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])

        if t_map[sero][garo]  == '5' :
            for i in range(4):
                nsero = sero + dsero[i]
                ngaro = garo + dgaro[i]
                if i == 1:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','3','5','6']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])
                if i == 3:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','2','4','5']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])

        if t_map[sero][garo]  == '6' :
            for i in range(4):
                nsero = sero + dsero[i]
                ngaro = garo + dgaro[i]
                if i == 1:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','3','5','6']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])
                if i == 2:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','2','6','7']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])

        if t_map[sero][garo]  == '7' :
            for i in range(4):
                nsero = sero + dsero[i]
                ngaro = garo + dgaro[i]
                if i == 0:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','3','4','7']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])
                if i == 2:
                    if -1<nsero<N and -1<ngaro<M and visited[nsero][ngaro] ==0:
                        if t_map[nsero][ngaro] not in ['0','2','6','7']:
                            visited[nsero][ngaro] = 1
                            stack.append([nsero,ngaro])
    
    p_cnt = 0
    for y in range(N):
        for x in range(M):
            if visited[y][x] == 1:
                p_cnt+=1
    
    return p_cnt


#main
T = int(input())
for tc in range(1,T+1):
    N,M,R,C,L = list(map(int,input().split()))
    # N : 세로 /M : 가로/ R,C: 맨홀좌표 / L : 탈주 후 시간
    t_map = [input().split() for x in range(N)]
    # print(N,M,R,C,L)
    hole = [R,C] # 맨홀 좌표
    visited = [[0]*M for v in range(N)]
    stack = [hole]
    if L == 1:
        print("#{} {}".format(tc,1))
    else:
        print("#{} {}".format(tc,dfs(hole)))