from typing import Dict,List
from re import match

from common.struct import numeric_word_map
from common.logger import log

def read_input(day: int, part: int) -> List[str]:
    with open(f"inputs/d{day}p{part}.txt", "r") as puzzle:
        return puzzle.readlines()

def get_calibration(line: str, wmap: Dict[str,str] = {}) -> int:
    try:
        word_matcher = "|".join(wmap.keys())
        if len(word_matcher) > 0:
            word_matcher = f"|{word_matcher}"
            log.vdebug(word_matcher)
        first_digit = match(f"^.*?(\d{word_matcher}).*", line).group(1)
        second_digit = match(f".*(\d{word_matcher}).*?$", line).group(1)
        
        if first_digit in wmap:
            first_digit = wmap[first_digit]
        if second_digit in wmap:
            second_digit = wmap[second_digit]

        return int(f"{first_digit}{second_digit}")
    except:
        print(line)
        raise

def part1(sample=False) -> int:
    puzzle = read_input(1,1,sample)
    run_sum = 0
    for line in puzzle:
        run_sum += get_calibration(line)
    return run_sum

def part2(sample=False) -> int:
    puzzle = read_input(1,1,sample)
    run_sum = 0
    wmap = {k:str(v) for k,v in numeric_word_map.items()}
    for line in puzzle:
        run_sum += get_calibration(line, wmap)
    return run_sum

if __name__ == "__main__":
    if "part2" not in globals():
        print(part1())
    else:
        print(part2())

