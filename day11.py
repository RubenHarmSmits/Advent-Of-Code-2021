import math

class Coor:
    def __init__(self, y, x):
        self.y=y
        self.x=x

    def eq(self, c):
        return c.y == self.y and c.x == self.x


grid = [list(map(int,list(x))) for x in open('input.txt').read().strip().split('\n')]

print(grid)

count = 0

def num10():
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 10:
                return True
    return False

    #1591  #1592

for i in range(99999999):
    grid  = [list(map(lambda n:n+1,line)) for line in grid]
    flashes = []
    while num10():
        for y,line in enumerate(grid):
            for x,num in enumerate(line):
                if grid[y][x] == 10:
                    count+=1

                    for fl in flashes:
                        if fl.eq(Coor(y,x)):
                            print("333")

                    flashes.append(Coor(y,x))
                    grid[y][x] = 11
                    for h in range(-1,2):
                        for v in range(-1,2):
                            try:
                                if grid[y+h][x+v] < 10 and y+h >= 0 and x+v >=0:
                                    grid[y+h][x+v] +=1
                            except:
                                5==5
    for fl in flashes:
        grid[fl.y][fl.x] = 0
    if len(flashes) == 100:
        print(i)
        break

    # print(grid)