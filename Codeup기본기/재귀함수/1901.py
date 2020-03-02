def goup(x):
    if x == 1:
        print(1)
        return 1
    goup(x-1)
    print(x)
    

goup(int(input()))