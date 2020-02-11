import sys
sys.stdin = open("palindrome1_input.txt","r")


for i in range(1,10+1):
    x = int(input()) # 4
    arr = []
    cnt = 0
    for j in range(8): # 크기
        arr += [list(map(str,input()))]
    # print(arr)
    for k in range(8):
        for l in range(8):
            # if l == 0:
            if l<8-x+1:
                if arr[k][l:l+x] == list(reversed(arr[k][l:l+x])):          
                    cnt+=1
            if l<8-x+1:
                check = True
                for m in range(x):
                    if arr[l+m][k] == arr[l+x-m-1][k]:
                        continue
                    else:
                        check = False
                        break
                if check ==True:
                    cnt+=1

    print('#{} {}'.format(i,cnt))
