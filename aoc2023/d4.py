from typing import List,Tuple
from re import findall,match

from common.preader import read_lines

def parse(card:str) -> Tuple[int, List[int], List[int]]:
    m = match("Card *(\d+): *(.*) \| *(.*)$", card)
    card = int(m.group(1))
    win_nums = list(map(int, [x for x in m.group(2).split(" ") if len(x) > 0]))
    nums = list(map(int, [x for x in m.group(3).split(" ") if len(x) > 0]))
    return (card, win_nums, nums)

def part1(sample: bool = False) -> int:
    p = read_lines(4,1,sample)
    run_sum = 0
    for line in p:
        _, win_nums, nums = parse(line)
        matches = sum(map(lambda x: 1 if x in win_nums else 0, nums)) 
        run_sum += 2**(matches - 1) if matches > 0 else 0
    return run_sum    

def part2(sample: bool = False) -> int:
    p = read_lines(4,1,sample)
    card_count = [1] * len(p)
    for line in p:
        game, win_nums, nums = parse(line)
        matches = sum(map(lambda x: 1 if x in win_nums else 0, nums)) 
        game -= 1 # 0 index
        for i in range(matches):
            card_count[game+i+1] += card_count[game] 
    return sum(card_count) 


if __name__ == "__main__":
    if "part2" not in globals():
        print(part1())
    else:
        print(part2())

