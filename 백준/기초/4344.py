'''
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''

tc = int(input())
for i in range(1,tc+1):
    scores = list(map(int,input().split()))
    N = scores.pop(0)
    avg = sum(scores)/N
    over_avg = 0
    for j in scores:
        if j >avg:
            over_avg +=1
    print("%.3f%%"%(over_avg/N*100))

    

    # print(round(sum(scores)/N,3))