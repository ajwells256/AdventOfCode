
import logging
import os

from base import Solution

dirname, filename = os.path.split(__file__)
filename = filename.rstrip(".py")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(filename)


class DayN(Solution):
    def part1(self):
        pass

    def part2(self):
        pass