tc = int(input())

for i in range(1,tc+1): # 테스트 케이스
    Ar1,Ar2,Ac1,Ac2 = list(map(int,input().split()))
    Br1,Br2,Bc1,Bc2 = list(map(int,input().split()))
    arr = []
    A_original = 0
    B_original = 0
    A_changed = 0
    B_changed = 0
    for j in range(10):
        arr += [list(map(int,input().split()))]

    for A1 in range(Ar1,Ac1+1):
        for A2 in range(Ar2,Ac2+1):
            A_original = arr[A1][A2]
            arr[A1][A2] = arr[A1][A2] * 2
            if arr[A1][A2]>=255:
                arr[A1][A2] = 255
            A_changed += abs(A_original - arr[A1][A2] )
            
            

    for B1 in range(Br1,Bc1+1):
        for B2 in range(Br2,Bc2+1):
            B_original = arr[B1][B2]
            arr[B1][B2] = arr[B1][B2] // 2
            B_changed += abs(B_original - arr[B1][B2] )
            

    print('#{} {}'.format(i,A_changed+B_changed))
