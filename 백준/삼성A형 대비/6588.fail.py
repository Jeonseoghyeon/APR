#에라토스테네스의 체 공부해서 다시 해보기

def sosu(x):
    cnt = 0
    for i in range(1,x+1):
        if x % i == 0:
            cnt+=1
            if cnt>=3:
                return 0
    if cnt == 2:
        return 1
    else:
        return 0

while True:
    check = 0
    x = int(input())
    if x == 0:
        break
    for up in range(3,x//2+1):
        for down in range(x-3,x//2-1,-1):
            if up + down == x:
                if sosu(up) == 1 and sosu(down) == 1:
                    print("{} = {} + {}".format(x,up,down))
                    check = 1
                    break
            else:
                continue
        
        if check ==1 :
            break