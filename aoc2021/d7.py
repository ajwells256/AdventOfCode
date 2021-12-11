
x = open("inputs/d7p1_input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

crabs = list(map(int, input[0].split(",")))


costs = {sum(map(lambda c:abs(pos-c), crabs)):pos for pos in crabs}
print(min(costs.keys()))