
def readlines(day, part):
    x = open(f"inputs/d{day}p{part}.txt")
    y = x.readlines()
    inp = [entry.rstrip("\n") for entry in y]
    while inp[-1] == "":
        inp.pop()
    splitLines = split(inp)
    if len(splitLines) == 1:
        return splitLines[0]
    else:
        return splitLines

def split(lines):
    result = [[]]
    for line in lines:
        if line != "":
            result[-1].append(line)
        elif len(result[-1]) != 0:
            result.append([])
    return result

