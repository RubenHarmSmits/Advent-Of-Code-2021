import math

lines = [list(map(int,list(x))) for x in open('input.txt').read().strip().split('\n')]

basins = []

class Coor:
    def __init__(self, y, x):
        self.y=y
        self.x=x

    def eq(self, c):
        return c.y == self.y and c.x == self.x

def getAllNeighbours(y, x):
    n = []
    if x>0:
        n.append(Coor(y,x-1))
    if y>0:
        n.append(Coor(y-1,x))
    if x <len(line)-1:
        n.append(Coor(y,x+1))
    if y <len(lines)-1:
        n.append(Coor(y+1,x))
    return n

def ninnb(n, nb):
    for nnb in nb:
        if nnb.eq(n):
            return True
    return False

def getSizeBasin(y,x,coor):
    coor.append(Coor(y,x))
    nb = getAllNeighbours(y,x)
    for n in nb:
        num = lines[n.y][n.x]
        if num != 9:
            if not ninnb(n, coor):
                getSizeBasin(n.y, n.x, coor)

    return len(coor)



for y,line in enumerate(lines):
    for x,num in enumerate(line):
        nb = getAllNeighbours(y, x)
        if num < min([lines[c.y][c.x] for c in nb]):
            basins.append(getSizeBasin(y,x, []))
basins.sort()
print(math.prod(basins[-3:]))