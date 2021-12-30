x = open("inputs/d13input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

points = [tuple([int(x) for x in point.split(",")]) for point in input if "," in point]
folds = [i for i in input if "fold along" in i]

def foldOverY(points, y):
    foldPoints = [point for point in points if point[1] > y]
    unfolded = [point for point in points if point[1] < y]
    foldedPoints = [(point[0], y-abs(y - point[1])) for point in foldPoints]
    return unfolded + foldedPoints

def foldOverX(points, x):
    foldPoints = [point for point in points if point[0] > x]
    unfolded = [point for point in points if point[0] < x]
    foldedPoints = [(x-abs(x - point[0]), point[1]) for point in foldPoints]
    return unfolded + foldedPoints

for fold in folds:
    _, foldLine = fold.split("=")
    if "y" in fold:
        points = foldOverY(points, int(foldLine))
    else:
        points = foldOverX(points, int(foldLine))

    if (fold == folds[0]):
        print(len(set(points)))

finalResult = set(points)
grid = [["." for x in range(1+max([a[0] for a in finalResult]))] for y in range(1+max(a[1] for a in finalResult))]

for point in finalResult:
    x,y = point
    grid[y][x] = "#"

for row in grid:
    print("".join(row))