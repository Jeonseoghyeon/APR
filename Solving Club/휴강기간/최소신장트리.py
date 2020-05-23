t = int(input())
for tc in range(1, t+1):
    V,E = map(int,input().split())
    adj = {i:[] for i in range(V+1)}
    for i in range(E):
        s,e,c = map(int,input().split())
        adj[s].append([e,c])
        adj[e].append([s,c])
    INF = float('inf')
    p = [0]*(V+1)
    key = [INF]*(V+1)
    mst = [0]*(V+1)
    cnt = result = 0
    key[0] = 0
    while cnt<V+1:
        min = INF
        u = -1
        for i in range(V+1):
            if not mst[i] and key[i]<min:
                min = key[i]
                u = i
        mst[u] = 1
        result += min
        cnt += 1
        for w,c in adj[u]:
            if not mst[w] and c<key[w]:
                key[w] = c
                p[w] = u

    print('#{} {}'.format(tc, result))