class Coor:
    def __init__(self, y, x):
        self.y=int(y)
        self.x=int(x)

    def eq(self, c):
        return c.y == self.y and c.x == self.x and c.z == self.z

    def __repr__(self):
        return ('y:'+str(self.y)+",x:"+str(self.x))
    
