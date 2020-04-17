import sys
sys.stdin = open("수영장_input.txt","r")

def dfs(month, cost):
    global min_cost
    if month >= 12:
        if cost < min_cost:
            min_cost = cost
        return
 
    elif cost > min_cost:
        return
 
    if plan[month] != 0:
        # print(month, cost)
        dfs(month + 1, cost + prices[0] * plan[month])
        dfs(month + 1, cost + prices[1])
        dfs(month + 3, cost + prices[2])
    else:
        dfs(month + 1, cost)
 
 
T = int(input())
for t in range(1, T + 1):
    prices = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_cost = prices.pop()
 
    dfs(0, 0)
    print('#{} {}'.format(t, min_cost))