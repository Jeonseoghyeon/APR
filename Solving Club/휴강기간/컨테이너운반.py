import sys
sys.stdin = open("컨테이너운반_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) # 컨테이너수 N  / 트럭수 M
    W = list(map(int,input().split())) # 화물의 무게 W
    T = list(map(int,input().split())) # 적재용량 T
    T.sort(reverse=True)
    W.sort(reverse=True)
    max_sum = 0 
    for cap in T:
        while len(W) != 0:
            weight = W.pop(0)
            if weight <= cap:
                max_sum += weight
                break

    print("#{} {}".format(tc,max_sum))