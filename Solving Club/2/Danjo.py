import sys
sys.stdin = open("Danjo input.txt","r")

def Danjo(kwgs): # 리스트의 범위 내에서 다음 인덱스의 수가 더 큰지 아닌지를 전체 판단해줌으로써 Boolean값을 반환해주는 함수
    for x in range(len(kwgs)-1):
        if kwgs[x]<=kwgs[x+1]:
            continue
        else:
            return False
    return 1

tc = int(input())
for i in range(1,tc+1):
    N = int(input())
    numul_list = []
    num1_list = list(map(int,input().split()))
    for j in range(0,N):
        for k in range(j+1,N):
            numul_list +=list(map(str,[num1_list[j]*num1_list[k]])) # 숫자들의 곱을 리스트에 저장 : Numul_list
    max = 0
    for l in numul_list: 
        if Danjo(l) == 1:
            if int(l)>max:
                max = int(l)
        elif Danjo(l) == 0:
            pass

    if max == 0:
        print("#{} -1".format(i))
    else:
        print("#{} {}".format(i,max))


'''
좋지 않은 코드. 실행시간 안에 겨우 들어왔음

'''