def backtrack(a,k,input):
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES
    if k == input :
        sum_10 = []
        if sum(a) == 10:
            for s10 in range(1,len(a)):
                if a[s10] !=0:
                    sum_10.append(a[s10])
            print(sum_10)
        

    else:
        k+=1
        ncanditates = construct_candidates(a,k,input,c)
        for i in range(ncanditates):
            a[k] = c[i] * b[k]
            backtrack(a,k,input)

def construct_candidates(a,k,input,c):
    c[0] = True
    c[1] = False

    return 2


MAXCANDIDATES = 2
NMAX = 11
a = [0]*11
b = [0,1,2,3,4,5,6,7,8,9,10,0]
backtrack(a,0,10)

