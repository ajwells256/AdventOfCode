
import logging
import os

from common.preader import read_lines
from base import Solution

dirname, filename = os.path.split(__file__)
filename = filename.rstrip(".py")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(filename)

DAY = 0

class DayN(Solution):
    def __init__(self, sample = False, separate_part_2: bool = False):
        self.sample = sample
        self.part2_input_index = 2 if separate_part_2 else 1

    def part1(self) -> int:
        pass

    def part2(self) -> int:
        pass

if __name__ == "__main__":
    solution = DayN(True)
    if solution.sample:
        if (part1 := solution.part1()) is not None:
            assert part1 == 1928, part1
        if (part2 := solution.part2()) is not None:
            assert part2 == 31, part2
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")