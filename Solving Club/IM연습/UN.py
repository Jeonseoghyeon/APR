import sys
sys.stdin = open("UN_input.txt","r")

tc = int(input())
for i in range(1,2+1):
    x=[]
    rngs = []
    times = int(input()) #5
    for j in range(times): 
        x+=[list(map(int,input().split()))]

    for k in range(times-1): # 0,1,2,3
        for l in range(times-1): # 0,1,2,3
            count_x = 0
            count_y = 0
            if x[k][l] == 99:
                continue
            if x[k][l] != 0:
                a = l
                b = k
                while x[k][l] != 0:
                    x[k][l] = 99
                    l +=1
                    count_y+=1
                    
                l = a # 원래 값으로
                while x[k][l] != 0:
                    x[k][l] = 99 # 99로 바꿔줘서 안들어가게끔?
                    k += 1
                    count_x+=1
                    
                k = b # 원래 값으로
        # print(x)
            if count_x !=0 and count_y !=0:
                rngs += [[count_x,count_y]] 
        # print(x)

                print(rngs)
            
            

# [4,3], [1,2] , [5,1], [2,4]

