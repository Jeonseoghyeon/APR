def dfs(cnt):
    visited = [0]*(N+1)
    for i in range(1,N+1):
        flag = False
        s = []
        s.append(i)
        while s:
            h = s.pop()
            if not visited[h]:
                visited[h] = 1
                flag = True
                for n in range(N, 0, -1):
                    if matrix[h][n] and not visited[n]:
                        s.append(n)
        if flag:
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    matrix = [[0]*(N+1) for _ in range(N+1)]
    for i in range(0,len(data),2):
        s,g = data[i],data[i+1]
        matrix[s][g] = 1
        matrix[g][s] = 1
    result = dfs(0)
    print('#{} {}'.format(tc, result))