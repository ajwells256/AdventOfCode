import reader


def part1():
    lines = reader.readlines(25, 1)
    totalFuel = sum(map(lambda x: stoi(x), lines))
    return itos(totalFuel)

def stoi(snafu):
    aggregate = 0
    littleEndian = snafu[::-1]
    for i in range(len(snafu)):
        value = 0
        if littleEndian[i] == '-':
            value = -1
        elif littleEndian[i] == "=":
            value = -2
        else:
            value = int(littleEndian[i])
        aggregate += 5**i * value
    return aggregate

def itos(decimal):
    largeI = 0
    while True:
        factor = decimal / 5**largeI
        if factor <= 2:
            break
        largeI += 1
    
    #algorithm
    snafu = "" #bigendian
    remainder = decimal
    for i in range(largeI, -1, -1):
        factor = remainder / 5**i
        rounded = round(factor)
        remainder -= rounded * 5**i
        if rounded == -2:
            snafu += "="
        elif rounded == -1:
            snafu += '-'
        else:
            snafu += str(rounded)
    return snafu
    

print(part1())
