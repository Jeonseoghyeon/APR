def odd(a,b):
    if a%2 == 0:
        if a==b:
            return 1
        odd(a+1,b)
    else:
        if a == b:
            print(a)
            return 1
        print(a)
        odd(a+1,b)

a,b = list(map(int,input().split()))
odd(a,b)