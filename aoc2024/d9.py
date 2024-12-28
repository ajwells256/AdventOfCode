
import logging
import os
from typing import List
from itertools import chain

from common.preader import read_lines
from base import Solution

dirname, filename = os.path.split(__file__)
filename = filename.rstrip(".py")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(filename)

DAY = 9

class Disk:
    def __init__(self, str_repr: str):
        self.disk = []
        for i in range(0, len(str_repr), 2):
            file_id = i // 2
            file_len = int(str_repr[i])
            self.disk.append((file_id, file_len))
            if (i+1) < len(str_repr):
                empty_len = int(str_repr[i+1])
                self.disk.append((-1, empty_len))

    def _first_free_idx(self, min_size = 1) -> int:
        for i, (file_id, file_len) in enumerate(self.disk):
            if file_id == -1 and file_len >= min_size:
                return i
        return -1

    def _last_file_idx(self, start_at = -1) -> int:
        start_at = start_at if start_at != -1 else len(self.disk) - 1
        for i in range(start_at, -1, -1):
            if self.disk[i][0] != -1:
                return i
        return -1

    def _compact_step(self):
        logger.debug("compacting: %s", self)
        free_idx = self._first_free_idx()
        free_slot = self.disk[free_idx]
        last_file_idx = self._last_file_idx()
        last_file = self.disk.pop(last_file_idx)
        if free_slot[1] == last_file[1]:
            self.disk[free_idx] = last_file
            self.disk.append((-1, free_slot[1]))
        elif free_slot[1] < last_file[1]:
            self.disk[free_idx] = (last_file[0], free_slot[1])
            self.disk.insert(last_file_idx, (last_file[0], last_file[1] - free_slot[1]))
            self.disk.insert(last_file_idx + 1, (-1, free_slot[1]))
        else:
            self.disk[free_idx] = (last_file[0], last_file[1])
            self.disk.insert(free_idx + 1, (-1, free_slot[1] - last_file[1]))
            self.disk.append((-1, last_file[1]))

    def _defrag_step(self, start_at = -1):
        logger.debug("defragging: %s", self)
        start_at = start_at if start_at != -1 else len(self.disk) - 1
        last_file_idx = self._last_file_idx(start_at=start_at)
        first_sufficient_free_idx = self._first_free_idx(min_size=self.disk[last_file_idx][1])
        if first_sufficient_free_idx == -1 or first_sufficient_free_idx >= last_file_idx:
            return

        last_file = self.disk[last_file_idx]
        free_slot = self.disk[first_sufficient_free_idx]
        if free_slot[1] == last_file[1]:
            self.disk[first_sufficient_free_idx] = last_file
            self.disk[last_file_idx] = (-1, free_slot[1])
        else:
            self.disk[first_sufficient_free_idx] = (last_file[0], last_file[1])
            self.disk[last_file_idx] = (-1, last_file[1])
            self.disk.insert(first_sufficient_free_idx + 1, (-1, free_slot[1] - last_file[1]))

    def _merge_empties(self):
        merge_indices = []
        for i in range(len(self.disk) - 1):
            if self.disk[i][0] == -1 and self.disk[i+1][0] == -1:
                merge_indices.append(i)
        # reverse so that the accuracy of the indices is not affected by the removal of the previous ones
        merge_indices.reverse()
        for i in merge_indices:
            self.disk[i] = (-1, self.disk[i][1] + self.disk[i+1][1])
            self.disk.pop(i+1)

    def compact(self):
        while self._first_free_idx() < self._last_file_idx():
            self._compact_step()
            self._merge_empties()

    def defrag(self):
        i = len(self.disk) - 1
        while i > 0:
            i = self._last_file_idx(start_at=i)
            self._defrag_step(i)
            self._merge_empties()
            i -= 1

    def checksum(self) -> int:
        return sum(i * block for i, block in enumerate(self._get_block_affiliation()))

    def _get_block_affiliation(self) -> List[int]:
        return list(chain.from_iterable([[file_id] * file_len if file_id > 0 else [0] * file_len for (file_id, file_len) in self.disk]))

    def __str__(self) -> str:
        build_str = ""
        for (file_id, file_len) in self.disk:
            if file_id == -1:
                file_id = '.'
            file_id = str(file_id)
            build_str += f"|{file_id * file_len}"
        return build_str

class Day9(Solution):
    def __init__(self, sample = False, separate_part_2: bool = False):
        self.sample = sample
        self.part2_input_index = 2 if separate_part_2 else 1

    def part1(self) -> int:
        input_lines = read_lines(DAY, sample=self.sample, rootdir=dirname)
        disk = Disk(input_lines[0])
        disk.compact()

        return disk.checksum()

    def part2(self) -> int:
        input_lines = read_lines(DAY, sample=self.sample, rootdir=dirname)
        disk = Disk(input_lines[0])
        disk.defrag()

        return disk.checksum()

if __name__ == "__main__":
    solution = Day9()
    if solution.sample:
        if (part1 := solution.part1()) is not None:
            assert part1 == 1928, part1
        if (part2 := solution.part2()) is not None:
            assert part2 == 2858, part2
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")