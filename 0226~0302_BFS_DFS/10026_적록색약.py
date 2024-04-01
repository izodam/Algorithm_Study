from collections import deque

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 정상사람
def bfs(x, y, c):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == c:
                q.append((nx, ny))
                board[nx][ny] = 0


# 색약
def bfs_have(x, y, c):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < n and 0 <= ny < n and new_board[nx][ny] == c:
                q.append((nx, ny))
                new_board[nx][ny] = 0




n = int(input())
board = [list(input()) for _ in range(n)]

# 적록색약 용 보드
new_board = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            new_board[i][j] = 'R'
        else:
            new_board[i][j] = board[i][j]

cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            bfs(i, j, board[i][j])
            cnt1 += 1
        if new_board[i][j] != 0:
            bfs_have(i, j, new_board[i][j])
            cnt2 += 1
print(cnt1, cnt2)