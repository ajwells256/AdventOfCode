
x = open("inputs/d10input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

def parse(line):
    openers = ['(', '{', '<', '[']
    closers = [')', '}', '>', ']']
    points = [3, 1197, 25137, 57]
    acPoints = [1, 3, 4, 2]
    stack = []
    for c in line:
        if (c in openers):
            stack.append(c)
        elif (c in closers):
            expected = stack.pop()
            if (openers.index(expected) != closers.index(c)):
                return (-1, f"Expected {closers[openers.index(expected)]} but found {c}", points[closers.index(c)])

    autoCompleteScore = 0
    stack.reverse()
    for c in stack:
        autoCompleteScore *= 5
        autoCompleteScore += acPoints[openers.index(c)]
    return (1, "Autocompleted", autoCompleteScore)

score = 0
acScores = []
for line in input:
    code, msg, val = parse(line)
    if (code == -1):
        score += val
    elif (code == 1):
        acScores.append(val)

acScores.sort()

print(score, acScores[(len(acScores)-1)//2])