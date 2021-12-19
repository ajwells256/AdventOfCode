
x = open("inputs/d10example.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

def parse(line):
    openers = ['(', '{', '<', '[']
    closers = [')', '}', '>', ']']
    points = [3, 1197, 25137, 57]
    stack = []
    for c in line:
        if (c in openers):
            stack.append(c)
        elif (c in closers):
            expected = stack.pop()
            if (openers.index(expected) != closers.index(c)):
                return (-1, f"Expected {closers[openers.index(expected)]} but found {c}", points[closers.index(c)])
    return (0, "unhandled", 0)

score = 0
for line in input:
    code, msg, val = parse(line)
    if (code == -1):
        score += val

print(score)