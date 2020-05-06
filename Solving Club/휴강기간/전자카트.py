import sys
sys.stdin = open("전자카트_input.txt","r")
from itertools import permutations

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*(N+1)] + [[0]+list(map(int,input().split())) for x in range(N)]
    routes = list(permutations(range(2,N+1),N-1))
    min_battery = 999999
    for route in routes:
        battery = arr[1][route[0]] + arr[route[-1]][1]
        for i in range(len(route)-1):
            battery += arr[route[i]][route[i+1]]
        if battery <= min_battery:
            min_battery = battery

    print("#{} {}".format(tc,min_battery))
