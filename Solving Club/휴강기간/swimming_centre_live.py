import sys
sys.stdin = open("swimming_centre_input.txt","r")

def f(n,s,d,m,m3):
    global minV
    if n>12:
        if minV >s:
            minV=s
        
    else:
        f(n+1,s+table[n]*d,d,m,m3)
        f(n+1,s+m,d,m,m3)
        f(n+3,s+m3,d,m,m3)
    return minV


T = int(input())
for tc in range(1,T+1):
    d,m,m3,y = map(int,input().split())
    table = [0] + list(map(int,input().split()))
    minV = y
    print(f(1,0,d,m,m3))
