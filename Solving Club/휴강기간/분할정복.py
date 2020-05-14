import sys
sys.stdin = open("분할정복_input.txt","r")

def binary_search(l,r,searched_num,direction):
    global cnt
    m = (l+r)//2
    if A[m] == searched_num:
        cnt+=1
        return

    if searched_num > A[m]:
        if direction != 1:
            binary_search(m+1,r,searched_num,1)
    else:
        if direction != -1:
            binary_search(l,m-1,searched_num,-1)


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))
    cnt = 0
    for searched_num in B:
        if searched_num in A:
            binary_search(0,N-1,searched_num,0)
    print("#{} {}".format(tc,cnt))
