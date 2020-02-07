def tusum(kwgs1,kwgs2): # 좌표끼리의 합 함수
    x = kwgs1[0]+kwgs2[0]
    y = kwgs1[1]+kwgs2[1]
    return (x,y)
# 리스트 뽑아냄
x=1
y=1
z=1
tu=[]
for i in range(1,15):
    if i == 1:
        tu +=[[1,1]]
    elif i == y:
        for j in range(1,z+1):
            tu += [[j,z-j+1]]
    else:
        continue
    y+=z
    z+=x
    

