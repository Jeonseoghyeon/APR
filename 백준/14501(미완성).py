t = int(input())
T = [0]
P = [0]
for i in range(1,t+1):
    x,y = list(map(int,input().split()))
    print(x,i)
    if i + x <=t+1:
        T.append(x)
    else:
        T.append(0)
    P.append(y)

print(T,P)
for j in range(len(T)):
    for k in range(len(T)):
        pass
        

    