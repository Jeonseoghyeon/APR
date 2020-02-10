import sys
sys.stdin = open("ladder input.txt","r")

for p in range(1,11): # 10번
    tc_number = int(input())
    x=[]
    # print(tc_number)
    start = list(map(int,input().split()))
    for q in range(99):
        x += [list(map(int,input().split()))]
    d = []
    for u in range(len(start)):
        if start[u] == 1:
            d += [u] # 스타트 하는 인덱스들 저장 : d
    min = 999
    min_d=0

    for a,i in enumerate(d):
        n = a
        j = 0 
        count = 0
        while j != 99: # 99열일 때 : 도착했을 때
            if i == 0:
                if x[j][i+1]!=1: #오른쪽 확인
                    j+=1
                    count+=1
                elif x[j][i+1]==1:#오른쪽 확인
                    i+=(d[a+1]-d[a])
                    count+=(d[a+1]-d[a])
                    a+=1
                    j+=1
                    count+=1
                    if x[j][i+1]==0:#오른쪽 확인
                        j=j+1
                        count+=1
            elif i == d[-1]:
                if x[j][i-1]!=1: #왼쪽 확인
                    j+=1
                    count+=1
                elif x[j][i-1]==1:#왼쪽 확인
                    i-=(d[a]-d[a-1])
                    count+=(d[a]-d[a-1])
                    a-=1
                    j+=1
                    count+=1
                    if x[j][i+1]==0:#오른쪽 확인
                        j=j+1
                        count+=1
            else:
                if x[j][i+1]==1:#오른쪽 확인
                    i+=(d[a+1]-d[a])
                    count+=(d[a+1]-d[a])
                    a+=1
                    j+=1
                    count+=1
                elif x[j][i-1]==1: #왼쪽 확인
                    i-=(d[a]-d[a-1])
                    count+=(d[a]-d[a-1])
                    a-=1
                    j+=1
                    count+=1
                else:
                    j+=1
                    count+=1
        if count<min:
            min = count
            min_d = d[n]
        n=n+1
    print("#{} {}".format(p,min_d))