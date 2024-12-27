from typing import List, Union

def read_raw_lines(day: int, part: int, sample: bool = False, rootdir: Union[str, None] = None) -> List[str]:
    directory = "samples" if sample else "inputs"
    if rootdir is not None:
        directory = f"{rootdir}/{directory}"
    with open(f"{directory}/d{day}p{part}.txt", "r") as p:
        return p.readlines()

def read_lines(day: int, part: int, sample: bool = False, rootdir: Union[str, None] = None) -> List[str]:
    return list(map(lambda l: l.rstrip("\n"), read_raw_lines(day, part, sample, rootdir)))

def read_array(day: int, part: int, sample: bool = False, rootdir: Union[str, None] = None) -> List[List[chr]]:
    return [[c for c in line] for line in read_lines(day, part, sample, rootdir)]
