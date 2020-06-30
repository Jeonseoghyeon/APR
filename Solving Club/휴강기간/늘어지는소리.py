import sys
sys.stdin = open('늘어지는소리_input.txt','r')

T = int(input())
for tc in range(T):
    string = input()
    hyphon_num = int(input())
    hyphon_location = list(map(int,input().split()))
    print(string, hyphon_num, hyphon_location)