import sys
sys.stdin = open("UN_input.txt","r")

tc = int(input())
for i in range(1,2+1):
    x=[]
    chem_x =[]
    chem_y =[]
    chem_xy=[]
    max_x=0
    max_y=0
    times = int(input()) #5
    for j in range(times): 
        x+=[list(map(int,input().split()))]

    for k in range(times-1): # 0,1,2,3
        for l in range(times-1): # 0,1,2,3
            count_x = 0
            count_y = 0
            if x[k][l] != 0:
                a = l
                b = k
                while x[k][l] != 0:
                    l +=1
                    count_y+=1
                l = a
                while x[k][l] != 0:
                    k += 1
                    count_x+=1
                k = b                          
                if l>=k :
                    chem_y += [[count_x,count_y]]
                elif l<k:
                    chem_x += [[count_x,count_y]]
                chxy=1
                for chx1 in range(len(chem_x)):
                    for chx2 in range(len(chem_x)):
                        if chem_x[chx2][1] == chxy:
                            if chem_x[chx2][0] > max_x:
                                chem_xy += [chem_x[chx2]]
                        chxy+=1
                chxy=1
                for chy1 in range(len(chem_y)):
                    for chy2 in range(len(chem_y)):
                        if chem_y[chy2][0] == chxy:
                            if chem_y[chy2][0] > max_y:
                                chem_xy += [chem_y[chy2]]
                        chxy+=1
                
    print(chem_x)
    print(chem_y)
    print(chem_xy)
    
                

