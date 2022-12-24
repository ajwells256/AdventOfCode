import reader
import array2d
from graph import node,bfs

class mapNode(node):
    def __init__(self, x, y, elevation):
        node.__init__(self)
        self.pos = (x, y)
        self.elevation = elevation
        if (self.elevation == "S"):
            self.elevation = "a"
        elif(self.elevation == "E"):
            self.elevation = "z"
    def __str__(self):
        return self.pos

def part1():
    map = reader.readlines(12, 1)
    startNode = None
    endNode = None
    graph = {}
    for y in range(len(map)):
        for x in range(len(map[0])):
            graph[(x,y)] = mapNode(x, y, map[y][x])
            if (map[y][x] == "S"):
                startNode = graph[(x,y)]
            elif (map[y][x] == "E"):
                endNode = graph[(x,y)]

    for y in range(len(map)):
        for x in range(len(map[0])):
            try:
                array2d.forEachPositiveCardinalNeighbor(map, x, y, lambda a, b: conditionallyAddNeighbor(graph[(x,y)], graph[(a,b)]))
            except:
                print(graph)
                raise
    print(bfs(startNode, endNode))

def conditionallyAddNeighbor(node, neighbor):
    if ord(node.elevation) - ord(neighbor.elevation) <= 1 and ord(node.elevation) - ord(neighbor.elevation) >= -1:
        node.neighbors.append(neighbor)
        neighbor.neighbors.append(node)

part1()