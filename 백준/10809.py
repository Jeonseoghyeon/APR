x = 'abcdefghijklmnopqrstuvwxyz'
y = input()

for i in x:
    if i in y :
        print(y.index(i), end=' ')
    else:
        print(-1,end =' ')
