def bfs(graph, start):
    visited = []
    queue = []

    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


graph1 = {
    10: [20, 30],
    20: [40, 50],
    30: [60],
    40: [],
    50: [70],
    60: [],
    70: []
}

graph2 = {
    11: [12, 13],
    12: [14, 15],
    13: [16],
    14: [],
    15: [17],
    16: [],
    17: []
}

graph3 = {
    100: [200, 300],
    200: [400],
    300: [500, 600],
    400: [],
    500: [700],
    600: [],
    700: []
}

graph4 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

print("BFS Traversal:")
bfs(graph1, 10)
print()

bfs(graph2, 11)
print()

bfs(graph3, 100)
print()

bfs(graph4, 'A')
