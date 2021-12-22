x = open("inputs/d12input.txt")
y = x.readlines()
input = [z.rstrip("\n") for z in y]

graph = {}
for line in input:
    src, dst = line.split("-")
    if (src not in graph.keys()):
        graph[src] = []
    graph[src].append(dst)
    if (dst not in graph.keys()):
        graph[dst] = []
    graph[dst].append(src)


paths = []
def pathsTo(src, dst, bld = [], doubleSmallCave = False):
    if (len(bld) == 0):
        bld.append(src)
    for connection in graph[src]:
        lower = connection.lower() == connection
        part1 = bld.count(connection) > 0
        part2 = connection == "start" or (doubleSmallCave and part1)
        newlyDoubleCaved = False
        if (part1 and connection != "start" and lower):
            newlyDoubleCaved = True
        if (part2 and lower):
            continue
        newBuild = bld.copy()
        newBuild.append(connection)
        if (connection == dst):
            paths.append(newBuild)
            continue
        pathsTo(connection, dst, newBuild, (doubleSmallCave or newlyDoubleCaved))

pathsTo("start", "end")
print(len(paths))