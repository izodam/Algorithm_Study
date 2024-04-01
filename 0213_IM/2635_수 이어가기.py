n = int(input())

def make_lst(lst):
    i = 1
    while True:
        if i >= len(lst):
            break
        if lst[i-1]-lst[i] < 0:
            break
        else:
            lst.append(lst[i-1]-lst[i])
            i += 1
    return lst

ans = []
for i in range(1, n+1):
    res = [n, i]
    res = make_lst(res)

    if len(res) > len(ans):
        ans = res

print(len(ans))
print(*ans)