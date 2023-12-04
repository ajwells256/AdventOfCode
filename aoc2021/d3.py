
x = open("d3p1_input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

g = ""
e = ""
for i in range(len(input[1])):
    sum = 0
    for j in range(len(input)):
        sum += int(input[j][i])
    g += "1" if sum / len(input) > 0.5 else "0"
    e += "0" if sum / len(input) > 0.5 else "1"

print(g,e)
gamma = int(g, 2)
epsilon = int(e, 2)
print(epsilon, ~gamma)
print(gamma * epsilon)

oxy = input[:]
offset = 0
while len(oxy) != 1:
    sum = 0
    zeros = []
    ones = []
    for j in range(len(oxy)):
        val = int(oxy[j][offset])
        sum += val
        if (val == 1):
            ones.append(oxy[j])
        else:
            zeros.append(oxy[j])
    oxy = ones if sum / len(oxy) >= 0.5 else zeros
    offset += 1
oxy = int(oxy[0], 2)

co2 = input[:]
offset = 0
while len(co2) != 1:
    sum = 0
    zeros = []
    ones = []
    for j in range(len(co2)):
        val = int(co2[j][offset])
        sum += val
        if (val == 1):
            ones.append(co2[j])
        else:
            zeros.append(co2[j])
    co2 = zeros if sum / len(co2) >= 0.5 else ones
    offset += 1

co2 = int(co2[0], 2)
print (oxy * co2)
        