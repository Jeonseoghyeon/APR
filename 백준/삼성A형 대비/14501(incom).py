def f(start,end):
    global sumX
    if start > end:
        return sumX
    elif start == end:
        if pays[start] == 1:
            sumX += pays[start]
        return sumX
    else:
        sumX+=pays[start]
        f(start+days[start],end)
    return sumX



N =int(input())
days = [0]
pays = [0]
# visit = [0]*(N+1)
sumX = 0
for i in range(N):
    a,b = map(int,input().split())
    days.append(a)
    pays.append(b)
print(days,pays)
print(f(1,N))


'''
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
'''