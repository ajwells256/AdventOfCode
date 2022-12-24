
def readlines(day, part):
    x = open(f"/home/andrew/code/git/AdventOfCode/aoc2022/inputs/d{day}p{part}.txt")
    y = x.readlines()
    inp = [entry.rstrip("\n") for entry in y]
    while inp[-1] == "":
        inp.pop()
    return inp