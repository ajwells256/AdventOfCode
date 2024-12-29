
import logging
import os

from typing import List, Union, Dict

from common.preader import read_lines
from base import Solution

dirname, filename = os.path.split(__file__)
filename = filename.rstrip(".py")
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(filename)

DAY = 11

class ExpansionTreeNode:
    def __init__(self, value: int):
        self.value = value
        self.children: List[Union["ExpansionTreeNode", "Placeholder"]] = []
        self.cached_count: Dict[int, int] = {}

    def add_children(self, children: List[Union["ExpansionTreeNode", "Placeholder"]]):
        self.children.extend(children)

    def count(self, at_depth) -> int:
        if at_depth not in self.cached_count:
            if at_depth == 0:
                self.cached_count[at_depth] = 1
            else:
                self.cached_count[at_depth] = sum(map(lambda x: x.count(at_depth-1), self.children))
        return self.cached_count[at_depth]

    def __repr__(self):
        return f"{self.value} -> {self.children}"

    def __str__(self):
        return f"{self.value} -> {self.children}"

class Placeholder:
    def __init__(self, node: ExpansionTreeNode, blink_offset: int):
        self.node = node
        self.blink_offset = blink_offset

    def count(self, at_depth) -> int:
        return self.node.count(at_depth)

class StoneLine:
    def __init__(self, stones: List[int]):
        self.expansion_tree_nodes = {stone: ExpansionTreeNode(stone) for stone in stones}
        self.initial_nodes = [self.expansion_tree_nodes[stone] for stone in stones]

    def _expand_dyno(self, node: Union[ExpansionTreeNode, Placeholder], blink_offset: int) -> List[Union[ExpansionTreeNode, Placeholder]]:
        expansion: List[Union[ExpansionTreeNode, Placeholder]] = []
        if isinstance(node, Placeholder):
            expansion.append(node)
        else:
            new_values = []
            if node.value == 0:
                new_values.append(1)
            elif len(str(node.value)) % 2 == 0:
                stone_str = str(node.value)
                new_values.append(int(stone_str[:len(stone_str) // 2]))
                new_values.append(int(stone_str[len(stone_str) // 2:]))
            else:
                new_values.append(node.value * 2024)

            for value in new_values:
                if value in self.expansion_tree_nodes:
                    expansion.append(Placeholder(self.expansion_tree_nodes[value], blink_offset))
                else:
                    new_node = ExpansionTreeNode(value)
                    self.expansion_tree_nodes[value] = new_node
                    expansion.append(new_node)
            node.add_children(expansion)
        return expansion

    def blink_dyno(self, times=1):
        nodes = [node for node in self.initial_nodes]
        for time in range(times):
            new_nodes = []
            for node in nodes:
                new_nodes.extend(self._expand_dyno(node, time))
            nodes = new_nodes

    def count_stones(self, at_depth: int) -> int:
        return sum(node.count(at_depth) for node in self.initial_nodes)


class Day11(Solution):
    def __init__(self, sample = False, separate_part_2: bool = False):
        self.sample = sample
        self.part2_input_index = 2 if separate_part_2 else 1

    def part1(self) -> int:
        puzzle = read_lines(DAY, sample=self.sample, rootdir=dirname)
        stones = list(map(int, puzzle[0].split()))
        stone_line = StoneLine(stones)
        stone_line.blink_dyno(25)
        return stone_line.count_stones(25)

    def part2(self) -> int:
        puzzle = read_lines(DAY, sample=self.sample, rootdir=dirname)
        stones = list(map(int, puzzle[0].split()))
        stone_line = StoneLine(stones)
        stone_line.blink_dyno(75)
        return stone_line.count_stones(75)

if __name__ == "__main__":
    solution = Day11(False)
    if solution.sample:
        if (part1 := solution.part1()) is not None:
            assert part1 == 55312, part1
        if (part2 := solution.part2()) is not None:
            assert part2 == 65601038650482, part2
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")