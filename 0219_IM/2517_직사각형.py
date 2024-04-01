for i in range(4):
    sq1x,sq1y,sq1p,sq1q,sq2x,sq2y,sq2p,sq2q = map(int,input().split())

    if sq1p < sq2x or sq1q < sq2y or sq1x > sq2p or sq1y > sq2q:
        print('d')
    elif sq1p == sq2x or sq1x == sq2p:
        if sq1q == sq2y or sq1y == sq2q:
            print('c')
        else:
            print('b')
    elif sq1q == sq2y or sq1y == sq2q:
        print('b')
    else:
        print('a')