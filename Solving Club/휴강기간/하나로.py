def union(x,y):
    px,py = find_set(x),find_set(y)
    if rank[px] > rank[py]:
        p[py] = px
    else:
        p[px] = py
        if rank[px] == rank[py]:
            rank[py] += 1

def find_set(x):
    if p[x] == x: return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def kruscal():
    cnt = result = 0
    for i in range(len(edges)):
        s,e,c = edges[i][0],edges[i][1],edges[i][2]
        if find_set(s) == find_set(e): continue
        result += c
        union(s,e)
        for j in range(N):
            find_set(j)
        cnt += 1
        if cnt == N-1: return result
    return result

t = int(input())
for tc in range(1, t+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())
    edges=[]
    p = list(range(N))
    rank = [0]*N
    for i in range(N-1):
        for j in range(i+1,N):
            x_diff,y_diff = abs(X[i]-X[j]),abs(Y[i]-Y[j])
            dist = pow(x_diff,2)+pow(y_diff,2)
            cost = E*dist
            edges.append([i,j,cost])
    edges.sort(key=lambda x:x[2])
    ans = kruscal()
    print('#{} {}'.format(tc, round(ans)))