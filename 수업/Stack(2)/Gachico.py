a = [1,2,3,4,5,6,7,8,9,10]
result = [False] * len(a)
def powerset(cnt,tot):
    if tot==10:
        print(set(a[i] for i in range(len(a)) if result[i]))
        return
    if tot>10:
        return
    if cnt==len(a):
        return
    result[cnt] = True
    powerset(cnt+1,tot+a[cnt])
    result[cnt] = False
    powerset(cnt+1,tot)
powerset(0,0)