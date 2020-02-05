import sys
sys.stdin = open("Find_page input.txt","r")

def Find_page(p,pf):
    r = p
    l = 1
    count = 0
    while 1:
        c = int((r+l)/2)
        if c == pf:
            return count
        elif c > pf:
            r = c
            count += 1
        else:
            l = c
            count += 1
    return count

tc = int(input())
for i in range(tc):
    p,pf1,pf2 = [int(x) for x in input().split()]
    if Find_page(p,pf1) < Find_page(p,pf2):
        print("#{} A".format(i+1))
    elif Find_page(p,pf1) == Find_page(p,pf2):
        print("#{} 0".format(i+1))
    else:
        print("#{} B".format(i+1))