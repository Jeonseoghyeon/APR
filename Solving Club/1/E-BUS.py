import sys
sys.stdin = open("E-BUS_input.txt","r")

T = int(input())

for i in range(T):
    K,N,M = map(int,input().split()) 
    s_nums = input() 
    a = list(map(int,s_nums.split())) 
    count = 0 # 충전 횟수
    j = 0 #충전소 값 설정(충전소를 들리면 다음 충전소 값으로 해줘야 진행이 되니까)
    KI = K # K의 기본값 설정 / 초기화 용
    for s in range(1,N+1):
        K -= 1
        if K == -1:
            count = 0
            break
        if s == a[0]: # 첫 충전소 들렸을 때
            if K >= a[1]-a[0]:
                j+=1
                pass
            else:
                j+=1
                count += 1
                K = KI
                  
        elif s == a[-1]: # 마지막 충전소 들렸을 때
            if K >= N-a[-1]:
                j+=1
                pass
            else:
                j+=1
                count += 1
                K = KI
        elif s in a: # 첫,마지막 충전소 제외 타 충전소들을 들렸을 때
            if K>= a[j+1]-a[j]:
                j+=1
                pass
            else:
                j+=1
                count += 1
                K = KI
        else:
            pass
    print('#{} {}'.format(i+1, count))
    



