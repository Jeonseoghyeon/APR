import sys
sys.stdin = open("card_input.txt","r")
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int,input().split()))
    def gawibawibo(x,y):
        a=lst[x-1]
        b=lst[y-1]
        if a == 1:
            if b == 2:
                return y
            elif b == 3:
                return x
            elif b == 1:
                return min(x, y)
        elif a == 2:
            if b == 1:
                return x
            elif b == 2:
                return min(x, y)
            elif b == 3:
                return y
        elif a == 3:
            if b == 1:
                return y
            elif b == 2:
                return x
            elif b == 3:
                return min(x,y)
    def tournament(st,ed):
        if st - ed == 0:
            return st
        v1 = tournament(st, (st+ed)//2)
        print(st,ed)
        v2 = tournament((st+ed)//2+1, ed)
        print(st,ed)
        return gawibawibo(v1,v2)
    result = tournament(1,len(lst))
    print('#{} {}'.format(tc,result))
    print()
    print()