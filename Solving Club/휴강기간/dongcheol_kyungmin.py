import sys
sys.stdin = open('dongcheol_input.txt','r')


def f(n,k):
    global visited, arr_p, max_p
    if n == k:
        if max_p < arr_p[-1]:
            max_p = arr_p[-1]
        return
    else:
        for i in range(N):
            if visited[i]==0 and arr_p[-1]*P[n][i]*0.01>max_p:
                visited[i] = n+1
                arr_p.append(arr_p[-1]*P[n][i]*0.01)
                f(n+1,k)
                visited[i] = 0
                arr_p.pop()
                 
for _ in range(int(input())):
    N = int(input())
    P = [list(map(int,input().split())) for _ in range(N)]
    max_p = 0
    arr_p = [1]
    visited = [0]*N 
    f(0,N)
    print(f'#{_+1} {format(max_p*100,".6f")}')