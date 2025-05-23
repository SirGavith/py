import math
import matplotlib.pyplot as plt
import numpy as np
from itertools import combinations  

class Point:
    x: float
    y: float
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return str(self.x) + ',' + str(self.y)
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y
    def __hash__(self):
        seed = 0
        for x in [self.x, self.y]:
            x = ((x >> 16) ^ x) * 0x45d9f3b
            x = ((x >> 16) ^ x) * 0x45d9f3b
            x = (x >> 16) ^ x
            seed ^= x + 0x9e3779b9 + (seed << 6) + (seed >> 2)
        return seed

class Line:
    p1: Point
    p2: Point
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    def __repr__(self):
        return repr(self.p1) + ' - ' + repr(self.p2)

def iterateEdges(p: list[Point]):
    for i in range(len(p)-1):
        yield Line(p[i],p[i+1])
    yield Line(p[-1],p[0])

#vector difference p1-p2
def subtract(p1: Point, p2: Point):
    return Point(p1.x-p2.x, p1.y-p2.y)

#Compute the angle made by three points (the angle <p1p2p3)
def angle(p1: Point, p2: Point, p3: Point):
    v1=subtract(p1, p2)
    v2=subtract(p3, p2)
    return np.atan2(np.linalg.det([[v1.x, v1.y],[v2.x, v2.y]]),np.dot([v1.x, v1.y],[v2.x, v2.y]))

#distance between two points
def dist(p1: Point, p2: Point):
    return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)

#point of intersection of the lines p1p2 and p3p4
def intersect(l1: Line, l2: Line):
    [p1, p2] = [l1.p1, l1.p2]
    [p3, p4] = [l2.p1, l2.p2]
    if ((p1.x - p2.x)*(p4.y - p3.y) - (p2.y - p1.y)*(p3.x - p4.x)) == 0 or \
        (p1.x*p3.y - p1.x*p4.y - p1.y*p3.x + p1.y*p4.x - p2.x*p3.y + p2.x*p4.y + p2.y*p3.x - p2.y*p4.x) == 0:
        return Point(0,0)
    return Point(-((p1.x - p2.x)*(p3.y*p4.x - p3.x*p4.y) - (p3.x - p4.x)*(p1.y*p2.x - p1.x*p2.y))/((p1.x - p2.x)*(p4.y - p3.y) - (p2.y - p1.y)*(p3.x - p4.x)),
                   -(-p1.x*p2.y*p3.y + p1.x*p2.y*p4.y + p1.y*p2.x*p3.y - p1.y*p2.x*p4.y + p1.y*p3.x*p4.y - p1.y*p3.y*p4.x - p2.y*p3.x*p4.y + p2.y*p3.y*p4.x)/(p1.x*p3.y - p1.x*p4.y - p1.y*p3.x + p1.y*p4.x - p2.x*p3.y + p2.x*p4.y + p2.y*p3.x - p2.y*p4.x))

#does the line p1p2 intersect the line segment p3p4?
def lineintseg(l1: Line, l2: Line):
    [p1, p2] = [l1.p1, l1.p2]
    [p3, p4] = [l2.p1, l2.p2]
    if p1.x-p2.x==0 and p3.x-p4.x==0:
        if p1.x==p3.x:
            return True
        else: return False
    if p1.x-p2.x!=0 and p3.x-p4.x!=0 and (p1.y-p2.y)*(p3.x-p4.x)==(p3.y-p4.y)*(p1.x-p2.x):
        if (p1.y-p2.y)*(p1.x-p4.x)==(p1.y-p4.y)*(p1.x-p2.x):
            return True
        else: return False
    return (p3.x==p4.x and ybetween(p3,intersect(p1,p2,p3,p4),p4)) or (p3.x!=p4.x and xbetween(p3,intersect(p1,p2,p3,p4),p4))

#Plot a piecewice linear curve.  Input vertices in cyclic order
def plotline(p: list[Point]):
    for i in range(len(p)-1):
        plt.plot([p[i].x,p[i+1].x],[p[i].y,p[i+1].y], marker='o')

#plot a set of points
def plotpoints(p: list[Point]):
    for point in p:
        plt.plot([point.x,point.x],[point.y,point.y], marker='o')

#plot a polygon.  Input vertices in cyclic order
def plotpoly(p: list[Point]):
    for edge in iterateEdges(p):
        plt.plot([edge.p1.x,edge.p2.x],[edge.p1.y,edge.p2.y], marker='o')

