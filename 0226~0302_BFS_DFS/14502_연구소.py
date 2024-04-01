from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))



n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

safe_zone = []
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            safe_zone.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

tmp = [[] for _ in range(n)]
res = 0

# 위치 3개 꺼내서 벽 세우기
for wall in combinations(safe_zone, 3):
    # tmp = copy.deepcopy(graph)
    # for i in range(n):
    #     tmp[i][:] = graph[i][:]
    tmp = [i.copy() for i in graph]
    for i, j in wall:
        tmp[i][j] = 1

    # 바이러스 퍼뜨리기
    for i, j in virus:
        bfs(i, j)
    cnt = 0

    for r in tmp:
        cnt += r.count(0)
    res = max(res, cnt)

print(res)