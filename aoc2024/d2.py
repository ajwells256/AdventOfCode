
import logging
import os

from base import Solution
from common.preader import read_lines

dirname, filename = os.path.split(__file__)
filename = filename.rstrip(".py")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(filename)

DAY = 2

class Day2(Solution):
    def __init__(self, sample = False):
        self.sample = sample
        self.part1_input_index = 1

    def _safe_report(self, report):
        return True if (
            all(report[i] - report[i-1] in [1, 2, 3] for i in range(1, len(report))) or
            all(report[i-1] - report[i] in [1, 2, 3] for i in range(1, len(report)))
        ) else False

    def _problem_dampner_safe_report(self, report):
        r = [r for r in report]
        if self._safe_report(report):
            return True
        for i in range(len(report)):
            r.pop(i)
            if self._safe_report(r):
                return True
            r = [r for r in report]
        return False

    def part1(self) -> int:
        list_input = read_lines(DAY, self.part1_input_index, sample=self.sample, rootdir=dirname)
        reports = [list(map(int, line.split())) for line in list_input]

        return sum(1 for report in reports if self._safe_report(report))

    def part2(self) -> int:
        list_input = read_lines(DAY, self.part1_input_index, sample=self.sample, rootdir=dirname)
        reports = [list(map(int, line.split())) for line in list_input]

        return sum(1 for report in reports if self._problem_dampner_safe_report(report))

if __name__ == "__main__":
    solution = Day2()
    if solution.sample:
        assert solution.part1() == 2, solution.part1()
        assert solution.part2() == 4, solution.part2()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")