#From a set of points, find one with smallest y-value
def smally(p: list[Point]):
    p1=p[0]
    for point in p:
        if point.y < p1.y: p1=point
    return p1


#is the x-coordinate of p2 between the x-coordinates of p1 and p3?
def xbetween(p1: Point, p2: Point, p3: Point):
    return p1.x<=p2.x<=p3.x or p3.x<=p2.x<=p1.x

#is the y-coordinate of p2 between the y-coordinates of p1 and p3?
def ybetween(p1: Point, p2: Point, p3: Point):
    return p1.y<=p2.y<=p3.y or p3.y<=p2.y<=p1.y

#Compute the slope of a line
def slope(l: Line):
  [p1,p2] = [l.p1, l.p2]
  if p2.x == p1.x:
    return math.inf
  return (p2.y-p1.y)/(p2.x-p1.x)

#A list of points called p
# p=[[0,0],[1,1],[2,4],[3,9]]


#1

#given three points on a line, returns whether p2 and p3 are on the same side of p1
def p1NotOnLineP2P3(p1: Point, p2: Point, p3: Point):
    #first case is for a vertical line
    return not (ybetween(p2,p1,p3) if (p1.x == p3.x) else xbetween(p2,p1,p3))

# print(p1NotOnLineP2P3([0,0],[1,1],[2,2]))
# print(p1NotOnLineP2P3([0,0],[2,2],[1,1]))
# print(p1NotOnLineP2P3([1,1],[2,2],[1,1]))

#2
def rayintseg(ray: Line, lineSeg: Line):
    [p1,p2] = [ray.p1, ray.p2]
    [p3,p4] = [lineSeg.p1, lineSeg.p2]

    inter = intersect(ray,lineSeg)
    if not xbetween(p3,inter,p4): return False

    if p1.x == p2.x: #vertical ray


        if p3.x-p4.x == 0:
            return p1.x == p3.x
        
        if p1.y >= p2.y: #ray is going down
            return inter.y <= p1.y
        return inter.y >= p1.y
    

    if p1.x <= p2.x: #ray is going right
        if (inter.x >= p1.x):
            return ybetween(p3,inter,p4)
        
    else: #ray left
        if (inter.x <= p1.x):
            return ybetween(p3,inter,p4)

# plotpoly(p)

#3
def segintseg(lineSeg1: Line, lineSeg2: Line):
    int = intersect(lineSeg1, lineSeg2)
    x1 = xbetween(lineSeg1.p1,int,lineSeg1.p2)
    x2 = xbetween(lineSeg2.p1,int,lineSeg2.p2)
    y1 = ybetween(lineSeg1.p1,int,lineSeg1.p2)
    y2 = ybetween(lineSeg2.p1,int,lineSeg2.p2)
    return x1 and x2 and y1 and y2

#4
def areParallel(l1: Line, l2: Line):
    return slope(l1) == slope(l2)

#5
def getNonParallelLine(p: list[Point]):
    p1 = Point(0,0)
    p2 = Point(0,10)

    def hasParallelSide(line,p):
        for edge in iterateEdges(p):
            if areParallel(edge, line):
                return True
        return False

    while True:
        if hasParallelSide(Line(p1,p2),p):
            p2.x += 10
            continue
        return Line(p1,p2)

#6
#ray p1-p2->  and polygon p
def countTangentVerticies(ray: Line, p: list[Point]):
    count = 0
    for i in range(len(p)):
        if pointIsOnLine(p[i], ray) and p[i].y > ray.p1.y:
            #ray goes thru vertex
            s1 = slope(Line(ray.p1), p[i-1])
            s2 = slope(ray)
            s3 = slope(Line(ray.p1), p[(i+1) % len(p)])

            if not (s1 > s2 > s3 or s1 < s2 < s3): count += 1

    return count

#7
def countCrossingVerticies(ray: Line, p: list[Point]):
    count = 0
    for i in range(len(p)):
        if pointIsOnLine(p[i], ray) and p[i].y > ray.p1.y:
            #ray goes thru vertex
            s1 = slope(Line(p[i], p[i-1]) if p[i].x <= p[i-1].x else Line(p[i-1], p[i]))
            s2 = slope(ray)
            n = p[(i+1) % len(p)]
            s3 = slope(Line(p[i], n) if p[i].x <= n.x else Line(n, p[i]))

            if (s1 > s2 > s3 or s1 < s2 < s3): count += 1
    return count

#8
def pointIsOnLine(p: Point, l: Line):
    return slope(l) == slope(Line(l.p1, p))
