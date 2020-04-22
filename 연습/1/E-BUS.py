import sys
sys.stdin = open("E-BUS input.txt","r")

T = int(input())

for i in range(T):
    K,N,M = map(int,input().split()) # 5, 20, 5
    s_nums = input() 
    a = list(map(int,s_nums.split())) # 4,7,9,14,17
    # ARR = [int(x) for x in a]
    count = 0
    j = 0
    KI = K
    for i in range(1,N+1):
        K -= 1
        if K == -1:
            count = 0
            break
        if i == a[0]:
            if K >= a[1]-a[0]:
                j+=1
                pass
            else:
                j+=1
                count += 1
                K = KI
                
                
        elif i == a[-1]:
            if K >= N-a[-1]:
                j+=1
                pass
            else:
                j+=1
                count += 1
                K = KI
        elif i in a:
            if K>= a[j+1]-a[j]:
                j+=1
                pass
            else:
                j+=1
                count += 1
                K = KI
        else:
            pass
    print('#{} {}'.format(i, count))



