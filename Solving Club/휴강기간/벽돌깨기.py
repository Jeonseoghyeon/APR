import sys
sys.stdin = open("벽돌깨기_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N, W, H = map(int,input().split())
    