import sys
sys.stdin = open("List_mul input.txt","r")

tc = int(input())

for i in range(1,tc+1):
    N,M = list(map(int,input().split()))
    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    max = 0
    lenai = len(Ai)
    lenbj = len(Bj)
    sum_mul = 0
    if lenai < lenbj:
        for x in range(lenbj-lenai+1):
            sum_mul =0
            for y in range(lenai):
                sum_mul += Ai[y]*Bj[x+y]
            if sum_mul>max:
                max = sum_mul
        result = max

    elif lenai > lenbj:
        for p in range(lenai-lenbj+1):
            sum_mul =0
            for q in range(lenbj):
                sum_mul += Bj[q]*Ai[p+q]
            if sum_mul>max:
                max = sum_mul
        result = max
    print('#{} {}'.format(i,result))

    

        

