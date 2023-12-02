from typing import Dict,List
from re import findall,match

from common.preader import read_lines

def part1(part=1) -> int:
    p = read_lines(2,part)
    run_sum = 0
    for line in p:
        game = int(match("Game (\d+):", line).group(1))
        legal = all([ \
                all([int(x) < 13 for x in findall("(\d+) red", line)]),  \
                all([int(x) < 14 for x in findall("(\d+) green", line)]),\
                all([int(x) < 15 for x in findall("(\d+) blue", line)])  \
            ])
        if legal:
            run_sum += game
    return run_sum    

def part2(part=1) -> int:
    p = read_lines(2,part)
    run_sum = 0
    for line in p:
        power = max([int(x) for x in findall("(\d+) red", line)])     \
                * max([int(x) for x in findall("(\d+) green", line)]) \
                * max([int(x) for x in findall("(\d+) blue", line)])
        run_sum += power
    return run_sum

if __name__ == "__main__":
    if "part2" not in globals():
        print(part1())
    else:
        print(part2())

