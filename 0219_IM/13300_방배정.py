# k = 한방 배정 최대 인원수
# s = 0 : 여/ 1 : 남
# y = 학년
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
room = 0
grade = [[0]*2 for _ in range(7)]
for i in range(n):
    s, y = map(int,input().split())
    grade[y][s] += 1

for g in grade:
    for s in g:
        room += s // k
        if s%k:
            room+=1
print(room)