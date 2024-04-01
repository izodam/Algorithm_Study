import sys
import copy
sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y,cnt,wall):
    # print(x, y, cnt)
    # print(wall)
    # 도착
    if x == n-1 and y == m-1:
        if wall == 1:
            res.append(visited2[x][y])
        else:
            res.append(visited1[x][y])
        print(res)
        return

    # 벽 뚫고 가기
    if board[x][y] == 1 and wall == 0:
        wall = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<=ny<m and board[nx][ny] == 0:
                visited2[x][y] = visited1[x][y] + 1
                dfs(nx, ny, cnt + 1, wall)


    if board[x][y] == 0:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if wall == 1:
                    if board[nx][ny] == 0 and visited2[nx][ny] == 0 and visited1[nx][ny] == 0:
                        visited2[nx][ny] = visited2[x][y] + 1
                        dfs(nx, ny, cnt + 1, wall)
                else:
                    if visited1[nx][ny] == 0:
                        visited1[nx][ny] = visited1[x][y] + 1
                        dfs(nx, ny, cnt + 1, wall)


n, m = map(int,input().split())
# 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽
board = [list(map(int,input())) for _ in range(n)]
visited1 = [[0] * m for _ in range(n)]
visited2 = [[0] * m for _ in range(n)]
visited1[0][0] = 1
res = []
dfs(0,0,0,0)
print('\n'.join(map(str,visited2)))
if res:
    print(min(res))
else:
    print(-1)