import sys
sys.stdin = open("New_cal input.txt","r")

def tusum(kwgs1,kwgs2): # 좌표끼리의 합 함수
    x = kwgs1[0]+kwgs2[0]
    y = kwgs1[1]+kwgs2[1]
    return [x,y]

# 리스트 출력
x=1
y=1
z=1
tu=[]
for i in range(1,40000):
    if i == 1:
        tu +=[[1,1]]
    elif i == y:
        for j in range(1,z+1):
            tu += [[j,z-j+1]]
    else:
        continue
    y+=z
    z+=x


tc = int(input())
for i in range(1,tc+1):
    N,M = list(map(int,input().split()))
    N1 = tu[N-1]
    N2 = tu[M-1]
    N3 = tusum(N1,N2)
    print("#{} {}".format(i,tu.index(N3)+1))
