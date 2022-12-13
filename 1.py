from sys import stdin, stdout

def BoundWhite(mtx):
    l = []
    if mtx == []:
        return 0
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            if mtx[i][j] == 1:
                TraverseMtx(mtx, i, j)
                l.append([i, j, len(mtx)-i, len(mtx[0])-j])
    return l

def TraverseMtx(mtx, x, y):
    if x < 0 or y < 0 or x >= len(mtx) or y >= len(mtx[0]) or mtx[x][y] != 1:
        return 
    mtx[x][y] = 2
    TraverseMtx(mtx, x-1, y)
    TraverseMtx(mtx, x, y-1)
    TraverseMtx(mtx, x+1, y)
    TraverseMtx(mtx, x, y+1)

mtx = [[1, 1, 0, 0, 0], [0, 1, 0, 0, 1], [1, 0, 0, 1, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 0]]
print(BoundWhite(mtx))