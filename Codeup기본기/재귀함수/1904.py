def odd(a,b): #start, end
    if a == b+1:
        return
    else:
        if a%2:
            print(a,end=' ')
    odd(a+1,b)

    
a,b = list(map(int,input().split()))
odd(a,b)