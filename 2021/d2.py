x = open("d2p1.txt")
y = x.readlines()
inst = [z.rstrip("\n").split(" ") for z in y]

h = 0
d = 0
aim = 0

for i in inst:
    val = int(i[1])
    if i[0] == 'forward':
        h += val
        d += aim * val
    elif i[0] == 'up':
        aim -= val
    elif i[0] == 'down':
        aim += val
    else:
        print(i[0])

print(h*d)
