# 0124 시작
import sys
sys.stdin = open("쇠막대기자르기_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    total = input()
    total = total.replace("()","L")
    total = list(total)
    print(total)
    cnt = 0
    temp = 0

    # print("#{} {}".format(tc,cnt))
    



