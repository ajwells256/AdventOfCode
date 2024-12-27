
import logging
import os

from typing import Tuple, Iterable
from collections import Counter

from base import Solution
from common.preader import read_lines

dirname, filename = os.path.split(__file__)
filename = filename.rstrip(".py")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(filename)

DAY = 1

class Day1(Solution):
    def __init__(self, separate_part_2: bool = False, sample=False):
        self.sample = sample
        self.part1_input_index = 1
        self.part2_input_index = 2 if separate_part_2 else 1

    def _get_lists(self) -> Tuple[Iterable[int], Iterable[int]]:
        list_input = read_lines(DAY, self.part1_input_index, sample=self.sample, rootdir=dirname)
        list1, list2 = zip(*[line.split() for line in list_input])
        list1 = map(int, list1)
        list2 = map(int, list2)
        return list1, list2

    def part1(self) -> int:
        list1, list2 = self._get_lists()
        ordered_list1 = sorted(list1)
        ordered_list2 = sorted(list2)
        diff_list = [abs(ordered_list1[i] - ordered_list2[i]) for i in range(len(ordered_list1))]
        return sum(diff_list)

    def part2(self) -> int:
        list1, list2 = self._get_lists()
        counter = Counter(list2)

        sim_scores = [item * counter.get(item, 0) for item in list1]
        return sum(sim_scores)

if __name__ == "__main__":
    solution = Day1()
    if solution.sample:
        assert solution.part1() == 11
        assert solution.part2() == 31
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")