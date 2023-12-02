from functools import reduce
import numpy as np

class Array2d:
    def __init__(self, array):
        self.array = array
        self.height = len(array)
        self.width = len(array[0])

    def defined(self, pos):
        return pos[0] < self.width and pos[0] >= 0 and \
                pos[1] < self.height and pos[1] >= 0

    def pad(self, empty):
        self.width = reduce(lambda acc, i: len(i) if len(i) > acc else acc, self.array, 0)

        for i in range(len(self.array)):
            line = self.array[i]
            if len(line) != self.width:
               self.array[i] = line + empty*(self.width-len(line))


    def toSparseArray(self, empty):
        sparse = SparseArray(empty)
        for y in range(self.height):
            for x in range(self.width):
                if self.array[y][x] != empty:
                    sparse.sparseArray[(x,y)] = self.array[y][x]
        return sparse

class CubeMap:
    def __init__(self, bottomMap, leftMap, upMap, rightMap, downMap, topMap):
        self.allMaps = { \
                "bottom": bottomMap, 
                "left": leftMap, \
                "up": upMap, \
                "right": rightMap, \
                "down": downMap, \
                "top": topMap }
        self.currentMap = None

        for map in self.allMaps.values():
                map.wrap = False

    def addFloor(self, floorTile):
        for map in self.allMaps.values():
            map.floors.add(floorTile)

    def addObstacle(self, obstacleTile):
        for map in self.allMaps.values():
            map.obstacles.add(obstacleTile)

    def walk(self, paces):
        m = self.currentMap


class Map(Array2d):
    def __init__(self, array, wrap=True):
        Array2d.__init__(self, array)
        self.obstacles = set()
        self.floors = set()
        self.cursor = [0,0] # x, y
        self.velocity = np.array([1,0])
        self.wrap = wrap

    # +1 for 90 degrees clockwise, -1 for 90 ccw
    def turn(self, direction):
        rotationMatrix = np.array([[0, -1*direction], \
                [direction, 0]])
        self.velocity = rotationMatrix.dot(self.velocity)

    def tile(self, cursor):
        return self.array[cursor[1]][cursor[0]]

    def walk(self, paces):
        for i in range(paces):
            if not self.tryPace():
                break

    def tryPace(self):
        if len(self.floors) == 0:
            raise Exception("make sure to initialize the floor tiles")
        testCur = self.peekStep(self.cursor)
        if not self.defined(testCur):
            return False
        while self.tile(testCur) not in self.floors \
                and self.tile(testCur) not in self.obstacles:
            testCur = self.peekStep(testCur)
        if self.tile(testCur) in self.floors:
            self.cursor = testCur
            return True
        else:
            return False

    def peekStep(self, fromCursor):
        testCur = fromCursor + self.velocity
        if (self.wrap):
            testCur[0] = testCur[0] % self.width
            testCur[1] = testCur[1] % self.height
        return testCur
        
    def __str__(self):
        copy = [[x for x in y] for y in self.array]
        copy[self.cursor[1]][self.cursor[0]] = '$'

        line = "\n".join(["".join(line) for line in copy])
        return line

class SparseArray:
    def __init__(self, emptyChar):
        self.emptyChar = emptyChar
        self.sparseArray = {}

    def getBoundingBox(self):
        minX = reduce(lambda acc,i: i[0] if i[0] < acc else acc, self.sparseArray.keys(), list(self.sparseArray.keys())[0][0])
        maxX = reduce(lambda acc,i: i[0] if i[0] > acc else acc, self.sparseArray.keys(), list(self.sparseArray.keys())[0][0])
        minY = reduce(lambda acc,i: i[1] if i[1] < acc else acc, self.sparseArray.keys(), list(self.sparseArray.keys())[0][1])
        maxY = reduce(lambda acc,i: i[1] if i[1] > acc else acc, self.sparseArray.keys(), list(self.sparseArray.keys())[0][1])
        return ((minX, minY), (maxX, maxY))

    def getNeighbors(self, pos):
        neighbors = [[False, False, False], \
                [False, False, False], \
                [False, False, False]] 
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (pos[0]+x, pos[1]+y) in self.sparseArray.keys():
                    neighbors[y+1][x+1] = True
        return neighbors

    def __str__(self):
        upperLeft, lowerRight = self.getBoundingBox()
        line = ""
        for y in range(upperLeft[1], lowerRight[1]+1):
            for x in range(upperLeft[0], lowerRight[0]+1):
                if (x,y) in self.sparseArray.keys():
                    line += self.sparseArray[(x,y)]
                else:
                    line += self.emptyChar
            line += '\n'
        return line

def forEachPositiveCardinalNeighbor(graph, x, y, func):
    neighbors = [[x+1, y], [x, y+1]]
    for neighbor in neighbors:
        x, y = neighbor
        if coordIsSafe(graph, x, y):
            func(x, y)

def forEachCardinalNeighbor(graph, x, y, func):
    neighbors = [[x+1, y], [x-1,y], [x, y+1], [x, y-1]]
    for neighbor in neighbors:
        x, y = neighbor
        if coordIsSafe(graph, x, y):
            func(x, y)

def forEachOrdinalNeighbor(graph, x, y, func):
    neighbors = [[x+1, y+1], [x-1,y+1], [x-1, y+1], [x+1, y-1]]
    for neighbor in neighbors:
        x, y = neighbor
        if coordIsSafe(graph, x, y):
            func(x, y)

def coordIsSafe(graph, x, y):
    return len(graph) > y and y > 0 \
        and len(graph[0]) > x and x > 0
