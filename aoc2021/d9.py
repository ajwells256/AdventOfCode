
from math import prod

a = open("inputs/d9input.txt")
b = a.readlines()
input = [z.rstrip("\n") for z in b]
lists = [[(x, y) for y in range(len(inp))] for x, inp in enumerate(input)]
minMemo = {}

def depthOf(xy):
	x, y = xy
	# if (lists[x][y] != xy):
		# return lookup(lists[x][y])
	return int(input[x][y])

def lookupMinPoint(xy):
	x, y = xy
	if (xy not in minMemo.keys()):
		if (lists[x][y] != xy):
			minMemo[xy] = lookupMinPoint(lists[x][y])
		else:
			minMemo[xy] = xy
	return minMemo[xy]
		
basins = {}
for i in range(len(input)):
	for j in range(len(input[0])):
		possibilities = [(i, j)]
		if (i > 0):
			possibilities.append((i-1, j))
		if (j > 0):
			possibilities.append((i, j-1))
		if (i < len(input)-1):
			possibilities.append((i+1, j))
		if (j < len(input[0])-1):
			possibilities.append((i, j+1))
		mini = min(possibilities, key=depthOf)
		maxi = max(possibilities, key=depthOf)
		if (depthOf(mini) == depthOf(maxi)):
			mini = possibilities[-1]
		lists[i][j] = mini
		basins[(i, j)] = [mini]

risksOfMins = [[1+int(input[x][y]) if lists[x][y] == (x, int(y)) else 0 for y in range(len(input[0]))] for x in range(len(input))]
print(sum(map(sum, risksOfMins)))

basinPointers = [lookupMinPoint((x,y)) if depthOf((x,y)) != 9 else (-1,-1) for x in range(len(input)) for y in range(len(input[0]))]
basinPoints = set(basinPointers)
basinPoints.remove((-1,-1))
basinLengths = [basinPointers.count(bp) for bp in basinPoints]
basinLengths.sort(reverse=True)

print(prod(basinLengths[:3]))
