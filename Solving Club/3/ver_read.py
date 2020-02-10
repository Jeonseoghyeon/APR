import sys
sys.stdin = open("ver_read_input.txt","r")

tc = int(input())

for i in range(1,tc+1):
    x = []
    for j in range(5):
        x += [list(input())]
    y =''
    max = 0
    min = len(x[0])
    for mx in range(len(x)):
        if len(x[mx])>max:
            max = len(x[mx])
        if len(x[mx])<min:
            min = len(x[mx])
    
    for k in range(max):
        for l in range(len(x)):
            if k>=len(x[l]): # Out of range 방지를 위해 len을 넘어갔을 땐 공백처리
                y += ''
            else:
                y +=x[l][k]
    print('#{}'.format(i),''.join(y))