import sys
sys.stdin = open("paper_input.txt","r")

def fac(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

tc = int(input())
for i in range(1,tc+1):
    L = int(input())//10
    sum_pa = 0
    sum_ver = 0

    for j in range((L//2)+1): 
        for k in range(L+1): 
            if 2*j + k == L:
                if j == 0:
                    sum_pa += 1
                else:
                    sum_pa += fac(j+k)//(fac(j)*fac(k))

    for l in range((L//2)+1): 
        for m in range((L//2)+1):
            for n in range(L+1):
                if 2*l + 2*m + n == L:
                    if m >= 1:
                        sum_ver += fac(l+m+n)//(fac(l)*fac(m)*fac(n))
    print("#{} {}".format(i,sum_pa + sum_ver))