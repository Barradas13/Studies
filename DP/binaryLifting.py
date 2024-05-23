from collections import defaultdict
import math

def transformTree(tree):
    graph = defaultdict(list)
    
    for i in tree:
        graph[i[0]].append(i[1])

    return graph

def dfs(graph, ancestors, node, parent):
    ancestors[node][0] = parent
    for i in graph[node]: 
        print(i)
        if ancestors[i][0] == -1:
            dfs(graph, ancestors, i, node)
       
    return ancestors

def precomputing(graph, v):
    ancestors = [[-1 for i in range(int(math.log2(v)))] for j in range(v)]

    dfs(graph, ancestors, 1, -1)
    
    for j in range(0, int(math.log2(v))):
        for i in range(1, v):
            if ancestors[i][j-1] != -1:
                ancestors[i][j] = ancestors[ancestors[i][j-1]][j-1]

    return ancestors

tree = [[1,1],[1,2],[1,3],[3,4],[3,5]]
v = 8
graph = transformTree(tree)
print(graph)
print(precomputing(graph, v))