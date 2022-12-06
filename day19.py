from collections import Counter
import numpy
from coor import Coor
import math

class Scanner:
    def __init__(self):
        self.beacons=[]



def makeScanner(str):
    sc = Scanner()
    l = str.split('\n')
    for i in range(1,len(l)):
        coors = l[i].split(',')
        sc.beacons.append(Coor(coors[1], coors[0], coors[2]))

    return sc

scanners = [makeScanner(x) for x in open('input.txt').read().split('\n\n')]
scanners[0].c = Coor(0,0,0)

first = scanners[0]
second = scanners[1]

for i in range 3:
    

print(scanners)