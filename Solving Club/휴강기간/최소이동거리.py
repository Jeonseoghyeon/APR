t = int(input())
for tc in range(1, t+1):
    N,E = map(int,input().split())
    adj = {i:[] for i in range(N+1)}
    for i in range(E):
        s,e,c = map(int,input().split())
        adj[s].append([e,c])
    INF = float('inf')
    dist = [INF]*(N+1)
    selected = [0]*(N+1)
    dist[0] = 0
    cnt = 0
    while cnt<N+1:
        min = INF
        for i in range(N+1):
            if not selected[i] and dist[i]<min:
                min = dist[i]
                u = i
        selected[u] = 1
        cnt += 1
        for w,cost in adj[u]:
            c = dist[u] + cost
            if c < dist[w]:
                dist[w] = c
    print('#{} {}'.format(tc, dist[N]))