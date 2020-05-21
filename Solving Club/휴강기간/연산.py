from _collections import deque

def bfs(s,g,d):
    deq = deque()
    deq.append((s,d))
    while deq:
        here = deq.popleft()
        s,d = here[0],here[1]
        for i in range(4):
            if i == 0:
                temp = s+1
                if temp == g:
                    return d+1
                elif 0 <= temp <= g+10 and not visited[temp] and temp <= 1000000:
                    deq.append((temp, d+1))
                    visited[temp] = 1
            elif i == 1:
                temp = s-1
                if temp == g:
                    return d+1
                elif 0 <= temp <= g+10 and not visited[temp] and temp <= 1000000:
                    deq.append((temp, d+1))
                    visited[temp] = 1
            elif i == 2:
                temp = s*2
                if temp == g:
                    return d+1
                elif 0 <= temp <= g+10 and not visited[temp] and temp <= 1000000:
                    deq.append((temp, d+1))
                    visited[temp] = 1
            else:
                temp = s-10
                if temp == g:
                    return d+1
                elif 0 <= temp <= g+10 and not visited[temp] and temp <= 1000000:
                    deq.append((temp, d+1))
                    visited[temp] = 1

t = int(input())
for tc in range(1, t+1):
    N,M = map(int,input().split())
    visited = [0]*1000001
    cnt = bfs(N,M,0)
    print('#{} {}'.format(tc, cnt))