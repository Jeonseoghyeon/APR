def f(start,end):
    global sumX,maxX
    if start+days[start] > end:
        print("i",sumX)
        return
    elif start+days[start] == end:
        if pays[start] == 1:
            sumX += pays[start]
        print("e",sumX)
        return
    else:
        for i in range(start+days[start],end):
            if i+days[i] <= N+1:
                sumX+=pays[i]
                print(i)
            f(i,end)
        
    return sumX



N =int(input())
days = [0]
pays = [0]

for i in range(N):
    a,b = map(int,input().split())
    days.append(a)
    pays.append(b)
print(days,pays)
for j in range(1,N):
    sumX=pays[j]
    maxX=0
    # print(j,'\n\n')
    print(f(j,N))


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