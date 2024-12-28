
import logging
import os
from typing import List, Callable
from re import match

from common.preader import read_lines
from base import Solution

dirname, filename = os.path.split(__file__)
filename = filename.rstrip(".py")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(filename)

DAY = 7

class Equation:
    def __init__(self, value: int, inputs: List[int]):
        self.value = value
        self.inputs = inputs

    def can_be_true_using(self, operators: List[Callable[[int, int], int]]) -> bool:
        if len(self.inputs) == 1:
            return self.value == self.inputs[0]
        for op in operators:
            new_inputs = [i for i in self.inputs]
            new_input = op(new_inputs.pop(0), new_inputs.pop(0))
            new_inputs.insert(0, new_input)
            new_eq = Equation(self.value, new_inputs)
            if new_eq.can_be_true_using(operators):
                return True
        return False

class Day7(Solution):
    def __init__(self, sample = False, separate_part_2: bool = False):
        self.sample = sample
        self.part2_input_index = 2 if separate_part_2 else 1

    def part1(self) -> int:
        equations_lines = read_lines(DAY, sample=self.sample, rootdir=dirname)
        equations: List[Equation] = []
        for line in equations_lines:
            m = match(r"(\d+): ([0-9 ]+)", line)
            if m:
                equations.append(Equation(int(m.group(1)), list(map(int, m.group(2).split()))))
        return sum(eq.value for eq in equations if eq.can_be_true_using([lambda x, y: x + y, lambda x, y: x * y]))

    def part2(self) -> int:
        equations_lines = read_lines(DAY, sample=self.sample, rootdir=dirname)
        equations: List[Equation] = []
        for line in equations_lines:
            m = match(r"(\d+): ([0-9 ]+)", line)
            if m:
                equations.append(Equation(int(m.group(1)), list(map(int, m.group(2).split()))))
        return sum(eq.value for eq in equations if eq.can_be_true_using([lambda x, y: x + y, lambda x, y: x * y, lambda x, y: int(str(x) + str(y))]))

if __name__ == "__main__":
    solution = Day7(True)
    if solution.sample:
        if (part1 := solution.part1()) is not None:
            assert part1 == 3749, part1
        if (part2 := solution.part2()) is not None:
            assert part2 == 11387, part2
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")