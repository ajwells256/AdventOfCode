
import logging
import os

from re import finditer

from common.preader import read_lines
from base import Solution

dirname, filename = os.path.split(__file__)
filename = filename.rstrip(".py")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(filename)

DAY = 3

class Day3(Solution):
    def __init__(self, sample = False):
        self.sample = sample
        self.part2_input_index = 1

    def _calculate_instructions(self, input_lines: str) -> int:
        instructions = finditer(r"mul\((\d{1,3}),(\d{1,3})\)", input_lines)
        return sum(int(instruction.group(1)) * int(instruction.group(2)) for instruction in instructions)

    def part1(self) -> int:
        corrupt_memory = "".join(read_lines(DAY, sample=self.sample, rootdir=dirname))
        return self._calculate_instructions(corrupt_memory)

    def part2(self) -> int:
        corrupt_memory = "".join(read_lines(DAY, part=self.part2_input_index, sample=self.sample, rootdir=dirname))
        valid_instruction_strings = finditer(r"(^|do\(\)).*?(don't\(\)|$)", corrupt_memory)
        valid_instruction_input = "".join([instruction.group() for instruction in valid_instruction_strings])
        return self._calculate_instructions(valid_instruction_input)

if __name__ == "__main__":
    solution = Day3(sample=False)
    if solution.sample:
        solution.part2_input_index = 2
        assert solution.part1() == 161
        assert solution.part2() == 48, solution.part2()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")