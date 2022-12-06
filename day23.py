from collections import Counter
from coor import Coor

input = [list(x) for x in list(open('input2.txt').read().split('\n'))]


costMap = {'A':1, 'B':10, 'C':100, 'D':1000}
homeMap = {'A':3, 'B':5, 'C':7, 'D':9}
lowest = 100000

def done(grid):
    for x in range (3,10,+2):
        for y in range(2,6):
            if grid[y][x]!='3':
                return False
    return True

def getMoves(b, grid,c):
    moves = []
    if b.y == 3 and grid[2][b.x].isalpha():
        return moves
    if b.y == 4 and (grid[2][b.x].isalpha() or grid[3][b.x].isalpha()):
        return moves
    if b.y == 5 and (grid[2][b.x].isalpha() or grid[3][b.x].isalpha() or grid[4][b.x].isalpha()):
        return moves    
    if b.y == 2 or b.y==3 or b.y == 4 or b.y==5:
        for x in range(b.x-1,0,-1):
            if grid[1][x].isalpha():
                break
            moves.append(makeMove(x))
            if x % 2 == 0 or x==1 or x ==11:
                steps = abs(x-b.x)+b.y-1
                cost = steps * costMap[c]
                copy = [x[:] for x in grid]
                copy[b.y][b.x]='.'
                copy[1][x]=c
                moves.append((copy,cost))          
        for x in range(b.x+1,12):
            if grid[1][x].isalpha():
                break
            if x % 2 == 0 or x==1 or x ==11:
                steps = abs(x-b.x)+b.y-1
                cost = steps * costMap[c]
                copy = [x[:] for x in grid]
                copy[b.y][b.x]='.'
                copy[1][x]=c
                moves.append((copy,cost))
    if b.y == 1:
        x=homeMap[c]
        if grid[2][x] == '.' and (grid[3][x]=='.' or grid[3][x]=='3') and (grid[4][x]=='.' or grid[4][x]=='3') and (grid[5][x]=='.' or grid[5][x]=='3'):
            possible = True
            for ox in range(min(b.x, x)+1,max(b.x,x)):
                if grid[1][ox].isalpha():
                    possible = False              
            if possible:
                copy = [x[:] for x in grid]
                for i in range(5,1,-1):
                    if grid[i][x]=='.':
                        steps = abs(x-b.x)+i-1
                        copy[i][x]='3'
                        break
                cost = steps * costMap[c]
                copy[b.y][b.x]='.'
                moves.append((copy,cost))

    return moves

def makeOptions(grid):
    options = []
    for y,line in enumerate(grid):
        for x,c in enumerate(line):
            if c.isalpha():
                options+=getMoves(Coor(y,x),grid, c)
    return options

def play(grid, costs):
    global lowest
    if done(grid):
        print(costs)
        lowest = costs
    elif costs < lowest:
        options = makeOptions(grid)
        for o in options: 
            if costs + o[1] < lowest:
                play(o[0],costs+o[1])


play(input,0)

print(lowest)