# 2477번
# 밭의 넓이는 큰 사각형 - 작은 사각형
# 작은 사각형의 가로는 가장 긴 세로의 전과 후 입력의 차
# 작은 사각형의 세로는 가장 긴 가로의 전과 후 입력의 차

k = int(input())
total = []

direc, length = map(int,input().split())
total.append(length)
if direc == 1 or direc == 2:
    # 가장 긴 가로,세로의 인덱스 저장 변수
    long_x, long_y= 0, 1
else:
    long_x, long_y = 1, 0


for i in range(1, 6):
    direc, length = map(int,input().split())
    total.append(length)

    if direc == 1 or direc == 2:
        if total[long_x] < length:
            long_x = i
    else:
        if total[long_y] < length:
            long_y = i

# 큰 사각형
res = total[long_x] * total[long_y]

# 작은 사각형
mini_x = total[long_y-1 if long_y > 0 else 5] - total[long_y+1 if long_y<5 else 0]
mini_y = total[long_x-1 if long_x > 0 else 5] - total[long_x+1 if long_x<5 else 0]


mini = mini_x * mini_y
if mini < 0: mini *= -1
res -= mini

print(res * k)