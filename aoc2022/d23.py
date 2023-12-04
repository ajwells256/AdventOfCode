from array2d import Array2d, SparseArray
from reader import readlines
from functools import reduce
import numpy as np
from logger import logger

log = logger()

class MovementRule:
    def __init__(self, predicate, rule):
        self.predicate = predicate
        self.rule = rule


movementRules = [MovementRule(lambda x: not (True in x[0]), lambda pos: (pos[0], pos[1]-1)), \
        MovementRule(lambda x: not (True in x[2]), lambda pos: (pos[0], pos[1]+1)), \
        MovementRule(lambda x: not (True in x[:,0]), lambda pos: (pos[0]-1, pos[1])), \
        MovementRule(lambda x: not (True in x[:,2]), lambda pos: (pos[0]+1, pos[1]))]

def part1():
    field = readlines(23, 1)
    array = Array2d(field)
    sparr = array.toSparseArray('.')
    for i in range(10):
        performTimeStep(sparr, i)
    upperleft, lowerright = sparr.getBoundingBox()
    area = (1+ lowerright[0]-upperleft[0])*(1+ lowerright[1]-upperleft[1])
    log.debug(upperleft, lowerright, area)
    return area - len(sparr.sparseArray)
        

def part2():
    sparr = Array2d(readlines(23, 1)).toSparseArray('.')
    i = 0
    while(not performTimeStep(sparr, i)):
        i+=1
    return i+1 

def performTimeStep(sparr, ts):
    movements = []
    for pos in sparr.sparseArray.keys():
        movement = proposeMovement(sparr, pos, ts)
        if movement is not None:
            movements.append((pos, movement))
    disallowedMovements = set()
    allowedMovements = {}
    for movement in movements:
        if movement[1] in allowedMovements.keys():
            allowedMovements.pop(movement[1])
            disallowedMovements.add(movement[1])
        elif movement[1] not in disallowedMovements:
            allowedMovements[movement[1]] = movement[0]
    for dest, src in allowedMovements.items():
        val = sparr.sparseArray.pop(src)
        sparr.sparseArray[dest] = val
    log.debug(ts, sparr)
    return len(allowedMovements) == 0
    
    
def proposeMovement(sparr, pos, ts):
    ns = np.array(sparr.getNeighbors(pos))
    ns[1,1] = False # for our purposes, ignore the point itself
    if (not reduce(lambda acc, i: acc or True in i, ns, False)):
        # There are no neighbors
        return None
    for i in range(len(movementRules)):
        rule = movementRules[(i+ts)%len(movementRules)]
        if rule.predicate(ns):
            return rule.rule(pos)
    return None


print(part1())
print(part2())
log.setLevel("debug")

