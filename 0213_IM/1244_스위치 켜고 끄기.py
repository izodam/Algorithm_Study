def turnswitch(switch, n):
    if switch[n] == 1:
        switch[n] = 0
    else:
        switch[n] = 1

n = int(input())
switch = list(map(int, input().split()))
# 0번 인덱스 처리
switch = [0] + switch
stu = int(input())

for _ in range(stu):
    s, num = map(int,input().split())
    # 남학생이면
    if s == 1:
        for i in range(num, n+1, num):
            turnswitch(switch, i)
    else:
        i = 1
        change = [num]
        # 대칭 찾기
        while True:
            if num - i < 1 or num + i > n:
                break
            elif switch[num-i] != switch[num+i]:
                break
            else:
                change.append(num+i)
                change.append(num-i)
            i += 1

        # 스위치 바꾸기
        for i in change:
            turnswitch(switch, i)
for i in range(1,n+1):
    print(switch[i],end=' ')
    if i%20==0:
        print()