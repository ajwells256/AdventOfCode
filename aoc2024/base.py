
from abc import ABC, abstractmethod

class Solution(ABC):
    @abstractmethod
    def part1(self) -> int:
        pass

    @abstractmethod
    def part2(self) -> int:
        pass