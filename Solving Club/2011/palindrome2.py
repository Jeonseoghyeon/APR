import sys
sys.stdin = open("palindrome2_input.txt","r")

for i in range(1,1+1):
    tc = int(input())
    arr = [input() for x in range(100)]
    result = 0
    for y in range(100):
        for n in range(99,1,-1):
            for x in range(100-n+1):
                pal = arr[y][x:x+n]
                if pal == pal[::-1]:
                    result = max(n,result)
                    break

    for x in range(100):
        for n in range(result,100):
            for y in range(100-n+1):
                pal = [arr[y+dy][x] for dy in range(n)]
                if pal == pal[::-1]:
                    result = max(n,result)
                    
    # print('#{} {}'.format(i,result))
    
                    