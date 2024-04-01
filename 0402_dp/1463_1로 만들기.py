n = int(input())

# n+1로 하면 input이 1이 들어오면 index error 발생
# n+2로 설정하면 그러한 에러를 방지한다.
dp = [0] * (n+2)
dp[1] = 0
dp[2] = 1

for i in range(3, n+1):
    if dp[i] == 0:
        # 2와 3 모두 나누어 떨어지면
        # 그 중 최소값 선택
        if i % 2 == 0 and i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1]) + 1
        else:
            dp[i] = dp[i-1] + 1
print(dp[n])