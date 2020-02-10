import sys
sys.stdin = open("miro_input.txt", "r")

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(1,1+1):
    tc = int(input())
    arr = [input().split() for x in range(16)]
    for j in range(1000):
        startX, startY = 1,1
        for R in range(16):
            for D in range(16):
                
    