from collections import Counter
import numpy
from coor import Coor
import math
line = list(map(int,filter(None,open('input.txt').read().replace('x=',',').replace('..',',').replace(' y=',',').split(','))))

def calc(dy,dx):
    y=0
    x=0
    hyghest=0
    found = False
    while y>-100:
        x+=dx
        y+=dy
        dy-=1
        if dx > 0:
            dx-=1
        hyghest = max(hyghest,y)
        if y in range(line[2],line[3]+1) and x in range(line[0],line[1]+1):
            found = True
            break

    return found, hyghest



options=[]
for dy in range(-1000,100):
    print(dy)
    for dx in range(-1000,1000):
        reached,highest = calc(dy,dx)
        if reached:
            options.append(highest)

print(len(options))




