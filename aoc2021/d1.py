
x = open("inputs/d1p1_input.txt")
y = x.readlines()
inp = [int(entry.rstrip("\n")) for entry in y]

next = [ inp[0]+1 ] + inp[:-1]

count = 0
process = []
for i in range(len(inp)-2):
    process.append(inp[i] + inp[i+1] + inp[i+2])

pcount=0
for i in range(len(inp)-1):
    count += 1 if inp[i+1] - inp[i] > 0 else 0

for i in range(len(process)-1):
    pcount += 1 if process[i+1] - process[i] > 0 else 0
print(count)
print(pcount)

