n = int(input())
for r in range(n):
    # 별 = 4, 동그라미 = 3, 네모 = 2, 세모 = 1
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a_count = {4:0, 3:0, 2:0, 1:0}
    b_count = {4:0, 3:0, 2:0, 1:0}

    for i in a[1:]:
        a_count[i] += 1
    for i in b[1:]:
        b_count[i] += 1


    for shape in range(4,0,-1):
        if a_count[shape] > b_count[shape]:
            print('A')
            break
        elif a_count[shape] < b_count[shape]:
            print('B')
            break
        else:
            continue
    else:
        print('D')