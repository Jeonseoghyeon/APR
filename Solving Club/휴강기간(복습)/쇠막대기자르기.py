# 0124 시작
import sys
sys.stdin = open("쇠막대기자르기_input.txt","r")

T = int(input())
for tc in range(1,1+1):
    total = list(input())
    for i in range(len(total)-1):
        if total[i] =='(' and total[i+1] == ')':
            total[i]='LAZER'
            total[i+1] = '0'
    for x in range(total.count('0')):
        total.remove('0')
    print(total)

    stack = []
    stack2 = []
    sumX = 0
    temp = 0

        



