# 2564번
w, h = map(int,input().split())
n = int(input())
store = [list(map(int,input().split())) for _ in range(n)]
dong = list(map(int,input().split()))


res = 0
this_store = []
for i in range(n):
    this_store = store[i]
    if dong[0] == 1:
        # 북북
        if this_store[0] == 1:
             res += abs(dong[1] - this_store[1])
        # 북남
        elif this_store[0] == 2:
            l1 = h + dong[1] + this_store[1]
            l2 = h + (w-dong[1]) + (w - this_store[1])
            if l1 > l2:
                res += l2
            else:
                res += l1
        # 북서
        elif this_store[0] == 3:
            res += dong[1] + this_store[1]
        # 북동
        else:
            res += (w - dong[1]) + this_store[1]

    elif dong[0] == 2:
        # 남북
        if this_store[0] == 1:
            l1 = h + dong[1] + this_store[1]
            l2 = h + (w - dong[1]) + (w - this_store[1])
            if l1 > l2:
                res += l2
            else:
                res += l1
        # 남남
        elif this_store[0] == 2:
            res += abs(dong[1] - this_store[1])
        # 남서
        elif this_store[0] == 3:
            res += dong[1] + (h - this_store[1])
        # 남동
        else:
            res += (w - dong[1]) + (h - this_store[1])

    elif dong[0] == 3:
        # 서북
        if this_store[0] == 1:
            res += dong[1] + this_store[1]
        # 서남
        elif this_store[0] == 2:
            res += (h - dong[1]) + this_store[1]
        # 서서
        elif this_store[0] == 3:
            res += abs(dong[1] - this_store[1])
        # 서동
        else:
            l1 = w + dong[1] + this_store[1]
            l2 = w + (h - dong[1]) + (h - this_store[1])
            if l1 > l2:
                res += l2
            else:
                res += l1
    else:
        # 동북
        if this_store[0] == 1:
            res += dong[1] + (w - this_store[1])
        # 동남
        elif this_store[0] == 2:
            res += (h - dong[1]) + (w - this_store[1])
        # 동서
        elif this_store[0] == 3:
            l1 = w + dong[1] + this_store[1]
            l2 = w + (h - dong[1]) + (h - this_store[1])
            if l1 > l2:
                res += l2
            else:
                res += l1
        # 동동
        else:
            res += abs(dong[1] - this_store[1])
print(res)