from reader import readlines
from array2d import Map
from logger import logger
import re

log = logger()


def part1(part = 1):
    grid, instructions = readlines(22, part)
    instructions = instructions[0]
    m = Map(grid)
    m.pad(' ')

    m.floors.add('.')
    m.obstacles.add('#')

    m.tryPace() # get onto the upper leftmost tile, starting from 0,0 facing right
    while len(instructions) > 0:
        match = re.search("\d+|\w", instructions)
        if match[0].isdecimal():
            log.debug("Walk", match[0])
            m.walk(int(match[0]))
        elif match[0] == "R":
            log.debug("Turn right")
            m.turn(1)
        elif match[0] == "L":
            log.debug("Turn left")
            m.turn(-1)
        else:
            raise Exception(f"Unexpected instruction: {match[0]}")

        instructions = instructions[match.span()[1]:]

    log.debug(m)

    directionBackingValue = 0
    if m.velocity[1] == 1:
        directionBackingValue = 1
    elif m.velocity[0] == -1:
        directionBackingValue = 2
    elif m.velocity[1] == -1:
        directionBackingValue = 3

    log.debug(m.velocity, m.cursor, directionBackingValue)
    return (1+m.cursor[1])*1000 + (1+m.cursor[0])*4 + directionBackingValue

print(part1())

log.setLevel("debug")
