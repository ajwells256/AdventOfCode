from typing import List

def read_raw_lines(day: int, part: int, sample: bool = False) -> List[str]:
    directory = "sample" if sample else "inputs"
    with open(f"{directory}/d{day}p{part}.txt", "r") as p:
        return p.readlines()

def read_lines(day: int, part: int, sample: bool = False) -> List[str]:
    return list(map(lambda l: l.rstrip("\n"), read_raw_lines(day, part, sample)))

def read_array(day: int, part: int, sample: bool = False) -> List[List[chr]]:
    return [[c for c in line] for line in read_lines(day, part, sample)]




