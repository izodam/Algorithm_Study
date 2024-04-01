def bingo(arr):
    cheak = 0
    # 가로줄 확인
    for i in range(5):
        cnt = 0
        for j in range(5):
            if arr[i][j] != 0:
                break
            else:
                cnt += 1
        if cnt == 5:
            cheak += 1

    # 세로줄 확인
    for i in range(5):
        cnt = 0
        for j in range(5):
            if arr[j][i] != 0:
                break
            else:
                cnt += 1
        if cnt == 5:
            cheak += 1

    # 대각선 확인
    cnt = 0
    for i in range(5):
        if arr[i][i] != 0:
            break
        else:
            cnt += 1
    if cnt == 5:
        cheak += 1

    cnt = 0
    for i in range(5):
        if arr[4-i][i] != 0:
            break
        else:
            cnt += 1
    if cnt == 5:
        cheak += 1

    if cheak >= 3:
        return True

    return False

def cheak(board, n):
    for i in range(5):
        for j in range(5):
            if board[i][j] == n:
                board[i][j] = 0

chul = [list(map(int,input().split())) for _ in range(5)]
mc = [list(map(int,input().split())) for _ in range(5)]
res = 0
for j in range(5):
    for i in mc[j]:
        cheak(chul, i)
        res += 1
        if bingo(chul):
            print(res)
            exit(0)
