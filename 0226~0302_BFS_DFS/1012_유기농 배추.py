from collections import deque
import sys
input = sys.stdin.readline

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + delta[i][0], y + delta[i][1]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))



T = int(input())
for tc in range(1, T+1):
    m, n, k = map(int,input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int,input().split())
        graph[x][y] = 1

    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                res += 1
    print(res)