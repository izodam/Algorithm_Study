n = int(input())
paper = [[0] * 1001 for _ in range(1001)]

res = [0]

for num in range(1,n+1):
    x,y,w,h = map(int,input().split())
    for i in range(h):
        for j in range(w):
            if paper[x+j][y+i] != 0:
               res[paper[x+j][y+i]] -= 1
            paper[x+j][y+i] = num

    res.append(w*h)


print('\n'.join(map(str,res[1:])))