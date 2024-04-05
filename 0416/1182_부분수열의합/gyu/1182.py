import sys

input = sys.stdin.readline


def dfs(idx,summ):
    global cnt,s

    if summ==s and len(ss)>=1: #부분수열의 길이는 0이 될 수 없다.
        cnt +=1
        #return 하지 않는다. 해당 부분수열에 값을 추가하여 0이 되는 경우가 있을 수 있음.
    if idx==n:
        return
    for i in range(idx,n):
        if not i in ss:
            ss.append(i)
            dfs(i+1,summ+an[i])
            ss.pop()


n,s = map(int,input().split())
an = list(map(int,input().split()))

cnt = 0
ss = []
dfs(0,0)
print(cnt)