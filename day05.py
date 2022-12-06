from collections import Counter
import re

lines = [x for x in open('input.txt').read().strip().split('\n')]


grid = [ [0 for x in range(1000)] for y in range(1000)]

for line in lines:
    line = line.replace('->', ',').split(',')
    line =list(map(lambda i:int(i.strip()),line))
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            grid[y][x1]+=1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            grid[y1][x]+=1
    else:
        if x1 < x2 and y1 > y2:
               for i,x in enumerate(range(x1,x2+1)):
                   grid[y1-i][x]+=1
        elif x1 < x2 and y1 < y2:
            for i,x in enumerate(range(x1,x2+1)):
                grid[y1+i][x]+=1
        elif x1 > x2 and y1 < y2:
            for i,x in enumerate(range(x2,x1+1)):
                grid[y2-i][x]+=1
        elif x1 > x2 and y1 > y2:
            for i,x in enumerate(range(x2,x1+1)):
                grid[y2+i][x]+=1


count = 0
for l in grid:
    for n in l:
        if n >= 2:
            count+=1
print(count)