
"""
    Implementation of Depth First Search algorithm.
"""

graph = {'A': ['B', 'C', 'D'],'B':['E'],'C':['D', 'E'], 'D':[], 'E':[]}

def dfs(graph, start):
    stack = [start]
    visited = set()
    step = 1
    while stack:
        print("Step: ",step)
        print("Visited: ", visited)
        print("Stack: ", stack)
        vertex = stack.pop()
        if vertex in visited:
            continue
        yield vertex
        visited.add(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
        step += 1
    return visited

#dfs(graph, 'A')
# iterate values from visited set
for value in dfs(graph, 'A'):
    print(value)
#print(dfs(graph, 'A'))

# create s set of 10 variables
s = set(range(10))
#print(s)