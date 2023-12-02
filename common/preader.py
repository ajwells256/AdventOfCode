from typing import List

def read_raw_lines(day: int, part: int) -> List[str]:
    with open(f"inputs/d{day}p{part}.txt", "r") as p:
        return p.readlines()

def read_lines(day: int, part: int) -> List[str]:
    return list(map(lambda l: l.rstrip("\n"), read_raw_lines(day, part)))




