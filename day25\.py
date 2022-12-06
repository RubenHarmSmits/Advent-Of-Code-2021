from collections import Counter
from coor import Coor

grid = [list(x) for x in list(open('input2.txt').read().split('\n'))]
hoogte = len(grid)
breedte = len(grid[0])

n=0
moved = True
while moved:
    moved = False
    n+=1
    copy = [x[:] for x in grid]
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if c == '>':
                try:
                    if grid[y][x+1] == '.':
                        copy[y][x+1] = '>'
                        copy[y][x] = '.'
                        moved = True
                except IndexError:
                    if grid[y][0] == '.':
                        copy[y][0] = '>'
                        copy[y][x] = '.'
                        moved = True
    copy2 = [x[:] for x in copy]
    for y, line in enumerate(copy):
        for x, c in enumerate(line):
            if c == 'v':
                try:
                    if copy[y+1][x] == '.':
                        copy2[y+1][x] = 'v'
                        copy2[y][x] = '.'
                        moved = True
                except IndexError:
                    if copy[0][x] == '.':
                        copy2[0][x] = 'v'
                        copy2[y][x] = '.'
                        moved = True
    grid = copy2




print(n)




