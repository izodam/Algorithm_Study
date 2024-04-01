# stack 사용해서 구현은 못하나 궁금!!!

# 재귀 limit 늘려주기
import sys
sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    # 방문처리
    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and bamboo[nx][ny] > bamboo[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)
    return dp[x][y]


n = int(input())
bamboo = [list(map(int,input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i,j))

print(res)