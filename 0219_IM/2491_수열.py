n = int(input())
arr = list(map(int,input().split()))

dp = [1] * n

for i in range(1,n):
    if arr[i-1] <= arr[i]:
        dp[i] = dp[i-1] + 1
res = 0
for i in dp:
    if i > res:
        res = i
dp = [1] * n

for i in range(1,n):
    if arr[i-1] >= arr[i]:
        dp[i] = dp[i-1] + 1
for i in dp:
    if i > res:
        res = i
print(res)