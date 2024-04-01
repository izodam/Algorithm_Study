def findmax(dice, arr):
    res = 0
    for i in arr:
        if dice[i] > res:
            res = dice[i]
    return res


n = int(input())
dice1 = list(map(int, input().split()))
# 2 3 1 6 5 4
other_dice = [list(map(int, input().split())) for _ in range(n-1)]

# (위 아래) = ([0] [5]) ([1] [3]) ([2] [4])
# 옆면의 인덱스를 미리 리스트로 저장
side = [[1,2,3,4], [0,2,4,5], [0,1,3,5], [0,2,4,5], [0,1,3,5], [1,2,3,4]]
# 인덱스별로 위로 와야하는 인덱스 번호를 미리 리스트로 저장
up_down = [5,3,4,1,2,0]

res = 0

# up = 1번 주사위의 위에 오는 숫자
for up in range(6):
    now_up = dice1[up]
    hap = findmax(dice1,side[up])

    for dice in range(n-1):
        # 현재 주사위에서 아래에 둬야하는 숫자의 인덱스 찾기
        for num in range(6):
            if other_dice[dice][num] == now_up:
                # 옆면 중 최대값 더하기
                hap += findmax(other_dice[dice], side[num])
                # 지금 주사위의 윗면 숫자 새로 update
                now_up = other_dice[dice][up_down[num]]
                break

    # 최대값 update
    if hap > res:
        res = hap

print(res)