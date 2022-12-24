
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