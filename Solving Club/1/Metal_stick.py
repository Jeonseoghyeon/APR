import sys
sys.stdin = open("Metal_stick_input.txt","r")

T = int(input())
for _ in range(T):
    n = int(input())
    n_list = list(map(int, input().split()))
    for k in range(n):
        for i in range(0,n*2,2):
            for j in range(i+3,n*2,2):
                if n_list[i] == n_list[j]:
                    n_list[j-1:j+1],n_list[i:i+2] = n_list[i:i+2],n_list[j-1:j+1]
    print('#{} {}'.format(_+1, " ".join(map(str,n_list))))
        


