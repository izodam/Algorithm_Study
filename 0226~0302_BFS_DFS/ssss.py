import sys
from collections import deque

input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
total = []


def bfs(row, col):
    q = deque()
    q.append([row, col])
    arr[row][col] = 3
    res = []

    while q:
        row, col = q.popleft()
        for k in range(4):
            nr = row + dr[k]
            nc = col + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 1:
                    q.append([nr, nc])
                    arr[nr][nc] = 3
                if arr[nr][nc] == 0:
                    if (row, col) in res:
                        continue
                    res.append((row, col))                          # 대륙의 끝점 저장
    return res


n = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

for row in range(n):
    for col in range(n):
        if arr[row][col] == 1:
            result = bfs(row, col)
            total.append(result)
print(total)
Min_ans = float('inf')
for i in range(len(total) - 1):                                      # 끝 점 꺼내서 비교
    for j in range(i + 1, len(total)):
        for k in total[i]:
            for l in total[j]:
                print(k,l)
                ans = abs(k[0] - l[0]) + abs(k[1] - l[1])            #
                if Min_ans > ans:
                    Min_ans = ans

print(Min_ans - 1)