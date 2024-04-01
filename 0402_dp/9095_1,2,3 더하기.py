T = int(input())
input_arr = [int(input()) for _ in range(T)]

cal_max = max(input_arr)

dp = [0] * (cal_max + 1)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, cal_max+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in input_arr:
    print(dp[i])