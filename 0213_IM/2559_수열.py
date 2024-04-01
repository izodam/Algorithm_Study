n, k = map(int, input().split())
temp = list(map(int, input().split()))

res = 0
for i in range(k):
    res += temp[i]
tmp = res

for i in range(n-k):
    tmp = tmp - temp[i] + temp[k+i]
    if tmp > res:
        res = tmp

print(res)