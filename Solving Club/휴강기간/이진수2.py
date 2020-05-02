import sys
sys.stdin = open("이진수2_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = float(input()) 
    i = 0
    result = ""
    while i !=13:
        i+=1
        N *= 2 
        if N == 0:
            print("#{} {}".format(tc,result))
            break
        else:
            if N >=1:
                N -=1 
                result+= '1'
            else: 
                result+= '0'
    if N != 0:
        print("#{} {}".format(tc,'overflow'))

        


