
x = open("inputs/d14input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

polymer = input[0]
rules = [rule.split(" -> ") for rule in input[2:]]
ruleDict = {r[0]:r[1] for r in rules}

def findAll(x: str, sub: str):
    indices = []
    index = x.find(sub)
    while (index != -1):
        indices.append(index)
        index = x.find(sub, index+1)
    return indices

def simulateBrute(n, inputPolymer):
    poly = inputPolymer
    for i in range(n):
        insertions = []
        for rule in rules:
            locations = findAll(poly, rule[0])
            insertions += [(rule[1], location+1) for location in locations]
        insertions.sort(key=lambda a: a[1], reverse=True)
        for insertion in insertions:
            poly = poly[0:insertion[1]] + insertion[0] + poly[insertion[1]:]
        return poly

def simulatePair(N, inputPair, memo):
    if (inputPair in memo.keys()):
        n, result = max([x for x in memo[inputPair] if x[0] <= N], key=lambda x: x[0])
        if (n != N):
            print(f"Cache miss at N = {N} for pair {inputPair}")
            result = simulatePolymer(N-n, result, memo)
            memo[inputPair].append((N, result))
        return result

def simulatePolymer(N, inputPolymer, memo):
        pairs = [inputPolymer[i:i+2] for i in range(len(inputPolymer)-1)]
        smallResults = [simulatePair(N, p, memo) for p in pairs]
        smallResults = [s if i == 0 else s[1:]  for i, s in enumerate(smallResults)]
        return "".join(smallResults)

def simulateSmart(n, inputPolymer):
    memo = {x[0]:[(1, x[0][0] + x[1] + x[0][1])] for x in rules}
    return simulatePolymer(n, inputPolymer, memo)


def stepPair(inputPair):
    ruleChar = ruleDict[inputPair]
    return [inputPair[0] + ruleChar, ruleChar + inputPair[1]]

def countPolymer(N, inputPolymer):
    pairs = [inputPolymer[i:i+2] for i in range(len(inputPolymer)-1)]
    pairCount = {}
    for p in pairs:
        if p not in pairCount.keys():
            pairCount[p] = 0
        pairCount[p] += 1
    for i in range(N):
        iterateDict = pairCount.copy()
        pairCount = {}
        for pair, count in iterateDict.items():
            for newPair in stepPair(pair):
                if newPair not in pairCount.keys():
                    pairCount[newPair] = 0
                pairCount[newPair] += count # 1 new newPairs for each of the n pairs
    return pairCount

def countElements(N, inputPolymer):
    pc = countPolymer(N, inputPolymer)
    elemCount = {}
    for pair, count in pc.items():
        for e in pair:
            if e not in elemCount.keys():
                elemCount[e] = 0
            elemCount[e] += count
    elemCount[inputPolymer[0]] += 1
    elemCount[inputPolymer[-1]] += 1
    return elemCount

for i in [10, 40]:
    elemCounts = countElements(i, polymer)

    print(max(elemCounts.values())/2 - min(elemCounts.values())/2)

#     frequencies = {}
#     for e in result:
#         if (e in frequencies.keys()):
#             frequencies[e] += 1
#         else:
#             frequencies[e] = 1

#     print(max(frequencies.values()) - min(frequencies.values()))
