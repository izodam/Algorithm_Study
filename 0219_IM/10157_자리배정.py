c, r = map(int, input().split())
k = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

sit = [[0] * c for _ in range(r)]

direction = 0
x,y = 0, 0

# k번째 사람 앉을 수 없음
if k > c*r:
    print(0)

else:
    for num in range(1, k):
        sit[x][y] = num
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 0<=nx<r and 0<=ny<c and sit[nx][ny] == 0:
            # 이동 가능!
            x = nx
            y = ny
        else:
            # 그게 아니라면 방향을 바꿔줘야 함
            direction = (direction+1)%4
            x += dx[direction]
            y += dy[direction]

    print(y+1,x+1)