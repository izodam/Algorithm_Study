n = int(input())

white = [[0] * 100 for _ in range(100)]
res = 100 * n
for i in range(n):
    x,y = map(int,input().split())
    for dx in range(10):
        for dy in range(10):
            if white[x+dx][y+dy]:
                res -= 1
            white[x+dx][y+dy] = 1
print(res)