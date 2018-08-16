from random import *

class point():
    x = 0
    y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def check (p, listPoint):
    for x in listPoint:
        if(x.x == p.x and x.y == p.y):
            return False
    return True


# Sinh diem ngau nhien khong trung
def genaratoRandomPoint():
    pointList = []
    while (len(pointList) < 1000):
        x = (randrange(0, 1000))
        y = (randrange(0, 1000))
        p = (x, y)
        if(check(p, pointList)):
            pointList.append(p)
            return pointList

#Main
pointList = genaratoRandomPoint()
print (pointList)
