import reader

def part1():
    instructions = reader.readlines(10, 1)
    signalStregths = [] 
    pinstructions = [x.split(" ") for x in instructions]
    state = {"x": 1, "cycle": 0, "cd": 0, "instructions": pinstructions, "currentInstruction": None }
    for i in [20, 60, 100, 140, 180, 220]:
        signalStregths.append(i*runComputer(i, state)["x"])
    return sum(signalStregths)


def runComputer(cycles, state):
    if state["currentInstruction"] is None:
        instruction = state["instructions"].pop(0)
    else:
        instruction = state["currentInstruction"]
    while state["cycle"] < cycles:
        state["cycle"] += 1
        if len(instruction) == 1:
            if instruction[0] == "noop":
                print(instruction[0])
                instruction = state["instructions"].pop(0)
        elif len(instruction) == 2:
            if instruction[0] == "addx":
                if state["cd"] == 0:
                    state["cd"] = 1
                else:
                    state["cd"] = 0
                    state["x"] += int(instruction[1])
                    print(" ".join(instruction))
                    instruction = state["instructions"].pop(0)
    state["currentInstruction"] = instruction
    return state

def run(cycles, x, instructions):
    cycle = 0

print(part1())