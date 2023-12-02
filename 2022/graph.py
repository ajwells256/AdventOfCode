
class node:
    def __init__(self):
        self.neighbors = []
        self.traversed = False

def dfs(startNode, targetNode):
    if startNode == targetNode:
        return [startNode]
    
    for neighbor in startNode.neighbors:
        if not neighbor.traversed:
            neighbor.traversed = True
            result = dfs(neighbor, targetNode)
            if result[-1] == targetNode:
                return result

    return []

def bfs(startNode, targetNode):
    oldPaths = [[startNode]]
    newPaths = []
    progress = True

    while (progress):
        progress = False
        while (len(oldPaths) > 0):
            path = oldPaths.pop()
            print(oldPaths)
            for neighbor in path[-1].neighbors:
                if not neighbor.traversed:
                    progress = True
                    if (neighbor == targetNode):
                        return path
                    neighbor.traversed = True
                    path.append(neighbor)
                    newPaths.append(path)
        newPaths = oldPaths
        oldPaths = []

    return []