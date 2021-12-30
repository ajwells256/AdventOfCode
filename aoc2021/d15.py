
x = open("inputs/d15input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

class dijkstra:
    def __init__(self, grid):
        self.unvisited = { (0,0): 0 }
        self.visited = { }
        self.grid = grid
        self.x = len(grid)
        self.y = len(grid[0])

def accRisk(d: dijkstra, xy):
    risk = 0
    if (xy in d.unvisited.keys()):
        risk = d.unvisited[xy]
    elif (xy in d.visited.keys()):
        risk = d.visited[xy]
    return risk

def visitFrom(d: dijkstra, xy):
    x,y = xy
    xdim = []
    ydim = []
    if x > 0:
        xdim.append(-1)
    if x < d.x-1:
        xdim.append(1)
    if y > 0:
        ydim.append(-1)
    if y < d.y-1:
        ydim.append(1)

    points = [(x+i, y) for i in xdim] + [(x, y+j) for j in ydim]
    for point in points:
        px, py = point
        pointRiskFromXY = accRisk(d, xy) + int(d.grid[px][py])
        if (point in d.visited.keys()):
            d.visited[point] = min(d.visited[point], pointRiskFromXY)
        elif (point in d.unvisited.keys()):
            d.unvisited[point] = min(d.unvisited[point], pointRiskFromXY)
        else:
            d.unvisited[point] = pointRiskFromXY

def minRiskPath(d: dijkstra):
    target = (d.x-1, d.y-1)
    while (len(d.unvisited) > 0):
        shortest = min(d.unvisited.items(), key=lambda x: x[1])
        if (shortest[0] == target):
            print(shortest[1])
            break
        visitFrom(d, shortest[0])
        d.visited[shortest[0]] = d.unvisited.pop(shortest[0])

# part 1
minRiskPath(dijkstra(input))

def wrap(x, n):
    wrapped = int(x) + n
    if wrapped > 9:
        wrapped = (wrapped % 10) + 1
    return wrapped

def partTwo(input):
    newInput = [[int(c) for c in row] for row in input]
    for i in range(1,5):
        # expand downwards
        newInput += [list(map(lambda x: wrap(x, i), row)) for row in input]
    for k, row in enumerate(newInput):
        rowCopy = row.copy()
        for j in range(1,5):
            # expand rightwards
            newInput[k] += list(map(lambda x: wrap(x, j), rowCopy))

    minRiskPath(dijkstra(newInput))

partTwo(input)



    
    