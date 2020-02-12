import sys
sys.stdin = open("OCL_input.txt","r")

def board():
    for brd in Board:
        print(brd)

tc = int(input())
for i in range(1,tc+1):#어차피 한 번 반복
    N,M = list(map(int,input().split())) # N: 판 크기 , M : 돌 놓는 횟수
    
    #1 : 흑돌 #2: 백돌
    Board = [[0]*N for x in range(N)]
    #초기설정
    InitX=(N-1)//2
    InitY=(N)//2
    Board[InitX][InitX] = Board[InitY][InitY] = 2
    Board[InitX+1][InitX] = Board[InitY-1][InitY] = 1

    board()

