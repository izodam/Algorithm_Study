from collections import deque
# 잠기지 않는 곳을 1, 잠기는 곳을 0으로 하여 보드 새로 만들어줌
def water(height):
    new_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > height:
                new_board[i][j] = 1
    return new_board

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, new_board):
    q = deque()
    # 방문처리
    q.append((x,y))
    new_board[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<=ny<n and new_board[nx][ny] == 1:
                q.append((nx, ny))
                new_board[nx][ny] = 0



n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
# 아무 지역도 물에 잠기지 않는다면 안전구역은 1이 되므로 초기값을 1로 설정
res = 1

# 높이 최대
height = max(map(max, board))

for h in range(1, height):
    new_board = water(h)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if new_board[i][j] == 1:
                bfs(i, j, new_board)
                cnt += 1
    res = max(res, cnt)


print(res)