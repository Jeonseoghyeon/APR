a = [1,2,3,4,5,6,7,8,9,10]

def powerset(cnt,t):
    if cnt==k:
        print(result)
        return
    for i in range(t,len(a)):
        result[cnt] = a[i]
        powerset(cnt+1,a[i])

k = 3
result = [0] * k
powerset(0,0)