

x = open("inputs/d11example.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

grid = [[int(y) for y in x] for x in input]

def simluate(grid):
    reprocess = set([])
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] += 1
            if (grid[x][y] > 9):
                reprocess.add((x, y))

    while (len(reprocess) > 0):
        x, y = reprocess.pop()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (x+i < 0 or y+j < 0 or x+i >= len(grid) or y+j >= len(grid[0])):
                    continue
                # each of these has already flashed, no reason to handle the 0,0 case with care
                grid[x+i][y+j] += 1
                # only specify for reprocessing if there's gonna be a new flash event
                # ie, wasn't previously ready to flash
                if (grid[x+i][y+j] == 10):
                    reprocess.add((x+i, y+j))

    flashes = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if (grid[x][y] > 9):
                grid[x][y] = 0
                flashes += 1
    return flashes

flashes = 0
for i in range(100):
    flashes += simluate(grid)
print(flashes)