import sys
from copy import deepcopy
from itertools import combinations
sys.stdin = open("swimming_centre_input.txt","r")

def Change_into_Three_months(tuple):
    new_JanToDec_Prices = deepcopy(JanToDec_Prices)
    for i in tuple:
        if i+2<=11:
            if sum(JanToDec_Prices[i:i+3]) >= Three_months:
                new_JanToDec_Prices[i] = Three_months
                new_JanToDec_Prices[i+1] = 0
                new_JanToDec_Prices[i+2] = 0
        
    return sum(new_JanToDec_Prices)


    

for tc in range(1,int(input())+1):
    Prices = list(map(int,input().split()))
    JanToDec = list(map(int,input().split()))
    One_day = Prices[0]
    One_month = Prices[1]
    Three_months = Prices[2]
    One_year = Prices[3]
    JanToDec_Prices = [0]*12
    for i in range(len(JanToDec)):
        if JanToDec[i] == 0:
            continue
        if JanToDec[i]*One_day >= One_month:
            JanToDec_Prices[i] = One_month
        else:
            JanToDec_Prices[i] = JanToDec[i]*One_day
    # print(JanToDec_Prices)
    # print(sum(JanToDec_Prices))
    One_price = sum(JanToDec_Prices) # 1달 기준으로 최소값 넣어놓은 놈

    Three = [0,1,2,3,4,5,6,7,8,9,10,11]
    Three = list(combinations(Three,4))
    Final_Three = []
    for thr in Three:
        if thr[1]-thr[0]>=3 and thr[2]-thr[1]>=3 and thr[3]-thr[2]>=3:
            Final_Three.append(thr)
    sum_min = 99999999999
    for change in Final_Three:
        if Change_into_Three_months(change) <=sum_min:
            sum_min = Change_into_Three_months(change)

    print("#{}".format(tc),min(sum_min,One_year))