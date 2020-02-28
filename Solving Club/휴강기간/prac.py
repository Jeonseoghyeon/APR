from itertools import permutations
import sys
from copy import deepcopy
from math import trunc
sys.stdin = open("make_nums_input.txt","r")

def cal (lst):
    while len(lst)!=1:
        if lst[1] == '+':
            result = lst[0]+lst[2]
            lst = lst[3:]
            lst.insert(0,result)
        elif lst[1] == '-':
            result = lst[0]-lst[2]
            lst = lst[3:]
            lst.insert(0,result)
        elif lst[1] == '*':
            result = lst[0]*lst[2]
            lst = lst[3:]
            lst.insert(0,result)
        else:
            result = trunc(lst[0]/lst[2])
            lst = lst[3:]
            lst.insert(0,result)
    return lst[0]

def per (nums,cals):
    new_nums = deepcopy(nums)
    for p in range(1,len(cals)+1):
        new_nums.insert(2*p-1,cals[p-1])
    return new_nums

tc=int(input())
for tc in range(1,tc+1):
    N = int(input())
    cal_nums = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    cals = []
    for i in range(len(cal_nums)):
        for j in range(cal_nums[i]):
            if i == 0:
                cals.append('+')
            elif i == 1:
                cals.append('-')
            elif i == 2:
                cals.append('*')
            else:
                cals.append('/')
    cals_p = set(permutations(cals)) # 연산 Permutations 다 출력
    
    min_cal = 100000000
    max_cal = -100000000

    for cp in cals_p:
        x = per(nums,cp)
        if cal(x) > max_cal:
            max_cal = cal(x)
        if cal(x) < min_cal:
            min_cal = cal(x)
    print("#{} {}".format(tc,max_cal - min_cal))

    
    
    
            
    