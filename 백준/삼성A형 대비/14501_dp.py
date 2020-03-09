N = int(input())
timepay = list(list(map(int, input().split())) for _ in range(N))
dp = [0] * N


for i in range(N):
    if i + timepay[i][0] <= N:
        dp[i] = timepay[i][1]
        for j in range(i):
            if j + timepay[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + timepay[i][1])

print(max(dp))