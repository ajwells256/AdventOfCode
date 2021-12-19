x = open("inputs/d12_long_example.txt")
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
def pathsTo(src, dst, bld = []):
    if (len(bld) == 0):
        bld.append(src)
    for connection in graph[src]:
        if (connection.lower() == connection and connection in bld):
            continue
        newBuild = bld.copy()
        newBuild.append(connection)
        if (connection == dst):
            paths.append(newBuild)
            continue
        pathsTo(connection, dst, newBuild)

pathsTo("start", "end")
print(len(paths))
