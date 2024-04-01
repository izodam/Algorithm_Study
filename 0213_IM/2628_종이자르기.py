def findsort(arr, n):
    for i in range(n-1):
        minidx = i
        for j in range(i+1, n):
            if arr[minidx] > arr[j]:
                minidx = j
        arr[i], arr[minidx] = arr[minidx], arr[i]


n, m = map(int,input().split())
n_cut = int(input())
# 가로로 자르기
r = [0,m]
# 세로로 자르기
c = [0,n]

for _ in range(n_cut):
    cutnum, index = map(int,input().split())
    if cutnum == 0:
        r.append(index)
    else:
        c.append(index)

findsort(r, len(r))
findsort(c, len(c))

print(r, c)

pr = 0
cr = 0

# 가로 중 가장 긴 길이 찾기
for i in range(len(r)-1):
    if r[i+1]-r[i] > pr:
        pr = r[i+1]-r[i]

# 세로 중 가장 긴 길이 찾기
for i in range(len(c)-1):
    if c[i+1]-c[i] > cr:
        cr = c[i+1]-c[i]

print(pr*cr)