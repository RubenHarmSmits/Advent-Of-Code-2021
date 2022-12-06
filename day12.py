import math

connections = [x.split('-') for x in open('input.txt').read().strip().split('\n')]

tot = 0

class Point:
    def __init__(self, isLarge, name):
        self.isLarge=isLarge
        self.name=name
        self.connecties = []

    def find(self, nameToFind, path, first):
        path.append(self.name)
        if nameToFind == self.name:
            global tot
            tot+=1
        else :
            for c in self.connecties:
                if not c.isLarge:
                    count = path.count(c.name)
                    if c.name != 'start':
                        if count == 1 and not first:    
                            c.find(nameToFind, path[:],True)
                        if count == 0:
                            c.find(nameToFind, path[:],first)
                else:
                    c.find(nameToFind, path[:],first)


    

points = []

def findP(name):
    return next(x for x in points if x.name == name)

def addPoint(name):
    if name not in [p.name for p in points]:
        isCapital = name == name.upper()
        points.append(Point(isCapital,name))


for con in connections:
    addPoint(con[0])
    addPoint(con[1]) 

for con in connections:
    first  = next(x for x in points if x.name == con[0])
    
    sec  = next(x for x in points if x.name == con[1])
    first.connecties.append(sec)
    sec.connecties.append(first)

    addPoint(con[1]) 


findP('start').find('end', [], False)

print(tot)

