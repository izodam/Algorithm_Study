# 10158번
'''
6 4
4 1
8

w는 [4,5,6,5,4,3,2,1,0,1,2,3]이 반복되는데 이 길이는 12 = w*2
h는 [1,2,3,4,3,2,1,0]이 반복되는데 이 길이는 8 = h*2
'''



w, h = map(int,input().split())
p, q = map(int,input().split())
t = int(input())

wlist = list(range(p,w)) + list(range(w,-1,-1)) + list(range(1,p))
hlist = list(range(q,h)) + list(range(h,-1,-1)) + list(range(1,q))

print(wlist[t%(2*w)],hlist[t%(2*h)])