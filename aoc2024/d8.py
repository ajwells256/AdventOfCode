
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

DAY = 8

class Disk:
    def __init__(self, str_repr: str):
        self.disk = []
        self.free_nodes = []
        for i in range(0, len(str_repr), 2):
            file_id = i // 2
            file_len = int(str_repr[i])
            empty_len = int(str_repr[i+1])
            self.disk.append((file_id, file_len))
            self.disk.append((-1, empty_len))
            self.free_nodes.append(i+1)

    def _defrag_step(self):
        free_idx = self.free_nodes.pop(0)
        free_slot = self.disk[free_idx]
        last_file = self.disk.pop()
        if free_slot[1] == last_file[1]:
            self.disk[free_idx] = last_file
        elif free_slot[1] < last_file[1]:
            self.disk.append((last_file[0], last_file[1] - free_slot[1]))
            self.disk[free_idx] = (last_file[0], free_slot[1])
        else:
            self.disk[free_idx] = (last_file[0], last_file[1])
            self.disk.insert(free_idx + 1, (-1, free_slot[1] - last_file[1]))
            self.free_nodes.insert(0, free_idx)

    def _merge_empties(self):
        new_free_nodes = []
        for i in range(len(self.free_nodes)-1):
            new_free_nodes.append(self.free_nodes[i])
            if self.free_nodes[i] + 1 == self.free_nodes[i+1]:
                self.disk[self.free_nodes[i]] = (-1, self.disk[self.free_nodes[i]][1] + self.disk[self.free_nodes[i+1]][1])
                self.disk.pop(self.free_nodes[i+1])
            else:
                new_free_nodes.append(self.free_nodes[i+1])
        self.free_nodes = new_free_nodes

    def defrag(self):
        while len(self.free_nodes) > 0:
            self._defrag_step()
            self._merge_empties()


class Day8(Solution):
    def __init__(self, sample = False, separate_part_2: bool = False):
        self.sample = sample
        self.part2_input_index = 2 if separate_part_2 else 1

    def part1(self) -> int:
        pass

    def part2(self) -> int:
        pass

if __name__ == "__main__":
    solution = Day8()
    if solution.sample:
        if (part1 := solution.part1()) is not None:
            assert part1 == 1928, part1
        if (part2 := solution.part2()) is not None:
            assert part2 == 31, part2
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")