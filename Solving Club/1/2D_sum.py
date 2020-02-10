import sys
sys.stdin = open("2D_sum_input.txt","r")

for tc in range(10):
    x = [] # 배열
    sum_list1 = [] # 가로합
    sum_list2 = [] # 세로합
    sum_dig1 = 0 # 대각선 1
    sum_dig2 = 0 # 대각선 2

    a = input()
    x = [list(map(int, input().split())) for q in range(100)]
    for i in range(100): # 가로 합
        sum_list1.append(sum(x[i]))
        
    for j in range(100): # 대각선 합
        sum_dig1 += x[j][j]
        sum_dig2 += x[j][99-j]

    for k in range(100):
        sum_ver = 0
        for l in range(100):
            sum_ver += x[l][k]
            if l == 99:
                sum_list2.append(sum_ver)
                
    total =  sum_list1 + sum_list2 + [sum_dig1] + [sum_dig2]

    print("#{} {}".format(a,max(total)))

    
    # print(total)