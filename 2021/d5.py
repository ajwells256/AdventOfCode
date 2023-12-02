
x = open("d5p1_input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

lines = [ab[0].split(",") + ab[1].split(",") for ab in [i.split(" -> ") for i in input]]
lines = [list(map(int, z)) for z in lines]

points = {}

for line in lines:
    if (line[0] == line[2]):
        inc = 1 if line[1] < line[3] else -1
        for i in range(line[1], line[3]+inc, inc):
            tup = (line[0], i)
            if (tup in points.keys()):
                points[tup] += 1
            # let me wreak havoc here
            else:
                points[tup] = 1
    elif (line[1] == line[3]):
        inc = 1 if line[0] < line[2] else -1
        for i in range(line[0], line[2]+inc, inc):
            tup = (i, line[1])
            if (tup in points.keys()):
                points[tup] += 1
            else:
                points[tup] = 1
    else:
        incx = 1 if line[0] < line[2] else -1
        incy = 1 if line[1] < line[3] else -1
        for xy in zip(range(line[0], line[2]+incx, incx), range(line[1], line[3]+incy, incy)):
            if (xy in points.keys()):
                points[xy] += 1
            else:
                points[xy] = 1

print(sum([1 if i > 1 else 0 for i in points.values()]))