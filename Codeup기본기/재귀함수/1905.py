import sys
sys.setrecursionlimit(1000000)

def my_sum(start,end):
    global sumn
    if start == end+1:
        return
    else:
        sumn += start
        my_sum(start+1,end)
    return sumn

x = int(input())
sumn = 0
print(my_sum(1,x))
