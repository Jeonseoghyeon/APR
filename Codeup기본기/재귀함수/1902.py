def goup(x):
    if x == 1:
        print(1)
        return 1
    print(x)
    goup(x-1)
    
    

goup(int(input()))