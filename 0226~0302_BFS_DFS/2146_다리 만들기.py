from collections import deque

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def findisland(x,y,number):
    q = deque()
    q.append((x, y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                board[nx][ny] = number
                q.append((nx, ny))



def bridge(number):
    global res
    visited = [[0] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):
            if board[i][j] == number:
                q.append((i, j))
                visited[i][j] = 1

    while q:
        x, y = q.popleft()
        if visited[x][y] > res:
            return visited[x][y]
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 바다면 다리 잇기
                if board[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                # 다른 섬 도착
                elif board[nx][ny] != number:
                    return visited[x][y] - 1


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

res = float('inf')

# 같은 섬들은 같은 숫자로 나타내주기
number = 2

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = number
            findisland(i, j, number)
            number += 1

print('\n'.join(map(str,board)))

for i in range(2, number):
    cnt = bridge(i)
    res = min(cnt, res)
print(res)