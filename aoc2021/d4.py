
x = open("d4p1_input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

boards = [[]]
for i in range(2, len(input)):
    if (len(input[i]) != 0):
        boards[-1] += input[i].split()
    else:
        boards.append([])

scorecards = [[0] * 25 for b in range(len(boards))]

def columnWin(scorecard, index):
    width = int(len(scorecard)**0.5)
    offset = index % width
    win = True
    for i in range(width):
        win &= scorecard[offset + width*i] == 1
    return win

def rowWin(scorecard, index):
    width = int(len(scorecard)**0.5)
    row = index // width
    win = True
    for i in range(width):
        win &= scorecard[i + row*width] == 1
    return win

def unmarkedSum(board, scorecard):
    unmarked = 0
    for i in range(len(board)):
        if (scorecard[i] == 0):
            unmarked += int(board[i])
    return unmarked
    
ignoreList = []
for nextNumber in input[0].split(","):
    for i in range(len(boards)):
        if (i in ignoreList):
            continue
        try:
            indexOf = boards[i].index(nextNumber)
            scorecards[i][indexOf] = 1
            if (rowWin(scorecards[i], indexOf) or columnWin(scorecards[i], indexOf)):
                ignoreList.append(i)
                if (len(ignoreList) == 1 or len(ignoreList) == len(boards)):
                    print(unmarkedSum(boards[i], scorecards[i])*int(nextNumber))
        except(ValueError):
            continue