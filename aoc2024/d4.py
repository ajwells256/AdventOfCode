
import logging
import os
from re import findall
from typing import List

from common.preader import read_array
from base import Solution

dirname, filename = os.path.split(__file__)
filename = filename.rstrip(".py")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(filename)


DAY = 4

class Day4(Solution):
    def __init__(self, sample = False):
        self.sample = sample

    def _count_xmas(self, lines: List[str]) -> int:
        count = sum([len(findall(r"(?=(XMAS|SAMX))", line)) for line in lines])
        logger.debug(f"Count: {count}")
        return count

    def part1(self) -> int:
        puzzle = read_array(DAY, sample=self.sample, rootdir=dirname)
        rows = ["".join(row) for row in puzzle.arr]
        cols = ["".join(row) for row in puzzle.T().arr]
        diags = ["".join(diag) for diag in puzzle.diagonals()]
        return self._count_xmas(rows) + self._count_xmas(cols) + self._count_xmas(diags)

    def part2(self) -> int:
        pass

if __name__ == "__main__":
    solution = Day4(sample=False)
    if solution.sample:
        assert solution.part1() == 18, solution.part1()
        assert solution.part2() == 31, solution.part2()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")