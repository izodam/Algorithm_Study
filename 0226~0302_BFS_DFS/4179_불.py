# 4179
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def jihun(fire_q, q):
    cnt = 1
    # while 한번이 1타임
    while True:
        cheak = 0
        # 불 이동
        fire_q = fire(fire_q)
        # 지훈 이동
        # 지훈이도 지금 이동 한 위치를 기준으로 다음 타임 때 이동
        tmp = deque()
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 탈출 성공
                if nx < 0 or nx >= r or ny < 0 or ny >= c:
                    return cnt
                elif board[nx][ny] == '.':
                    tmp.append((nx,ny))
                    board[nx][ny] = 'J'
                    cheak = 1
        q = tmp
        cnt += 1

        # 지훈이 이동 못했으면 탈출 불가능
        if not cheak:
            return 0

def fire(fire_q):
    # 한번 이동 했던 불은 다음 타임 때 이동 불필요
    # 지금 불이 이동한 곳을 tmp에 담고 다음 타임 때 tmp에 담아있는 자리들만 이동시키면 된다
    tmp = []
    for j in range(len(fire_q)):
        x,y = fire_q[j][0], fire_q[j][1]
        for i in range(4):
            # 4방향으로 불 퍼짐
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and (board[nx][ny] == '.' or board[nx][ny] == 'J'):
                board[nx][ny] = 'F'
                tmp.append((nx,ny))
    return tmp



r, c = map(int,input().split())
board = [list(input().rstrip()) for _ in range(r)]

q = deque()
fire_q = deque()

# 불과 지훈이 위치 받아서 덱에 넣어주기
for i in range(r):
    for j in range(c):
        if board[i][j] == 'F':
            fire_q.append((i,j))
        if board[i][j] == 'J':
            q.append((i,j))

res = jihun(fire_q, q)

if res:
    print(res)
else:
    print('IMPOSSIBLE')

