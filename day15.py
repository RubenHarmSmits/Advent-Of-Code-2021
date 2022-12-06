from collections import Counter
import numpy
from coor import Coor



def makeGrid(g):
    length = len(g[0])
    l = []
    grid = []
    for x in range(5):
        for y in range(5):
            ng = list(map(lambda l:list(map(lambda n:((n+x+y-1)%9)+1,l)),g[:]))
            l.append(ng)
    
    for n in range(5):
        grid+=l[n]
    

    for i in range(length):
        grid[i] += l[5][i]

    for i in range(length):
        grid[i+length] += l[6][i]
    
    for i in range(length):
        grid[i+(2 *length)] += l[7][i]
    
    for i in range(length):
        grid[i+(3 *length)] += l[8][i]

    for i in range(length):
        grid[i+(4 *length)] += l[9][i]


    for i in range(length):
        grid[i] += l[10][i]

    for i in range(length):
        grid[i+length] += l[11][i]
    
    for i in range(length):
        grid[i+(2 *length)] += l[12][i]
    
    for i in range(length):
        grid[i+(3 *length)] += l[13][i]

    for i in range(length):
        grid[i+(4 *length)] += l[14][i]


    for i in range(length):
        grid[i] += l[15][i]

    for i in range(length):
        grid[i+length] += l[16][i]
    
    for i in range(length):
        grid[i+(2 *length)] += l[17][i]
    
    for i in range(length):
        grid[i+(3 *length)] += l[18][i]

    for i in range(length):
        grid[i+(4 *length)] += l[19][i]


    for i in range(length):
        grid[i] += l[20][i]

    for i in range(length):
        grid[i+length] += l[21][i]
    
    for i in range(length):
        grid[i+(2 *length)] += l[22][i]
    
    for i in range(length):
        grid[i+(3 *length)] += l[23][i]

    for i in range(length):
        grid[i+(4 *length)] += l[24][i]
    return grid



grid = makeGrid([list(map(int,x)) for x in open('input.txt').read().split('\n')])

a=5

c = Coor(0,0)
e = Coor(len(grid) -1,len(grid[0]) -1)
def makeKey(y,x):
    return 'y'+str(y)+'x'+str(x)

class Point:
        def __init__(self, number, c):
            self.number=number
            self.c=c
            self.n = []
            self.visited = False
            self.shortest = 999999999
            self.touched = False
        
points = {}
for y in range(len(grid[0])):
    for x in range(len(grid)):
        points[makeKey(y,x)]=Point(grid[y][x],Coor(y,x))

for key in points:
    # print(len(points)-i)
    p = points[key]
    n=[]
    if p.c.y>0:
        n.append(points[makeKey(p.c.y-1,p.c.x)])
    if p.c.y<e.y:
        n.append(points[makeKey(p.c.y+1,p.c.x)])
    if p.c.x>0:
        n.append(points[makeKey(p.c.y,p.c.x-1)])
    if p.c.x<e.x:
        n.append(points[makeKey(p.c.y,p.c.x+1)])
    p.n = n

def neighbors4(r, c, h, w):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if 0 <= rr < w and 0 <= cc < h:
            yield rr, cc

unvisited = dict(points)

points[makeKey(0,0)].shortest =0

touched = {makeKey(0,0):points[makeKey(0,0)]}


while (a := min(touched, key=lambda x:touched[x].shortest, default=None)) != None:
    node =points[a]
    node.visited = True
    del touched[a]
    del unvisited[a]
    for nb in list(filter(lambda p: not p.visited,node.n)):
        nb.shortest = min(nb.number + node.shortest,nb.shortest)
        touched[makeKey(nb.c.y,nb.c.x)] = nb




print(points[makeKey(e.y,e.x)].shortest)

