import sys
sys.stdin = open("2D_sum input.txt","r")

for tc in range(10):
    x = []
    sum_list1 = []
    sum_list2 = []
    sum_dig1 = 0
    sum_dig2 = 0
    sum_ver = 0
    a = input()
    x = [list(map(int, input().split())) for q in range(100)]
    for i in range(100):
        sum_list1.append(sum(x[i]))
        
    for j in range(100):
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