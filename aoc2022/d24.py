import reader
import sys

class basin:
    def __init__(self, lines):
        self.rpb = {}
        self.rnb = {}
        self.cpb = {}
        self.cnb = {}
        self.height = len(lines)-2
        self.width = len(lines[0])-2
        for y in range(1, len(lines)):
            for x in range(1, len(lines[y])):
                #offset so that the wall is ignored
                xEf = x-1
                yEf = y-1
                if lines[y][x] == "^":
                    if (xEf in self.cnb.keys()):
                        self.cnb[xEf].append(yEf) 
                    else:
                        self.cnb[xEf] = [yEf]
                elif (lines[y][x] == "v"):
                    if (xEf in self.cpb.keys()):
                        self.cpb[xEf].append(yEf)
                    else:
                        self.cpb[xEf] = [yEf]
                elif (lines[y][x] == "<"):
                    if (yEf in self.rnb.keys()):
                        self.rnb[yEf].append(xEf)
                    else:
                        self.rnb[yEf] = [xEf]
                elif (lines[y][x] == ">"):
                    if yEf in self.rpb.keys():
                        self.rpb[yEf].append(xEf)
                    else:
                        self.rpb[yEf] = [xEf]

    def blizzardPresent(self, x, y, time):
        impact = False
        if (y in self.rpb.keys()):
            impact |= sum(map(lambda bx: ((bx + time) % self.width) == x, self.rpb[y])) 
        if not impact and y in self.rnb.keys():
            impact |= sum(map(lambda bx: ((bx - time) % self.width) == x, self.rnb[y])) 
        if not impact and x in self.cpb.keys():
            impact |= sum(map(lambda by: ((by + time) % self.height) == y, self.cpb[x])) 
        if not impact and x in self.cnb.keys():
            impact |= sum(map(lambda by: ((by - time) % self.height) == y, self.cnb[x])) 
        return impact

    def print(self, ts):
        for y in range(self.height):
            for x in range(self.width):
                if self.blizzardPresent(x, y, ts):
                    print("X", end='')
                else:
                    print(".", end='')
            print("")

    def __str__(self):
        self.print(0)


def part1():
    lines = reader.readlines(24, 1)
    b = basin(lines)
    return(len(findPath(b, (0, -1), (b.width-1, b.height))))

def findPath(b, start, target, startTs=0):
    queue = [(start, [], startTs)]
    memo = set()
    memoMod = b.width * b.height
    oldTs = 0
    while len(queue)>0:
        pos, path, ts = queue.pop(0)
        validMoves = getValidMoves(b, pos[0], pos[1], target)
        for x,y in validMoves: 
            if (x, y, (ts+1)%memoMod) not in memo and not b.blizzardPresent(x, y, ts+1):
                newPath = [a for a in path] + [(x,y)]
                if x == target[0] and y == target[1]:
                    return newPath
                queue.append([(x, y), newPath, ts+1])
                memo.add((x, y, (ts+1) % memoMod))
    print("Couldn't find path")
    return []
                
                

def getValidMoves(b, x, y, target):
    moves = []
    if x < b.width-1 and y >= 0 and y < b.height:
        moves.append((x+1, y))
    if y < b.height-1 or x == target[0]:
        moves.append((x, y+1))
    if x > 0 and y >= 0 and y < b.height:
        moves.append((x-1, y))
    if y > 0 or x == target[0]:
        moves.append((x, y-1))
    moves.append((x, y))
    return moves
    

def part2():
    lines = reader.readlines(24, 1)
    b = basin(lines)
    totalMoves = len(findPath(b, (0, -1), (b.width-1, b.height)))
    totalMoves += len(findPath(b, (b.width-1, b.height), (0, -1), totalMoves))
    totalMoves += len(findPath(b, (0,-1), (b.width-1, b.height), totalMoves))
    return totalMoves

print(part2())
