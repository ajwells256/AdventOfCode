
import logging
import os
from uuid import uuid4

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

DAY = 12

class GardenNode:
    def __init__(self, node_type: str):
        self.neighbors: List[GardenNode] = []
        self.node_type = node_type
        self._root = self
        self.id = uuid4()

    def get_permimeter(self):
        return 4 - sum(1 for neighbor in self.neighbors if neighbor.node_type == self.node_type)

    @property
    def root(self):
        node = self
        while node._root != node:
            node = node._root
        return node

    @root.setter
    def root(self, node):
        self._root = node

    @property
    def is_root(self):
        return self.root == self

    def __repr__(self):
        return f"{self.node_type} ({self.id})"

    def __str__(self):
        return f"{self.node_type} ({self.id})"

class Day12(Solution):
    def __init__(self, sample = False, separate_part_2: bool = False):
        self.sample = sample
        self.part2_input_index = 2 if separate_part_2 else 1

    def _union_merge(self, garden_nodes: List[GardenNode]) -> None:
        for node in garden_nodes:
            for neighbor in node.neighbors:
                if neighbor.node_type == node.node_type:
                    if neighbor.root != node.root and neighbor.is_root and node.is_root:
                        neighbor.root = node
                    elif neighbor.root != node.root and neighbor.is_root:
                        neighbor.root = node.root
                    elif neighbor.root != node.root and node.is_root:
                        node.root = neighbor.root
                    else:
                        neighbor.root.root = node.root


    def part1(self) -> int:
        garden_arr = read_array(DAY, sample=self.sample, rootdir=dirname).arr
        garden_nodes = []
        garden_node_arr = [[None for _ in range(len(garden_arr[y]))] for y in range(len(garden_arr))]
        for y in range(len(garden_arr)):
            for x in range(len(garden_arr[y])):
                garden_node = GardenNode(garden_arr[y][x])
                garden_nodes.append(garden_node)
                garden_node_arr[y][x] = garden_node

        for y in range(len(garden_node_arr)):
            for x in range(len(garden_node_arr[y])):
                garden_node = garden_node_arr[y][x]
                if y + 1 < len(garden_node_arr):
                    garden_node.neighbors.append(garden_node_arr[y+1][x])
                if y - 1 >= 0:
                    garden_node.neighbors.append(garden_node_arr[y-1][x])
                if x + 1 < len(garden_node_arr[y]):
                    garden_node.neighbors.append(garden_node_arr[y][x+1])
                if x - 1 >= 0:
                    garden_node.neighbors.append(garden_node_arr[y][x-1])

        self._union_merge(garden_nodes)

        area_counter = {}
        perim_counter = {}
        for node in garden_nodes:
            root = node.root
            if root.id not in area_counter:
                area_counter[root.id] = 0
                perim_counter[root.id] = 0
            area_counter[root.id] += 1
            perim_counter[root.id] += node.get_permimeter()

        for key in area_counter:
            logger.debug(f"Area: {area_counter[key]}, Perimeter: {perim_counter[key]}")

        return sum([area_counter[key] * perim_counter[key] for key in area_counter])

    def part2(self) -> int:
        pass

if __name__ == "__main__":
    solution = Day12(False)
    if solution.sample:
        if (part1 := solution.part1()) is not None:
            assert part1 == 1930, part1
        if (part2 := solution.part2()) is not None:
            assert part2 == 31, part2
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")