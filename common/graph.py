from typing import List

class Node:
    def __init__(self):
        self.neighbors = []

    def dfs(self, target_node: Node, visited: Set[Node] = set()):
        path: List[Node] = [self]
        if (self == target_node):
            return path
        
        for neighbor in self.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs_result = neighbor.dfs(target_node, visited)
                if dfs_result[-1] == target_node:
                    return path + dfs_result
        return []

    

class Graph:
    def __init__(self):
        self.nodes: List[Node] = []

class Tree(Graph):
    def __init__(self):
        super.__init__(self)
        self.root: Node = Node()

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
