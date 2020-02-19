import sys
sys.stdin = open("Magnetic_input.txt","r")

for i in range(1,11):
    t = int(input())
    arr = [list(map(int,input().split())) for a_rr in range(t)]
    cnt = 0
    for y in range(100):
        test = []
        for x in range(100):
            if arr[x][y] == 1:
                test = [arr[x][y]]
            elif arr[x][y] == 2:
                test.append(arr[x][y])
            if len(test) == 2 and test[0] ==1:
                cnt+=1
                test.clear()
    print("#{} {}".format(i,cnt))