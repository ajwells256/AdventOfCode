
memo = {}

# returns the number of fish produced by a fish with daysLeft days to reproduce
# excludes from the count the original fish itself
def fishy(daysLeft):
    if (daysLeft < 0):
        return 0
    newFish = list(map(lambda x: x-9, list(range(daysLeft, -1, -7))))
    fishCount = 0
    for fish in newFish:
        if (fish not in memo.keys()):
            memo[fish] = fishy(fish)
        fishCount += 1 + memo[fish]
    return fishCount

def simulate(originals, days):
    result = 0
    for originalFish in originals:
        result += 1 + fishy(days - 1 - originalFish)
    return result

x = open("d6p1_input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

originals = list(map(int, input[0].split(",")))

print(simulate(originals, 80))
print(simulate(originals, 256))