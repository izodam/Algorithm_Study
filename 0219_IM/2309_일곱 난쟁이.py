nan = [int(input()) for _ in range(9)]
ssum = 0

# 정렬과 전체 합 구하는 for문
for i in range(9):
    ssum += nan[i]
    # idx = i
    # for j in range(9):
    #     if nan[idx] < nan[j]:
    #         idx = j
    #     nan[i], nan[idx] = nan[idx], nan[i]

nan.sort()

sub = ssum - 100

for i in nan:
    if (sub - i) in nan:
        nan.remove(i)
        nan.remove(sub-i)
        break

print('\n'.join(map(str,nan)))