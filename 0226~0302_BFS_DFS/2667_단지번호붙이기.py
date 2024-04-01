# 2667
from collections import deque

# 재귀 범위 넓히기
import sys
sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# bfs 구현
# def bfs(x,y):
#     q = deque()
#     q.append((x,y))
#     cnt = 1
#     graph[x][y] = 0
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
#                 q.append((nx,ny))
#                 graph[nx][ny] = 0
#                 cnt += 1
#     return cnt

# dfs 구현 - stack
# def dfs(x,y):
#     stack = [(x,y)]
#     cnt = 1
#     graph[x][y] = 0
#
#     while stack:
#         x,y = stack.pop()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
#                 cnt += 1
#                 graph[nx][ny] = 0
#                 stack.append((nx,ny))
#     return cnt

# dfs 구현 - 재귀
def dfs_recu(x,y):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] == 0:
        return

    graph[x][y] = 0
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs_recu(nx, ny)


n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

res = []

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            cnt = 0
            dfs_recu(i,j)
            res.append(cnt)

res.sort()
print(len(res))
print('\n'.join(map(str,res)))