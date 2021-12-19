
x = open("inputs/d9example.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

markers = [[0 for i in range(len(x))] for x in input]

markers[0][0] = 1 + int(input[0][0])

for i in range(len(input)):
    for j in range(len(input[0])):
        update = False
        if (i > 0 and j > 0):
            if (input[i][j] < input[i-1][j] and input[i][j] < input[i][j-1]):
                markers[i][j] = 1+int(input[i][j])
                update = True
            elif (input[i][j] < input[i-1][j] or input[i][j] < input[i][j-1]):
                if (markers[i][j-1] > markers[i-1][j] and markers[i-1][j] > 0):
                    markers[i][j-1] = 0
                elif (markers[i][j-1] < markers[i-1][j] and markers[i][j-1] > 0):
                    markers[i-1][j] = 0
        elif (i > 0 and input[i][j] < input[i-1][j]):
            markers[i][j] = 1+int(input[i][j])
            update = True
        elif (j > 0 and input[i][j] < input[i][j-1]):
            markers[i][j] = 1+int(input[i][j])
            update = True
        
        if (update):
            if (j > 0):
                markers[i][j-1] = 0
            if (i > 0):
                markers[i-1][j] = 0

print(sum(map(sum, markers)))
