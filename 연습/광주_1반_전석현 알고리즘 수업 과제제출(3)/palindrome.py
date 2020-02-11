import sys
sys.stdin = open("palindrome_input.txt","r")

tc = int(input())
for i in range(1,tc+1):
    N,M = list(map(int,input().split())) # N = 크기 / M = 길이
    arr = [(input()) for x in range(N)]
    result = ''
    for x in range(N):
        for y in range(N-M+1):
            pal = arr[x][y:y+N]
            if pal == pal[::-1]:
                result = pal
      
    for y in range(N):
        for x in range(N-M+1): #1까지만
            for dx in range(M): #dx = 0
                check = True
                if arr[x+dx][y] == arr[x+M-dx-1][y]:
                    continue
                else:
                    check = False
                    break
            if check == True:
                result = ''.join([arr[x][y] for x in range(N-M,M)])
    print('#{} {}'.format(i,result))
            







