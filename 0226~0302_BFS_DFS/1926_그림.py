from collections import deque


def bfs(x, y, graph):
    # 이동 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque()
    # 방문 처리
    q.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny]:
                q.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1

    return cnt


n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]

res = []

for i in range(n):
    for j in range(m):
        if pic[i][j]:
            res.append(bfs(i, j, pic))

if len(res) == 0:
    print(0)
    print(0)
else:
    print(len(res))
    print(max(res))