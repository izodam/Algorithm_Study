# 가장 높은 건물을 기준으로 오/왼 나눠서 생각
n = int(input())

house = [0] * 1001
m = 0
m_idx = 0

for _ in range(n):
    L, H = map(int,input().split())

    # 창고 높이 저장
    house[L] = H

    # 가장 높은 기둥, 그 인덱스 찾기
    if m < H:
        m = H
        m_idx = L

res = 0
height = 0
# 높은 건물 기준 왼쪽 탐색
for i in range(m_idx + 1):
    # 왼쪽 건물들 사이에서 지금까지 나왔던 건물들 중 최대값 찾기
    if house[i] > height:
        height = house[i]
    res += height

height = 0
# 높은 건물 기준 오른쪽 탐색
for i in range(1000, m_idx, -1):
    if house[i] > height:
        height = house[i]
    res += height
print(res)