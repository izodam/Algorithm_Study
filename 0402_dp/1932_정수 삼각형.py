n = int(input())
tri = [list(map(int,input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(tri[i])):
        # 제일 왼쪽이면 선택지는 바로 위에 있는 애밖에 없음
        if j == 0:
            tri[i][j] += tri[i-1][j]
        # 제일 오른쪽도 마찬가지
        elif j == len(tri[i])-1:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

# 출력은 제일 마지막줄의 최대값
print(max(tri[-1]))