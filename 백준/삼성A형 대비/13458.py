N = int(input()) # 시험장 개수
rooms = list(map(int,input().split()))
B,C = list(map(int,input().split()))
sumS=0
for i in rooms:
    i-=B
    sumS+=1
    if i>0 and i%C==0:
        sumS+=(i//C)
    elif i>0 and i%C!=0:
        sumS+=(i//C+1)
    
print(sumS)