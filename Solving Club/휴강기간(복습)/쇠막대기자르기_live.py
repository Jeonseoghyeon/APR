# 0124 시작
import sys
sys.stdin = open("쇠막대기자르기_input.txt","r")


T = int(input())
for tc in range(1,T+1):
    s = input()
    stick = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            stick += 1
        elif s[i]==')' and s[i-1]=='(':
            stick -=1
            cnt += stick
        else:
            cnt +=1
            stick -=1
    print("#{} {}".format(tc,cnt))