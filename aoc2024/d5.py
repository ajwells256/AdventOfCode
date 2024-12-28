
import logging
import os
from typing import List, Dict, Set
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

DAY = 5

class Rule:
    def __init__(self, before: int, after: int):
        self.before = before
        self.after = after

class UpdateSet:
    def __init__(self, ordered_pages: List[int], rules: List[Rule]):
        self.rules = rules
        self.ordered_pages = ordered_pages
        self.after_rules: Dict[int, Set[int]] = {}
        for rule in rules:
            if rule.after not in self.after_rules:
                self.after_rules[rule.after] = set([rule.before])
            else:
                self.after_rules[rule.after].add(rule.before)

    def is_correct_ordering(self) -> bool:
        correct = True
        remaining = set(self.ordered_pages)
        for page in self.ordered_pages:
            remaining.remove(page)
            if page in self.after_rules:
                if not self.after_rules[page].isdisjoint(remaining):
                    correct = False
                    break
        return correct

    def correct_ordering(self):
        remaining = set(self.ordered_pages)
        for page in self.ordered_pages:
            remaining.remove(page)
            if page in self.after_rules:
                if not self.after_rules[page].isdisjoint(remaining):
                    new_index = max(map(self.ordered_pages.index, self.after_rules[page].intersection(remaining)))
                    self.ordered_pages.remove(page)
                    self.ordered_pages.insert(new_index, page)
                    self.correct_ordering()
                    break

class Day5(Solution):
    def __init__(self, sample = False):
        self.sample = sample

    def _parse_rules(self, input_lines):
        rules = []
        for line in input_lines:
            match_obj = match(r"(\d+)\|(\d+)", line)
            if match_obj:
                rules.append(Rule(int(match_obj.group(1)), int(match_obj.group(2))))
            else:
                break
        return rules

    def _parse_ordered_page_sets(self, input_lines) -> List[List[int]]:
        ordered_pages = []
        for line in input_lines:
            match_obj = match(r"^[0-9,]+$", line)
            if match_obj:
                ordered_pages.append(list(map(int, match_obj.group().split(","))))
            elif len(ordered_pages) > 0:
                break
            else:
                # seeking the start of the ordered pages section
                continue
        return ordered_pages

    def part1(self) -> int:
        input_lines = read_lines(DAY, sample=self.sample, rootdir=dirname)
        rules = self._parse_rules(input_lines)
        ordered_page_sets = self._parse_ordered_page_sets(input_lines)
        update_sets = [UpdateSet(ordered_page_set, rules) for ordered_page_set in ordered_page_sets]
        correct_sets = [update_set for update_set in update_sets if update_set.is_correct_ordering()]
        return sum(set.ordered_pages[(len(set.ordered_pages) // 2)] for set in correct_sets)

    def part2(self) -> int:
        input_lines = read_lines(DAY, sample=self.sample, rootdir=dirname)
        rules = self._parse_rules(input_lines)
        ordered_page_sets = self._parse_ordered_page_sets(input_lines)
        update_sets = [UpdateSet(ordered_page_set, rules) for ordered_page_set in ordered_page_sets]
        incorrect_sets = [update_set for update_set in update_sets if not update_set.is_correct_ordering()]
        for s in incorrect_sets:
            s.correct_ordering()
        return sum(set.ordered_pages[(len(set.ordered_pages) // 2)] for set in incorrect_sets)

if __name__ == "__main__":
    solution = Day5(sample=False)
    if solution.sample:
        part1 = solution.part1()
        assert part1 == 143, part1
        if (part2 := solution.part2()) is not None:
            assert part2 == 31, part2
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")