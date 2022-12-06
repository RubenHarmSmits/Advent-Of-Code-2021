import math

from coor import Coor
input = [x for x in open('input.txt').read().strip().split('\n')]


coor = [Coor(x.split(',')[1],x.split(',')[0]) for x in input[:input.index('')]]
folds = [x.split(' ')[2] for x in input[input.index('')+1:]]

print(folds)


for f in folds:
    isX = f.split('=')[0] == 'x'
    line = int(f.split('=')[1])
    print(isX, line)

    # print(len(coor))

    for c in coor:
        if isX:
            dif = c.x - line
            if dif > 0:
                c.x = line - dif
        else:
            dif = c.y - line
            if dif > 0:
                c.y = line - dif

    for c in coor:
        for c2 in coor:
            if c.eq(c2) and c != c2:
                coor.remove(c2)
    

grid = [ [1] * 50 for _ in range(10)]

# print(grid)

for c in coor:
    grid[c.y][c.x]=0




for line in grid:
    l = ''.join(list(map(lambda l:'#' if l==0 else '.',line)))
    print(l)