def my_bin(n,k): # 
    if n<k:
        if n==0:
            return
        else:
            print(n,end ='')
    else:
        my_bin(n//k,k)
        print(n%k,end='')
    
    

n = int(input())
if n == 0:
    print(0)
else:
    my_bin(n,2)