def pointIsOnLineSeg(p: Point, seg: Line):
    return xbetween(seg.p1, p, seg.p2) and ybetween(seg.p1, p, seg.p2) and \
        pointIsOnLine(p, seg)

def IsOnBoundaryOfPolygon(p1: Point, p: list[Point]):
    for edge in iterateEdges(p):
        if pointIsOnLineSeg(p1, edge): return True
    return False

#9
def IsInsidePolygon(p1: Point, p: list[Point]):
    if IsOnBoundaryOfPolygon(p1, p): return True

    ray = getNonParallelLine(p)
    ray = Line(p1, Point(p1.x+ray.p2.x, p1.y+ray.p2.y))

    crosses = countCrossingVerticies(ray, p)
    for edge in iterateEdges(p):
        if rayintseg(ray, edge):
            crosses += 1
            
    return crosses % 2 == 1


# #the polygon from problem 3d
# d = [Point(*p) for p in [[16,42],[46,141],[192,218],[231,89],[362,254],[417,15],[364,94],[110,45],[184,141]]]
# # plotpoly(d)

# inside = np.zeros((260, 430))

# for y in range(0, 430):
#     for x in range(0, 260):
#         inside[x,y] = IsInsidePolygon(Point(y,x), d)


# plt.imshow(inside, cmap='gray', interpolation='nearest')
# plt.show()

def segIntSegNotAtEnd(lineSeg1: Line, lineSeg2: Line):
    int = intersect(lineSeg1, lineSeg2)

    return segintseg(lineSeg1, lineSeg2) and not (lineSeg1.p1 == lineSeg2.p1 or lineSeg1.p1 == lineSeg2.p2 or lineSeg1.p2 == lineSeg2.p1 or lineSeg1.p2 == lineSeg2.p2 or \
        int == lineSeg1.p1 or int == lineSeg2.p1)

def IsInVertexKernel(p1: Point, P: list[Point]):
    if not IsInsidePolygon(p1, P): return False
    for vertex in P:
        line = Line(vertex, p1)
        crosses = 0
        for edge in iterateEdges(P):
            if segIntSegNotAtEnd(line, edge):
                crosses += 1 
        if crosses > 2: return False
    return True

# N = 300
# P = [Point(p[0] * N/10, N - p[1] * N/10) for p in [[0,0],[10,0],[10,10],[1,10],[8,8],[8,2],[5,6],[2,2],[0,9]]]
# plotpoly(P)

# IsInsidePolygon(Point(90,90), P)

# kernel = np.zeros((N, N))

# for y in range(0, N):
#     for x in range(0, N):
#         kernel[y,x] = IsInVertexKernel(Point(x, y), P)
#         # kernel[y,x] = IsInsidePolygon(Point(x,y), P)

# plt.imshow(kernel, cmap='gray', interpolation='nearest')

# S = [Point(*p) for p in [[0,0],[1,0],[1.5,1], [1,2]]]

def LineDoesntPartitionPoints(pointset: list[Point], line: Line):
    angles = [angle(line.p1, line.p2, p) for p in pointset]
    return  all(a >= 0 for a in angles) or all(a < 0 for a in angles)


# assert LineDoesntPartitionPoints(S, Line(Point(0,1), Point(1,1.5))) == False
# assert LineDoesntPartitionPoints(S, Line(Point(0,1), Point(1,3))) == True
# assert LineDoesntPartitionPoints(S, Line(Point(0,1), Point(-0.5,0))) == True
# plotpoints(S)



def FindTriContainingPoint(triangulation: list[tuple[Point]], p: Point):
    for tri in triangulation:
        if IsInsidePolygon(p, tri):
            return tri
    return False

p = Point(0.75, 0.75)

T = [ (Point(0,0),Point(0,1),Point(1,0)), (Point(1,1),Point(0,1),Point(1,0)), (Point(1,0),Point(1,1),Point(2,0)), (Point(2,1),Point(1,1),Point(2,0)), (Point(2,1),Point(3,2),Point(2,0))]


def FindFlippableEdges(triangulation: list[tuple[Point]]):
    flippableEdges = []

    for t1,t2 in combinations((set(t) for t in triangulation), 2):
        polygon = t1.union(t2)
        diag = t1.intersection(t2)
        flipped = polygon.difference(diag)

        if len(polygon) == 4 and not LineDoesntPartitionPoints(diag, Line(*flipped)):
            flippableEdges.append((*diag,))
    return flippableEdges

print(FindFlippableEdges(T))

[plotpoly(t) for t in T]

plt.show()