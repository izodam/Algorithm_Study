n = int(input())
par = list(map(int,input().split()))
fir_d = int(input())

left = [-1] * n
right = [-1] * n

# 트리 구현
for i in range(n):
    if par[i] == -1:
        continue
    if left[par[i]] != -1:
        right[par[i]] = i
    else:
        left[par[i]] = i

delete = [fir_d]

while delete:
    d = delete.pop()

    # 왼쪽이 차있어야 오른쪽도 있을 가능성 있음
    if left[d] >= 0:
        delete.append(left[d])
        if right[d] >= 0:
            delete.append(right[d])
    left[d] = -2
    right[d] = -2

res = 0
for i in range(n):
    if left[i] == fir_d:
        # 처음 잘라낸 노드가 왼쪽 노드라면, 오른쪽 노드도 비어있으면
        # 그 노드가 리프노드가 됨
        if right[i] < 0:
            res += 1
    if left[i] == -1:
        res += 1
print(res)